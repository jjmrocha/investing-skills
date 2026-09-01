#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Compute the intrinsic value data points from a filings-derived input file.

Usage:  uv run scripts/valuation.py input.json

The caps, the discount floor and the tier multiple are applied here rather than by
hand, so they cannot be forgotten under a persuasive growth story. Everything the
script cannot decide -- the moat tier, whether a base year is distorted -- stays a
judgment call and must be supplied in the input.

See references/input-schema.md for the input format.
"""
import json
import sys

TIER = {  # moat tier -> (discount premium over the 10-yr Treasury, terminal multiple)
    "inevitable": (0.03, 15),
    "formidable": (0.04, 13),
    "strong":     (0.06, 11),
    "none":       (0.08, 9),
}
FLOOR = 0.10        # discount rate floor, binds regardless of the Treasury yield
CAP_1_5 = 0.15      # growth cap, years 1-5
CAP_6_10 = 0.10     # growth cap, years 6-10
MOS = 0.70          # margin of safety multiplier


def maintenance_ratio(years):
    """Greenwald: average capex/sales across flat or declining revenue years."""
    ys = sorted(years)
    ratios = {y: years[y]["capex"] / years[y]["revenue"] for y in ys}
    flat = [y for prev, y in zip(ys, ys[1:])
            if years[y]["revenue"] <= years[prev]["revenue"]]
    if flat:
        return sum(ratios[y] for y in flat) / len(flat), None
    return min(ratios.values()), (
        "WEAK: no flat or declining revenue year in the window; used the lowest "
        "observed capex/sales ratio. Report this on the maintenance capex line.")


def owner_earnings(years, ratio):
    """Per year: operating cash flow, less SBC (a real cost), less maintenance capex."""
    return {y: years[y]["ocf"] - years[y]["sbc"] - ratio * years[y]["revenue"]
            for y in years}


def cagr(series):
    ys = sorted(series)
    n = len(ys) - 1
    if n < 1 or series[ys[0]] <= 0:
        return None
    return (series[ys[-1]] / series[ys[0]]) ** (1 / n) - 1


def main(path):
    d = json.load(open(path))
    tier = d["moat_tier"].lower()
    premium, multiple = TIER[tier]
    years = {int(k): v for k, v in d.get("years", {}).items()}
    if years:
        ratio, weak = maintenance_ratio(years)
        oe = owner_earnings(years, ratio)
    else:
        ratio, weak, oe = None, None, {}
    if "owner_earnings_override" in d:
        base = d["owner_earnings_override"]
    elif oe:
        base = oe[max(oe)]
    else:
        sys.exit("supply either years[] or owner_earnings_override")

    g_oe = d.get("oe_cagr", cagr(oe))
    g_rev = d.get("revenue_cagr", cagr({y: years[y]["revenue"] for y in years}))
    candidates = [g for g in (g_oe, g_rev) if g is not None]
    g1 = min(candidates + [CAP_1_5])
    g2 = min(g1, CAP_6_10)

    rate = max(FLOOR, d["treasury_10y"] + premium) + d.get("country_risk", 0.0)

    pv, cf, flows = 0.0, base, []
    for t in range(1, 11):
        cf *= 1 + (g1 if t <= 5 else g2)
        disc = cf / (1 + rate) ** t
        pv += disc
        flows.append((t, cf, disc))
    tv = cf * multiple
    tv_pv = tv / (1 + rate) ** 10
    iv = pv + tv_pv

    ev = None
    if "market_cap" in d:
        ev = d["market_cap"] + d.get("total_debt", 0) - d.get("cash_and_st_investments", 0)

    p = print
    p(f"{d.get('company', path)}   as of {d.get('as_of', 'n/a')}")
    if ev is not None:
        p(f"\nEnterprise value  {ev:>12,.0f}   "
          f"(mkt cap {d['market_cap']:,.0f} + debt {d.get('total_debt', 0):,.0f} "
          f"- cash {d.get('cash_and_st_investments', 0):,.0f})")

    if ratio is not None:
        p(f"\nMaintenance capex ratio  {ratio * 100:.2f}% of sales")
        if weak:
            p(f"  !! {weak}")
    if oe:
        p("\nOwner earnings by year")
        for y in sorted(oe):
            p(f"  {y}  {oe[y]:>10,.0f}")
        p(f"  {'mean':>4}  {sum(oe.values()) / len(oe):>10,.0f}")
    if "owner_earnings_override" in d:
        p(f"  base overridden to {base:,.0f} — {d.get('override_reason', 'no reason given')}")

    p(f"\nGrowth candidates: owner earnings {fmt(g_oe)}, revenue {fmt(g_rev)}, "
      f"caps {CAP_1_5:.0%}/{CAP_6_10:.0%}")
    p(f"  applied: years 1-5 {g1 * 100:.2f}%   years 6-10 {g2 * 100:.2f}%")
    p(f"Discount rate: max({FLOOR:.0%}, {d['treasury_10y']:.2%} + {premium:.0%} "
      f"[{tier}]) = {rate:.2%}" + ("  <- floor binds" if rate <= FLOOR + 1e-9 else ""))
    p(f"Terminal multiple: {multiple}x  [{tier}]")

    p(f"\n  PV of years 1-10   {pv:>12,.0f}")
    p(f"  PV of terminal     {tv_pv:>12,.0f}   ({tv_pv / iv * 100:.0f}% of IV)")
    p(f"\n  1. INTRINSIC VALUE {iv:>12,.0f}")
    p(f"  2. IV x {MOS:.0%}        {iv * MOS:>12,.0f}")
    if ev is not None:
        p(f"     enterprise value {ev:>12,.0f}")
    if tv_pv / iv > 0.80:
        p("\n  !! Terminal value is over 80% of IV. Say so on the line: the "
          "valuation rests on the multiple, not on the cash flows.")


def fmt(g):
    return "n/a" if g is None else f"{g * 100:.2f}%"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
