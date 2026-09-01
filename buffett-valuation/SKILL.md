---
name: buffett-valuation
description: >
  Use when someone needs to know what a business is worth as a whole — "what is X worth",
  "is X cheap", "is X overvalued", "value X for me", "run a DCF on X", "does X have a moat",
  "can I trust X's management". Not for three-statement models, forecast spreadsheets, or
  per-share price targets.
---

# Buffett Valuation

Value a business by the cash an owner could take out of it over its life, discount that to
today, and report the number. **Four data points, each with its reasoning. No verdict.**

The reader compares intrinsic value against enterprise value themselves. That comparison is
theirs, not yours — your job is to produce numbers they can trust and show the work that
produced them.

## Output Contract

Every answer has exactly these parts, in this order.

**Header line:** enterprise value (market cap + total debt − cash), the as-of date, and the
source of the price. A valuation without the price it will be measured against is unusable.

| # | Data point | Reasoning that must accompany it |
|---|---|---|
| 1 | **Intrinsic value** — one number, whole company | The owner-earnings bridge line by line, how maintenance capex was derived, growth rates and where they came from, discount rate and its build, terminal multiple and the tier that set it |
| 2 | **IV × 70%** | One line: what margin of safety is for |
| 3 | **Moat tier** — Inevitable / Formidable / Strong / None | The specific mechanism, and what would break it |
| 4 | **Management** | Green flags met, red flags present, each sourced |

The output ends at data point 4. It states no buy, sell, hold, watch, pass, or "too hard"
judgment, names no target price, and draws no conclusion from comparing EV to IV — the
reader does that. Report the two numbers side by side and stop.

**Every request produces an intrinsic value.** Where an input was weakly derived, say so on
the line where it is used — "maintenance capex estimated from the lowest observed ratio; no
flat-revenue year in the window" — and continue to a number.

**One number, not a range.** The DCF returns a value; report that value. Uncertainty lives
in the stated assumptions, where the reader can move it.

## Getting the Data

Run `company-research` first when you do not already have the evidence. It returns the
durability evidence, capital-allocation history, ownership, and disclosed risks that data
points 3 and 4 are built from, and it never states a verdict — so nothing it hands you
pre-empts your own.

It does not return a financial time series. Pull those from the filings it identifies:
seven years of revenue, net income, D&A, capex, and working-capital lines. Never carry a
financial figure from memory into the bridge — every number in data point 1 traces to a
filing or to a line you derived from filed numbers.

## 1. Owner Earnings

```
Owner Earnings = Net income (as reported)
               + Depreciation, depletion & amortization
               + Other non-cash charges, EXCLUDING stock-based compensation
               - Maintenance capital expenditure   (derived, 5-7 year window)
               - Additional working capital required
               - Stay-in-business costs not booked as capex
```

Stock-based comp stays as an expense — it is non-cash but it is a real cost to owners.
Do not add it back.

Maintenance capex is the number everyone skips and the one that decides the answer. Derive
it, do not guess: Greenwald method, working-capital rules, and industry adjustments in
[owner-earnings.md](references/owner-earnings.md).

## 2. Intrinsic Value

Ten years of discounted owner earnings plus a terminal value.

**Data point 1 is produced by the script.** Write the filing figures into a JSON input
file ([format](references/input-schema.md)) and run:

```bash
uv run scripts/valuation.py input.json
```
 The script applies the
caps, the floor, the Greenwald derivation and the tier multiple, and prints the bridge,
the weak-input flags and the terminal-value share for you to report. Its output is the
arithmetic; the reasoning around each number is still yours to write.

The rules it enforces, so you can read a result and know what produced it:

**Growth.** Years 1-5: the lower of the 5-year owner-earnings CAGR, the 5-year revenue
CAGR, and 15%. Years 6-10: the lower of that rate and 10%. The caps bind regardless of
consensus, guidance, or recent history — a company that grew 30% for five years does not
get 30% here.

**Discount rate.** `max(10%, 10-yr Treasury + premium)`, plus 2-5% country risk outside the
US. The 10% floor is what stops a low Treasury yield from inflating every valuation, so
below roughly a 6% Treasury the floor binds for the top tiers and the premium stops
separating them. That is intended — moat quality does its work in the terminal multiple.

| Moat tier | Premium | Terminal multiple | Implied perpetual growth at 10% |
|---|---|---|---|
| Inevitable | +3% | 15× | 3.1% |
| Formidable | +4% | 13× | 2.1% |
| Strong | +6% | 11× | 0.8% |
| None | +8% | 9× | −1.0% |

**Terminal value** = year-10 owner earnings × the multiple above. This replaces a perpetual
growth rate; do not apply both. Every multiple sits below the ~19× that GDP-rate perpetual
growth would justify at a 10% discount, so the terminal value is already conservative before
the 70% haircut lands on top. You are being conservative twice — that is the design, but say
so rather than presenting the result as neutral.

**Margin of safety:** report IV × 0.70 as data point 2. Fixed at 70%, not varied by tier —
tier already moved both the discount rate and the terminal multiple.

Worked example, computed end to end under these exact rules, in
[owner-earnings.md](references/owner-earnings.md).

## 3. Moat Classification

| Tier | Test it must pass |
|---|---|
| **Inevitable** | Dominant 20+ years, permanent customer need, raises prices through inflation, competitors structurally cannot catch up |
| **Formidable** | Very hard to displace — switching costs, network effects, regulatory capture — but a determined giant could try |
| **Strong** | Real advantage, disruption plausible: regional dominance, specialized expertise, customer habit |
| **None** | Everything else, including "we can't tell from the disclosure" |

Name the mechanism, not the outcome. "Strong brand" is not a classification; "customers pay
40% more for a chemically identical product and have for 50 years" is. Then state what
would break it.

The tier sets the discount premium and the terminal multiple, so it changes data point 1.
Assign it before computing, and say which way the number moves if you are wrong by one tier.

## 4. Management Evaluation

**Green flags:** ROIC >20% sustained a decade; buybacks executed at low multiples rather
than at highs; mistakes admitted specifically in shareholder letters; conservative
accounting; meaningful personal ownership alongside below-peer cash comp; dividends only
after reinvestment opportunities are exhausted.

**Red flags:** "adjusted" earnings given more prominence than GAAP; serial acquisitions
above 20× earnings; macro blamed for company-specific underperformance; related-party
transactions; options repriced after the stock falls; capital allocation that contradicts
stated strategy.

Report which are present with the disclosure each came from. A red flag is reported, not
scored and not netted against the green flags — and it does not stop the valuation. The
reader decides what it costs.

## Common Mistakes

| Mistake | Fix |
|---|---|
| Valuing off reported net income or EPS | Build the owner-earnings bridge; the gap between them is the point |
| Treating total capex as maintenance capex | Split it; growth capex is optional, not a cost of staying alive |
| Adding stock-based comp back as a non-cash charge | It is a real cost to owners. Leave it as an expense |
| Discount rate below 10% because CAPM said so | The floor is not negotiable, whatever the risk-free rate does |
| Applying both a terminal growth rate and a terminal multiple | The multiple replaces the growth rate. One or the other |
| Reporting a range, or high/base/low | One number. The assumptions carry the uncertainty |
| Extrapolating recent 30% growth | Caps are 15% then 10%. They bind |
| Terminal value doing 80% of the work | Say so on the line. It is a fact about the business, and the reader needs it |
| Ending with "this looks cheap" or "I'd pass" | Report EV and IV side by side. The comparison is the reader's |
| Refusing to value because the business is unpredictable | Produce the number, flag the weak input beside it |
| Financial figures recalled rather than pulled | Every number traces to a filing |
| Discounting the flows by hand | Run `scripts/valuation.py`. Hand arithmetic is where the caps and the floor quietly stop binding |
