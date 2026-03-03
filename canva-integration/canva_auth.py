"""
Mirella Manelli HBBU — Canva API Integration
OAuth 2.0 + PKCE authentication flow
"""

import os
import hashlib
import base64
import secrets
import urllib.parse
import webbrowser
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests

# ── Config ────────────────────────────────────────────────────────────────────
CLIENT_ID = "AAHAAJaj97E"
REDIRECT_URI = "http://localhost:8080/callback"
SCOPES = [
    "design:content:write",
    "design:content:read",
    "design:meta:read",
    "asset:read",
    "asset:write",
    "brandtemplate:content:read",
    "brandtemplate:meta:read",
    "profile:read",
]
TOKEN_FILE = os.path.join(os.path.dirname(__file__), ".canva_tokens.json")

# ── PKCE Helpers ──────────────────────────────────────────────────────────────
def generate_code_verifier():
    return base64.urlsafe_b64encode(secrets.token_bytes(32)).rstrip(b"=").decode()

def generate_code_challenge(verifier: str):
    digest = hashlib.sha256(verifier.encode()).digest()
    return base64.urlsafe_b64encode(digest).rstrip(b"=").decode()

# ── Local callback server ─────────────────────────────────────────────────────
auth_code = None

class CallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        if "code" in params:
            auth_code = params["code"][0]
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"""
                <html><body style="font-family:sans-serif;text-align:center;padding:60px;background:#F8EEE5">
                <h2 style="color:#015A42">Connected to Canva!</h2>
                <p style="color:#FA5185">You can close this tab and return to the terminal.</p>
                </body></html>
            """)
        else:
            self.send_response(400)
            self.end_headers()

    def log_message(self, format, *args):
        pass  # suppress server logs

# ── Token exchange ────────────────────────────────────────────────────────────
def exchange_code_for_tokens(code: str, verifier: str) -> dict:
    resp = requests.post(
        "https://api.canva.com/rest/v1/oauth/token",
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI,
            "code_verifier": verifier,
            "client_id": CLIENT_ID,
        },
    )
    resp.raise_for_status()
    return resp.json()

def save_tokens(tokens: dict):
    with open(TOKEN_FILE, "w") as f:
        json.dump(tokens, f, indent=2)
    print(f"  Tokens saved to {TOKEN_FILE}")

def load_tokens() -> dict | None:
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE) as f:
            return json.load(f)
    return None

def refresh_access_token(refresh_token: str) -> dict:
    resp = requests.post(
        "https://api.canva.com/rest/v1/oauth/token",
        data={
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": CLIENT_ID,
        },
    )
    resp.raise_for_status()
    return resp.json()

# ── Main auth flow ────────────────────────────────────────────────────────────
def authenticate() -> str:
    """Returns a valid access token, authenticating if needed."""
    tokens = load_tokens()

    if tokens:
        print("Refreshing existing Canva token...")
        try:
            tokens = refresh_access_token(tokens["refresh_token"])
            save_tokens(tokens)
            return tokens["access_token"]
        except Exception:
            print("Refresh failed — re-authenticating...")

    # Full OAuth + PKCE flow
    verifier = generate_code_verifier()
    challenge = generate_code_challenge(verifier)
    state = secrets.token_urlsafe(16)

    auth_url = (
        "https://www.canva.com/api/oauth/authorize?"
        + urllib.parse.urlencode({
            "client_id": CLIENT_ID,
            "response_type": "code",
            "redirect_uri": REDIRECT_URI,
            "scope": " ".join(SCOPES),
            "state": state,
            "code_challenge": challenge,
            "code_challenge_method": "S256",
        })
    )

    print("\nOpening Canva login in your browser...")
    print(f"If it doesn't open automatically, visit:\n{auth_url}\n")
    webbrowser.open(auth_url)

    # Wait for callback
    server = HTTPServer(("localhost", 8080), CallbackHandler)
    print("Waiting for Canva authorization...")
    server.handle_request()

    if not auth_code:
        raise RuntimeError("No authorization code received.")

    print("Authorization received. Exchanging for tokens...")
    tokens = exchange_code_for_tokens(auth_code, verifier)
    save_tokens(tokens)
    print("Successfully connected to Canva!")
    return tokens["access_token"]


if __name__ == "__main__":
    token = authenticate()
    print(f"\nAccess token ready. You can now run canva_create_post.py")
