# Integration contract — 2026-11-20
This is a skills package using existing apps, not a newly deployed API or background service. App IDs are copied from installed manifests. Each invited person needs an authorized connection or an explicitly available workspace connection. Plugin access grants neither Meta asset permissions nor Drive sharing.

## Meta Ads Manager through Windsor.ai
Discover tools. Use get_connectors to resolve accounts and connector ID; get_fields before get_data; get_options before selecting attribution or breakdowns; list_actions for exact action IDs and parameter schemas. Follow the active provider skill. Do not invent identifiers. ChatGPT Ads Manager is not a substitute for Meta Ads Manager.

Read plan: client/account, date interval, currency, account timezone, attribution, reporting level, conversion event, fields, filters, breakdowns, pagination and completion status. Missing data is not zero; pending pulls are not completed reports. Fetch only relevant client data.

Write plan: exact client/account/object IDs, current state, proposed parameters, creative assets, objective, budget mode/units/currency, schedule/timezone, destination, conversion event, business impact, authorizer and reversal. Complete a concrete preview before required confirmation. Explicit authorization is required for spend, activation, budget changes, purchases or paid-provider usage; provider confirmation rules also apply. New objects should be paused when supported. Re-read state and log actual IDs/status. Never blindly retry an uncertain creation. Preauthorized changes within a clear scope need no invented extra approval.

If a needed action is unsupported, report the gap and provide an exact manual Ads Manager change plan or assess a separately authorized direct Marketing API build. Skill text cannot create missing tools. Credentials never belong in plugin files, logs or Sheets.

## Google Sheets through Google Drive
Use active Sheets skills. Resolve exact spreadsheet/tab IDs, headers and bounded ranges before writing. Preview changes. Existing sources are read-only unless editing is authorized. Use an authorized destination and preserve unknown ranges. Batch appropriate writes, control upserts and verify cells/formulas afterwards. This package installs no continuous sync or schedule.

Daily fact key: client_id + account_id + date_start + date_stop + ad_id + attribution_setting + breakdown_key + action_type. Keep separate grains in separate tables. Upsert a defined recent interval for late conversions; never append duplicate facts. Record extraction time, completeness and report settings. Preserve IDs as text, financial values as numeric with currency metadata. Import untrusted text as literals (RAW where available), intentional formulas separately. Never sum reach across dates/ads as unique reach. Calculate ratios from totals, not means of ratios.

## Private team access
Use host private, invite-based distribution. No public listing or whole-workspace sharing. Suggested responsibilities: owner manages invitations, strategist drafts, buyer executes authorized changes, analyst reads/reports, reviewer approves. These are operating roles, not implemented custom RBAC. Enforcement is host sharing plus provider permissions. Resolve explicit recipients; never infer them from transcript names. A private link does not grant access. External guests depend on workspace support. Revocation must be checked at plugin, provider and Drive layers. Invitees can access packaged training.

## Official architecture references checked 2026-11-20
- https://developers.facebook.com/documentation/ads-commerce/marketing-api/insights — performance at account/campaign/ad-set/ad level; ads_read required.
- https://developers.facebook.com/documentation/ads-commerce/marketing-api/get-started/authorization — permissions and access depend on use case; re-check before a direct API build.
- https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.values/batchUpdate — write multiple value ranges.
- https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets.values/append — append is not an upsert.
Creative training is primary; current official documentation governs platform mechanics. Connected acceptance tests remain pending until accounts and a destination are selected.
