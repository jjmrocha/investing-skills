# buffett-valuation

What a business is worth to an owner, as four numbers you can check.

## What it does

Answers one question — what is this whole company worth — and returns four data points, each
with the reasoning that produced it:

1. **Intrinsic value.** One number for the whole company, from a discounted owner-earnings
   model. Shows the bridge from reported net income, how maintenance capex was derived, the
   growth rates and where they came from, the discount rate build, and the terminal multiple.
2. **Intrinsic value × 70%.** The same number with the margin of safety applied.
3. **Moat tier.** Inevitable, Formidable, Strong, or None — with the mechanism behind it and
   what would break it.
4. **Management.** Green flags met, red flags present, each sourced to a disclosure.

Above them sits the enterprise value — market cap + debt − cash — and the date it was taken.

## What it deliberately doesn't do

**It never gives a verdict.** No buy, no pass, no watch list, no target price. It puts
enterprise value and intrinsic value side by side and stops. The comparison is yours: the
business is cheap when intrinsic value exceeds what it costs to own the whole thing, and
what to do about that is a judgment the skill doesn't make for you.

**It never refuses.** There is no "too hard" exit. An unpredictable business still gets a
number, with the weak inputs flagged on the lines where they were used. A judgment about
whether the number is worth trusting is yours too.

**It never reports a range.** The DCF returns a value; you get that value. The uncertainty
lives in the assumptions, stated where you can move them.

## When it triggers

"What is X worth", "is X cheap", "is X overvalued", "value X for me", "run a DCF on X",
"does X have a moat", "can I trust this management".

## The opinions it holds

Maintenance capex is the number everyone skips and the one that decides the answer, so it
gets derived from the Greenwald method rather than approximated by total capex.

Growth caps at 15% for years 1-5 and 10% for years 6-10 regardless of what the company has
recently done, and the discount rate has a hard 10% floor whatever the Treasury yield does.
The floor exists so that cheap money doesn't quietly inflate every valuation — which means
in a low-rate environment it binds for the best businesses and the moat premium stops
separating them. Moat quality does its work in the terminal multiple instead.

Terminal value is an exit multiple set by moat tier, not a perpetual growth rate — 15× down
to 9× of year-10 owner earnings. Every one of those sits below what GDP-rate perpetual
growth would justify, so the terminal value is already conservative before the 70% haircut
lands on top. The skill says so in its own output rather than presenting the result as
neutral.

Stock-based compensation is an expense, not a non-cash charge to add back.

The arithmetic is a script, not a habit. Growth caps, the discount floor and the terminal
multiple are the rules most easily lost to a persuasive story about why this company is
different, so they are enforced in code rather than left to be remembered.

## Comparing against enterprise value

Owner earnings starts from net income, so it is an after-interest figure, while enterprise
value includes the debt. Debt therefore counts on both sides. This is intentional: enterprise
value is what ownership actually costs, because buying every share means paying off the debt
too. It makes the test harder on leveraged businesses, and the skill documents it so nobody
later "corrects" it into an unlevered model.

## Pairs with

Run [company-research](../company-research/) first. It assembles the durability evidence,
capital-allocation history and disclosed risks that data points 3 and 4 are built from, and
it states no verdict — so nothing it hands over pre-empts the valuation. It does not return a
financial time series; the owner-earnings inputs come from the filings it identifies.

## Files

| File | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | The skill — output contract, valuation rules, moat tiers, management flags |
| [scripts/valuation.py](scripts/valuation.py) | `uv run scripts/valuation.py input.json` — computes the intrinsic value. Enforces the caps, the discount floor, the Greenwald derivation and the tier multiple so they can't be argued away |
| [references/input-schema.md](references/input-schema.md) | The script's JSON input format, and what it decides versus what you decide |
| [references/owner-earnings.md](references/owner-earnings.md) | Maintenance capex derivation, industry adjustments, negative-earnings cases, the Coca-Cola 1988 example computed under these rules |
| [examples/jnj-2026.json](examples/jnj-2026.json) | A filled-in input file — Johnson & Johnson, FY2021-25 |

See [SKILL.md](SKILL.md).
