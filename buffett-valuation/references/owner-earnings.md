# Owner Earnings — Derivation Detail

Loaded from `SKILL.md` when you need to compute the number rather than cite the formula.

## Maintenance CapEx (Greenwald method)

Total capex is not a cost of staying in business — part of it buys growth, which is
optional. Only the maintenance portion belongs in owner earnings.

```
Step 1: Compute capex / sales for each of the past 7 years
Step 2: Identify the years with flat or declining revenue
Step 3: Average the capex/sales ratio across those years = maintenance ratio
Step 4: Maintenance capex = maintenance ratio x current sales
        Growth capex      = current capex - maintenance capex
```

Excerpt from a 7-year window, showing only the years that qualified:

| Year | CapEx | Sales | Ratio | Revenue trend |
|---|---|---|---|---|
| 2010 | $400M | $5.5B | 7.3% | rising — excluded |
| 2011 | $385M | $5.4B | 7.1% | declining — counted |
| 2012 | $390M | $5.4B | 7.2% | flat — counted |

Maintenance ratio = average of the counted years = **7.15% of sales**.

If no flat or declining year exists in the window, extend the window. If the business has
never had one, use the lowest observed ratio, and flag on the line in your output that the
estimate is weak. Produce the number either way.

## Working Capital Adjustments

- Exclude cash held above operating needs (operating need ≈ 2% of sales)
- Add back deferred revenue — customer prepayments are float, not a liability to fund
- Subtract inventory growth in excess of the sales growth rate
- Normalize receivables to the historical collection period

## Industry-Specific Adjustments

| Industry | Adjustment |
|---|---|
| Insurance | Treat float separately from operating earnings; it is investable capital, not profit |
| Banks | Average loan-loss provisions across a full credit cycle, not the current benign year |
| Retail | Capitalize operating leases at 8x annual rent and treat as debt |
| Technology | Capitalize R&D and amortize over 5 years |

## When Owner Earnings Are Negative or Absent

Loss-making, pre-revenue, or a single distorted year. Still produce a number:

- **One bad year in an otherwise profitable history** — normalize across the cycle, use the
  7-year average as the base, and say that is what you did.
- **Structurally loss-making** — the DCF base is zero or negative, so the intrinsic value is
  driven entirely by the growth assumption reaching profitability. Report the value that
  falls out and state plainly that the terminal multiple is doing all the work.

## Stock-Based Compensation

SBC is a real cost to shareholders through dilution even though it is non-cash. Treat it as
an expense — do not add it back with other non-cash charges. State the convention in your
output so the reader can compare against models that treat it differently.

## Worked Valuation — Coca-Cola, 1988

Computed end to end under this skill's rules. Use it to check the shape of your own output.

```
Owner earnings (1988)          $828M
Moat tier                      Inevitable
Growth, years 1-5              15%   (cap binds)
Growth, years 6-10             10%   (cap binds)
Discount rate                  10%   (6% Treasury + 3% = 9%, floor raises it to 10%)
Terminal multiple              15x   (Inevitable)

Year-10 owner earnings         $2,682M
PV of years 1-10               $9,910M
PV of terminal value           $15,511M   ($2,682M x 15, discounted 10 years)

  1. Intrinsic value           $25.4B
  2. IV x 70%                  $17.8B
  3. Moat                      Inevitable — see tier test
  4. Management                Reported separately

Market cap at the time         $14.8B
```

The four data points and the price, side by side. No verdict follows — that is the whole
output.

**Why the famous $48.3B figure is different.** The widely cited 1988 valuation uses 15%
growth for all ten years, a 9% discount rate, and 5% perpetual growth thereafter, which
reproduces $48.3B exactly. This skill's rules cut it to $25.4B: the year 6-10 cap removes
the second five years of 15% growth, the 10% floor overrides the 9% rate, and a 15×
terminal multiple is far less generous than perpetual growth at 5% against a 9% discount,
which is worth 26×.

Both numbers sit above the $14.8B price. That is the point of the exercise — the conservative
rules cost you nothing on a business this good, and they are what stop you from reaching the
same conclusion about a business that is not.
