# Sources — 2026-11-06

Generated: 2026-11-06 (Asia/Bangkok)
Runtime: WEBFETCH mixed — most trusted-source domains DNS-blocked (techcrunch, theverge, openai, blognone, beartai, thairath, matichon, prachachat, thestandard, nectec, depa, deepmind, meta, nvidia, research.google, arxiv, wired, technologyreview, reuters, bloomberg, ft, theinformation). Reachable: microsoft.com, anthropic.com.
Freshness window: rolling 24h (Asia/Bangkok), i.e. 2026-11-05 ~ 2026-11-06
Dedup against: articles/2026-11-05-brief.md (0 URLs loaded — yesterday was a stub)

1. **Formally verifying agent-written full-stack web apps with PDD Kit**
   - Publisher: Microsoft Research
   - URL: https://www.microsoft.com/en-us/research/blog/formally-verifying-agent-written-full-stack-web-apps-with-pdd-kit/
   - Published: November 5, 2026
   - FreshnessCheck: ✅ within last 24h — publication date "November 5, 2026" surfaced in the fetched article body and listing page; 1 day before today 2026-11-06 Asia/Bangkok.
   - DedupCheck: ✅ URL not in YESTERDAYS_URLS (yesterday was a stub with zero URLs; host microsoft.com did not appear).
   - Verification: Tier 1 — WebFetch (microsoft.com responded 2xx; fetched headline, authors, body, and technical claims matched the research-blog listing page).
   - Summary: Microsoft Research introduces PDD Kit, a research-preview toolkit for "Proof-Driven Development" that turns a developer's intent into formal Verus specifications, has a coding agent produce Rust code plus proof annotations, and runs the proofs in CI. A 5,000-line case study on a Rust storefront (Axum/SQLite backend, Leptos/WebAssembly frontend) formally verified login logic with eight `ensures` clauses on `login_flow` and surfaced existing bugs. The authors flag it as a research prototype — Rust-only, proofs still take effort — and position it as a shift of review focus toward intent rather than a replacement for human review.

## Dropped
- Anthropic news index — latest post "AI for Science expands to foundations and research institutions" dated Oct 28, 2026 → Filter A (>24h, 9 days old).
- Microsoft Research — "From synthetic enterprise data evaluations to real Microsoft Copilot AI confidence" dated Oct 30, 2026 → Filter A (>24h, 7 days old).
- Catherine Wu moves from Anthropic to OpenAI (Nov 5) — surfaced only on newsbytesapp.com, which is NOT in `trusted-sources.md` → cannot cite.
- Fox News live blog "Anthropic IPO filing reveals AI security breaches, training halt" (10-27-26) — foxnews.com not in `trusted-sources.md`; and it is also Filter-A-aged (10 days).
- Yahoo Finance live Anthropic-IPO page — finance.yahoo.com not in `trusted-sources.md`.
- PDD Kit coverage on alphasignal.ai / hermes-ai.net / aiposthub.com — secondary blogs, not in `trusted-sources.md`. (Primary microsoft.com URL used instead.)
- Various "cheaper models" / Claude Opus 5.5 / GPT-6 rumours surfaced by cryptobriefing.com / kucoin.com / thejoai.com — none in `trusted-sources.md`.

> Note: 1 item passed both filters this run. Of ~15+ candidates surfaced by WebSearch/WebFetch probes, most failed Filter A (outside 24h window) and the remainder were on non-trusted-source domains. No Thai-language trusted source could be reached today — every allow-listed Thai domain (blognone, beartai, thairath, matichon, prachachat, thestandard, nectec, depa) returned DNS ENOTFOUND, and WebSearch did not surface any 24h-fresh article URL from those domains.
