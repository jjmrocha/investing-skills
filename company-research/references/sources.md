# Where the Documents Live

Organised by document type. Filing regimes differ by jurisdiction; the work does not.

## Annual report

The primary source. Read the footnotes, not just the narrative.

| Where | What it's called | Find it at |
|---|---|---|
| US domestic | 10-K | EDGAR, or the company's investor relations site |
| US-listed foreign issuer | 20-F | EDGAR |
| UK | Annual Report & Accounts | Company IR; RNS via the London Stock Exchange news service |
| EU | Annual financial report | Company IR; the national officially appointed mechanism (OAM) |
| Portugal | Relatório e Contas | CMVM (`sistemas.cmvm.pt`); company IR |
| Canada / Australia | AIF / Annual Report | SEDAR+; ASX announcements |
| Japan | Yūka shōken hōkokusho | EDINET |
| Private | Statutory accounts | National companies registry (Companies House, IRN, Handelsregister) |

**Footnotes worth going to directly:** customer and supplier concentration; segment detail; litigation and contingencies; debt maturities and covenants; related-party transactions; revenue recognition policy; pension obligations; any reserve, with its year-over-year movement.

## Interim report

10-Q in the US. Half-year reporting is the norm in much of Europe — a missing quarterly is a disclosure-regime fact, not a gap in your research, and should be described as such.

## Results calls

| Source | Notes |
|---|---|
| Company IR — webcast and slides | Always check here first; often the only free transcript |
| Seeking Alpha, Motley Fool, Quartr | Transcripts, US-heavy coverage |
| Investor day / capital markets day | Multi-year targets stated more explicitly than on quarterly calls |

Read the Q&A, not only the prepared remarks. What analysts press on repeatedly, and what management declines to answer, is signal.

## Ownership

| Source | What it gives |
|---|---|
| US proxy (DEF 14A) | Beneficial ownership table, insider holdings, compensation |
| SEC 13F / 13D / 13G | Institutional positions, activist stakes |
| EU/UK major-holdings notifications | Crossings of 3%/5% thresholds |
| Company IR — shareholder structure page | Often the fastest route outside the US |

## Material events

8-K in the US; RNS or equivalent regulatory news service elsewhere. Sweep from the annual report date forward.

## Employee sentiment

Glassdoor primarily — rating, review count, and whether the trend is moving. Indeed and local equivalents where Glassdoor coverage is thin. Read the negative reviews for recurring specifics, not the star count alone. Small-sample ratings for a subsidiary or a single country office are not the company.

## Customer and product evidence

G2, Capterra and Gartner Peer Insights for software and enterprise; app store ratings for consumer apps; trade press and clinician or practitioner forums for regulated products; retail reviews for consumer goods. Some companies — industrial suppliers, contract manufacturers — have no reviewable surface at all. Say so rather than reaching.

## Searching EDGAR

The full-text search UI is at `https://www.sec.gov/edgar/search/`. Company filing indexes are at `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=<ticker>&type=10-K`.

**SEC servers return HTTP 403 to requests without a declared User-Agent.** Browser-style fetch tooling will fail. Use a request that identifies you:

```bash
curl -s -A "Your Name your@email" "https://www.sec.gov/Archives/edgar/data/<CIK>/<accession>/<file>.htm"
```

Filing documents are large HTML; strip tags before reading, and search within the text rather than reading linearly.

## Source quality

- **Primary over secondary.** Filing beats press release beats news article beats blog.
- **The press release is the company's summary of itself.** It is a pointer to the filing, not a substitute for it.
- **Check non-GAAP against the reconciliation.** Adjusted figures exclude something; find out what.
- **Date everything.** A figure without its fiscal period is unusable.
- **Two independent sources** for any claim that carries weight.
- **Never cite a page number.** Cite document and section.
