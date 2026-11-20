# Embedded ad image generation

This is an executable workflow using an available native image tool, not just a prompt-writing checklist. The transcript basis is T01 hook/body/CTA, T02 angle expansion, T04 format selection and T09 concept-first AI production. The production and review methods below are operational extensions, not word-for-word training claims.

## Choose the right deliverable
- Static ad, product/lifestyle image or edit requested: produce the actual image when tools and authorization allow.
- Script, storyboard, concept or image prompt requested: deliver that artifact; do not consume generation usage unnecessarily.
- Existing image with a requested change: edit the image, preserving everything the user did not ask to change. Inspect local targets before editing. Distinguish edit target, product reference, logo asset and style reference.
- Batch request: produce the requested distinct assets, not one near-duplicate repeatedly. Keep a coherent product/brand identity. Use native calls rather than switching to a billed batch API without authorization.

## From buying motivation to visual concept
Establish audience/awareness, one buying motivation, one angle, actual offer, verified proof, destination and requested placement. Pick a visual mechanism that makes the reason to care visible: show a process, clarify an objection, make a credible contrast, demonstrate the product, or connect it to a recognizable use moment. A product floating over a gradient is not automatically a persuasive concept.

Choose only the relevant design family:
| Concept family | Visual mechanism | Evidence constraint |
|---|---|---|
| Demonstration | Product or workflow doing the useful action | Real product behavior; synthetic scene must not fabricate results |
| Objection answer | Show how a specific purchase barrier is resolved | Actual policy/process; no invented guarantee |
| Value/offer | Make meaningful inclusions and one next action easy to scan | Verified inclusions and price; no fake bonus valuation |
| Comparison | Show a relevant feature/process distinction | Matched conditions and evidence; do not invent competitor defects |
| Founder/process | Make accountability or real work visible | Authorized genuine person/facility; no invented identity |
| Statistic/proof | One useful number and readable source context | Verified source and correct interpretation; no fake dashboard |
| Native phone/notes | A direct, specific argument in an appropriate native style | Real evidence/wording; do not forge customer messages or reviews |
| Lifestyle/identity | Put the product in a relevant use context | Preserve product and avoid implied fabricated endorsement |

If alternatives are useful, vary the motivation, argument or format deliberately. Changing background colour alone is a visual variant, not a new strategy. Recommend one direction when the user wants a single ad. Do not force an arbitrary three-concept approval step before generation already requested.

Read [evidence and release checks](evidence-and-release-checks.md) for product provenance, exact variants, conflicting commercial claims and pixel-fidelity limits.

## Build a concrete brief
Record creative_id and the test hypothesis where helpful. State:
- Buyer, buying context, awareness and one intended action.
- The reason to care and how the image will demonstrate it.
- Exact product/reference assets and invariants: shape, packaging, label, colour, material, logo, approved people/likenesses.
- One dominant focal point; the reading order among headline, visual, offer/proof and CTA. Use supporting elements only when they add meaning.
- Composition, scene, camera/framing, light and material detail that support the actual offer and brand. Prefer credible product-specific detail over generic luxury adjectives or arbitrary neon decoration.
- Exact short in-image text in quotation marks and language/script. Keep essential qualification visible. Do not bury a condition in unreadable small print or duplicate the entire primary text inside the image.
- Intended crop/aspect ratio and room for platform overlays. Feed portrait, square or vertical placements are creative choices; verify current placement specifications before claiming upload readiness. Never guarantee perfect crops from a mismatched generation size.

Respect the user's supplied design direction. Do not invent brand colours, slogans, props or people simply to fill the canvas. If product fidelity depends on a missing reference, request that specific asset; continue copy/concept work independently. A fictional/demo image may proceed with clear labelling when that is the authorized task.

## Prompt for the image tool
Use only the relevant fields of this structure; it is a brief, not tool argument syntax:
```
Use case: ads-marketing
Output: [static ad / product image / edit], [placement and aspect]
Audience and purpose: [specific buyer and one action]
Core message: [one reason to care]
Inputs: [image 1 product/edit target; image 2 logo/style; roles]
Scene and subject: [concrete depiction of the mechanism]
Composition: [framing, focal point, reading order, copy area]
Look: [appropriate medium, light, materials, credible environment]
Text verbatim: "[headline]" / "[approved offer or qualification]" / "[CTA]"
Preserve: [real product/brand/likeness invariants]
Avoid: [specific misleading claims, fake evidence, extra text, visual defects]
```
For an edit say: change only X; preserve Y and Z. Re-state invariants on subsequent edits. Keep prompts focused; contradictory directions and excessive element lists reduce clarity. Do not rely on unsupported model, size, quality or output-path arguments. Use the live tool schema.

## Execute actual generation or editing
Use the native image-generation tool by default. Load and inspect local edit targets with the available image viewer first. Use the exact supported image-reference mechanism; do not invent filesystem-path support. For transparency request genuine alpha and preserve it. If no native tool exists, report the limitation. Do not silently switch to another model, third-party provider or API billed separately.

Generating or editing when explicitly requested uses the permitted native workflow; do not purchase credits or exceed an explicit no-credit/no-generation limit. For a no-spend test with no confirmed included generation allowance, produce only the authorized concept/brief and mark rendering not exercised. Never describe a code-drawn placeholder as an image-generation test. Configuration work alone does not authorize sample generation; an explicit image-evaluation request does, within the stated usage limits.

## Inspect and revise
Read [visual review](visual-review.md) and inspect the returned image rather than inferring success from a tool response. Check exact text, product identity, crop, hierarchy, visual proof, artifact defects and agreement with landing-page claims. Use a small/mobile preview when feasible. Correct the most important issue with a targeted image edit; preserve successful elements. Avoid uncontrolled regeneration loops: stop when the request is met, or when the tool/authorization boundary prevents correction, and state what remains.

Return the actual image in chat and a usable artifact path/link where provided. For workspace-bound assets copy/preserve the final output in the requested project location and avoid overwriting unrelated assets. Attach matching primary text, headline, CTA and the test hypothesis concisely. An attractive image is not evidence of conversion, real product quality or campaign performance. Publish/upload/launch only when separately authorized.

For examples of stronger visual arguments, consult [image brief examples](image-brief-examples.md) when needed.



## Real-reference acceptance
Check the generated result beside the exact source: model/edition, colour, print/label, controls/closure and overall proportions. Record visible matches and unresolved details, not a fabricated preservation percentage. If the generator has changed identity-critical artwork or packaging, revise through the native edit tool and re-check. If fidelity remains inadequate, deliver it as an incomplete concept, not a finished product ad. Keep actual source URLs and images in the task's evidence folder; do not silently add third-party product images to the private training library.
