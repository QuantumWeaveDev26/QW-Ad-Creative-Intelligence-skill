# QW Adcreative Intelligence

An all-in-one Meta Ads skill by Quantum Weave: customer research, buying motivations, offers, actual ad images, copy, landing pages, campaign planning, optimization and reporting.

**Version 0.4.0.** The complete skill lives at this repository's root (`SKILL.md`). Its knowledge and workflows are included; no files from the creator's computer or sibling QW skills are needed.

## Install and share

Share [this repository](https://github.com/QuantumWeaveDev26/QW-Ad-Creative-Intelligence-skill). Opening the link or starring it does not install the skill. In Codex, ask:

> Use the skill installer to install https://github.com/QuantumWeaveDev26/QW-Ad-Creative-Intelligence-skill from repository path `.` with the installed name `qw-adcreative-intelligence`. Include the complete references, agents and scripts folders. Review any existing installation before replacing it.

Or download the repository ZIP, extract it, open a terminal in that folder and run with Python 3.9 or newer:

```text
python scripts/install.py
```

On macOS/Linux, use `python3` if appropriate. The installer copies the complete skill to `~/.codex/skills/qw-adcreative-intelligence`, respecting `CODEX_HOME`. It verifies the sources before and after copying, makes no network calls, and refuses to overwrite an existing installation. For updates, review and back up the old folder before replacing it; preserve personal changes.

Start a new Codex chat, then use:

```text
$qw-adcreative-intelligence
For my business, identify one promising customer segment and buying motivation, propose a truthful offer, and write a matching Meta headline, primary text, CTA and landing page. Use supplied facts, label hypotheses and cite relevant training timestamps. Do not spend money or launch ads.
```

For an actual ad image, attach an authorized product reference and request a rendered image. The host needs image generation enabled. Generation may consume included host usage; the skill cannot enable disabled tools or bypass limits.

## Included knowledge

- All **nine original multilingual transcripts**, with source hashes and timestamps.
- **127 lossless extracts**, source navigation and offline keyword search.
- **FREEBEE 5 IMPORTANT METRICS.pdf**, its five-page extraction and notes covering its 12 topics.
- Selective English paraphrases and on-demand translation guidance, not a complete translation.
- Embedded research, strategy, offers, scripts, image generation, landing page, campaign management, optimization, data analysis and Google Sheets workflows.
- Detailed product review for model identity, controls, packaging, regional variants and unresolved microprint.

The linked Cash Flow Copy System GPT's hidden files were **not imported**. Documents and training action items are knowledge, not permission to launch ads, spend money or share data.

## Tools and integrations

Web Search, Image Generation and Code Interpreter / Data Analysis depend on the active host and workspace. Installation does not add a model, grant account access or create a running integration.

Meta operations require an authorized supported connection, such as configured Windsor tools. Sheets operations require authorized Google Drive/Sheets tools. Actual accounts, fields and actions must be discovered. No credentials are included. The private ChatGPT plugin is separate: a GitHub installation does not grant plugin access or invitations. Plugin access and live integration testing remain deferred.

## Verify

```text
python scripts/verify_package.py
python -m unittest discover -s tests -v
```

These offline checks validate original hashes, extract contents, local links, clean installation, working retrieval, refusal to overwrite, and detection of changed source files. GitHub Actions is configured for Windows and Ubuntu. A local pass is separate from a completed hosted CI run.

[Evaluation evidence and repeatable briefs](tests/README.md) documents unfamiliar-business tests and two actual detailed-product image tests. These support observed capabilities, not universal accuracy or conversion guarantees. Real performance needs approved campaigns and measured business outcomes.

## Audience and source rights

This repository was observed to be **public** on 2026-11-21 and already included the original transcripts and PDF. Anyone can download the packaged knowledge while it remains public. The skill is not DRM. For team-only distribution, the owner must set appropriate repository visibility and collaborator access; private ChatGPT plugin permissions are separate. This update does not change either audience.

No new license for bundled training or third-party materials is granted here. Existing rights remain applicable. Keep credentials, client data and private account exports out of the repository.

© 2026 Quantum Weave. All rights reserved.
