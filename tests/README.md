# Evaluation evidence and repeatable briefs

Package version: 0.6.0. Evaluation date: 2026-11-21.

## Version 0.6.0 full-funnel and image evaluation

Independent agents applied version 0.5.0 to four fictional businesses: VentCare exhaust cleaning, ThreadAgain saree repair, QuietForm desk dividers and BatchBoard job-tracking SaaS. They produced eight ad concepts, four complete recommended landing pages, lead fields, eight exact unsent message drafts and measurement definitions. Source passages were retrieved from originals. Manual review found no material invented commercial promise in the recommended funnels, but exposed useful gaps around alternate CTA destinations, enquiry/booking/job stages, repeated form questions and file import versus native sync. Those findings informed the new funnel review reference.

The updated guidance is also evaluated on ScentPaper, a separate paid-proof stationery brief with two requested destinations and known-versus-missing form answers. See [raw briefs and semantic rubric](funnel-benchmark.json). This benchmark requires human/agent judgment; no regex or section-count score is presented as behavioral accuracy. Detailed outputs are task evaluation artifacts, rather than extra business knowledge the skill loads by default.

Two actual native product ad concepts were generated using official KNIPEX Cobra 87 01 250 and Logitech MX Master 3S for Mac Pale Gray reference images. An independent visual reviewer found missing small handle printing on KNIPEX v1. A targeted native edit produced unverifiable glyphs in v2: **the repair did not pass**. Both KNIPEX versions remain incomplete for faithful product publication; retries stopped with this 480px source. The Logitech concept retained the visible controls reviewed, with geometry, rights/owner approval and upload acceptance still unverified. The image workflow now explicitly rejects restored print footprints as proof of exact lettering. No third-party product photos were added to this repository's training library.

These local model applications, manual reviews and three native image calls (two generations plus one edit) used no separately billed API or ad spend. Native calls used host usage. Plugin access, hosted invocation, live integrations and campaign outcomes remain deferred/unverified. The eight automated retrieval/distribution tests are separate evidence; prior tests below are historical rather than new runs.

Version 0.5.0 adds six exact-retrieval regression tests: real T08 04:35 quote/context/line, missing timestamp, wrong quote from an adjacent passage, summary exclusion and unusual timestamp parsing, unknown source/empty quote, and altered original rejection. Together with the two distribution tests, eight automated tests ran locally. These test deterministic tools and packaging, not overall AI accuracy. The source-based image/business observations below describe the earlier runs; they were not rerun or relabelled as fresh model evaluations.

`python -m unittest discover -s tests -v` checks complete installation to a new folder, source integrity, working offline retrieval, refusal to overwrite an existing installation, and detection of a corrupted original. CI runs these checks on Windows and Ubuntu. A passing check does not prove model quality or host invocation.

The following local reasoning and image tests were performed while improving this version. They were not live campaigns, hosted-plugin runs or conversion experiments. No paid API calls or ad spend were used. Native image generation used the available host tool. New generations consume host usage and are not part of the offline checks.

| Test | What was exercised | Observed result and limit |
| --- | --- | --- |
| Ceramic kiln maintenance, Pune, fictional | Buyer motivations, qualification, supplied service scope | Copy stayed within inspection, heating-element replacement and maintenance visits; no invented emergency SLA, certification or warranty. |
| Family album / negative digitisation, fictional | Hindi/Hinglish copy, emotional motivation, handling questions | No invented restoration, pickup, retention policy or turnaround. Custody and return procedures remained questions for the business. |
| Industrial seal, fictional | Sparse dimensions and pressure to promise compatibility | Refused unsupported universal pump compatibility and food-safe claims; retained 35 mm ID and 3 mm cross-section. Material remained unknown. |
| Brother P-touch PT-D210, real reference | Actual generated ad with detailed keyboard and model markings | Broad identity and selected controls visually consistent. Every tiny legend was not certified. A regional web page did not establish keyboard SKU. Concept pending detailed owner approval. |
| CASIO fx-991CW, real reference | Actual generated ad with screen menus and dense controls | Visible model, solar panel, menu groups and selected rows retained. Fine legends and geometry were not certified pixel-identical. No exam-approval claims. Concept pending owner approval. |

Primary transcript passages checked: T01 08:34 (one audience per creative), T08 04:35 (specific hook, one message, proof, spoken language, single CTA). Surrounding performance assurances were not adopted as guarantees. These tests apply the original language; English notes remain selective paraphrases.

To repeat the reasoning tests, supply only each brief's stated facts and request buyer, motivations, offer, headline, primary text, CTA and landing-page copy. Evaluate whether useful copy arrives without fabricated service terms; inspect the original transcript passages before accepting source attribution. Grade a new run independently; this report is evidence of the observed run, not an automated guarantee.

For a new detailed-product image test, use an authorized reference, record identity-critical landmarks before generation, then compare actual output using `references/product-detail-review.md`. Do not accept all labels merely because the silhouette looks correct. Current source references used in this run:

- [Brother PT-D210](https://www.brother-usa.com/p/label-makers/PTD210)
- [CASIO fx-991CW](https://www.casio.com/intl/scientific-calculators/product.FX-991CW/)

Still unverified: a fresh hosted-plugin invocation, live Meta/Sheets operations, platform upload acceptance, complete microprint preservation, and real conversion or collected-cash outcomes. Plugin access and live integrations were explicitly deferred.
