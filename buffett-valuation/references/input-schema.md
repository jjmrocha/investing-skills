# Input Format for `scripts/valuation.py`

```bash
uv run scripts/valuation.py input.json
```

One JSON file per valuation. Every figure traces to a filing.

```json
{
  "company": "Johnson & Johnson",
  "as_of": "2026-09-01",
  "moat_tier": "formidable",
  "treasury_10y": 0.0477,
  "country_risk": 0.0,

  "years": {
    "2021": {"revenue": 78740, "capex": 3652, "ocf": 23410, "sbc": 1135},
    "2025": {"revenue": 94193, "capex": 4832, "ocf": 24530, "sbc": 1354}
  },

  "market_cap": 653540,
  "total_debt": 49036,
  "cash_and_st_investments": 20758
}
```

| Field | Required | Notes |
|---|---|---|
| `moat_tier` | yes | `inevitable` / `formidable` / `strong` / `none`. Sets both the discount premium and the terminal multiple — assign it before running. |
| `treasury_10y` | yes | Decimal. The 10-year yield on the as-of date. |
| `country_risk` | no | Decimal, 0.02-0.05 outside the US. Added after the floor. |
| `years` | yes* | 5-7 consecutive fiscal years. `ocf` is net cash from operating activities; `sbc` is stock-based compensation, which the script subtracts rather than adds back. |
| `market_cap`, `total_debt`, `cash_and_st_investments` | no | Enterprise value is reported when all three are present. Intrinsic value computes without them. |
| `owner_earnings_override` | no | *Replaces the series-derived base year. Use when the base year is distorted — pair it with `override_reason`. |
| `oe_cagr`, `revenue_cagr` | no | Decimals that replace the series-derived growth candidates. The caps still bind. |

**Window length.** Seven years is the target. Use fewer only when a separation or
disposal makes earlier years non-comparable, and say so on the maintenance capex line.

## What the script decides, and what you decide

Applied mechanically, so they cannot be argued away: the 15%/10% growth caps, the 10%
discount floor, the Greenwald maintenance-capex derivation and its weak-estimate flag,
the tier premium and terminal multiple, the 70% haircut, and the warning when terminal
value exceeds 80% of intrinsic value.

Left to you, because no script can settle them: the moat tier, whether a base year is
distorted enough to override, whether the window is comparable, and every part of data
points 3 and 4.
