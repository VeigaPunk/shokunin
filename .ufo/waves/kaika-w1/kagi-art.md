# kagi ART dossier — secrets and vault operations

As of 2026-10-19. Read-only ART research; the source pages below were opened in this session. Lane files consulted were `corpus/README.md`, `PROVINCE.md`, `SKILL.md`, the `corpus/knowledge/` filename inventory, and the absent `corpus/QUALITY.md` path. No vault access, secret scanning, installation, or live-target interaction was performed. Public documentation sometimes contains example credential material; none is reproduced here.

## Uncovered ground and lane fit

**Observed in lane sources:** The domain is secrets and vault operations, with credential hygiene and the-janitor-specific flows. The corpus coverage map and knowledge filenames primarily cover the local handler, 1Password CLI and refs, the Chrome bridge, on-disk state, transcripts, audit gates, and evidence custody. `SKILL.md` explicitly forbids copying secret values, tokens, cookies, or vault fields into durable artifacts; `PROVINCE.md` says vault-side structure remains deliberately unmapped. These are good constraints for any new source curation: teach access boundaries and operational evidence, never inventory the vault.

**Uncovered by the reviewed coverage map and filenames:** no listed knowledge entry covers SOPS/age; Vault or OpenBao; workload identity federation/OIDC trust policy; Gitleaks or TruffleHog; or NIST key-management guidance. Existing 1Password material is about the lane's local CLI/handler behavior, not the newly documented Credential Broker model. Current 1Password Connect and Service Account credentials are also distinct from one another and from Broker's integration key.

**Contract defects observed:**
- **Defect D1:** `kagi-shokunin/corpus/QUALITY.md` was not present; the targeted search reported that path skipped as missing. The lane's admission bar cannot be applied to candidates from the inspected files.
- **Defect D2:** `corpus/README.md` has a `## Coverage map` but no `## Frontier` section. Thus the requested frontier rows for these uncovered topics do not currently exist to fill; the rows below are proposals, not claims that a lane frontier is already declared.

`2 defects — grep -c '^- \*\*Defect ' local://kaika-w1-kagi-art.md`

Because `QUALITY.md` is absent, the dossier can only show candidate design evidence (primary source, exact location, scoped claim, falsifier/recheck); it cannot assert that any candidate clears the lane's actual quality gate. Require a read of the restored quality criteria before admitting entries.

## Current art observed in opened sources

### 1Password CLI, Service Accounts, Connect, and Credential Broker

- The CLI docs describe `op run` as starting a subprocess with Environment variables for the process duration, and describe `op read` / `op inject` as other retrieval paths. 1Password recommends Service Accounts and limiting their vault permissions. This establishes a process-lifetime delivery surface; it does **not** establish a short lifetime for the Service Account's own authentication token. [S001, S004]
- A 1Password Service Account token authenticates direct CLI access and is scoped to selected vaults and read/write permissions; the vendor documents rotation and revocation. It is not the Connect API token. [S004]
- Connect has a separate server credential file for the Connect deployment and Connect API access tokens for calling applications; the setup guide recommends a token for each application/service. Treat the server credential file and client API tokens as different custody boundaries. [S002, S003]
- Credential Broker is documented as **public preview**, not generally available. The current setup guide requires OIDC workload verification against configured claims and states all configured claims must match. It says access lasts only for the workflow duration. [S005–S007]
- Important qualification: the public-preview GitHub setup guide directs an administrator to save the integration key as a GitHub organization secret. 1Password describes that key as an encryption key, not a standing vault-access token, and says the OIDC credential is also needed to decrypt. Therefore, the supported claim is “no Service Account token / no standing vault access,” **not** “there are no persistent secrets or keys in the workflow environment.” Treat the integration-key custody and rotation/revocation procedure as a separate control to verify. [S005–S007]
- The Broker documentation scope is changing quickly: its product page and July 2026 preview post describe GitHub Actions and custom OIDC workflows; the setup instructions spell out claim configuration and an integration key. Recheck the current workflow support, audience/claim constraints, and key handling before authoring an operational recipe. [S005–S007]

### SOPS and age

- SOPS is an encrypted-file editor supporting common structured formats and multiple key providers, including age. The age guide says recipients are configured on files and private identities are loaded from configured locations or environment settings. [S008, S009]
- SOPS key groups use Shamir secret sharing across groups; the default threshold is the number of key groups, while the threshold can be configured. Do not conflate multiple recipient keys within a group with independent recovery groups. [S010]
- The key-management docs distinguish updating encrypted-file recipients from replacing the per-file data key: `updatekeys` changes the key access set; `rotate` creates a new data key and re-encrypts values. For a compromised key-group identity, the documented order is remove/update recipients first, then rotate the data key, then rotate the secret values inside the file. [S011]

### Vault, OpenBao, and workload identity

- HashiCorp Vault's JWT/OIDC auth supports browser OIDC login and direct JWT authentication; the JWT method verifies signatures with configured keys, JWKS, or discovery and applies audience/claim matching. Vault's docs require exact `bound_audiences` matching when the submitted JWT has `aud`. [S012]
- Vault documents plugin Workload Identity Federation as exchanging Vault-issued identity tokens for short-lived cloud credentials; its AWS and GCP secret-engine pages label the plugin WIF configuration as Enterprise. This is a specific integration, not a synonym for every JWT/OIDC login. [S013–S015]
- Vault leases are a lifecycle mechanism for dynamic secrets and service-type auth tokens. The lease docs explicitly distinguish the KV backend, which stores arbitrary static values and does not issue leases. Do not promise auto-revocation/rotation merely because a stored value was read from KV. [S016]
- OpenBao's current docs identify version 2.7.x. Its JWT/OIDC method validates external JWTs and maps role claims into OpenBao tokens; token docs describe policy attachment and token TTL/renewal/revocation. [S017, S020]
- OpenBao's Kubernetes-specific JWT page warns that JWT auth validates signatures and does **not** use Kubernetes `TokenReview`; a revoked token can remain accepted until its expiration. It recommends short-lived service-account tokens or Kubernetes auth when `TokenReview` behavior is required. This boundary should not be erased by general “OIDC is short-lived” language. [S019]
- OpenBao KV v2 has versioned data and distinct `data`, `metadata`, `delete`, `undelete`, and `destroy` API paths, so policy examples must use the correct API path and separate read/write/destructive permissions. OpenBao identity tokens are a different flow again: OpenBao signs OIDC-shaped ID tokens for an entity. [S018, S021]

### OIDC federation

- GitHub Actions documents job-specific OIDC JWTs that cloud providers validate against configured trust conditions, then exchange for short-lived access. It also documents repository custom-property claims and an immutable default `sub` format for repositories created after 2026-07-15; trust examples based on older subject formats need deliberate review. [S022]
- Google Cloud WIF accepts external workload identities, maps claims into attributes, and applies attribute conditions; its docs recommend direct resource access where supported and describe service-account impersonation as an alternative. AWS likewise recommends dynamically obtained temporary credentials instead of long-lived AWS credentials in external applications. [S023, S024]
- This suggests a useful protocol focus: issuer, audience, subject/attribute mapping, allowed repositories/environments/branches, and the resulting role permissions are separate policy decisions. “Uses OIDC” alone does not prove a workload is narrowly authorized. [S022–S024]

### Secret scanning and NIST

- Gitleaks scans repositories/history, directories, and stdin; documents reports, baselines, rule configuration, and output redaction. Its current upstream README says the project is feature-complete and that new development is moving to Betterleaks, with future Gitleaks releases limited to security patches. That is a tool-selection freshness fact, not a reason to stop using a pinned existing deployment. [S028]
- TruffleHog positions its workflow as discovery, classification, validation, and analysis, and supports provider verification. Its current README also notes that local Git repositories are cloned before scanning by default to avoid malicious Git-config behavior; `--trust-local-git-config` is explicitly only for trusted repositories. A scan result marked unknown/unverified must not be reported as “no active exposure”; verification is distinct from pattern detection. [S029]
- The NIST SP 800-57 Rev. 6 Part 1 initial public draft was published 2025-12-05; its announced changes include post-quantum algorithms and a new section on keying-material storage. The opened PDF's §5.2.2 separates storage availability, integrity, confidentiality, and key-information association. This is still an IPD with its comment period closed, not final guidance. SP 800-57 Part 1 Rev. 5 is the final edition opened here. SP 800-133 Rev. 3 is also an IPD (published 2026-04-17); it discusses generation and seed expansion and requests feedback on HSM/root-seed and PQC key-storage designs. Preserve the draft/final distinction in any adopted policy. [S025–S027]

## Candidate knowledge entries

These are proposed entries, not admitted corpus facts. Each claim is scoped so a reviewer can falsify it against the cited primary docs. For every entry, `QUALITY.md` clearance remains **unverified** until the missing lane criteria are restored and reviewed.

### Candidate 1 — `credential-broker-access-boundaries.md`

- **Falsifiable claim:** In the currently documented public-preview setup, a GitHub Actions or configured custom-OIDC workload receives Environment credentials only after its identity satisfies the integration's configured claims; access is limited to the workflow duration. The GitHub setup still requires an integration key stored as a GitHub secret, so the entry must distinguish that decryption key from a Service Account token and must not claim “zero stored keys/secrets.” A counterexample would be a documented supported flow that bypasses claim match or retains Broker-delivered access beyond the workflow.
- **Source and exact location:** S007, “Set up 1Password Credential Broker…” → workflow verification. Quote: “Secrets are only accessible after a workload has been verified, and only remain accessible for the duration of the workflow.” [S007]
- **Fills:** proposed Frontier row `workload identity → brokered credential access`; no existing frontier row found.
- **Recheck:** Re-open S007's OIDC integration and GitHub Actions setup sections plus S006's public-preview status before admission; recheck on product release. [S006, S007]
- **Quality gate:** exact primary citations, explicit boundary, no secrets copied, counterexample and refresh trigger specified; actual lane quality criteria unavailable.

### Candidate 2 — `sops-age-recipient-and-data-key-rotation.md`

- **Falsifiable claim:** In SOPS, `updatekeys` updates recipient access without rotating the data key; `rotate` generates a fresh data key and re-encrypts values. For a compromised key-group identity, update recipients before rotating the data key and before changing plaintext credentials. A SOPS release/documentation change that changes those semantics would falsify the claim.
- **Source and exact location:** S011, “Key management” → `updatekeys` / `rotate` commands. Quotes: “The SOPS team recommends the `updatekeys` approach.” and “Use `updatekeys` if you want to add a key without rotating the data key.” [S011]
- **Fills:** proposed Frontier row `encrypted configuration and recipient/key lifecycle`; expands beyond the lane's current local `op.env` handling.
- **Recheck:** Re-open S009 “Encrypting using age,” S010 “Key groups,” and S011 “Rotating secrets after a key in a key group has been compromised”; check on SOPS release. [S009–S011]
- **Quality gate:** exact documented mechanism and compromise order are citable and falsifiable; actual lane quality criteria unavailable.

### Candidate 3 — `vault-openbao-auth-and-secret-lifecycle.md`

- **Falsifiable claim:** Treat authentication, authorization, and generated-secret lifecycle as separate facts: a workload JWT's issuer/audience/claims decide whether auth succeeds; an issued Vault/OpenBao token's policy and TTL govern its API access; Vault's dynamic AWS/GCP credentials use leases while KV is static storage. For Kubernetes, OpenBao JWT signature validation alone does not provide TokenReview revocation. A counterexample in current docs or an unsupported assertion of Vault/OpenBao parity falsifies the entry.
- **Source and exact location:** S019, “Kubernetes” → note about JWT auth and TokenReview. Quote: “The JWT auth engine does not use Kubernetes' `TokenReview` API during authentication.” S016, “Lease, renew, and revoke” → lease definition. Quote: “All dynamic secrets in Vault are required to have a lease.” [S016, S019]
- **Fills:** proposed Frontier row `Vault/OpenBao workload auth, policy, token and secret lifecycle`; keep OpenBao-specific caveats separate from Vault's Enterprise plugin WIF.
- **Recheck:** Re-open S012, S016–S020 and compare exact product/version docs before admission; recheck on product release. [S012, S016–S020]
- **Quality gate:** primary-doc-based distinction avoids treating a token TTL as a dynamic-secret lease or assuming OpenBao feature parity; actual lane quality criteria unavailable.

### Candidate 4 — `oidc-federation-trust-policy.md`

- **Falsifiable claim:** Replacing a stored cloud key with OIDC federation only narrows workload access when the trust policy validates the intended issuer and audience and maps/binds identity claims to the intended repository, environment, branch, or other workload attributes; the role permission policy separately limits cloud actions. A trust configuration permitting an unrelated workload or wrong audience falsifies a claim that it is least-privilege.
- **Source and exact location:** S023, “Workload Identity Federation” → “Attribute conditions.” Quote: “An attribute condition is a CEL expression that can check assertion attributes and target attributes.” S022, “OpenID Connect” → token validation and immutable subject note; S024, “OIDC federation” → temporary credentials mapped to a role. [S022–S024]
- **Fills:** proposed Frontier row `OIDC workload identity and cloud trust-policy review`; include the GitHub subject-format change documented for new repos created after 2026-07-15.
- **Recheck:** Re-open the provider's trust-policy docs for the target cloud and current GitHub OIDC subject reference; do not reuse sample subject strings without checking current claim format. [S022–S024]
- **Quality gate:** claim names separate issuer/audience/claims from role permissions, with a testable denial counterexample and primary-source citations; actual lane quality criteria unavailable.

### Candidate 5 — `secret-scanning-detection-verification-and-response.md`

- **Falsifiable claim:** Secret detection, provider verification, output handling, and incident response are separate stages: Gitleaks supplies rule/history detection and can redact output; TruffleHog can validate supported credential types. A detection result alone does not prove a credential live, and “unknown” verification does not prove it invalid. Baselines/allowlists must be documented as suppressions, not evidence that an exposed credential is safe.
- **Source and exact location:** S028, Gitleaks README → Usage / baseline and redaction flags. Quote: “redact secrets from logs and stdout.” S029, TruffleHog README → “Validation.” Quote: “For every secret TruffleHog can classify, it can also log in to confirm if that secret is live or not.” [S028, S029]
- **Fills:** proposed Frontier row `secret scanning coverage, verification, redaction, and response`; explicitly flag Gitleaks's upstream maintenance status so tool freshness is part of the entry.
- **Recheck:** Re-open the pinned release docs and current upstream project status before admission; test only against synthetic fixtures in any future round, never the lane's real vault or live credentials. [S028, S029]
- **Quality gate:** avoids raw findings and distinguishes suppression from remediation; actual lane quality criteria unavailable.

### Candidate 6 — `nist-key-management-draft-status-and-storage.md`

- **Falsifiable claim:** Key-management advice must track key type and lifecycle needs (including storage confidentiality, integrity, availability, and association) and distinguish final NIST guidance from the 2025–2026 IPDs. Any entry claiming SP 800-57 Rev. 6 or SP 800-133 Rev. 3 is final would be false against the opened NIST records.
- **Source and exact location:** S025, SP 800-57 Rev. 6 IPD → Announcement; PDF §5.2.2. Quote: “A section has been added to discuss keying material storage and mechanisms.” S026 is Rev. 5 final; S027 identifies Rev. 3 as an IPD and describes the proposed key-generation changes. [S025–S027]
- **Fills:** proposed Frontier row `key classification, storage, recovery, rotation, and draft-status tracking`.
- **Recheck:** Re-open NIST's publication records and relevant current final documents before adopting control requirements; refresh on release of a final revision. [S025–S027]
- **Quality gate:** status is explicit and every operational claim points to a NIST section; actual lane quality criteria unavailable.

`6 candidate entries — grep -c '^### Candidate ' local://kaika-w1-kagi-art.md`

## Paths

- **Workload secrets:** S022 GitHub OIDC claims → S023 GCP WIF attribute mapping/conditions → S007 1Password Broker setup. Order: establish job identity, see how a provider binds claims, then apply the Broker's current supported workflow and key custody.
- **Encrypted configuration:** S009 age recipient handling → S010 SOPS key-group threshold → S011 recipient and data-key rotation → S025 NIST key storage. Order: identity custody, recovery threshold, compromise procedure, then broader key-storage governance.
- **Runtime and detection:** S012 Vault JWT auth → S016 Vault leases and static KV distinction → S017/S019 OpenBao JWT/Kubernetes caveats → S028 Gitleaks and S029 TruffleHog. Order: authenticate, distinguish secret lifecycle, compare implementation-specific behavior, then detect/verify without exposing findings.

## Rejected candidates / mistakes mined

These are research-candidate rejections, not claims about past lane rounds (the ART probe did not inspect lesson history).

### Rejected: “`op run` means the machine credential itself is short-lived.”

Reason: the CLI documentation says the resolved process environment is scoped to the subprocess, while Service Account authentication is a separate token and access-control surface. Conflating exposure window with token lifetime overstates the source. Retain only the narrower process-scope statement. [S001, S004]

### Rejected: “Credential Broker removes every secret from CI.”

Reason: the current public-preview GitHub setup asks the operator to store an integration key as a GitHub secret. The product distinguishes that encryption key from a standing Service Account access token; do not erase the remaining key-custody requirement. [S005–S007]

### Rejected: “Removing an age recipient alone completes rotation after compromise.”

Reason: SOPS distinguishes recipient synchronization from data-key rotation and documents an order for compromise response; a recipient-list change by itself is not equivalent to replacing encrypted values. [S009–S011]

### Rejected: “A KV read has a Vault lease, or a JWT login implies a dynamic secret is revoked on token expiry.”

Reason: Vault says KV does not issue leases; leases apply to dynamic secrets and service-type auth tokens. Token TTL, dynamic-secret lease, and value rotation are distinct lifecycle controls. [S016]

`4 research rejections mined — grep -c '^### Rejected:' local://kaika-w1-kagi-art.md`

## Sources registry (draft rows for later `corpus/SOURCES.md`)

All rows below were opened in this session. Tier A means primary/authoritative publisher documentation, project source, or standard. Status remains `queued` or `watch` because no lane knowledge entry cites them yet; `used-by` is therefore `—`. Current-preview and frequently changing references are `watch`; stable foundational guidance is `queued`. Recheck dates are cadence signals, not claims of an existing lane review.

|id|source|kind|tier|teaches|status|opened|recheck|used-by|
|---|---|---|---|---|---|---|---|---|
|S001|Load secrets into scripts — https://www.1password.dev/cli/secrets-scripts|docs|A|`op run` subprocess delivery plus `op read`/`inject` mechanisms and the recommended least-privilege Service Account pattern.|watch|2026-10-19|90d|—|
|S002|1Password Connect — https://www.1password.dev/connect|docs|A|Connect is a self-hosted REST API with local caching; applications call it using access tokens.|queued|2026-10-19|90d|—|
|S003|Get started with a 1Password Connect server — https://www.1password.dev/connect/get-started|docs|A|Separates Connect deployment credentials from client API tokens and recommends individual application/service tokens.|queued|2026-10-19|90d|—|
|S004|1Password Service Account security — https://www.1password.dev/service-accounts/security|docs|A|Vault-scoped read/write access, token lifecycle, revocation, and rotation for direct programmatic CLI authentication.|watch|2026-10-19|90d|—|
|S005|Machine and AI agent credential runtime access — https://1password.com/product/credential-broker|docs|A|1Password's Broker product description says workloads use WIF, receive policy-scoped credentials at runtime, and get attributed delivery logs.|watch|2026-10-19|on-release|—|
|S006|1Password Credential Broker is now in public preview — https://1password.com/blog/1password-credential-broker-public-preview|docs|A|The July 2026 public-preview post distinguishes an integration encryption key from a Service Account token and describes OIDC-bound workflow access.|watch|2026-10-19|on-release|—|
|S007|Set up 1Password Credential Broker for workflows — https://www.1password.dev/brokered-access|docs|A|The current setup path requires matching configured OIDC claims, documents workflow-duration access, and directs GitHub setup to store an integration key.|watch|2026-10-19|on-release|—|
|S008|SOPS upstream README — https://raw.githubusercontent.com/getsops/sops/main/README.rst|code|A|SOPS supports encrypted structured files with age and cloud KMS backends and links to maintainer documentation.|queued|2026-10-19|on-release|—|
|S009|Age — https://getsops.io/docs/usage/identities/age/|docs|A|Age recipient configuration, private identity lookup, supported sources, and `updatekeys` use for recipient changes.|watch|2026-10-19|on-release|—|
|S010|Key groups — https://getsops.io/docs/usage/identities/key-groups/|docs|A|SOPS distributes data-key fragments across groups with a configurable Shamir threshold.|watch|2026-10-19|on-release|—|
|S011|Key management — https://getsops.io/docs/usage/key-management/|docs|A|SOPS distinguishes recipient updates from data-key rotation and documents compromise-remediation order.|watch|2026-10-19|on-release|—|
|S012|Use JWT/OIDC authentication — https://developer.hashicorp.com/vault/docs/auth/jwt|docs|A|Vault supports OIDC and direct-JWT login with configured signature verification and role-bound claims/audience.|watch|2026-10-19|on-release|—|
|S013|Manage identities and authentication — https://developer.hashicorp.com/vault/docs/about-vault/why-use-vault/identities|docs|A|Vault identity tokens and plugin WIF are separate from ordinary auth; WIF exchanges internal identity tokens for short-lived cloud credentials.|watch|2026-10-19|on-release|—|
|S014|AWS secrets engine — https://developer.hashicorp.com/vault/docs/secrets/aws|docs|A|Vault AWS dynamic credential modes, lease behavior, and plugin WIF setup with its Enterprise qualification.|watch|2026-10-19|on-release|—|
|S015|Google Cloud secrets engine — https://developer.hashicorp.com/vault/docs/secrets/gcp|docs|A|Vault's GCP secrets engine supports token/key issuance and plugin WIF; generated service-account keys are lease-linked.|watch|2026-10-19|on-release|—|
|S016|Lease, renew, and revoke — https://developer.hashicorp.com/vault/docs/concepts/lease|docs|A|Vault leases govern dynamic-secret and service-token lifecycle; KV stores arbitrary values without issuing leases.|queued|2026-10-19|90d|—|
|S017|JWT/OIDC auth method — https://openbao.org/docs/auth/jwt/|docs|A|OpenBao 2.7.x JWT/OIDC auth verifies external tokens and maps role claims into OpenBao authentication.|watch|2026-10-19|on-release|—|
|S018|KV secrets engine version 2 — https://openbao.org/docs/secrets/kv/kv-v2/|docs|A|OpenBao KV v2 versions data and separates data, metadata, deletion, undelete, and destroy ACL paths.|watch|2026-10-19|on-release|—|
|S019|Kubernetes JWT provider — https://openbao.org/docs/auth/jwt/oidc-providers/kubernetes/|docs|A|OpenBao JWT signature validation does not call Kubernetes TokenReview; revoked tokens remain usable until expiry.|watch|2026-10-19|on-release|—|
|S020|Tokens — https://openbao.org/docs/concepts/tokens/|docs|A|OpenBao authentication tokens carry policies and TTL/renewal/revocation behavior; token internals are documented as volatile.|watch|2026-10-19|on-release|—|
|S021|Identity tokens — https://openbao.org/docs/secrets/identity/identity-token/|docs|A|OpenBao can issue signed OIDC-shaped ID tokens with issuer, subject, audience, expiration, and published verification keys.|watch|2026-10-19|on-release|—|
|S022|OpenID Connect — https://docs.github.com/en/actions/concepts/security/openid-connect|docs|A|GitHub documents job-specific OIDC identity claims, provider trust checks, custom-property claims, and a changed immutable subject format for new repos.|watch|2026-10-19|90d|—|
|S023|Workload Identity Federation — https://docs.cloud.google.com/iam/docs/workload-identity-federation|docs|A|Google Cloud WIF maps external identity claims, evaluates attribute conditions, and supports direct resource access or service-account impersonation.|watch|2026-10-19|90d|—|
|S024|OIDC federation — https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html|docs|A|AWS recommends temporary role credentials exchanged from an OIDC JWT instead of long-lived external application keys.|watch|2026-10-19|90d|—|
|S025|NIST SP 800-57 Rev. 6 Part 1 IPD record and PDF — https://csrc.nist.gov/pubs/sp/800/57/pt1/r6/ipd ; https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r6.ipd.pdf|spec|A|The 2025 IPD adds PQC references and key-storage guidance; §5.2.2 addresses storage availability, integrity, confidentiality, and associations; it remains a draft.|watch|2026-10-19|on-release|—|
|S026|NIST SP 800-57 Part 1 Rev. 5 final — https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final|spec|A|NIST's opened final publication is the established key-management baseline while Rev. 6 remains an IPD.|queued|2026-10-19|on-release|—|
|S027|NIST SP 800-133 Rev. 3 IPD — https://csrc.nist.gov/pubs/sp/800/133/r3/ipd|spec|A|The 2026 draft updates key-generation treatment for seed expansion and PQC and solicits HSM/root-seed feedback.|watch|2026-10-19|on-release|—|
|S028|Gitleaks upstream README — https://raw.githubusercontent.com/gitleaks/gitleaks/master/README.md|code|A|Gitleaks scans Git history and directories, supports baselines and redaction, and upstream says feature work has moved to Betterleaks.|watch|2026-10-19|on-release|—|
|S029|TruffleHog upstream README — https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/README.md|code|A|TruffleHog distinguishes discovery/classification/verification and clones local repos by default to guard against malicious Git config.|watch|2026-10-19|on-release|—|

`29 source rows — grep -cE '^\| S[0-9]{3} ' local://kaika-w1-kagi-art.md`

`29 tier-A rows — grep -E '^\| S[0-9]{3} ' local://kaika-w1-kagi-art.md | awk -F'|' '{gsub(/ /,"",$5); print $5}' | sort | uniq -c`

## Leads (unopened)

- Betterleaks — linked by the current Gitleaks README as the destination for new feature work; not opened in this wave.
- The age encryption specification — linked by the SOPS age page; not opened independently.
- TruffleHog verification-caching documentation — surfaced during search, not opened; verify cache semantics before making retention claims.
- Provider-specific GitHub OIDC setup pages for each AWS/GCP role configuration — leads only; the AWS OIDC overview and Google WIF overview above were opened, not every provider-specific configuration page.

## Top recommendations

- Prioritize the Broker/Service Account/Connect distinction and document the integration-key requirement explicitly; the 2026 public preview is the clearest fresh lane-relevant change.
- Add SOPS/age key-group and compromise-order study next; avoid equating `updatekeys`, data-key rotation, and secret-value rotation.
- Make workload OIDC claim binding and token-vs-lease lifecycle the next frontier, with OpenBao's Kubernetes TokenReview caveat and Vault WIF Enterprise boundary preserved.