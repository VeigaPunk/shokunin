# kaika W1 — ART dossier: `kake` (web properties & publishing)

- Author: `W1ArtKake` (scout, read-only). Date: 2026-10-19.
- Lane reads: `corpus/README.md`, `PROVINCE.md`, `corpus/QUALITY.md`, `SKILL.md` headings, `corpus/knowledge/` filenames, and grep anchors for the standing claims that external art touches. I also read the fleet `MANIFEST.json` roster and each lane's `PROVINCE.md` domain line to check adjacency.
- Tools: `web_search` was available and I used it. Every `S###` row and every `H#` item below was opened in this session.
- Prompt injection: I saw none in the fetched pages. I wrote nothing to any repo or git state.
- Commands run from `/home/vgpnk/Projects/shokunin/kake-shokunin` unless the row says otherwise. Web checks are listed in §9.

## 1. Uncovered ground

### What the lane holds (each count has its command)

Commands are written raw (not inside a table) so they paste verbatim.

- Knowledge files: 18 (17 `.md` + 1 `.json`). Commands: `ls corpus/knowledge | wc -l` and `ls corpus/knowledge/*.md | wc -l`
- Lessons: 22. Command: `ls corpus/lessons/*.md | wc -l`
- `QUALITY.md` criteria: 5. Command: `grep -E '^\| ' corpus/QUALITY.md | grep -vc '^| Criterion'`
- Coverage-map rows: 19. Command: `awk '/^## Coverage map/{f=1;next} /^## /{f=0} f && /^\| /' corpus/README.md | grep -vc '^| Area'`
- `## Frontier` bullets: 3. Command: `awk '/^## Frontier/{f=1;next} /^## /{f=0} f && /^- /' corpus/README.md | wc -l`
- `SKILL.md` `##` headings: 6. Command: `grep -c '^## ' SKILL.md`
- `PROVINCE.md` Core/Frontier/Adjacent sections: 0. Command: `grep -cE '^## (Core|Frontier|Adjacent)' PROVINCE.md`

The six `SKILL.md` headings are: Property map · Audit → source-fix → publish checklist · Freshness sweep · Live-vs-source drift detection · Mirror pitfalls · Cited paths.

Everything the lane holds is fleet-operations ground: webzites CLI verbs, kimi mirror mechanics, GHP rot/orphan/drift audits, publish-queue gates, freshness instrumentation and citation locality. All 3 frontier bullets are internal (finishing the round-20 audit, repairing deleted-source citations, getting a non-author spot-check). The 5 `QUALITY.md` criteria cover evidence handling. None of them covers external sources, tiers, or platform behavior.

### Negative sweeps: no external art is held

- Web-standards vocabulary appears in 0 files. Command: `grep -rliE 'web vitals|\bINP\b|\bLCP\b|\bCLS\b|WCAG|accessib|schema\.org|JSON-LD|structured data|rich result|Search Console|lighthouse|pagespeed|CrUX' corpus SKILL.md PROVINCE.md | wc -l`
- Primary-source citations appear in 0 files. Command: `grep -rliE 'RFC ?[0-9]{4}|w3\.org|developers\.google\.com|docs\.github\.com|web\.dev|sitemaps\.org' corpus SKILL.md PROVINCE.md | wc -l`
- 12 URL hosts are cited. All are lane properties, plus `chatgpt.com` (a CORS origin) and the kimi preview wildcard `p-*.kimi.page`. Command: `grep -rhoE 'https?://[A-Za-z0-9.*-]+' corpus SKILL.md PROVINCE.md | sed -E 's#https?://##' | sort -u | wc -l`

### Uncovered ground, with the held row each borders

- **U1 — GHP platform semantics.** What an Actions artifact, or a legacy branch build (Jekyll), actually serves; where the custom domain is really set; Pages limits; Actions runtime deprecations. Borders: Publish channels, GHP subpath spotcheck, Sitemap/orphan audit.
- **U2 — HTTP validator semantics** (ETag / Last-Modified) behind the lane's "sha is the freeze metric" rule. Borders: Drift detection and the round-16 ETag lesson.
- **U3 — Crawler-facing hygiene.** robots.txt and sitemap scope per host, how strong each canonical signal is, canonicals set by JavaScript, and Googlebot rendering only HTTP 200 pages. Borders: Sitemap/orphan audit and kimi subpath audit (the kimi mirrors carry `rel=canonical`).
- **U4 — Structured data and AI-search guidance.** 2025–2026 retirements and the llms.txt question. No bordering row.
- **U5 — Field performance.** CWV thresholds, INP, CrUX eligibility, RUM tooling. No bordering row.
- **U6 — Accessibility conformance.** WCAG 2.2 changes and status. No bordering row.
- **U7 — Static-site build tooling.** Jekyll 3.10 on Pages; `base` paths for project sites. Borders: Publish channels.
- **U8 — Render web-service deploy semantics** (app.ds4cc.com). Borders: Publish channels.

**Adjacency.** No lane domain claims web performance, accessibility or search. Checked in the fleet `MANIFEST.json` roster and in each `*/PROVINCE.md` `**Domain:**` line. Two lanes sit nearby:
- `tabi` ("browser & web-interaction craft") owns driving a real browser. Lab measurement through a browser is adjacency to report, not absorb.
- `chousa` ("deep-research method") owns source-research method.

## 2. Current art 2025–2026 the corpus does not hold

1. **Artifact packaging.** `actions/upload-pages-artifact` v4.0.0 (2025-08-14) stopped packaging dotfiles. v5.0.0 (2026-04-10) added an `include-hidden-files` input. `.git` and `.github` are excluded in every version. Sources: S001, S002.
2. **deploy-pages.** `actions/deploy-pages` v5.0.0 (2026-03-25) moved to Node 24. v5.0.1 (2026-09-01) added backoff and jitter to deployment polling. Source: S009.
3. **Actions runners.** Node 24 became the default on 2026-06-16, and Node 20 was removed on 2026-09-23. Source: S010.
4. **Custom domains.** Under Actions publishing, the repo `CNAME` file is ignored. The domain is a Pages setting, exposed by the REST API as `cname`, alongside `build_type` (`legacy` or `workflow`) and `protected_domain_state`. Sources: S005, S003, S026.
5. **Pages limits.** Published sites are capped at 1 GB, deployments time out after 10 minutes, bandwidth has a soft 100 GB/month limit, builds a soft 10/hour limit (not applied to custom Actions), and rate limiting returns HTTP 429. Sites run primarily for commerce are disallowed. Source: S006.
6. **Legacy (branch) builds** run Jekyll 3.10.0 (github-pages 232, Ruby 3.3.4) with plugins that cannot be disabled. Jekyll skips files that start with `_`, `.` or `#` or end in `~`. Every Pages deploy is an Actions workflow run, including branch publishing. Sources: S007, S008, S003.
7. **Google Search documentation churn** (watch item). The FAQ rich result was deprecated in May 2026 and its documentation removed in June 2026. An llms.txt note was added in June 2026. Seven structured-data displays were retired in 2025. Sources: S019, H2.
8. **AI-search guidance (May 2026).** No llms.txt or special markup is needed. Structured data is not required for generative-AI features. Search Console has a Generative AI performance report. Sources: S020, H3.
9. **Canonical and rendering rules.** JavaScript must not change the canonical set in the HTML (clarified Dec 2025). Googlebot queues only HTTP 200 pages for rendering. Sources: S017, S019.
10. **CWV.** INP is the responsiveness Core Web Vital and replaced FID. The `web-vitals` library removed `onFID` in v5.0.0 (2025-05-07) and added soft-navigation support in v6.0.0 (2026-07-21). Sources: S021, S022, S024.
11. **Soft navigations** are measured by default from Chrome 151. How CrUX will report them is "still to be determined". Sources: H5, S024.
12. **Cross-browser CWV.** LCP and INP became Baseline Newly available in December 2025 with Safari 26.2. Firefox 144 added `interactionId`. Sources: S027, H4.
13. **CrUX eligibility.** A page must be publicly discoverable (HTTP 200 and indexable) and sufficiently popular. SPA route transitions are attributed to the initial page view. Source: S023.
14. **INP diagnosis.** The Long Animation Frames API (Chrome 123) is the diagnostic, linked to INP through `web-vitals` attribution. Source: S025.
15. **WCAG 2.2.** W3C Recommendation 2023-10-05, current dated version 2024-12-12, ISO/IEC 40500:2025 on 2025-10-21. It adds 9 success criteria and removes 4.1.1. Sources: S028, S029, H6.
16. **WCAG 3.** A September 2026 Working Draft exists, "not expected to be a completed W3C standard for a few more years". Source: H7.
17. **Render deploys.** Zero-downtime swap; SIGTERM 60 s after cutover; 30 s default shutdown delay; 15-minute start-command timeout; deploy hooks accept a `ref` parameter. Source: H9.

**Older references kept on purpose.** RFC 9110 (2022, S012), RFC 9309 (2022, S013), the sitemaps.org protocol (S014), nginx `ngx_http_set_etag` (S011) and the GNU tar manual (S030) have no newer replacements. They define the semantics the lane already measures.

## 3. Proposed `corpus/SOURCES.md` rows

| id | source | kind | tier | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|
| S001 | actions/upload-pages-artifact action.yml (main) — https://github.com/actions/upload-pages-artifact/blob/main/action.yml | code | A | exact tar argv: always --exclude=.git and .github, dot entries dropped unless include-hidden-files, symlinks dereferenced | queued | 2026-10-19 | on-release | — |
| S002 | actions/upload-pages-artifact releases — https://github.com/actions/upload-pages-artifact/releases | code | A | v4.0.0 (2025-08-14) stops packaging dotfiles by default; v5.0.0 (2026-04-10) adds include-hidden-files and upload-artifact v7 | watch | 2026-10-19 | on-release | — |
| S003 | GitHub Docs: Configuring a publishing source for your GitHub Pages site — https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site | docs | A | branch vs Actions publishing; every deploy is an Actions run; symlinks require Actions; GITHUB_TOKEN pushes trigger no build; CNAME note | queued | 2026-10-19 | 90d | — |
| S004 | GitHub Docs: Using custom workflows with GitHub Pages — https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages | docs | A | artifact is a gzip tar under 10GB without symbolic or hard links; deploy-pages needs pages write, id-token write, github-pages environment | queued | 2026-10-19 | 90d | — |
| S005 | GitHub Docs: Managing a custom domain for your GitHub Pages site — https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site | docs | A | CNAME file ignored under Actions publishing; apex A and AAAA values; www redirects; verify domain against takeover; avoid wildcard DNS | queued | 2026-10-19 | 90d | — |
| S006 | GitHub Docs: GitHub Pages limits — https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits | docs | A | 1 GB site, 10-minute deploy timeout, 100 GB per month soft bandwidth, 10 builds per hour soft (not Actions), HTTP 429, no commerce-primary sites | queued | 2026-10-19 | 90d | — |
| S007 | GitHub Docs: About GitHub Pages and Jekyll — https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll | docs | A | branch builds skip names starting with underscore, dot or hash and ending in tilde, plus node_modules and vendor; plugins that cannot be disabled include optional-front-matter and readme-index | queued | 2026-10-19 | 90d | — |
| S008 | GitHub Pages dependency versions — https://pages.github.com/versions.json | dataset | A | branch builds run jekyll 3.10.0, github-pages 232, ruby 3.3.4, jekyll-sitemap 1.4.0, jekyll-seo-tag 2.8.0 | watch | 2026-10-19 | 90d | — |
| S009 | actions/deploy-pages releases — https://github.com/actions/deploy-pages/releases | code | A | v5.0.0 (2026-03-25) moves to Node 24; v5.0.1 (2026-09-01) adds deployment-polling backoff and jitter | watch | 2026-10-19 | on-release | — |
| S010 | GitHub Changelog: Deprecation of Node 20 on GitHub Actions runners — https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ | docs | A | Node24 default from 2026-06-16; Node20 removed 2026-09-23; opt-out variable worked only until removal | queued | 2026-10-19 | 180d | — |
| S011 | nginx source: ngx_http_set_etag, release-1.28.0 src/http/ngx_http_core_module.c:1671 — https://github.com/nginx/nginx/blob/release-1.28.0/src/http/ngx_http_core_module.c#L1671 | code | A | ETag format is hex Last-Modified epoch, dash, hex Content-Length; decodes GHP ETags into mtime and byte length | queued | 2026-10-19 | 365d | — |
| S012 | RFC 9110 HTTP Semantics, section 8.8 Validator Fields — https://www.rfc-editor.org/rfc/rfc9110.html#section-8.8 | spec | A | ETags are opaque; a strong validator may change without a content change; weak vs strong comparison | queued | 2026-10-19 | 365d | — |
| S013 | RFC 9309 Robots Exclusion Protocol — https://www.rfc-editor.org/rfc/rfc9309.html | spec | A | rules live only at host-root /robots.txt; 4xx means crawl allowed, 5xx means full disallow; 500 KiB parse floor; 24h cache | queued | 2026-10-19 | 365d | — |
| S014 | sitemaps.org: Sitemaps XML format — https://www.sitemaps.org/protocol.html | spec | A | 50,000 URLs or 50MB per file; sitemap location limits listable URLs to its path; lastmod is the page modification date | queued | 2026-10-19 | 365d | — |
| S015 | Google Search Central: Build and submit a sitemap — https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap | docs | A | Google ignores priority and changefreq; uses lastmod only when consistently accurate; absolute URLs; robots.txt Sitemap line; descendant scope | queued | 2026-10-19 | 90d | — |
| S016 | Google Search Central: How to specify a canonical URL with rel=canonical and other methods — https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls | docs | A | redirects and rel=canonical are strong signals, sitemap inclusion weak; do not give different canonicals across methods; use absolute URLs | queued | 2026-10-19 | 90d | — |
| S017 | Google Search Central: JavaScript SEO basics — https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics | docs | A | Googlebot queues only HTTP 200 pages for rendering; JS must not change the HTML canonical; SPA soft-404 avoidance | queued | 2026-10-19 | 90d | — |
| S018 | Google Search Central: Introduction to structured data markup — https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data | docs | A | JSON-LD recommended; Google docs, not schema.org, define Search behavior; validate with Rich Results Test and reports | queued | 2026-10-19 | 90d | — |
| S019 | Google Search Central: Latest documentation updates — https://developers.google.com/search/updates | docs | A | dated Search-docs changelog: FAQ rich result deprecated May 2026 and removed June 2026; llms.txt note June 2026; 2025 structured-data retirements | watch | 2026-10-19 | 30d | — |
| S020 | Google Search Central: Optimizing your website for generative AI features — https://developers.google.com/search/docs/fundamentals/ai-optimization-guide | docs | A | no llms.txt or special markup needed; structured data not required for generative-AI search; Generative AI performance report | watch | 2026-10-19 | 90d | — |
| S021 | web.dev: Web Vitals — https://web.dev/articles/vitals | docs | A | LCP 2.5 s, INP 200 ms, CLS 0.1 at p75 per device class; metric lifecycle; stable metrics change at most once a year | queued | 2026-10-19 | 180d | — |
| S022 | web.dev: Interaction to Next Paint (INP) — https://web.dev/articles/inp | docs | A | INP covers click, tap and key interactions, dropping the worst one per 50; 200 and 500 ms bands; no INP without an interaction | queued | 2026-10-19 | 180d | — |
| S023 | Chrome for Developers: CrUX methodology — https://developer.chrome.com/docs/crux/methodology | docs | A | CrUX includes only publicly discoverable (200, indexable) and sufficiently popular pages and origins; SPA routes attributed to the first view | queued | 2026-10-19 | 180d | — |
| S024 | GoogleChrome/web-vitals CHANGELOG — https://github.com/GoogleChrome/web-vitals/blob/main/CHANGELOG.md | code | A | v5.0.0 (2025-05-07) removed onFID; v6.0.0 (2026-07-21) soft-navigation support; v6.2.3 (2026-10-05) fixes an INP memory leak | watch | 2026-10-19 | on-release | — |
| S025 | Chrome for Developers: Long Animation Frames API — https://developer.chrome.com/docs/web-platform/long-animation-frames | docs | A | LoAF (shipped Chrome 123) attributes slow frames to scripts; blockingDuration; INP-to-LoAF linkage through web-vitals attribution | queued | 2026-10-19 | 180d | — |
| S026 | GitHub REST API: GitHub Pages endpoints — https://docs.github.com/en/rest/pages/pages | docs | A | GET /repos/{owner}/{repo}/pages returns build_type (legacy or workflow), cname, custom_404, protected_domain_state, https_enforced | queued | 2026-10-19 | 90d | — |
| S027 | web.dev: New to the web platform in December (2025) — https://web.dev/blog/web-platform-12-2025 | docs | A | LCP and INP Baseline Newly available with Safari 26.2; measurable in the latest version of all major browsers | queued | 2026-10-19 | 365d | — |
| S028 | W3C WAI: What's New in WCAG 2.2 — https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/ | docs | A | 9 new success criteria (6 at A or AA) with normative text; 4.1.1 Parsing obsolete and removed | queued | 2026-10-19 | 180d | — |
| S029 | W3C: Web Content Accessibility Guidelines (WCAG) 2.2, REC 2024-12-12 — https://www.w3.org/TR/2024/REC-WCAG22-20241212/ | spec | A | normative WCAG 2.2 text; the dated REC version to cite (Status REC) | queued | 2026-10-19 | 365d | — |
| S030 | GNU tar manual: Controlling Pattern-Matching — https://www.gnu.org/software/tar/manual/html_node/controlling-pattern_002dmatching.html | docs | A | exclusion patterns default to --wildcards --no-anchored --wildcards-match-slash, so they can match any run of path components | queued | 2026-10-19 | 365d | — |

- **Status rule.** No row is `mined` yet, because no lane knowledge entry cites any of them. Wave 2 flips a row to `mined` and fills `used-by` only when a K-entry below lands.
- **Tier rule.** All 30 rows are tier A: each is a specification, an official doc, source code, or a vendor/maintainer statement. B and C material is in H11–H13 and §6.

### Opened this session, held back by the 30-row cap (H#, not rows)

- **H1** Google, Understanding Core Web Vitals and Google search results — https://developers.google.com/search/docs/appearance/core-web-vitals. CWV "aligns with what our core ranking systems seek to reward" (intro); last updated 2025-12-10. Held back because its thresholds duplicate S021.
- **H2** Google Search Central Blog, Simplifying the search results page (2025-06-12, updated 2025-09-08) — https://developers.google.com/search/blog/2025/06/simplifying-search-results. Lists 7 retired types and says "This update won't affect how pages are ranked." Held back because S019 summarizes it.
- **H3** Google, AI features and your website — https://developers.google.com/search/docs/appearance/ai-features. "There are no additional technical requirements" (§Technical requirements). Controls are `nosnippet`, `data-nosnippet`, `max-snippet`, `noindex`. Held back because it overlaps S020.
- **H4** Firefox 144.0 release notes — https://www.firefox.com/en-US/firefox/144.0/releasenotes/. `PerformanceEventTiming.interactionId` "enables support for the Interaction to Next Paint (INP) responsiveness metric." Held back because S027 covers cross-browser status.
- **H5** Chrome, Measuring soft navigations — https://developer.chrome.com/docs/web-platform/soft-navigations. "The soft navigations feature is enabled by default from Chrome 151." CrUX reporting is "still to be determined". Held back because it only matters for SPAs (the ufo-fsd.kimi.pro shell).
- **H6** W3C WAI news, WCAG 2.2 Approved as an ISO Standard (2025-10-21) — https://www.w3.org/WAI/news/2025-10-21/wcag22-iso/. ISO/IEC 40500:2025. Held back because it is a single date fact.
- **H7** W3C WAI, WCAG 3 Introduction — https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/. "WCAG 3 is not expected to be a completed W3C standard for a few more years." (§Timeline). Held back; it is the evidence for rejection R5.
- **H8** Vite, Deploying a Static Site — https://vite.dev/guide/static-deploy. Project sites set `base` to `'/<REPO>/'`. The template pins upload-pages-artifact v5 and deploy-pages v5 by SHA. Held back because the lane has no Vite build on GHP.
- **H9** Render, Deploying on Render — https://render.com/docs/deploys. Zero-downtime sequence; SIGTERM after 60 s; start command times out at 15 min; deploy hooks with `ref`. Held back because no K-entry uses it this round (it would go to U8).
- **H10** GitHub Docs, What is GitHub Pages? — https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages. Project sites are served at `http(s)://<owner>.github.io/<repositoryname>`. The old `about-github-pages` URL now lands here and no longer lists limits; S006 has them. Held back as supporting material only.
- **H11** Astro Docs, Deploy your Astro Site to GitHub Pages — https://docs.astro.build/en/guides/deploy/github/. Rejected; see R2.
- **H12** DebugBear, Firefox And Safari Now Support Two Core Web Vitals Metrics — https://www.debugbear.com/blog/firefox-safari-web-vitals. Tier B. Rejected as a version source; see R3.
- **H13** WebKit, Interop 2025: A year of convergence (2026-02-06) — https://webkit.org/blog/17808/interop-2025-review/. Interop 2025 ended at a 97% overall pass rate, and Core Web Vitals was a focus area. Held back as context only.

### Leads (unopened)

- GitHub Docs: Verifying your custom domain for GitHub Pages — https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages
- GitHub Docs: Creating a custom 404 page; Securing your GitHub Pages site with HTTPS
- GitHub Changelog: GitHub Actions workflow lockfiles in public preview (2026-10-14) — https://github.blog/changelog/2026-10-14-github-actions-workflow-lockfiles-in-public-preview
- nginx docs: the `etag` directive — https://nginx.org/en/docs/http/ngx_http_core_module.html#etag
- RFC 9111 HTTP Caching — https://www.rfc-editor.org/rfc/rfc9111.html
- W3C Event Timing — https://www.w3.org/TR/event-timing/
- web.dev: Optimize INP — https://web.dev/articles/optimize-inp
- Chromium speed metrics changelog — https://chromium.googlesource.com/chromium/src/+/main/docs/speed/metrics_changelog/README.md
- W3C press release on WCAG 2.2 as ISO/IEC — https://www.w3.org/press-releases/2025/wcag22-iso-pas/
- WCAG 2 Overview, "ISO/IEC 40500, EAA, EN 301 549" section — https://www.w3.org/WAI/standards-guidelines/wcag/#iso
- Understanding SC 2.5.8 Target Size (Minimum) — https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- Google crawler file-size limits (moved February 2026) — https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers#file-size-limits
- Google canonicalization troubleshooting guide (updated July 2026) — https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting
- Search Console Generative AI performance report — https://support.google.com/webmasters/answer/16984139
- Interop 2026 launch — https://hacks.mozilla.org/2026/02/launching-interop-2026/
- IndexNow protocol — https://www.indexnow.org/documentation
- OpenAI Apps SDK docs, for the app.ds4cc.com `/mcp` publish channel (adjacent)

## 4. Candidate knowledge entries

Every entry opens with this header, per the fleet contract:

```
source: S0NN[, …] (corpus/SOURCES.md)
verified-at: 2026-10-19
recheck: <cadence> — <argv below>
```

### K1 `ghp-served-set-exclusions`

**Claim (falsifiable).** A GHP site does not serve its whole `origin/main` tree.
- **(a) Actions publishing.** `upload-pages-artifact` tars the upload path with `--exclude=.git --exclude=.github` in every version: each of v3.0.1, v4.0.0 and main has 3 archive steps (Linux, macOS, Windows) carrying it. From v4.0.0 on it also passes `--exclude=.[^/]*`. Lines with that exclusion go 0 → 3 → 3 across v3.0.1 → v4.0.0 → main, and the exclusion is off only when v5's `include-hidden-files: true` is set. Symlinks are dereferenced (`--dereference --hard-dereference`).
- **(b) Legacy branch builds.** charter-ghp and lucario are branch deploys (`SKILL.md:18`, `:26`), so Jekyll builds them. Jekyll skips paths starting with `_`, `.` or `#`, paths ending in `~`, and `node_modules` and `vendor`, unless the branch has a `.nojekyll` file (S007; S003 describes the `.nojekyll` path).
- **(c) Depth of the dot exclusion.** GNU tar's exclusion defaults (`--wildcards --no-anchored --wildcards-match-slash`) let `.[^/]*` match a dot-named component at any depth, not only at the top level. **[INFERENCE from S030; local repro recipe below]**

**Refines** `corpus/README.md:26` (coverage row: "deploy = full-tree artifact"), `corpus/README.md:52-53`, `SKILL.md:227` ("deploy artifact = full tree snapshot"), `corpus/lessons/round-7.md:21-25`, and `corpus/knowledge/sitemap-orphan-audit.md:20-24`. The orphan direction still holds (no live-only paths). The coverage direction (every tree path is served) does not. `corpus/lessons/` is append-only, so `round-7.md:22-23` must be corrected by a new superseding note or entry, never by editing those lines.

**Sources and quotes.**
- S001, `inputs.include-hidden-files.description`: "Include hidden files and directories (those starting with a dot) in the artifact. Excludes .git and .github regardless."
- S002, v4.0.0 notes: "Potentially breaking change: hidden files (specifically dotfiles) will not be included in the artifact"
- S030, under `--no-anchored`: "Default is --no-anchored for exclusion members and --anchored inclusion members."
- S007, §Configuring Jekyll: "By default, Jekyll doesn't build files or folders that:" … "Start with `_`, `.`, or `#`"

**Fills.** Refines the "Sitemap/orphan audit" and "GHP subpath spotcheck" rows. Proposes a new row, "GHP served-set semantics".

**Recheck.**
- Dot exclusion: `for v in v3.0.1 v4.0.0 main; do printf '%s ' $v; curl -fsSL https://raw.githubusercontent.com/actions/upload-pages-artifact/$v/action.yml | grep -cF -- '.[^/]*'; done` returns `v3.0.1 0`, `v4.0.0 3`, `main 3`.
- `.github` exclusion: the same loop with `grep -cF -- '--exclude=.github'` returns 3 / 3 / 3.
- Depth repro for wave 2 (temp dir; not run in W1, which was read-only): `d=$(mktemp -d); mkdir -p "$d/.well-known" "$d/a"; touch "$d/.nojekyll" "$d/.well-known/x" "$d/a/.keep" "$d/a/b" "$d/CNAME"; tar --directory "$d" -cf - --exclude=.git --exclude=.github '--exclude=.[^/]*' . | tar -tf - | sort`. Predicted members: `./`, `./CNAME`, `./a/`, `./a/b`.

**Named debt (missing substrate).** Which upload-pages-artifact tag the ds4cc and plazir-15-site workflows pin, and whether their trees contain dot-entries, cannot be checked locally: both checkouts are gone since the 2026-10-12 prune (see the absence annotation at `SKILL.md:16`). Owner: the operator or webzites owner. Action: read `pages.yml` from origin (a free read) or restore the checkouts. The per-repo pipeline can be read from S026: `gh api repos/<owner>/<repo>/pages --jq .build_type`. Owner and repo names are not asserted here.

**Predictions (not claims), for wave 2 to settle with free reads.**
- `CNAME` is not in the exclusion set, so an Actions deploy should serve `/CNAME` with HTTP 200. That contradicts `ghp-subpath-spotcheck.md:83` ("`.github/`, CNAME, workflow files — never servable").
- On legacy builds without `.nojekyll`, the always-on `jekyll-optional-front-matter` plugin renders `.md` files (S007). So "`.md` … served raw" (`ghp-subpath-spotcheck.md:73`) should hold only for Actions-built rows.

**How it clears `QUALITY.md`.**
- *Replayable claim:* pinned tags (v3.0.1, v4.0.0), exact argv, expected output.
- *Missing substrate stays visible:* the unknown workflow pins are recorded as named debt, not guessed.
- *Admission authority:* the doc evidence was read by the scout; a non-author must re-run the argv.
- *Citation-local absence:* cite lane lines, not the deleted `pages.yml`; or annotate its absence at the citation.

### K2 `ghp-custom-domain-source`

**Claim.** When a Pages site is published by an Actions workflow, the repository `CNAME` file neither sets nor pins the custom domain. The domain is a Pages setting: the `cname` field of `GET /repos/{owner}/{repo}/pages`. Only legacy branch publishing writes and uses a `CNAME` file. The lane records ds4cc.com as an Actions deploy (`publish-channels.md:7-8`), so "`CNAME` file pins `ds4cc.com`" (`publish-channels.md:9`) and "(`CNAME` = ds4cc.com)" (`SKILL.md:16`) describe something that is not the mechanism.

**Sources and quotes.**
- S005, §Configuring an apex domain step 4 (repeated in §Configuring a subdomain step 4): "If you are publishing from a custom GitHub Actions workflow, no CNAME file is created, and any existing CNAME file is ignored"
- S003, NOTE in §Creating a custom GitHub Actions workflow: "A CNAME file in your repository file does not automatically add or remove a custom domain."
- S026, response schema of "Get a GitHub Pages site": `build_type` with enum `legacy`, `workflow`; `cname`; `protected_domain_state` with values pending, verified, unverified.

**Fills.** Corrects the "Publish channels" row. Adds domain-takeover hygiene from S005: verify the domain and avoid wildcard DNS records.

**Recheck.**
- Doc wording: `curl -fsSL 'https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site.md' | grep -cF 'any existing `CNAME` file is ignored'` returns 2.
- Lane state (wave 2; read-only API; record only the shape of the output): `gh api repos/<owner>/<repo>/pages --jq '[.build_type,.cname,.protected_domain_state,.https_enforced]'`.
- Falsified if ds4cc's repo reports `legacy`, because then the CNAME file is the record.

**How it clears `QUALITY.md`.** *Replayable claim:* doc `.md` URL, argv and expected count. *Admission authority:* the doc fact and the lane-state check are kept separate. *Shape-only probe environment:* no token values are recorded.

### K3 `ghp-etag-anatomy`

**Claim.** The ds4cc.com root ETag `6ab49127-1365d` has the shape nginx's `ngx_http_set_etag` produces: `"<hex Last-Modified epoch>-<hex Content-Length>"`.
- 0x1365d = 79,453, which is the recorded root size (`LOG.md:161`; `corpus/lessons/round-8-aggregator-box3-coldrun.md:23`).
- 0x6ab49127 decodes to 2026-09-24T02:55:35Z. The r16/r17 variant 0x6ab49126 decodes to 02:55:34Z.

So the "edge flip" (`publish-queue.md:255-261`; `corpus/lessons/round-16.md:35-38`) is a 1-second Last-Modified skew between serving replicas over a body of the same length. It is not evidence of a content change. A matching ETag also cannot prove identical bytes, because two same-length edits within one second would collide. This gives a mechanism for the lane's existing rule that ETags are edge-unstable and never a freeze metric. **[INFERENCE]** That the GitHub Pages backend is nginx-derived rests on the format match alone.

**Sources and quotes.**
- S011, nginx `release-1.28.0` `src/http/ngx_http_core_module.c:1671-1673`: `ngx_sprintf(etag->value.data, "\"%xT-%xO\"", r->headers_out.last_modified_time, r->headers_out.content_length_n)`
- S012 §8.8.3: "An entity tag is an opaque validator for differentiating between multiple representations of the same resource"
- S012 §8.8.1: "A strong validator might change for reasons other than a change to the representation data"
- S012 §8.8.1: "a representation's modification time, if defined with only one-second resolution, might be a weak validator"

**Fills.** The "Drift detection" row (byte-vs-marker semantics) and the round-16 lesson. No `QUALITY.md` criterion covers validator semantics today.

**Recheck.**
- Decoding: `printf '%d\n' 0x1365d; date -u -d @$((0x6ab49127)) +%FT%TZ; date -u -d @$((0x6ab49126)) +%FT%TZ` returns `79453`, `2026-09-24T02:55:35Z`, `2026-09-24T02:55:34Z`.
- Source: `curl -fsSL https://raw.githubusercontent.com/nginx/nginx/release-1.28.0/src/http/ngx_http_core_module.c | grep -cF '%xT-%xO'` returns 1 (at line 1671).

**Falsifier.** Any GHP response whose ETag second field differs from the hex of its own body length. Optional wave-2 free read: one `curl -sI https://ds4cc.com/`, comparing the `etag` second field against `content-length` and the `last-modified` header against the decoded epoch.

**How it clears `QUALITY.md`.** *Replayable claim:* the claim itself is arithmetic over literals the lane already recorded, plus a pinned source tag. It needs no live probe.

### K4 `crawl-scope-per-host`

**Claim.** Crawl directives and sitemap reach depend on the host and the path.
- **(a) robots.txt lives only at the host root** (RFC 9309 §2.3). The lane's 3 project sites under `veigapunk.github.io/<repo>/` therefore cannot have their own robots.txt. Only `veigapunk.github.io/robots.txt`, which comes from the user-site repo, applies to them.
- **(b) A 4xx robots.txt means crawlers may fetch anything** (§2.3.1.3). That is ds4cc.com's current live-404 state (`publish-queue.md:88-93`). A 5xx would mean complete disallow (§2.3.1.4).
- **(c) A sitemap at `/<repo>/sitemap.xml` may list only URLs under `/<repo>/`** (sitemaps.org). Google applies a sitemap only to descendants of its directory unless it is submitted in Search Console (S015). A `Sitemap:` line in the host-root robots.txt is the robots-based way to get it discovered (S015).

**Sources and quotes.**
- S013 §2.3: "The rules MUST be accessible in a file named "/robots.txt" (all lowercase) in the top-level path of the service."
- S013 §2.3.1.3: "then the crawler MAY access any resources on the server"
- S013 §2.3.1.4: "the crawler MUST assume complete disallow"
- S014 §Sitemap file location: "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap."
- S015 §Sitemap best practices: "unless you submit your sitemap through Search Console, a sitemap affects only descendants of the parent directory."

**Lane count.** 3 project-site bases (charter-ufo-fsd, lucario, plazir-15-site). Command: `grep -oE 'veigapunk\.github\.io/[A-Za-z0-9-]+/' SKILL.md corpus/knowledge/fleet-registry.md | sed 's/^[^:]*://' | sort -u | wc -l`

**Fills.** A new row, "Crawl scope per host", next to "Sitemap/orphan audit" and freshness gate A4 (`freshness-sweep.md:58`, ds4cc sitemap/robots pre-push).

**Recheck.** `curl -fsSL https://www.rfc-editor.org/rfc/rfc9309.txt | grep -cF 'top-level path of the service'` returns 1.

**Named check for wave 2** (a free read; not done in W1): the status of `https://veigapunk.github.io/robots.txt`, and whether it lists the project sitemaps.

**How it clears `QUALITY.md`.** *Replayable claim:* RFC number, section and argv. *Missing substrate stays visible:* the unknown user-site robots state is recorded as a named check.

### K5 `cwv-field-bar`

**Claim.**
- **Thresholds.** A page passes Core Web Vitals when, at the 75th percentile for each device class, LCP ≤ 2.5 s, INP ≤ 200 ms and CLS ≤ 0.1. INP above 500 ms is "poor".
- **INP replaced FID.** `web-vitals` removed `onFID()` in v5.0.0 (2025-05-07). LCP and INP became measurable in every major engine with Safari 26.2 (December 2025).
- **CrUX eligibility.** CrUX reports only pages and origins that are publicly discoverable (HTTP 200 after redirects, indexable) and sufficiently popular (the threshold is not disclosed). The lane's 404 dead slots and kimi preview-404 slots therefore can never appear in CrUX.
- **Measurement path.** Low-traffic fleet origins may have no field data at all **[INFERENCE]**, so RUM (`web-vitals`) or lab runs are the measurement path. Lab runs that drive a browser are `tabi` adjacency.

**Sources and quotes.**
- S021 §Core Web Vitals: "a good threshold to measure is the 75th percentile of page loads, segmented across mobile and desktop devices."
- S022 §What is a good INP score?: "An INP above 500 milliseconds means a page has poor responsiveness."
- S023 §Publicly discoverable: "A page must be publicly discoverable to be considered for inclusion in the CrUX dataset."
- S023 §Sufficiently popular: "Pages and origins that don't meet the popularity threshold are not included in the CrUX dataset."
- S024 v5.0.0: "[BREAKING] Remove the deprecated onFID() function"
- S027: "you can now measure these metrics in the latest version of all major browsers."

**Fills.** A new coverage row, "Field performance (CWV/CrUX)". The lane holds none of this today (§1 sweep).

**Recheck.**
- `curl -fsSL https://raw.githubusercontent.com/GoogleChrome/web-vitals/main/CHANGELOG.md | grep -cF 'Remove the deprecated `onFID()` function'` returns 1.
- Thresholds: re-read S021 every 180 days. S021 §Lifecycle says stable metrics "won't change more than once per year".

**How it clears `QUALITY.md`.** *Replayable claim:* changelog argv plus a dated citation. *Admission authority:* the facts here come from docs. Any lane CWV measurement needs its own replayable run within lane rules.

### K6 `wcag22-delta`

**Claim.** WCAG 2.2 was published as a W3C Recommendation on 2023-10-05; the current dated version is `REC-WCAG22-20241212`; it was approved as ISO/IEC 40500:2025 on 2025-10-21.
- It adds exactly 9 success criteria over 2.1: 2 at A (3.2.6, 3.3.7), 4 at AA (2.4.11, 2.5.7, 2.5.8, 3.3.8) and 3 at AAA (2.4.12, 2.4.13, 3.3.9).
- It removes 4.1.1 Parsing.
- SC 2.5.8 requires pointer targets of at least 24×24 CSS px unless the spacing, equivalent, inline, user-agent or essential exception applies.
- WCAG 3 is still a draft, so WCAG 2.2 AA is the current target for lane pages.

**Sources and quotes.**
- S028 §Changes from WCAG 2.1 to WCAG 2.2: "WCAG 2.2 provides 9 additional success criteria since WCAG 2.1." and "4.1.1 Parsing is obsolete and removed from WCAG 2.2."
- S028 §2.5.8: "The size of the target for pointer inputs is at least 24 by 24 CSS pixels"
- S029, metadata: "Latest Version: https://www.w3.org/TR/2024/REC-WCAG22-20241212/"
- H6 (ISO approval date) and H7 (WCAG 3 status).

**Fills.** A new coverage row, "Accessibility conformance (WCAG 2.2)".

**Recheck.**
- `curl -fsSL https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/ | grep -oE '(2\.4\.1[123]|2\.5\.[78]|3\.2\.6|3\.3\.[789]) [A-Z][A-Za-z ()]+\((A|AA|AAA)\)' | sort -u | wc -l` returns 9.
- Append `| sed -E 's/.*\((A+)\)/\1/' | sort | uniq -c` (instead of `wc -l`) to get `2 A`, `4 AA`, `3 AAA`. A `grep -oE '\((A|AA|AAA)\)$'` variant printed nothing on this host, so use the `sed` form.

**How it clears `QUALITY.md`.** *Replayable claim:* dated REC URL, argv and expected counts. No live probe is needed.

## 5. Paths

- **GHP served-set semantics** — S003 → S004 → S026 → S001 → S030 → S002 → S007 → S008 → S005 → S006. Order:
  1. Which pipeline publishes (branch or workflow).
  2. The workflow contract.
  3. Each repo's `build_type` via the REST API.
  4. The exact tar argv and tar's matching rules.
  5. When dotfiles started being dropped.
  6. The legacy Jekyll path and its pinned versions.
  7. Who owns the domain, then the platform limits.
- **Validators and crawl hygiene for a mirror fleet** — S012 → S011 → S013 → S014 → S015 → S016 → S017 → S019. Order: validator semantics from the spec, then the concrete GHP ETag mechanism. Then crawler rules from the specs (robots, sitemaps), then Google's implementation (sitemaps, canonical signals, JS rendering). The dated changelog comes last, to stay current.
- **Page quality bar** — S021 → S022 → S023 → S027 → S024 → S025 → S028 → S029. Order:
  1. Thresholds and the INP definition.
  2. Why small origins may have no CrUX data.
  3. Cross-browser measurability.
  4. The RUM library, then diagnosis with LoAF.
  5. For accessibility: the delta page first, then the normative REC.

## 6. Rejected candidates

- **R1 — llms.txt or "AI text files" as a discoverability lever.** Rejected. S020 §Mythbusting: "You don't need to create new machine readable files, AI text files, markup, or Markdown to appear in Google Search". The same section says Google Search itself doesn't use them. Adding one would create a surface no gate can verify.
- **R2 — Astro's `public/CNAME` step as the GHP custom-domain mechanism** (H11, §Change your GitHub URL to a custom domain). Rejected for Actions-built sites, because S005 says the CNAME file is ignored there. A framework guide does not override the platform's own documentation. This is kept as evidence that framework docs can carry stale platform behavior.
- **R3 — DebugBear's "INP support in Firefox 114"** (H12, heading of that section; tier B). Rejected as a version source. The interactionId/INP line is in the Firefox **144.0** release notes (H4). Version and date numbers from tier B need a tier-A recheck before admission.
- **R4 — FID or `onFID()`-based measurement.** Rejected. S021 §Pending: INP was promoted "with the intent to eventually retire FID". S024 v5.0.0 removed `onFID()`.
- **R5 — WCAG 3 as a conformance target.** Rejected. H7 calls it an "incomplete draft that will change", and WCAG 2 "will not be deprecated for several years after WCAG 3 is finalized".
- **R6 — FAQ rich results as a structured-data target.** Rejected. S019: a deprecation notice was added in May 2026 and the documentation was removed in June 2026.

## 7. Mistakes this art explains

Four mistakes: three from the lane's own history and one research trap from this session.

- **M1 — The ETag back-and-forth** (`publish-queue.md:255-261`, `LOG.md:245-247`, `corpus/lessons/round-16.md:35-38`). Class: treating a validator as an identity, and "refuting" one sampler with a fetch that hit another replica. The rule already exists in round-16, but it has no mechanism and no `QUALITY.md` criterion (no criterion row mentions validators). K3 supplies the mechanism.
- **M2 — "served set ≡ `origin/main` tree"** (`corpus/README.md:52-53`, `corpus/lessons/round-7.md:21-25`). Class: a platform-mechanism proof built from the workflow's shape, without reading the action's source at the pinned version. No `QUALITY.md` criterion covers this; the 5 rows are citation-local absence, replayable claim, missing substrate, admission authority and shape-only probe environment.
- **M3 — "`CNAME` file pins ds4cc.com"** (`publish-channels.md:9`, `SKILL.md:16`). Class: reading a repo file as platform configuration. Not captured by any criterion; see K2.
- **M4 — Tier-B version error** (R3). Class: admitting a number from a secondary source. This is a research-process trap, not a lane mistake.

**Proposed `QUALITY.md` row ("Platform mechanism"), grounded in K1, K2, K3 and R3:**
- **Admit:** claims about what a hosting, CI or crawler platform serves, ignores or validates cite tier-A source at a pinned tag or SHA, or the platform's own doc with a fetch date. Each carries a recheck argv.
- **Reject:** inferring platform behavior from repo files or workflow shape alone. Taking versions, dates or mechanisms from tier B or C without a tier-A recheck.

## 8. Incidental defects (for STATE and wave 2; nothing was touched)

Five in total: 2 contract defects and 3 conflicts between standing claims and primary sources (one of them a prediction only).
- **D1 — Truncated sentence.** `corpus/README.md:60` ends mid-sentence: "kimi `apiv2` authenticated ops are capability-recorded but intentionally". Command: `grep -n 'intentionally$' corpus/README.md`.
- **D2 — `PROVINCE.md` lacks the Core/Frontier/Adjacent sections.** 0 of 3 present. Command: `grep -cE '^## (Core|Frontier|Adjacent)' PROVINCE.md`.
- **D3 — "Full tree" claim conflicts with S001/S002** (dotfiles dropped since v4.0.0) and with S007 for legacy builds. Locations: `corpus/README.md:26`, `corpus/README.md:53`, `SKILL.md:227`, `corpus/lessons/round-7.md:22-23` (append-only), `corpus/knowledge/sitemap-orphan-audit.md:21`. See K1.
- **D4 — "CNAME pins the domain" conflicts with S005 and S003 for an Actions deploy.** Locations: `publish-channels.md:9`, `SKILL.md:16`. See K2.
- **D5 — "CNAME never servable" is predicted false** by the S001 exclusion set. Location: `ghp-subpath-spotcheck.md:83`. Unverified; one free-read GET of `/CNAME` settles it (K1).

**Old-string inventory** for the correcting writer. The counts match `W1StateKake`'s independent counts for the first five strings. Command: `for s in 'served set ≡' 'full tree snapshot' 'full-tree artifact' 'CNAME` file pins' 'CNAME` = ds4cc.com' 'never servable' 'entire checked-out tree'; do printf '%s\t%s\t' "$s" "$(grep -rFo -- "$s" corpus SKILL.md | wc -l)"; grep -rnF -- "$s" corpus SKILL.md | cut -d: -f1,2 | tr '\n' ' '; echo; done`

| String | Count | Locations |
|---|---|---|
| `served set ≡` | 2 | `corpus/README.md:53`, `corpus/lessons/round-7.md:23` |
| `full tree snapshot` | 1 | `SKILL.md:227` |
| `full-tree artifact` | 2 | `corpus/README.md:26`, `corpus/README.md:53` |
| ``CNAME` file pins`` | 1 | `corpus/knowledge/publish-channels.md:9` |
| ``CNAME` = ds4cc.com`` | 1 | `SKILL.md:16` |
| `never servable` | 1 | `corpus/knowledge/ghp-subpath-spotcheck.md:83` |
| `entire checked-out tree` | 2 | `corpus/knowledge/sitemap-orphan-audit.md:21`, `corpus/lessons/round-7.md:22` |

**Operator-facing adjacency, not a lane claim.** S006 says Pages "is not intended for or allowed to be used as a free web-hosting service to run your online business, e-commerce site". Whether the ds4cc.com marketplace is "primarily directed at facilitating commercial transactions" is unknown. Report it; do not absorb it.

## 9. Verification log (run 2026-10-19)

Commands are written raw so they paste verbatim. Web checks were read-only fetches of public pages; I probed no lane property.

- **upload-pages-artifact dot exclusion.** `for v in v3.0.1 v4.0.0 main; do printf '%s ' $v; curl -fsSL https://raw.githubusercontent.com/actions/upload-pages-artifact/$v/action.yml | grep -cF -- '.[^/]*'; done` returned `v3.0.1 0`, `v4.0.0 3`, `main 3`.
- **`.github` exclusion.** The same loop with `grep -cF -- '--exclude=.github'` returned 3, 3, 3.
- **nginx ETag format.** `curl -fsSL https://raw.githubusercontent.com/nginx/nginx/master/src/http/ngx_http_core_module.c | grep -cF '%xT-%xO'` returned 1 (master, line 1736). The same format is at line 1671 on `release-1.28.0`.
- **ETag decode.** `printf 'len=%d mtime_a=%d mtime_b=%d\n' 0x1365d 0x6ab49127 0x6ab49126; date -u -d @$((0x6ab49127)) +%FT%TZ; date -u -d @$((0x6ab49126)) +%FT%TZ` returned `len=79453 mtime_a=1790218535 mtime_b=1790218534`, `2026-09-24T02:55:35Z`, `2026-09-24T02:55:34Z`.
- **Recorded size anchors.** `grep -n -E '79,453B|79453B|79 453 B' LOG.md corpus/lessons/round-8-aggregator-box3-coldrun.md corpus/knowledge/free-read-verbs.md` returned `LOG.md:161`, `round-8-aggregator-box3-coldrun.md:23`, `free-read-verbs.md:166`.
- **GitHub custom-domain doc.** `curl -fsSL 'https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site.md' | grep -cF 'any existing `CNAME` file is ignored'` returned 2.
- **RFC 9309 location rule.** `curl -fsSL https://www.rfc-editor.org/rfc/rfc9309.txt | grep -cF 'top-level path of the service'` returned 1.
- **WCAG 2.2 delta sentence.** `curl -fsSL https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/ | grep -cF '9 additional success criteria'` returned 1.
- **WCAG 2.2 new SC by level.** The K6 recheck argv with the `sed` variant returned 9 SC: `2 A`, `4 AA`, `3 AAA`.
- **web-vitals `onFID` removal.** `curl -fsSL https://raw.githubusercontent.com/GoogleChrome/web-vitals/main/CHANGELOG.md | grep -cF 'Remove the deprecated `onFID()` function'` returned 1.
- **Project-site bases.** The K4 lane-count command returned 3.
- **Proposed SOURCES rows, tiers and statuses** (fleet census commands, run against this file):
  - `grep -cE '^\| S[0-9]{3} ' local://kaika-w1-kake-art.md` returned 30.
  - `grep -E '^\| S[0-9]{3} ' local://kaika-w1-kake-art.md | awk -F'|' '{gsub(/ /,"",$5); print $5}' | sort | uniq -c` returned `30 A`.
  - The same with `$7` returned `24 queued`, `6 watch`.
  - `awk -F'|' '{print NF}'` over the rows returned `30 11`: every row has 9 cells and no cell contains a stray `|`.
