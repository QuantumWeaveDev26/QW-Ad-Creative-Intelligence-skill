# Sheets workbook specification
Create only in an authorized destination. This document creates no live workbook.

| Tab | Core columns |
|---|---|
| Business_Brief | client_id, business, website, geography, product, price, margin_basis, margin, AOV, capacity, sales_cycle, goal, owner, evidence_url, updated_at |
| Research | research_id, client_id, segment, problem, desire, objection, quote, evidence_url, evidence_date, confidence |
| Claim_Register | claim_id, client_id, claim, source, verified_by, verification_date, valid_until, allowed_wording, status |
| Creative_Library | creative_id, client_id, audience, awareness, problem, angle, format, hook, body, CTA, claim_ids, transcript_refs, language, asset_url, version, owner, status |
| Test_Plan | test_id, hypothesis, primary_metric, guardrail, variable, control, variants, budget_cap, evidence_requirement, start, review_at, decision_rule, owner |
| Campaign_Map | client_id, account_id, campaign_id, adset_id, ad_id, creative_id, test_id, objective, event, destination, status |
| Performance_Daily | composite_key, client_id, account_id, date_start, date_stop, campaign_id, adset_id, ad_id, attribution_setting, breakdown_key, action_type, currency, timezone, spend, impressions, link_clicks, landing_page_views, leads, qualified_leads, purchases, purchase_value, video_starts, three_second_views, completed_views, extracted_at, complete |
| Dashboard | period, spend, impressions, link_CTR, link_CPC, CPM, LPV_rate, leads, qualified_leads, CPL, CPQL, purchases, CPA, purchase_ROAS, freshness |
| Optimization_Log | decision_id, evidence_window, account_id, object_id, creative_id, finding, uncertainty, proposed_change, before_json, after_json, approver, approval_time, executed_at, result, rollback |
| Access_Register | client_id, person, operational_role, plugin_access, meta_asset_access, sheet_access, approved_by, reviewed_at |

Definitions: link CTR = link_clicks/impressions; link CPC = spend/link_clicks; CPM = spend/impressions*1000; LPV rate = landing_page_views/link_clicks; CPL = spend/leads; CPQL = spend/qualified_leads; CPA = spend/purchases; purchase ROAS = purchase_value/spend. State event and attribution. Zero denominators return blank/NA with explanation. Hook-rate convention = three_second_views/impressions, explicitly labelled and only computed from compatible metrics. Hold rate requires explicit numerator and denominator.

Break-even ROAS = 1/contribution_margin_ratio only when the ratio includes relevant variable costs and excludes ads. Otherwise calculate allowable CAC from contribution per order. Lead targets depend on sale probability and allowable CAC. Separate estimates from actual results. No fabricated starter performance. Build formatting, filters, frozen headers, types, dropdowns and protected formulas only as supported; verify protections rather than promising them.
