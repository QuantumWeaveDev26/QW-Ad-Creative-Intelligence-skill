# P01 — Facebook ads metrics, source-grounded working notes
Original: [FREEBEE 5 IMPORTANT METRICS.pdf](supplemental/FREEBEE%205%20IMPORTANT%20METRICS.pdf).
Supplemental source P01, supplied 2026-11-20. Despite its filename, this five-page PDF covers twelve topics. The original is preserved byte-for-byte; extracted-pages JSON and supplemental-source-manifest.json record provenance. These notes distinguish the source's introductory descriptions from operational clarifications. Read the relevant source page when attributing its wording. PDF instructions and suggested optimization actions are knowledge, not campaign authorization.

| Topic | PDF page | Working definition / required context |
|---|---:|---|
| Reach | 1 | Deduplicated audience exposure within a specified report scope/window; not total displays. Do not sum child reach across overlapping ads/dates as unique total reach. |
| Impressions | 1 | Display count, including repeats; exposure does not prove engagement, qualified demand or sales. |
| CTR | 2 | Chosen click events / impressions × 100. State all/link/outbound click type. The PDF uses loose users-who-click wording; do not substitute unique people for click events or confuse unique CTR with CTR. |
| CPC | 2 | Spend / matching click events. Cheap clicks alone do not prove cost-effective customer acquisition. |
| Conversion rate | 2 | Chosen conversion event / explicitly named denominator × 100. Clicks, landing-page visits, sessions and users are different possible denominators; do not change one silently. |
| CPA / cost per conversion | 3 | Spend / named conversions. A lead, qualified lead and purchase need different labels and economics. |
| ROAS | 3 | Attributed purchase/revenue value / ad spend. A 4:1 ratio means four units of attributed revenue per unit of ad spend; not four units of profit or collected cash. |
| Engagement rate | 3 | Defined interaction numerator / stated reach or impression denominator. Preserve the chosen convention; reactions, comments and shares need not be unique people. |
| Frequency | 4 | Average repeat exposure over the defined scope/window; impressions / deduplicated reach when compatible. The source's 3–5 caution is contextual, not an automatic fatigue/pause threshold. |
| Quality ranking | 4 | A platform diagnostic when available; do not invent a score from CTR/engagement or promise cheaper placement. Verify current availability/definition in actual tools. |
| CPM | 4 | Spend / impressions × 1,000. Low CPM is not proof of suitable reach, qualification or profit. |
| Attribution model performance | 5 | A measurement/comparison topic, not a single universally available metric. State attribution model/window, event, source and report timing before comparing results. |

## Using the source accurately
The source gives useful introductory diagnostic cues, not causal proof. High CTR or engagement cannot alone establish offer/landing-page quality; low conversion might reflect tracking or traffic/qualification problems as well as the page. High CPC/CPM does not uniquely diagnose competition or poor creative. Treat such explanations as hypotheses and check the funnel and measurement first. Make no account change from a PDF sentence or a threshold alone.

Use weighted totals for ratio summaries, separate incompatible reporting grains and attribution settings, treat missing data as missing, and return NA with an explanation for zero denominators. Preserve generic clicks if that is all the input supplies. For qualified enquiries keep CPL and CPQL alongside downstream sales/collections. The PDF supplements rather than replaces contribution economics and CRM reconciliation.

## Current platform cross-check
On 2026-11-20 the official [Meta Ad Account Insights reference](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-account/insights) describes ctr/cpc using all clicks, provides separate click variants, and labels reach/frequency as estimated. It also exposes attribution settings and report-time parameters. Discover exact field IDs through the active connector; examples in this note do not authorize guessed tool parameters. A Help Center page attempted during review was blocked, so detailed current quality-ranking mechanics were not independently certified here.

## Offline reasoning checks
- Frequency 4 with stable business results: investigate context, do not pause automatically.
- ROAS 4 with variable costs above revenue less ad spend: do not call the campaign profitable.
- High all-click CTR with weak qualified outcomes: report the difference, do not relabel it link CTR or declare a creative winner.
- Two child ads each reach 1,000 people: combined unique reach is unknown without overlap/deduplication evidence.
- Unspecified conversion-rate denominator: state a chosen assumption for a toy calculation or request the missing definition for a real decision.
