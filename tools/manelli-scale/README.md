# The Manelli Scale — Interactive Tool

> **Mirella Manelli & Hair B&B University**
> A fully interactive, brand-aligned comparison tool for 50 professional hair bleaches.

---

## What It Is

The Manelli Scale is Mirella's proprietary ranking system for professional hair bleach products. This interactive tool brings the static PDF to life — letting stylists sort, filter, compare, and explore the data in real time.

**50 products · 10 criteria · fully searchable**

---

## Scoring Criteria

| Criterion | What It Measures |
|-----------|-----------------|
| **Dust** | Mess level when mixing — 10 = minimal dust |
| **Odor** | Scent experience during processing — 10 = pleasant/odorless |
| **Viscosity** | Consistency & spreadability — 10 = ideal texture |
| **Timing** | Processing time predictability — 10 = very consistent |
| **Swell** | Product expansion on hair — affects saturation |
| **Lift** | Levels of lightening achieved — 10 = maximum lift |
| **Integrity** | Hair condition post-processing — 10 = least damage |
| **Neutral** | Tone neutrality — 10 = no unwanted warmth |
| **Versatility** | Range of techniques it works well with |
| **Price** | Value for money — 10 = best value |

---

## Features

### Heat Map Table
Every score cell is color-coded using the Mirella Manelli brand palette:
- **Deep green** → high scores (8–10)
- **Warm pink** → mid scores (5–7)
- **Light cream** → low scores (0–4)
- **★ star** marks the #1 product in each column

### Sort & Filter
- Click any column header to sort ascending / descending
- Search by brand name
- Filter by minimum total score (80+, 75+, 70+)
- "Highlight" dropdown dims all other columns to spotlight one criterion
- **Elite 85+** pill — shows only top-tier products
- **Best Value** pill — auto-calculates best total score among products with price ≥ 7

### Side-by-Side Comparison
1. Check up to 4 products using the row checkboxes
2. A compare bar appears at the bottom
3. Click **Side-by-Side →** to open a modal with:
   - Radar / spider charts for each product
   - Full score grid with heat-map coloring

---

## Brand Colors Used

| Token | Hex | Usage |
|-------|-----|-------|
| Cream | `#F8EEE5` | Page background |
| Forest Green | `#015A42` | Header, high scores, accents |
| Hot Pink | `#FA5185` | CTAs, active states, radar fill |
| Light Pink | `#FFB8B5` | Mid-range scores, badges |
| Brown | `#8A5A3E` | Body text, chart labels |

**Typography:** Playfair Display (headings) · Open Sans (body)

---

## File Location

```
tools/
└── manelli-scale/
    ├── index.html   ← interactive tool (open in any browser)
    └── README.md    ← this file
```

---

## How to Use

1. Open `index.html` in any modern browser — no server required
2. For website embedding, upload `index.html` to your hosting and link directly
3. For WordPress, use the data-URI iframe method (see `brand-assets/wordpress-embedding.md`)

---

*The Manelli Scale — created by Mirella Manelli · @mirellamanelli*
