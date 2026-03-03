"""
Mirella Manelli HBBU — Create a branded Canva Instagram post
Requires: canva_auth.py to have run successfully first
"""

import requests
import json
from canva_auth import authenticate

# ── Brand colors ───────────────────────────────────────────────────────────────
BRAND = {
    "cream_blush":  "#F8EEE5",
    "light_pink":   "#FFB6BA",
    "medium_pink":  "#FF879E",
    "hot_pink":     "#FA5185",
    "deep_green":   "#015A42",
}

BASE_URL = "https://api.canva.com/rest/v1"

def create_instagram_post(title: str = "HBBU Instagram Post") -> dict:
    """Creates a new 1080x1350 Instagram post design in Canva."""
    token = authenticate()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    payload = {
        "design_type": {
            "type": "preset",
            "name": "instagramPost"
        },
        "title": title,
    }

    resp = requests.post(f"{BASE_URL}/designs", headers=headers, json=payload)

    if resp.status_code not in (200, 201):
        print(f"Error {resp.status_code}: {resp.text}")
        resp.raise_for_status()

    data = resp.json()
    design = data.get("design", {})

    edit_url  = design.get("urls", {}).get("edit_url", "")
    view_url  = design.get("urls", {}).get("view_url", "")
    design_id = design.get("id", "")

    print("\n✓ Canva design created!")
    print(f"  Design ID : {design_id}")
    print(f"  Edit URL  : {edit_url}")
    print(f"  View URL  : {view_url}")
    print(f"\n  Open your design: {edit_url}\n")

    result = {
        "design_id": design_id,
        "edit_url": edit_url,
        "view_url": view_url,
        "title": title,
        "brand_colors": BRAND,
    }

    with open("last_design.json", "w") as f:
        json.dump(result, f, indent=2)
    print("  Design info saved to last_design.json")

    return result


def list_my_designs(limit: int = 10):
    """Lists your recent Canva designs."""
    token = authenticate()
    headers = {"Authorization": f"Bearer {token}"}

    resp = requests.get(f"{BASE_URL}/designs?limit={limit}", headers=headers)
    resp.raise_for_status()

    designs = resp.json().get("items", [])
    print(f"\nYour last {len(designs)} Canva designs:")
    for d in designs:
        print(f"  [{d['id']}] {d.get('title','Untitled')} — {d.get('urls',{}).get('edit_url','')}")
    return designs


if __name__ == "__main__":
    import sys

    command = sys.argv[1] if len(sys.argv) > 1 else "create"

    if command == "create":
        title = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "HBBU Instagram Post"
        create_instagram_post(title)

    elif command == "list":
        list_my_designs()

    else:
        print("Usage:")
        print("  python3 canva_create_post.py create [optional title]")
        print("  python3 canva_create_post.py list")
