# Canva Integration — Mirella Manelli HBBU

Connect to Canva and create on-brand Instagram posts automatically.

## Setup

### 1. Add your Client Secret

Go to [canva.dev](https://www.canva.dev/) → your app → copy the **Client Secret**.

Then run:
```bash
export CANVA_CLIENT_SECRET="your_secret_here"
```

Or add it to a `.env` file (never commit this).

### 2. Connect your Canva account (first time only)

```bash
cd canva-integration
python3 canva_auth.py
```

This opens Canva in your browser. Log in and approve access. Your tokens are saved locally.

### 3. Create an Instagram post

```bash
python3 canva_create_post.py create "Hair Colour Tips — Post 001"
```

This creates a new 1080x1350 design in your Canva account and returns an edit link.

### 4. List your recent designs

```bash
python3 canva_create_post.py list
```

## Brand Colors (pre-loaded)

| Name | Hex |
|------|-----|
| Cream Blush | `#F8EEE5` |
| Light Pink | `#FFB6BA` |
| Medium Pink | `#FF879E` |
| Hot Pink | `#FA5185` |
| Deep Green | `#015A42` |

## Files

| File | Purpose |
|------|---------|
| `canva_auth.py` | OAuth 2.0 + PKCE authentication |
| `canva_create_post.py` | Create & list Canva designs |
| `.canva_tokens.json` | Saved tokens (auto-generated, git-ignored) |
| `.gitignore` | Keeps secrets out of GitHub |
