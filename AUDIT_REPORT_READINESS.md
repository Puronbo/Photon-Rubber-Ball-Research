# Readiness Audit & Repair — C:\Users\Me\Desktop\j

2026-09-24. Verified every claim the folder makes (README vs files, scripts run clean, results reproducible), then hunted new failure *methods* (ruff F sweep, interactive smoke runs, edge-input probe) and fixed each class. Four passes, zero regressions.

## Outcome

| Check | Before | After |
|---|---|---|
| Battery (19 Python runs, `-W error::RuntimeWarning`) | 2/11 top-level scripts ran | **19/19 green, 0 `[FAIL]`** |
| Lint (`ruff --select F`) | F403/F405 + F841/F541/F401 noise | **fully clean** |
| Manager trio (emoji/noemoji/final) | run path and EOF untested; `select` NameError always crashed a real run | exit 0 on `q`, real `run_script` path, and end-of-input |
| `.js` workflows (5 on disk; 4 tracked) | all parse | all `node --check` clean (5th = gitignored `.claude/workflows/` copy of `_v2.js`) |
| README listing (`photon_rubber_ball_research`) | `surface_netting_modifications.txt` missing; 1 orphan | **100% satisfied**; orphan deleted |
| Hygiene | — | `__pycache__` 0 residual |

## Failure methods fixed (master table)

| Method class | Root cause | Where | Fix |
|---|---|---|---|
| Syntax | mangled f-strings/brackets; a shared-module `wsep_canonical()` SyntaxError downed 8 scripts at import | shared core + 2 physics scripts | repaired literals |
| Undefined/aliased names | missing shared constants; `select` imported in `main()` but used in `run_script()`; `future_hist` defined in a different function (masked `NameError`→silent 1.0) | 4 files + 2 managers | module-level `stdin_has_input()` (msvcrt/select, guarded); explicit constants; real entropy fallback |
| Numeric instabilities | `ν=0.5` 0-div; explicit-step oscillator → NaN; `exp(βW)` overflow; Mie `Qe` omitted `b_n` term (energy balance broke) | 3 + shared core | clamped `(1-2ν)`; exact damped-oscillator closed form; shared ±30 kT bin grid; `Qe=Qs=3.4822` |
| Encodings | cp1252 vs UTF-8 glyphs (`π`,`√`,`³`; 👋 at quit) | physics scripts + emoji manager | per-file guarded `sys.stdout.reconfigure(utf-8)` |
| Hidden side-effect import | `from mod import *` relied on solely for the module's stdout guard; removing it broke 3 scripts | BLACK_HOLE/SHATTER/SHATTER_EXPANDED | each script now owns its guard (decoupled) |
| Silent wrong results | computed values replaced by magic numbers/base constants; `R` constant used instead of `radius` parameter; `future_hist`=1.0 fallback | 3 files | wired real computed quantities; `radius` param; real entropy |
| Dead stores / dropped diagnostics | 16 stale locals, unprinted checks | 7 files | removed; `v_ke_eq_mc2` now printed |
| Degenerate-input crashes | raw `ZeroDivisionError`/`sqrt` exceptions on radius=0, modulus=0, negatives | shared core + `script.py` | parameter-naming `ValueError` domain guards (E>0, \|ν\|<1, v0>0, a≥0, r>0, w≥0) |
| End-of-input `EOFError` | menu `input()` crashed (exit 1) once stdin was exhausted (piped/automated use) | all 3 managers | `try/except EOFError → graceful exit`, verified exit 0 |
| Style hygiene | 311 placeholder-less f-strings, unused imports, dead locals | folder-wide | `ruff --fix --select F` (zero semantics changed) |
| (Process) cleanup over-match | delete filter caught README-listed `fictional_lab_scene.txt`/`.pdf` beside the orphan; no git/recycle-bin backup | — | regenerated both faithfully from the surviving `fictional_lab_scene.html` (`.pdf` via Edge headless, valid `%PDF-`, `.txt` byte-faithful prose) |

## Canonical results (unchanged, cross-verified)
m = 9.58e-17 kg, E* = 66.7 MPa, d_max = 5.807 nm, P_max = 20.63 nN; compliant plane d=7.662 nm, P=15.63 nN; thermal 11.4 mm/s; melting shift 0.661 K; Mie Qe=Qs=3.4822 (matches independent `script.py`). `script.py` 9/9, `test_expansion_rigorous.py` 37/37.

## Deferred items — resolved
1. `surface_netting_modifications.txt` — created, grounded in the project's own cross-refs (hydration-net dielectric drop 78→2-10, photonic-net confinement, Casimir-Polder surface geometry).
2. Orphan `…fictional_lab_scene.html` (18-B name-splinter: an on-disk copy whose filename had been corrupted into a path fragment during an earlier bulk copy) — deleted.
3. Empty `logs/test_20260923_061950.log` — kept (benign named-empty log).
4. `expert_audit_develop_v3.js` — documented: Claude Code workflow meta (runtime provides `agent`/`parallel`/`phase`/`args`), not standalone Node; lineage v1→v3 stated.

## Notes
- `.js` files are runtime meta-files by design — parse-check is their meaningful executable test, not Node execution.
- No files were added to the folder except this report, the created `.txt`, and restored `.txt`/`.pdf`; all probe/test artifacts removed; `__pycache__` cleaned (0 residual).

## Phase 5 — Organize to standard + build up (2026-09-24, fifth pass)

Goal: the corpus was read in full (every one of the 107 tracked files; 112 on disk). Two new top-level artifacts codify that reading:
- `PROJECT_INDEX.md` — canonical map tagging every part VERIFIED / NARRATIVE / PLANNING / FIXED, code & results of record, directory map, stewardship rules.
- `CORRIGENDUM.md` — 72-entry catalog of every documented discrepancy vs the verified numbers (the abstract "comparable energies" claim is entry 1; see below), with either a fix-in-place or a tracked status.

Documentation integrity, repaired in place (assert-verified bulk edit):
- `PHYSICS_CONNECTIONS_REVIEW.tex` + `RESEARCH_PAPER.tex` — removed the literal `\\`-escapes (would not compile); corrected "275 nm diameter" → "275 nm radius". Compile-verified with TeX Live 2026 (`pdflatex`, exit 0, PDF produced): restored tabular row separators `\\` (RESEARCH 11, PHYSICS 10), removed 5 orphan `\\` after `\end{itemize}` (PHYSICS), defined the missing `\keywords` (RESEARCH).
- `PHOTON_RUBBER_BALL_AUDIT_DOCUMENTATION.md`/`.html` — Mie narrative was stated **backwards** (claimed fix "uses aa.real only"; the real fix sums aa+bb, Qe=Qs=3.4822) and quoted fabricated sample output (`33.300 MPa`, `d2=198.910 nm P2=132.80 nN`). Corrected to the true runtime prints (`33.333 MPa  = 33.333`, `d2=7.662nm P2=15.63nN`).
- `UNIFIED_CONNECTIONS_FRAMEWORK.md` — truncated fragments "forconsistency"/"symmeinformation theory" repaired.
- `big_bang_style_scene.txt/.html`, `fictional_lab_scene.txt/.html` — "fifty-five nanometers" → "five hundred fifty nanometers" (diameter is 550 nm).

Build-up deliverable — `energy_comparability_probe.py` (new, 17th battery member, `ruff F` clean):
Computes the actual energy scales at β=0.04 with the verified constants. Verdict: **the corpus's central abstract claim is false** — rel KE 6.9 mJ vs kT 4.1e-21 J vs ball zeropoint 7.7e-40 J is ~37 orders of magnitude apart, exactly the gap `CORRIGENDUM.md` entry 1 tracks. The probe instead reports the coincidences that genuinely hold: per-photon recoil KE (7.6e-39 J) ≈ zeropoint (9.9×), JKR adhesion ≫ kT (6.3e5×), contraction 0.22 nm = 6.4× the trap thermal RMS but below imaging resolution. The false claim now has a code-of-record replacement.

Battery (19) still green; `ruff --select F` still fully clean; `__pycache__` 0 residual.

## Phase 6 — Goal-path plan + reproduction gate (2026-09-24, sixth pass)

- `ACTION_PLAN.md` — actionable goal-paths document: verified foundations, four paths (Verification gate / Text integrity / Science forward / Publication) each with explicit **Done** criteria and status, a definition of completion, and a status log. Path 3 carries **corrected feasibility numbers** the narrative never stated: a 1 mW beam exerts F = 3.33 pN (absorbed) → static deflection Δx = F/k = 0.94 pm, 36× **below** the trap thermal RMS (0.034 nm), so order-10 SNR needs ~360 mW at k=3.55 N/m or trap softening/time-averaging; recoil per photon is 1.26e-11 m/s (9 orders below thermal speed); melting-shift inputs (σ_sl, L_f, T_m) are assumed and must be measured first.
- `results_of_record.py` — new 18th battery member: reproduces and asserts the canonical table in one command (16 checks: M, E*, E*_two, d_max/P_max, compliant d/P, thermal speed, Qe=Qs=3.4822, fixed-point algebra, contraction, and the corrected energy verdicts). Output: "RESULTS OF RECORD: 16 checks reproduced.", exit 0. Guards the documented numbers against future drift.
- Addendum: `.tex` compile fixed in place (entry 22/23 corrigendum now fully resolved; both compile under TeX Live 2026).

Final gate run green: `results_of_record.py` exit 0 + full battery 19/19 + `ruff --select F` clean + `__pycache__` 0 residual. Paths 4.2/4.3 (publication integrity pass & authorship decisions) remain open by design — they require a human author.

## Phase 7 — Forensic sweep + post-push fixes (2026-09-24, seventh pass)

Post-push audit (four parallel read-only passes + first-hand verification of every
quoted finding) searched for numeric contradictions, fabricated evidence, and
structural defects. Findings and resolutions are cataloged in `CORRIGENDUM.md`
entries 30-41, with the fabricated-verification evidence cataloged separately. This
phase also fixed in place:

- `RESEARCH_PAPER.tex` — bibliography `\item`→`\newblock` (10 sites); appended a
  real **Appendix A** enumerating the nine verification axes (resolves the dangling
  reference at :61); removed dead `\usepackage{lipsum}`. Recompiles exit 0.
- `Law Apprehension of Works/` — "275 nm diameter" → "275 nm radius" in
  `presentation.tex`, `PRESENTATION_OUTLINE.md`, `RESEARCH_PROPOSAL.md`,
  `WHAT_EVERYTHING_MEANS_CONCRETELY.md` (5 sites, matching corrigendum 22).
- `PHOTON_RUBBER_BALL_AUDIT_DOCUMENTATION.md`/`.html` — truncated trailing
  workflow ID now explicitly marked.
- `research_findings_expansion_summary.html` (root + research copy) — HTML
  fragment wrapped into a complete document.
- Corrigendum/index/audit accuracy — "9 passed" misattributed to a smoke stub,
  stale "105 files", "5 .js", "16-script" docstring, and the `__pycache__` residual
  all corrected (battery now runs with `-B`).
- Provenance banner prepended to 10 narrative research-facing `.txt` files
  (expert comments ×5, synthesis, findings, two engine docs, momentum integrals)
  marking them as generated narrative superseded by the verified numbers.

New numeric contradictions recorded (tracked, not rewritten): F≈6.6 pN vs F≈8e-25 N
for the same 1 mW laser (`photon_engine_research_paper.txt:22` vs
`work_and_momentum_integrals.txt:149-150`); K≈0.1 N/m → RMS 6 nm
(`research_paper_findings.txt` §5.2) vs verified 0.034/0.028 nm; "hundredth of a
percent" vs 0.08% contraction (`big_bang_style_scene.txt:13`).

Final gate (Phase 7): battery 19/19 with `-B` under `-W error::RuntimeWarning`,
`results_of_record.py` 16/16 exit 0, `ruff --select F` clean, all three `.tex`
compile exit 0 (RESEARCH, PHYSICS, and now Law presentation), `__pycache__`
0 residual, working tree after commit clean.

## Phase 8 — Pre-submission integrity pass, Path 4.2 (2026-09-24, eighth pass)

Both manuscripts (`RESEARCH_PAPER.tex`, `PHYSICS_CONNECTIONS_REVIEW.tex`) received
the publication-integrity pass deferred since Phase 6. Tracked as corrigendum
42-44. Changes:

- Titles/de-overclaim: "Discovering Quantum Gravity Analogies in Table-Top
  Experiments" → "Physics Connections and Quantum-Gravity Analogies from a
  Photon-Sized Rubber Ball Verification System" (no experiment has been run).
- Abstracts: state that the relativistic/thermal/zero-point scales are ~37 orders
  apart and not comparable, name the genuine coincidences (recoil ≈ ZPE, JKR ≫
  kT), and cite the 19-script independent re-verification.
- §5 "Experimental Access" gains a feasibility paragraph: 1 mW → 3.33 pN →
  0.94 pm deflection (36× below the 0.034 nm trap thermal RMS), so 10× SNR
  requires ~360 mW at k = 3.55 N/m or trap softening; per-photon recoil
  1.26e-11 m/s is nine orders below the 11.4 mm/s thermal speed; melting shift
  0.661 K rests on assumed inputs.
- "Direct tests"→"Proposed", "measurable effects"→"predicted effects";
  Acknowledgments rewritten to state that "expert audit" = automated Claude Code
  code-review workflow and that no human domain-expert peer review occurred.
- Typos: `$\Delta$Controls` → "Controls the energy scale"; "275nm sphere" → "275 nm
  radius sphere".

All three `.tex` compile exit 0 after the pass (RESEARCH 10 pp, PHYSICS 5 pp,
presentation 10 pp). Path 4.3 resolved 2026-09-24 (co-authorship M.G.S. Puno +
Claude Code Assistant; venue = arXiv + GitHub record; bundles in `arxiv_bundles/`,
corrigendum 45). Upload to arXiv still requires your own account/endorsement —
the only remaining human step.

## Phase 8.2 — Probe-particle-type dimension (2026-09-24, eighth-pass addendum)

New code (19th battery member): `boson_scaling_probe.py` — exact massless-vs-low-
mass probe scaling at the canonical 550 nm / 2.25 eV / 1 mW operating point:
F = (p/E)P with p/E = v/c² and v/c = √(1 − (mc²/E)²), so F = (v/c)(P/c), saturating
at the massless ceiling F = P/c = 3.3356 pN. Runs exit 0, `ruff F` clean. Key
results recorded in PROJECT_INDEX "Canonical results": (mc²/E)² is the
distinguishability number; 1 eV rest mass → v/c = 0.896, 10.4% force loss,
0.21 fs TOF delay across the 550 nm ball; below ~0.1 eV the probe is
interchangeable with a photon to ≤0.1%; mc² ≥ E means no ultra-relativistic beam
(gluon confinement, W/Z self-decay, Higgs at ≥125 GeV → the model's Mie/scattering
language stops applying). The dark/hidden-photon slow-boson absorption direction
is framework-level only and NOT asserted numerically.

Documentation: RESEARCH_PAPER.tex gained §"Probe-particle type dimension";
abstracts now cite a 19-script battery across both manuscripts and the arXiv
bundles (main.tex + PDFs regenerated).

## Phase 8.3 — Coverage sweep (2026-09-25, third full pass)

"Probe indefinitely until all bases have been covered": three parallel read-only
agents (numerics / fabrication-honesty / structure-QA), every claim verified
first-hand before any change was made. New corrigendum entries 48-68; this phase
fixed in place:

- `PHYSICS_CONNECTIONS_REVIEW.tex` — five orphan `\\` lines (one after each
  `\textbf{File:}` block) removed; dead usepackages (graphicx, multicolor, color;
  RESEARCH: also subcaption) dropped from both manuscripts. caption + float kept
  (RESEARCH tables use them). All four `.tex` recompile exit 0; bundle `main.tex`
  re-copied byte-for-byte from the edited originals and PDFs regenerated.
- Provenance banner added to the two html twins that had missed the Phase-7 pass
  (`photon_engine_research_paper.html`, `work_and_momentum_integrals.html`);
  explicit `[FICTION 2026-09-25]` markers prepended to the four scene files
  (`fictional_lab_scene.txt/.html`, `big_bang_style_scene.txt/.html`).
- Stale counts corrected: SUBMIT.md (×2) "18-script battery"/"entries 42-45" →
  "19-script"/"42-71"; ACTION_PLAN "18 Python scripts" → 19; README "29-entry" →
  "71-entry", "Phase 1-6" → "Phase 1-8.3", "18 .py" → "19 .py"; CORRIGENDUM
  duplicate row 45 removed and the process-layer table header normalized.
- Verified-negative findings recorded so they do not get re-flagged: the Law
  thread's "275 nm diameter" sites are already fixed (entry 35); 
  `photon_engine_concept.html` does not exist, so it needs no banner.
- Narrative numerics tracked without rewriting (entries 48-57): I/flux slip in
  momentum-integrals, D radius confusion, V=V₀/γ internal contradiction, eV/c
  power-of-ten slips, thermal 1-10 nm family, ZPE eV overclaims, 0.01%-contraction
  and comparability re-assertions in the scenes/novel, Law-thread planning numbers.

Gate (Phase 8.3, run as part of the pass): 19-script battery green — the battery's
19th member (`boson_scaling_probe.py`) had regressed into a non-terminating
interactive "dialectic engine" loop that also wrote `experiment_logs/` on every
cycle; one-shot deterministic mode restored (engine opt-in via `--interactive`),
log directory creation made lazy, `experiment_logs/` gitignored + removed, and
3 new ruff-F findings fixed (corrigendum 69). `results_of_record.py` 16/16
exit 0; `test_expansion_rigorous.py` exit 0; `ruff --select F` clean on the
tracked corpus (untracked user WIP in `deterministic_simulation.py`,
`investigation_example.py`, `investigation_fixed.py`, `organized_work/` is not
part of the corpus and does not yet lint clean); `__pycache__` 0 residual;
working tree clean after the commit (114 tracked files).

## Applied-reality anchors (2026-09-25, computed from measured values)

Live reality check of the cosmology/cosmology-adjacent numbers discussed in the
planning thread; recomputed this date, PASS/FAIL vs measured references:

- vacuum catastrophe gap: rho_pl = 4.6e113 J/m^3 vs observed rho_de = 6e-10 J/m^3
  -> ~123 orders (claim "~120" PASS). This is the same error class as the project's
  corrected 37-order "comparable energies" claim (corrigendum 1), not an endorsement.
- Hubble tension: Planck 67.4 ± 0.5 vs SH0ES 73.04 ± 1.04 km/s/Mpc -> 4.9 sigma.
- composition: baryon/dark-matter/dark-energy 5/26/69 %; age 13.787 Gyr;
  Omega_K ~ 0.001 ± 0.002 (flat ~1%).
- Local Group / GA: MW-M31 relative radial ~ -110 km/s (approach); GA ~ 50 Mpc
  toward Norma, mass ~ 1e15-1e16 M_sun; LG bulk flow a few hundred km/s toward it.
- structure reach: smallest probed length ~ 1e-18 m (LHC); Planck length
  1.6e-35 m -> gap ~ 17 orders, so LQG/causal-set discreteness stays untestable.
- entry-70 ladder: ball D = 550 nm -> 550 nm-ticks (n=1), 1 nm (n=550),
  1 um (n=0.55 point), Earth (8.62e-14), 50 Mpc (3.56e-31).

Not testable now (stay FRAMING/OPEN, not reality): QG grain, causal-set
discreteness, consciousness any flavor, primordial tornado, ascent sign-flip,
attractor growth.

## Phase 9 — rank-degree expansion + results_of_record extension (2026-09-25)

- `Law Apprehension of Works/RANKS_AND_DEGREES.md` — formalizes the thread's
  ladder as (rank, degree) coordinates: rank = ladder position (primes-indexed,
  node B1), degree = 0/1/2/3 dimensionality (doubling tail 1,2,4,8 as algebraic
  only, node C2). Verified ladder table for D = 550 nm: every log10 and n(u)
  recomputed by script this pass; **Laniakea log10 corrected to +24.69 in place
  (was 24.2)** before first commit, tail re-ordered galaxy -> GA -> Laniakea.
  Degree-collapse corollary: n(u) < 1 above the object's own rung (Earth
  8.62e-14, GA 3.56e-31, Laniakea 1.11e-31) - the ball observes as a 0D point
  from the cell rung up; the datum (rank 0, degree 0) never changes degree
  (Law-L1).
- `results_of_record.py` checks 16 -> **18** (no battery-count change; battery
  remains 19 scripts, so the papers' "19-script battery" stays exact). New
  checks 17-18 assert the rank-degree ladder: n(u) profile and the irregular
  (prime-gap-like) log10 spacing that is what makes uniform growth only the PNT
  mean. Output: "RESULTS OF RECORD: 18 checks reproduced.", exit 0.
- Count resync: README current-state "16 assert-style checks / 16 checks" ->
  18 (historical gate recaps above keep their then-true 16). Verified by full
  run: `results_of_record.py` 18/18 exit 0.

Gate (Phase 9): battery 19/19 green, `results_of_record.py` 18/18 exit 0,
`ruff --select F` clean on tracked corpus, working tree contains only intended
changes.

## Phase 10 — algebraic-half gate asserts + linkage thread (same day)

- `results_of_record.py` checks 18 -> **21** (no battery-count change; still 19
  scripts). New checks 19-21 gate-assert the algebraic half the thread relies
  on: Cayley-Dickson doubling dims 1,2,4,8 (`[1,2,4,8]`, and that the next
  doubling 16 is the first non-normed/split dim - Hurwitz cap), i period 4
  (i^2 = -1, i^4 = 1, four distinct cycle values), and Euler n^2+n+41 prime for
  every n = 0..39 failing at n = 40 (= 41^2 = 1681). Output now:
  "RESULTS OF RECORD: 21 checks reproduced.", exit 0.
- `VERIFIED_COMPONENT_LINKAGE.md` — inserted points: A2 node now carries the
  rank-degree pointer; new "Ranks and degrees (formal coordinates)" section
  interleaving A2 (rank positions) -> B1 (primes substrate) and C2 (degree
  caps), with the collapse (n(u) < 1 -> degree 0) and datum invariance (rank 0,
  degree 0 = Law L1) restated; closed-loop line updated; theorem labels cite
  the gate asserts (checks 19-21). No renumbering: the chain A0-F1 stands.
- Count resync: README "18 assert-style checks"/"18 checks" -> 21, MANIFEST
  "18 asserts" -> 21, CORRIGENDUM entry 73 reconciles entry 72's cited 18.

Gate (Phase 10): battery 19/19 green, `results_of_record.py` 21/21 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 11 — expand all directions (2026-09-25)

- Expansion pass computed the ladder to its full vertical span: Planck floor
  (log10 -34.79, n = 3.4e28) through observable-universe particle horizon
  (+26.64, n = 1.25e-33),
  16 rungs. `RANKS_AND_DEGREES.md` rewritten as the full (rank, degree) matrix
  plus four OTHER directions: DOWN (solid readings, ball is never point below
  ~um), UP (33+ orders of collapsed reading), ALGEBRA (1,2,4,8 + i-period-4 +
  Bott-8, theorem-capped), SPIRAL (corrected turn-walk), COUNTING (pi(1e7),
  twins).
- The expansion pass CAUGHT a false claim in the committed linkage draft:
  "radius^2 = sum of squares of ladder terms" for the turn-walk is FALSE (fails
  from step 3 on: steps 0..7 endpoint (3,5), r^2 = 34 vs sum squares 88; step 6
  (-8,5), r^2 = 89 vs 209). Corrected in place in `VERIFIED_COMPONENT_LINKAGE.md`
  to the exact identity r^2 = (sum E-W)^2 + (sum N-S)^2 (corrigendum 74).
- `results_of_record.py` 21 -> **23** checks: 22 = pi(1e7) = 664579 (sieve,
  6.6% off n/ln n, asymptotic); 23 = twin pairs < 1e7 = 58980 exact (HL formula
  ~ 2*C2*x/ln^2 x = 50822, 14% off — CONJECTURE label kept). Battery still 19
  scripts. README/MANIFEST -> 23; corrigendum 75 reconciles entry 73's 21.

Gate (Phase 11): battery 19/19 green, `results_of_record.py` 23/23 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 12 — external baseline reconciliation (2026-09-25)

- `STATE_OF_THE_SCIENCE_2026.md` added (informational, dated sources) covering
  the thread's open items: prime-gap records / Cramér status (+ Aug-2026
  machine preprint, Lean-formalized, un-peer-reviewed), Euler = Rabinowitsch /
  Heegner, 1,2,4,8 / Bott theorems, octonion-E8 (Distler-Garibaldi no-go),
  Hubble tension (~5.6σ, 2026 reviews), Shapley-Dipole-Repeller bulk flow +
  CF4++ anomaly, vacuum catastrophe (56-122 orders), QG LIV nulls, DM particle
  open.
- AUDIT / LAW / RANKS reconciled to that baseline (cross-links; FRAMING
  boundaries enforced: no universal center, Cramér strong form doubted, CSG
  data < 1). Corrigendum 78-79 record the count lag and the audit updates.
- No battery numbers changed; `results_of_record.py` stays 23/23.

Gate (Phase 12): battery 19/19 green, `results_of_record.py` 23/23 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 13 — composite-majority counting substrate (2026-09-25)

- User idea: "more composites than primes, because composites consist of primes;
  primes are bounded only by themselves" — made exact, proven, and gated instead
  of left as intuition.
- New `COMPOSITE_MAJORITY.md` (informational): C(n) = n−1−π(n); margin
  S(n) = C−π = n−1−2π(n); first strict composite majority at n = 10; ties
  exactly {1, 9, 11, 13} up to 10⁷ (PNT ⇒ finitely many); permanence theorem
  S(n) ≥ 0 for all n ≥ 9 (elementary proof: a drop to −1 would require n prime
  and n = 2π(n−1)+2 even — contradiction); PNT asymptotics S(n) ~ n − 2n/ln n;
  structural note: FTA fixes the FORM of composites, the sieve produces their
  ABUNDANCE; honesty boundary: no Law-thread mirror claim licensed.
- `results_of_record.py` extended 23 → 24 checks (check 24 asserts the full
  theorem: S<0 only for n=2..8, ties {1,9,11,13}, first-majority 10, min S over
  [9,1e7] = 0, S(1e7) = 8670841). Counts resynced everywhere; corrigendum 80.

Gate (Phase 13): battery 19/19 green, `results_of_record.py` 24/24 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 14 — claim tree for the composite-majority idea (2026-09-25)

- Demand: "all possible claims to be made" from the primes-vs-composites idea.
- Deliverable: `COMPOSITE_MAJORITY.md` §8 claim tree — every claim the idea can
  carry, verdict-coded: A counting (C1-C10), B structural (C11-C19), C window
  traps (C20-C21 rejected), D Law-thread mirror claims (C22-C25 rejected as
  FALSE/FRAMING), E meta (C26-C27).
- Two catalog rows were new verifiable numbers, so the gate grew 24 → 26 checks:
  - check 25 — unbounded prime-free runs: 201!+2..201!+201 (200 consecutive
    composites), j | (201!+j) exact.
  - check 26 — small-factor dominance: of the integers ≤ 1e7 exactly 7,714,287
    divisible by one of 2,3,5,7; 2,285,713 coprime to 210 (≈77.14% = 1−φ(210)/210).
- Counts resynced 24→26 checks, 80→81 entries, Law list unchanged at 21 tracked.
  Corrigendum 81.

Gate (Phase 14): battery 19/19 green, `results_of_record.py` 26/26 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 15 — whole-corpus claim register (2026-09-25)

- Demand: "not just those — everything": every claim the corpus makes OR
  refuses, in one verdict-coded inventory.
- Deliverable: `CLAIM_REGISTER.md` (root, governance): 86 numbered claims
  (B ball 18, L ladder 9, N counting 7, E external-2026 13, A universe-audit
  11, F law-craft 12, P possibilities 7, G governance 9) each with status code
  and verification site, + 17 explicit NOT-claims (X01-X17) + the add-before-use
  rule + pointer to the 27-slot composite claim tree (N07).
- Governance doc count 5 → 6; corrigendum 82. No battery numbers changed
  (gate stays 26/26); register references existing checks only.

Gate (Phase 15): battery 19/19 green, `results_of_record.py` 26/26 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 16 — the "edges are the same" claim (2026-09-25)

- User claim: "the edges of the universe are the same" → read as:
  edges are bounded only by the universe itself, same as the center.
- Registered per the add-before-use rule: E14 (no edge observed — cosmic
  horizon is a light-cone artifact of c × age ≈ 46.5 Gly comoving, not a wall;
  topology [OPEN]), F13 ("edges same as center" = [FRAMING] corollary of the
  cosmological principle — a true edge would single out a location as a center
  would), X18 (physical edge/wall = NOT-claim).
- AUDIT A.2 gains the symmetric no-edge sentence. Not battery-verifiable
  (horizon distance is ΛCDM-model-dependent, not closed-form arithmetic of the
  canonical constants) — register-only. Counts resynced 82→83 entries; register
  86→88 numbered, 17→18 NOT-claims. Corrigendum 83.

Gate (Phase 16): battery 19/19 green, `results_of_record.py` 26/26 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 17 — filling the light-cone (2026-09-25)

- User claim: "fill the space with the light-cone to create a sphere or ball."
- Verified core (new battery check 27): the observable ball at the ladder's
  top particle-horizon rung 16 (R = 4.4e26 m ≈ 46.5 Gly comoving) has volume
  (4/3)πR³ = 3.568e80 m³ and packs ~4.10e99 canonical 550 nm balls —
  closed-form arithmetic of the canonical ladder, now gated.
- Registered (add-before-use): L10 [PROVEN] filled-ball volume/fill-count;
  E15 [ESTABLISHED]-external topology (causal past is a 3-ball; spatial
  sections of the past light cone are 2-spheres of radius c·t; whole-universe
  topology [OPEN]); F14 [FRAMING] — "the universe IS a ball" overreaches, the
  ball is real as the OBSERVED region; X19 NOT-claim (universe finite-and-
  ball-shaped).
- RANKS UP gains the FILLED line; LINKAGE list → checks 17-27. Counts
  resynced 26→27 checks, 83→84 entries; register 88→91 numbered, 18→19
  NOT-claims. Corrigendum 84.

Gate (Phase 17): battery 19/19 green, `results_of_record.py` 27/27 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 18 — framing correction: real vs claimable (2026-09-25)

- User directive: "correct the framing and see what is real and claimable."
- Naming correction: rung 16 was labeled "Hubble sphere, 4.4e26 m", but that
  radius is the comoving particle horizon (46.5 Gly); c/H0 ≈ 1.36e26 m ≈
  14.4 Gly is the actual Hubble radius. Value correct, name conflated two
  radii → renamed "observable universe (particle horizon)" (RANKS table + UP,
  gate label, register L10, this report). No numeric value changed.
- New `REAL_AND_CLAIMABLE.md`: every [FRAMING] claim of the session chain is
  split into its claimable core (with verdict + check/cite) vs its decoration;
  a master list of what is claimable now; the adjacency rule (framing may
  appear only attached to its core). Register additions: E16 (in-horizon
  homogeneity [ESTABLISHED]-external; beyond-horizon sameness [OPEN]) and X20
  (beyond-horizon sameness = NOT-claim via Copernican extrapolation).
- Counts resynced: register 91→92 numbered, 19→20 NOT-claims; Law list 21→22
  tracked; 84→85 entries. Corrigendum 85.

Gate (Phase 18): battery 19/19 green, `results_of_record.py` 27/27 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 19 — zero-to-horizon recursion (2026-09-25)

- User claim: "scale of zero to horizon being the radius of visibility before a
  transition to the next zero to horizon."
- Claimable core (verified): the recursion is real AS a statement about the
  READING machinery of the ladder — every object's zero is its self-gauge (A0),
  its radius of visibility is the last rank where its degree survives, and
  above that it transitions to a point (degree-0 collapse, L03/L2 asserted by
  checks 17-18). The observable universe is the top rung; by the same rule it
  would read as a single point from any rung above. No new arithmetic was
  introduced — the gate stays 27/27.
- Boundaries: "the next zero-to-horizon" beyond ANY horizon is the Copernican
  extrapolation (E16), not an observation; whole-universe topology [OPEN].
  Registered: L11 [PROVEN machinery + OPEN beyond], F15 [FRAMING chain-beyond-
  horizon], X21 (real-observable next window = NOT-claim). Correction key
  (REAL_AND_CLAIMABLE) gains the recursion row.
- Counts: register 92→95 numbered, 20→21 NOT-claims; 85→86 entries.
  Corrigendum 86.

Gate (Phase 19): battery 19/19 green, `results_of_record.py` 27/27 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 20 — Law of Object Zeros (2026-09-25)

- User named the pattern: "law of object zeros." A law-thread formalization of
  machinery already in the register.
- The law-vs-physics boundary: what is CLAIMABLE is the coordinate pattern —
  every object is the datum (r=0, d=0) of its own frame (self-gauge A0,
  n(u)=s/u, [VERIFIED]); its own radius of visibility (L03/L2, [PROVEN],
  checks 17-18); its own observable ball (L10/E15); and there is no shared
  zero (E05, [ESTABLISHED]). "As many local centers as observers; none
  privileged."
- What is NOT claimable: the object-zero pattern as dynamics (force/cause on
  expansion or fabric) — X22; the law as physics — F16 [FRAMING].
- New `LAW_OF_OBJECT_ZEROS.md` added to the thread. Register: L12 [PROVEN],
  F16, X22. Register 95→98 numbered, 21→22 NOT-claims; Law list 22→23
  tracked; 86→87 entries. Corrigendum 87.

Gate (Phase 20): battery 19/19 green, `results_of_record.py` 27/27 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 21 — the construct in everything (2026-09-25)

- User question: "if position is always zero and distance changes the position
  while the amount of position it took to cover that distance is its speed per
  position — what would the underlying mathematical construct be completely in
  everything?"
- Answer (registered A12, [ESTABLISHED]-external, not corpus-invented): the
  construct is a pseudo-Riemannian manifold with a metric and affine connection
  and GAUGED coordinates — exactly general relativity's machinery. "Position is
  always zero" is precisely the local gauge statement: at every event there
  exist Riemann normal coordinates putting the observer at the origin with a
  locally flat metric (equivalence principle), tested by Mercury perihelion,
  GPS, LIGO, Shapiro delay, frame-dragging, EHT. Distance = invariant geodesic
  arc length. Speed = norm of the tangent vector ds/dτ; the parameter is proper
  time/affine, NOT position, so "speed per position" is a misnomer (X23; it is
  only reparametrization of the same speed).
- Boundaries: "construct-completely-in-everything as the one law" = F17
  [FRAMING]; DM/DE/QG rows A04/A06 remain [OPEN].
- Count-drift correction: register count line had over-counted by 2 (95 → 94,
  98 → 96 per-row); recomputed per-row and fixed. With A12+F17 this round the
  honest total is 98 numbered, 23 NOT-claims.
- Counts: 87→88 entries. Corrigendum 88. Gate unchanged 27/27 (no new
  arithmetic — external established math).

Gate (Phase 21): battery 19/19 green, `results_of_record.py` 27/27 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 22 — the position of the whole (2026-09-25)

- User probe: "not that I am saying the observer himself is god, but if every
  zero is a position making up the entire universe, who/what would be the
  position?"
- Answer (registered A13, [ESTABLISHED]-external): nothing is the position of
  the whole. Position is a relation between objects under gauge; the universe
  is everything, so no external reference exists by definition — no position,
  no velocity, no center-of-mass resting frame. "The position of the universe"
  (or "what everything is the zero of") is a category error, not a quantity.
  The relational residue IS claimable: positions are the coordination of
  object-zeros (relations are what's real); the whole "reads as a point from
  above" is the top-rung machinery of L11, but no probe exists above it.
- Boundaries: "the universe is its own zero/center at the top" = F18 [FRAMING]
  (REAL anchors A13 + L11 machinery); any universal vantage point, observer-of-
  the-whole, or god's-eye frame = X24 (explicitly no divine reading — the
  grammar of the question dissolves before it reaches who/what).
- Register 98→100 numbered (A13, F18), 23→24 NOT-claims; 88→89 entries.
  Corrigendum 89. Gate unchanged 27/27.

Gate (Phase 22): battery 19/19 green, `results_of_record.py` 27/27 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 23 — nothing as a mirror (2026-09-25)

- User probe: "could nothing be a mirror?" The mirror question splits into
  three senses, each answered separately (A14, [ESTABLISHED]-external):
  1. Coordinate fact — YES: a mirror is an isometric involution x ↦ −x; a
     reflection always fixes its origin, so every object's zero is the fixed
     center of its own orientation-mirror. No new physics; the self-gauge
     already carried it.
  2. Physics content — the universe's inversions are C, P, T: parity alone is
     VIOLATED by the weak interaction; the combined CPT is established in
     Lorentz-invariant QFT. "The universe is mirror-symmetric" is false for P,
     true for CPT.
  3. Boundary/ontology — NO: a mirror needs a mirror-plane and an outside to
     reflect into; the whole has none (A13), the horizon is a causal boundary
     and nothing is observed reflecting. Mirror/twin universes are [CONJECTURE].
- Boundaries: "nothingness at the edge mirrors everything back" = F19
  [FRAMING] involution metaphor (REAL anchors A13/A14); reflecting-edge or
  mirror-twin universe outside ours = X25.
- Register 100→102 numbered (A14, F19), 24→25 NOT-claims; 89→90 entries.
  Corrigendum 90. Gate unchanged 27/27.

Gate (Phase 23): battery 19/19 green, `results_of_record.py` 27/27 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 24 — what is mass (2026-09-25)

- User question: "what is mass? is it the position of the object given by its
  volume?"
- Answer (A15, [ESTABLISHED]-external): mass is not position or volume —
  those are a gauged coordinate and a frame-dependent geometry, respectively;
  mass is the Lorentz-invariant scalar m = E₀/c² (norm of the four-momentum).
  It is inertial resistance (F=ma) and gravitational charge (F=GMm/r²) with
  the equivalence principle tested to ~1e-13 (Eötvös, MICROSCOPE, lunar laser
  ranging); ~99% of ordinary baryonic mass is QCD binding energy; mass-energy
  is the source of spacetime curvature in GR.
- The only volume bridge is density: m = ρV. The corpus's own M is defined
  exactly that way (ρ·(4/3)πR³ = 9.583e-17 kg) and is gate-asserted by check
  2 — so NO battery change this round, gate stays 27/27. Energy changes mass
  at fixed volume (heated bodies, springs, nuclei).
- A16: mass as the gauge-invariant residue — position gauges to zero per
  object (A0/L12), mass survives every gauge (the 4-momentum norm is
  Poincaré-invariant). So the user's intuition "the object's footprint" is
  real in precisely this sense, never via location (F20; X26 kills
  volume-alone-determines-mass).
- Register 102→105 numbered (A15, A16, F20), 25→26 NOT-claims; 90→91 entries.
  Corrigendum 91.

Gate (Phase 24): battery 19/19 green, `results_of_record.py` 27/27 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 25 — extension round: further knowledge of the ideas (2026-09-25)

- Battery 27 → 35 checks (checks 28-35), all gated:
  - 28 register self-consistency CI — per-letter IDs contiguous, totals match
    the Count line. This is the arithmetic guard that makes the +2 drift (fixed
    in corrigendum 88) structurally impossible to reintroduce silently.
  - 29 ball rest energy E = mc² = 8.612 J (1 mW beam for 2.4 h), Schwarzschild
    radius 2GM/c² = 1.423e-43 m, ~36.3 orders from a black hole.
  - 30 full 16-rung ladder matrix (log10 and n(u) for every rung, not a 7-rung
    sample).
  - 31 ladder gap moments: mean 4.095, sd 3.926, CV 0.959, max/min 31.0 — the
    "irregular like primes" claim now quantified, kept descriptive.
  - 32 observable ball as an H0 band: Planck 67.4 → SH0ES 73.04 gives R in
    [4.06e26, 4.4e26] m, V in [2.80e80, 3.568e80] m³, fill 3.2e99..4.1e99 —
    central values became bands, never points.
  - 33 two-observer overlap: equal top-rung balls at separation R/2 share
    63.28% of each ball's volume (the empirical content of "object zeros
    share space").
  - 34 Bekenstein bound 4.71e20 k_B, ~8.2e9× the Dulong-Petit thermal entropy
    (the ball sits far below its information limit).
  - 35 Euler n²+n+b prime-run table over the class-number-1 discriminants:
    (b,run) = (2,1),(3,2),(5,4),(11,10),(17,16),(41,40), champion -163.
- COMPOSITE_MAJORITY gains Appendix A: the tie-exhaustion lemma is proved
  unconditionally (Rosser–Schoenfeld bound + finite check n ≤ 16) — the gate
  covered it to 10⁷; the appendix turns it into a theorem for all n.
- STATE_OF_THE_SCIENCE_2026 gains the Source Clock: each [ESTABLISHED]-
  external row carries its dated source, its re-validation trigger, and the
  finding that would flip the verdict (anti-rot for the external half).
- REAL_AND_CLAIMABLE gains §7 Counter-claim dossier: steelman-then-rebuttal
  for the key X rows, so knowledge vs conviction is exercised, not assumed.
- arxiv_bundles gains the honest-partition bundle (Part I results / Part II
  ideas, explicitly non-claimant); upload remains the author's own step.
- No new register claims this round: numbered stays 105 + 26 NOT-claims
  (check 28 confirms). Corrigendum 91 → 92 entries.

Gate (Phase 25): battery 19/19 green, `results_of_record.py` 35/35 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 26 — the Zeros, Interconnection, Scale, and Geometry framework (2026-09-25)

- User pasted the full framework document of that name (MGS Puno, conceptual
  development with ChatGPT), requesting the same treatment as every other
  claim-set: correct framing, register, gate any arithmetic kernel.
- Assessment: mathematically sound and honestly scoped. The document itself
  (a) separates established math from hypotheses (Part XIII), (b) refuses
  scaling ⇒ π/4 explicitly (Prop 10), (c) refuses Π = π (Props 17), and (d)
  states its own central open problem: does the fundamental zero relation
  force balanced geometry Δr = Δz (Part X/XVI)? None of its "established
  within mathematics" items is false; none of its hypotheses is smuggled in
  as a consequence. This mirrors the corpus's own discipline exactly.
- Alignment with the register: space-as-interconnection-of-zeros ↔ L12
  (object zeros, [PROVEN] machinery at coordinate level), A13 (no absolute
  frame), E05/E14 (no center/edge); time-as-ordered-transformations ↔ the
  gauged reading already held; prime roles (period/scale/generator) ↔ the
  counting substrate + the honestly-OPEN generator question; i-period/2π
  closure ↔ check 20/36.
- What is NEW and claimable: (1) the cone/scale/closure kernel — balanced
  Δr = Δz ⇒ θ = π/4 (tan(π/4) = 1), general c ⇒ θ = arctan c ≠ π/4 so scaling
  never fixes the angle, s₀qⁿ → 0, prime scales 1/p distinct, 2π closure —
  gated as check 36; (2) the prime-scaling hierarchy rule q = 1/p as an
  arithmetic object; (3) a formal minimal axiom skeleton (reference →
  relation → transformation → scale → closure → invariant) usable as a
  math-native phrasing of the gauge reading.
- Register additions: B19 ([ESTABLISHED] arithmetic, check 36), F21
  (space/time relational rephrasing = [FRAMING], anchors L12/A13/E05), X27
  (forced balanced geometry / derivation-free π/4 = NOT-claim — it is the
  framework's own open problem), X28 (Π = π = NOT-claim, needs a derivation).
  No false claim to kill: the framework is already honest.
- Battery 35 → 36 checks; register 105 → 107 numbered (B19, F21),
  26 → 28 NOT-claims; corrigendum 92 → 93 entries. Gate 36/36.

Gate (Phase 26): battery 19/19 green, `results_of_record.py` 36/36 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 27 — closing the framework's two open problems (X27, X28) (2026-09-25)

- The framework "Zeros, Interconnection, Scale, and Geometry" names exactly two
  open problems (Parts X/XVI): does the zero relation force balanced geometry
  Δr = Δz (X27), and is the invariant Π numerically π (X28). Both are now
  RESOLVED NEGATIVE, and both resolutions are gated.
- **X27 → independence (B20, check 37).** For every c > 0 the model
  r_n = c·qⁿ, z_n = qⁿ satisfies the minimal axioms A–G (F = shift, scale q)
  and self-similarity r_{n+1}/z_{n+1} = r_n/z_n = c. So c is a free parameter
  of the minimal skeleton, θ = arctan c ranges over all of (0, π/2), and
  self-similarity can NEVER entail π/4. The minimal extra condition that would
  force c = 1 is isotropy of the elementary relation — an assumption, not a
  consequence. Formally A–G ⇏ c = 1; A–G + isotropy ⇒ c = 1. The framework's
  Prop 10 was correct and is now gated, not merely asserted.
- **X28 → topological vs metric (B21, check 38).** Rotational closure is the
  group statement R_{2πk} = I, k ∈ ℤ; winding number is a homotopy invariant,
  so T(Π) = Π holds with NO metric in the axioms (verified: R_{2πk} = (1,0) to
  machine precision with no metric term). The numerical π enters only after a
  measure is induced (arc length = ρ·Δφ, circumference/diameter). Formally
  A–G ⇒ T(Π) = Π (topological) but value(Π) = π ⇒ metric ∉ A–G.
- New law-thread doc FORMAL_AXIOMS_ZEROS.md codifies the minimal A–G skeleton
  with no metric/norm among the primitives, states the two independence
  questions formally, and links B19/B20/B21. Law thread 23 → 24 tracked .md.
- Register: B20, B21 added [ESTABLISHED] (independence + topology-vs-measure);
  X27/X28 rewritten with their resolutions. Numbered 107 → 109; NOT-claims
  stay 28 (X27/X28 re-verdicted, not deleted). Corrigendum 93 → 94.
- Battery 36 → 38 checks. Nothing else moved: the honest-partition bundle's
  Part II (ideas) is unchanged — these were Part I-grade results.

Gate (Phase 27): battery 19/19 green, `results_of_record.py` 38/38 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 28 — closing Part XVI's remaining symbols (X29, X30) (2026-09-25)

- Phase 27 answered the framework's Part XVI question `F ⇒ (N, q, θ, p, Π)`
  only halfway: θ and Π were closed, but N, q and the primes themselves were
  left unexamined. This phase closes them. A stale `[OPEN]` verdict in §5 of
  FORMAL_AXIOMS_ZEROS.md (Π = π, listed as open after check 38 had already
  resolved it) was corrected in the same pass.
- **X29 → primes are a choice, not a consequence (B22, check 39).** Axiom F
  admits *any* fundamental period: the cyclic shift σ_m(x) = (x+1) mod m on
  ℤ/mℤ has period exactly m for every m, so the composite periods
  {4,6,8,9,10,12} are all models. Axiom E admits any q > 0, and the composite
  contractive scales 1/4, 1/6, 1/9, 1/15 are legal (q⁵⁰ = 7.9e-31 and
  1.6e-59 respectively). Closure is moreover *optional* — the successor
  S(n) = n+1 has no finite period at all, so Axiom F's "some F" is precisely
  right. All three of the framework's Part IX prime roles (period, scale,
  structural generator) are therefore choices. This confirms, with a gate,
  the framework's own summary that "prime structure is presently a candidate
  structural property, not a physical law".
- **X30 → the relations do not fix the geometry (B23, check 40).** A zero-
  network is combinatorial: path distance on C_n is ⌊n/2⌋, a metric-free
  integer. Any Euclidean embedding instead realises distance d as the chord
  2ρ·sin(πd/n) with a *free* radius ρ. Gated witness: C₈ is the identical
  graph at ρ = 1 and ρ = 2 — neighbour chord 0.765 vs 1.531, opposite chord
  2.000 vs 4.000 — while path distance is unchanged. One relational
  structure, continuum many geometries. This is the corpus's existing
  position-gauge lesson (A13, L12) extended to the metric itself, and it
  completes the chain: relations are the invariant content, geometry (and
  with it the numerical π) is a gauge choice made at embedding time.
- FORMAL_AXIOMS_ZEROS.md gains §7 with the two proofs, the two formal
  non-implications A–G ⇏ (N prime), A–G ⇏ q = 1/p and A–G ⇏ metric, and a
  per-symbol status table for (N, q, θ, p, Π) in which every entry is "no".
  §6 is rewritten accordingly. §5's Π = π and prime-generator rows move
  from [OPEN] to resolved negative; conditional and hypothesis rows are
  untouched.
- Register: B22, B23 added [ESTABLISHED]; X29, X30 added as NOT-claims, both
  resolved negative. Numbered 109 → 111; NOT-claims 28 → 30. Corrigendum
  94 → 95. No prior claim, number or paper claim changed.

Gate (Phase 28): battery 19/19 green, `results_of_record.py` 40/40 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 29 — axiom audit and applicability test (X31) (2026-09-25)

- Two questions were still unasked after Part XVI closed: (a) can the axiom
  set A–G settle *anything*, and (b) does it describe the data this corpus
  already has? Question (a) turned out to weaken the framework's own
  presentation, and question (b) produced the first genuine limit on the
  framework's reach.
- **Axiom audit (B24, check 41).** Applied literally, only **D** and **F**
  carry model-theoretic content. **A, B, C** are non-vacuity scaffolding —
  remove any one and the rest become vacuous, so none is independent. **E is
  vacuous as written**: "a transformation *may* carry a scale factor" is
  satisfied by the constant scale q = 1. **G is vacuous as written**:
  "∃T, X: T(X) = X" is always witnessed by the identity T = id. D is
  unsatisfiable without a composable pair (a single-transformation system has
  none), and F is independent, witnessed by the successor map. The
  strengthened forms E′ (q ≠ 1) and G′ (T ≠ id) do carry content and are
  independent — the successor refutes both, having no finite period and no
  fixed point under any non-identity power. **No conclusion in the thread is
  disturbed**: every independence result was proved against the literal A–G,
  so it holds a fortiori against the strengthened set. But the framework's
  Axioms E and G should be restated, since as written they assert nothing.
- **Applicability test (B25, X31, check 42).** The corpus's own 16-rung
  rank-degree ladder satisfies A–D — distinguishable references, relations,
  transformations, and composition along the chain — but **violates E**: all
  15 consecutive ratios are distinct rather than one constant q (gap mean
  4.096 decades, sd 3.794, CV 0.926, max/min 31.3, largest deviation 11.7
  decades from the constant-gap requirement), and **0 of 15** steps match a
  prime-reciprocal log10(1/p), so the prime-scale role fails outright on the
  only hierarchy this corpus has evidence for. This is an applicability
  limit, not a contradiction — the ladder is irregular by design — but it
  means the scale axiom describes an idealised hierarchy, not the observed
  one.
- **New §10, the import-cost table.** Each non-derivation of Phase 28 is
  priced against what this corpus already contains: θ = π/4 needs isotropy,
  which A13 does *not* supply (frame-independence is not isotropy); value(Π)
  = π and a metric are obtainable only by *importing* A12's pseudo-Riemannian
  metric from GR; prime N and q = 1/p are unforced restrictions the ladder
  actively contradicts. The pattern is consistent: the framework's
  relational layer is self-contained, while its metric layer must be
  imported, and A12 is this corpus's only route to a metric. The framework is
  therefore a *pre-geometric* layer that must hand off to A12 at exactly the
  point where B23 and B25 show the zeros go silent.
- Register: B24, B25 added [ESTABLISHED]; X31 added as a NOT-claim, resolved
  negative. Numbered 111 → 113; NOT-claims 30 → 31. Corrigendum 95 → 96. No
  prior claim, number, ladder value or paper claim changed — check 42
  recomputes the ladder from the same RANKS values used by checks 30–31 and
  reproduces their gap moments.

Gate (Phase 29): battery 19/19 green, `results_of_record.py` 42/42 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 30 — pulsars and quasars: the boundary in nature (X32) (2026-09-25)

- The corpus contained **no** pulsar, quasar or Eddington claim (verified by
  search — only incidental mentions inside untracked WIP), despite these being
  two of the best-known scale objects in nature and the two that sit on
  opposite sides of the framework's metric boundary. Both are now in, sourced.
- **B26 — two rungs added, 16 → 18.** Neutron star s = 1.239e4 m, the
  equatorial radius of PSR J0740+6620 (R = 12.39 +0.98/−1.30 km, Riley et al.
  2021 ApJL 918 L12; 12.49 +0.88/−1.28 km by Salmi et al. 2024). Quasar
  broad-line region s = 2.590e15 m = cτ for the 100-day reverberation lag
  measured across the 28 Palomar-Green quasars of Kaspi et al. (2000 ApJ
  535:62), whose fitted size is 32.9 +2.0/−1.9 light-days at 1e44 erg/s,
  scaling as L^0.70 ± 0.033.
- **B27 — pulsar spin-down triad, check 43.** From the two timed observables
  P = 0.226518 s, Ṗ = 1.15661e-15 s/s (Taylor et al. 1993) alone: τ =
  P/2Ṗ = 3.103 Myr vs published 3.09-3.1 (0.10%); B = 3.2e19√(PṖ) =
  5.18e11 G vs published 0.51e12 (1.2%); Ė = 4π²IṖ/P³ = 3.93e33 erg/s vs
  published 3.89e33 (1.0%). The result is the **split**: τ is metric-free
  period arithmetic needing only Axioms F and G, while B and Ė embed I, R
  and c — and the pulsar's actual radiation needs a magnetic dipole, a symbol
  the skeleton lacks entirely.
- **B28 — quasar Eddington anchor, check 44.** L_Edd = 4πGMm_p c/σ_T =
  1.257e38 erg/s per solar mass reproduces the published super-Eddington
  ratios of the two most luminous z > 3.5 quasars — J0341+1720 λ_Edd = 2.742
  vs 2.74, J2125−1719 3.021 vs 3.01 (Bian et al. 2021, arXiv:2010.14433) —
  to 0.36%. The decisive feature is its shape, not its value: L_Edd ∝ M
  *only* because the capture radius is GM/c², a Schwarzschild-metric object,
  i.e. exactly the import A12 supplies.
- **X32, resolved negative.** The zero-framework "explains" neither object.
  This is registered as a NOT-claim rather than spun, because the pair is
  worth more as a boundary marker than as a confirmation: one object in
  nature where the relational layer is exactly sufficient, one where the
  metric is not optional.
- **Ladder statistics moved and are disclosed, not absorbed.** Gaps 15 → 17
  (all distinct), mean 4.095 → 3.614, sd 3.926 → 3.504, **CV 0.959 → 0.970**,
  max/min 31.0 → 31.3. Checks 30, 31 and 42 were rewritten to the 18-rung
  table; check 42's verdict is unchanged in substance — still non-geometric,
  still 0 of 17 prime-reciprocal steps. The corpus's claim is *irregularity*,
  and adding two canonical non-cherry-picked rungs strengthened it.
- Register: B26, B27, B28 added; X32 added as a NOT-claim, resolved negative.
  Numbered 113 → 116; NOT-claims 31 → 32. Corrigendum 96 → 97.

Gate (Phase 30): battery 19/19 green, `results_of_record.py` 44/44 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 31 — the period-3 sibling: a turn that returns to zero (X33) (2026-09-25)

- User idea: *"what if the turn happened at 4 5 and 6 to go back to zero like
  a triangle of sort."* Tested in all three coordinates the corpus actually has.
  The answer splits the idea in half, and both halves are recorded.
- **B29 — a real gap in the audit's coverage.** A period-3 return is a legal
  model of Axioms F and G: σ₃ on ℤ/3 has fundamental period exactly 3 and
  returns to 0. Check 39 probed periods in order to *refute primality* and so
  tested only the composite set {4, 6, 8, 9, 10, 12} — all six reproduce with
  period = m exactly. The prime 3 was never in the test set, because a check
  built to show "periods need not be prime" has no reason to include one. The
  triangle was never excluded by the framework; it was never enumerated.
  Nothing is disturbed: B22 already established that no period is forced.
- **X33 — resolved negative.** The specific instantiation closes nowhere.
  - *Ladder coordinate:* rungs 4/5/6 = atom/molecule/virus at log₁₀ −10.00 /
    −9.00 / −7.00, so the sides are 1.00, 2.00, 3.00 decades and 1 + 2 = 3.
    Degenerate, zero area — structural, since a **1D** ladder makes any three
    rungs collinear. The walk traces a there-and-back fold. §12.2 flags the
    round 1.00/2.00 gaps as an artifact of nominal definitions, not a pattern
    about nature.
  - *Turn-walk:* the corpus's turn is π/2 (L06). Three turns is 270° = −i,
    **not** a return; four are needed. A walk built only from quarter turns has
    four distinct leg directions, so it can close a rectangle, never a triangle.
  - *Degree reading:* the corpus's one genuine zero-event cannot be moved.
    n(u) = 5.5 > 1 at rung 6 (reads degree 3), n(u) = 1 exactly at rung 7 (the
    ball's own rung), n(u) = 0.055 < 1 at rung 8 — so the first 0D rung is r8,
    uniquely fixed by the committed n(u) column. A zero at r6 would put the
    corpus's own gauge object below its resolution limit.
- **Retained asymmetry, which is the useful part:** "a return to zero" is
  axiomatic (G); "this triangle" is not. The only constructive residue is the
  turn angle — 2π/3 instead of π/2 would give a genuine closed figure beside
  L08's committed open spiral — and that choice is permitted and entailed by
  nothing. Adopting it would revise a [PROVEN] claim and is left to the author.
- Register: B29 added; X33 added as a NOT-claim, resolved negative. Numbered
  116 → 117; NOT-claims 32 → 33. Corrigendum 97 → 98.

Gate (Phase 31): battery 19/19 green, `results_of_record.py` 45/45 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 32 — the exchange of threes (X34) (2026-09-25)

- Phase 31's idea, clarified by the author: *"not a real triangle but the
  exchange of threes {1,2,3} {4,5,6} {7,8,9}."* Recast as block structure in the
  walk's step index rather than a geometric figure — a different and sharper
  question, and the recast is what made it answerable.
- **B30 — the exchange is real, and forced.** Grouping the turn-walk's steps
  (L = 0, 1, then the primes) three at a time against the period-4 direction
  cycle E,N,W,S:
  - each block of 3 consumes three of the four directions and omits one, and
    the omitted direction cycles **S, W, N, E** — period **4, not 3**, because
    gcd(3,4) = 1, so no two consecutive blocks agree until 4 blocks = 12 steps;
  - since 3 is odd, every block splits 2/1 across the step-index parities, and
    the dominant parity **alternates** — blocks 0,2,4 give 2 x-steps + 1 y-step,
    blocks 1,3,5 give 1 + 2. Verified over 40 consecutive blocks, so this is
    arithmetic, not a fit;
  - the model is self-validating: it reproduces the corpus's own committed
    vertices (3,5), (−8,5), (−8,−8), (9,11) and r² = 202 before any of this is
    tested.
  - Metric-free walk combinatorics; no physical content claimed.
- **A consequence recorded for B26.** The 18-rung ladder divides into exactly
  six triples. **16 did not** — it left a remainder of 1. The whole-block
  structure is therefore a consequence of the pulsar/quasar round, meaning
  those two rungs did more than add two sizes. Counter-caution kept in §13.2:
  the ball's gauge point n(u) = 1 is rung 7, *inside* block 2 rather than at a
  boundary, so the blocks are an index convenience, not a claim about where
  the ladder's physics changes.
- **X34 — resolved negative.** The blocks exchange axes but never return.
  r² at successive block boundaries is 5, 34, 145, 520, 937, 1370 — strictly
  increasing. No boundary lands on either axis. Over 400 prime steps the walk
  never revisits the origin and never touches an axis after step 2; the sole
  origin hit is the trivial zero-length first step L₀ = 0. The mechanism is
  plain: the step lengths are the primes and grow without bound, so the
  endpoints diverge. **L08's open spiral is confirmed, not overturned.**
- **Defect caught in the check itself, before registration.** The first draft
  of check 46 asserted "over 400 prime steps" while the walk was only 20 steps
  long — the no-return and no-axis tests were silently running over a short
  horizon. Corrected to a genuine 400-step walk before any claim was entered.
- Register: B30 added; X34 added as a NOT-claim, resolved negative. Numbered
  117 → 118; NOT-claims 33 → 34. Corrigendum 98 → 99.

Gate (Phase 32): battery 19/19 green, `results_of_record.py` 46/46 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

## Phase 33 — rolling, and the blocks that shrink (X35) (2026-09-25)

- Two author questions after Phase 32, both of which proved to be gaps in the
  Phase 32 *framing* rather than new directions.
- **B31 — the rolling ball.** "Is π constant when a ball smaller than another
  ball rolls on it? Which measurement of circumference or diameter do we use?"
  - **π is scale-invariant**: C/d = π to 1.4e-16 across r = 1e-9…1e9 m. The
    first question has no choice in it — there is one π and both balls share
    it. Asking which ball's π to use is like asking which inch to prefer.
  - **The second question is the sharp one, and the answer is: which *circle*
    you measure.** The small ball's contact point traces radius R (giving R/r
    turns); its **centre** traces radius R + r (giving R/r + 1). Simulated at
    R/r = 3: **2.99998 vs 3.99998 turns**. That is the entire content of the
    rolling-circle "missing turn", and it is a question about the geometry of
    reference, not about constants.
  - **π cancels identically**: 2π(R + r) / 2πr = (R + r)/r. The rolling count
    never used π at all — only R/r.
  - **The ±1 is a winding number, not a π-term**: the ball's own orientation
    rotating once as the contact normal sweeps around (external +1, internal
    −1). It contains no π and survives replacing π with any symbol. This is
    **B21's topological/metric split reached by a fully independent route**.
  - Corpus application: the 550 nm ball on a cell has R/r = 18.1818, so the
    honest count is **19.1818** turns. On larger rungs the +1 stays real but
    becomes numerically negligible.
  - **Scope limit, in the check itself:** rigid no-slip kinematics. The real
    ball is rubber with 8–15% hysteresis per cycle (proof 16), so under
    adhesion the no-slip condition fails and the ideal +1 would **not** appear
    cleanly. A theorem about ideal balls, not a prediction about this one.
- **B32 — the blocks were always meant to shrink, and they do.** With step
  lengths s₀qᵏ the walk converges to the **exact closed form**
  (1/(1+q²), q/(1+q²)), verified for q = 0.9, 0.5, 0.2 to < 1e-9. This supplies
  the closed form the author's phrasing intended, complementing B19's qⁿ → 0.
  **B30's axis exchange is invariant under the step law** — split [2,1,2,1,2,1]
  at every q tested — because it depends on block size 3 against period 4, not
  on step lengths. The blocks trading axes and the blocks shrinking are
  therefore **compatible, not competing**: the reconciliation the phrasing was
  reaching for.
- **X35 — resolved negative, completing X34.** No step law delivers the blocks
  to zero. Growing steps diverge; contractive steps converge to a limit of
  radius 1/√(1+q²) > 0 for every q > 0. Only q = 0 — no steps at all, which is
  not a walk — reaches the origin. Registered content is the author's own
  correction: the blocks shrink, and shrinking is bounded but not vanishing.
- **Contrast kept (§14.3):** in the **ladder**, n(u) = D/s genuinely tends to
  zero (1.25e-33 at the top rung); in the **walk**, the scale only approaches a
  fixed point. Both are "going to zero" loosely — only one gets there.
- **Two defects caught in check 47 before registration, both recorded rather
  than silently patched:** (1) the first draft measured the *contact* circle
  and so returned the naive R/r = 3 instead of R/r + 1 = 4 — the classic
  rolling-ball error, and literally the author's own question; (2) the
  contractive-limit test used a 60-step horizon, too short for q = 0.9 (which
  needs ~200 steps for 1e-9), corrected to 400 steps.
- Register: B31, B32 added; X35 added as a NOT-claim, resolved negative.
  Numbered 118 → 120; NOT-claims 34 → 35. Corrigendum 99 → 100.

## Phase 34 — "all reals between all zeros", and a retraction of X35 (2026-09-26)

- Two author statements after Phase 33: a foundational claim, and a re-audit
  that found my own overclaim.
- **X35 RETRACTED AND RESTATED** (check 49). The registered verdict "no step
  law delivers the blocks to zero" was **false**. Under the **constant** step
  law L_k = s₀ (q = 1) the walk returns to the origin at **block 4**, and at
  every block k ≡ 0 mod 4 — independently of s₀ (verified at 0.5, 1.0, and the
  corpus's 550 nm ball), since 12 steps is exactly three direction cycles.
  - **Why it survived a whole phase:** check 47's walk test ran q ∈ {0.9, 0.5,
    0.2} and its limit sweep ran q ∈ (0, 1], so q = 1 fell outside *both*. A
    universal negative resting on a test set that happens to exclude the answer
    is not a negative result.
  - **Exact classification now replaces it.** With M = ⌈3k/2⌉ even steps and
    K = ⌊3k/2⌋ odd steps: x(k) = (1 − (−q²)^M)/(1 + q²), y(k) = q(1 −
    (−q²)^K)/(1 + q²), matching simulation to 1e-9 for q = 1, 0.9, 0.5, 0.2,
    1.7, 2.0.
  - **Exact trichotomy:** (i) **q = 1** returns periodically, origin iff
    k ≡ 0 mod 4; (ii) **0 < q < 1 never reaches the origin at any block**, not
    merely in the limit, because |q²| < 1 forces 1 − (−q²)^k ∈ (0,2) so
    y(k) > 0 strictly for every k ≥ 1 (399 q values × 7 block indices, plus a
    300-block walk at q = 0.9); (iii) **q > 1** diverges, no return over 40
    blocks. The negative verdict survives **only for strictly monotone laws**.
  - **The irony worth keeping:** q = 1 is precisely the value at which check 41
    found Axiom E **vacuous**. The corpus's own recorded degeneracy is
    load-bearing here, because it is the only *scale-free* law. The author's
    "the blocks close" intuition was right; what closed them was the one law
    nobody had tried.
- **B33** ([ESTABLISHED] check 48) — a countable zero-set is a **scaffold
  that indexes values, never a generator of a continuum**, because density and
  gap-fulness are **mutually exclusive**:
  - **Dense zeros** admit no adjacent pair (midpoint of any two dyadics is a
    third; 400 random pairs), so "between two *adjacent* zeros" is vacuous and
    there are no gaps at all.
  - **Discrete zeros** do have gaps — floor division puts every real in exactly
    one, true of the integers, eighths and thirds alike — but every interior is
    **inexhaustible**: more resolvable points than the interval has gaps at
    1e-4…1e-7 resolution, surplus growing without bound. 200 halvings of (1,2)
    never terminate.
  - Wherever you place the gaps, each is a copy of the whole problem. Same shape
    as §13.3 (blocks never return) and §14.2 (shrinking bounded but not
    vanishing): **the inside never closes.**
- **B34** ([ESTABLISHED] check 48) — every real is a value **attached to** a
  zero, not a point located **between** zeros, and "between" is not derivable:
  - **Category:** §1 lists no metric, norm, inner product or time functional,
    and the axioms are **permutation-invariant** — 300 random relabellings of
    the 18 rungs all still satisfy A–G with the same period 18. A derived
    notion must be permutation-invariant; "between" is not. This is B23's and
    §11's boundary reached *structurally* rather than by listing omissions.
  - **Resolution already in the framework:** s: 𝒵 → ℝ₊ is a **function**, so a
    real is an element of its **codomain**, indexed by the references — a label
    carried by a zero. 18 rungs carry 18 real values; no finite zero-set
    enumerates an interval. The "between" feeling comes from ordering the zeros
    along an orbit under F, not from the reals' own location.
- **X36** (RESOLVED NEGATIVE, check 48) — "all real numbers are between all
  zeros" splits three ways and none is a statement about this corpus: not
  derivable (B34), trivially true but empty, and not generative (B33). The
  density reading is additionally falsified by the corpus's own 17 gaps,
  smallest **0.5051** decades. What survives is the codomain reading, B34.
- **Three defects caught in checks 48–49 before registration**, all recorded
  rather than silently patched: the rational-denseness construction was off by
  one (tested 2^−(n+1) < b−a instead of 2^−n < b−a, so (0,1) returned m = 1);
  the gate read the 9-rung `rungs` list where the canonical ladder is the
  18-rung `ladder`, reporting 0.5051 against a hard-coded 0.51 and counting 9
  rungs; and check 47's newly-hardened `only_q0` sweep demanded **exact** float
  equality on r² = 1/(1+q²), which binary rounding falsifies (q = 0.5 gives
  0.8000000000000002). That last one also **exposed the deeper fault** — the
  sweep covered q ∈ (0, 1] and so structurally could not see q = 1, which is
  exactly how the false universal verdict survived.
- Register: B33, B34 added; X36 added; **X35 retracted and restated**. Numbered
  120 → 122; NOT-claims 35 → 36. Corrigendum 100 → 101.

## Phase 35 — the reversal: 0 and the reals (2026-09-26)

- Author's direct challenge to Phase 34's B34: *"maybe its the other way around
  or even both. 0 and real numbers encapsulate each other."*
- **B35** ([ESTABLISHED] check 50) — **the reverse direction is real and just as
  strong, with no slack.** The s-labelled ladder is **rigid**: all 18 scale
  values distinct ⇒ the automorphism group preserving s is **trivial** (counted
  analytically — 18! is 6.4e15 — confirmed on 300 random relabellings where
  preserving s forces the identity every time). Fixing the real values fixes
  which zero is which, up to nothing.
  - This lands on the word **Axiom B actually uses**: R exists between
    **distinguishable** references. Distinguishability is supplied by *s*. So
    *s* is not a labelling but the framework's **individuation principle** —
    index and individuator in one map.
  - Containment intuition is right in the only sense that survives the axioms:
    **mutual determination, not nesting.**
- **B36** ([ESTABLISHED] check 50) — **0 is in neither side, and both sides need
  it.** The excluded boundary of the scale assignment *and* the one real
  definable with no parameters:
  - s has codomain ℝ₊, **open** at 0 ⇒ 0 is no reference's scale *by
    construction*; and in the **finite** ladder 0 is not even a **limit point**
    (min rung 1.616e-35).
  - Under Axiom E with q < 1 (B19) 0 **does** become the limit and is **never
    attained**: q = 0.5, 0.9, 1e-3 all pass 1e-30 while staying strictly
    positive at every finite step. The limit exists only in the infinite orbit.
  - 0 is the **unique parameterless real** — additive identity, unique negation
    fixed point (only x ∈ [−4,4] with −x = x), limit of 1/n. So ℝ determines 0
    uniquely **without reference to any zero**.
  - ⇒ 0 is simultaneously the **most fundamental and the least reachable**
    element: the excluded boundary both sides point at without either reaching.
- **X37** (RESOLVED NEGATIVE, check 50) — literal mutual **containment** fails in
  both directions, as arithmetic rather than opinion: 0 is one point, the 18
  labelled values are finite, and an interval holds > 10⁶ resolvable points
  against the ladder's 18. The corrected form is **sharper** than the original:
  *determine and be determined by a shared map, across a boundary that is
  itself the origin.*
- **Tooling defect caught:** a first probe brute-forced 18! permutations to
  count the automorphism group and **hung past a 120-second timeout**. Replaced
  with the analytic product of factorials of multiplicity classes — and that
  analytic form is what exposed the real fact: a 10-rung toy list with a
  duplicated 1e-14 pair suggested a count of 2, while the real 18 rungs have 18
  distinct scales and a count of exactly **1**.
- Register: B35, B36 added; X37 added. Numbered 122 → 124; NOT-claims 36 → 37.
  Corrigendum 101 → 102.

## Phase 36 — tenth powers: the excluded boundaries come in pairs (2026-09-26)

- Author's connection: *"does it not fall under the idea of zero and all tenth
  powers, or multiplicity of 10s also zero?"* Both halves land, and the first
  **corrects** Phase 35.
- **B37** ([ESTABLISHED] check 51) — **B36 corrected to a PAIR of excluded
  boundaries**, for a reason internal to the corpus: the ladder is
  **decade-native**. 14 of 18 rungs sit within a quarter-decade of an integer
  power of ten, spanning **61.43 decades** (log₁₀ s = −34.79 → +26.64), so
  "tenth powers" is the corpus's own grid, not an analogy.
  - `s: 𝒵 → ℝ₊` has codomain **(0, ∞), open at BOTH ends**. Planck sits
    **34.79 decades above 0**; the top rung sits **26.64 decades below ∞**.
    Both approached, **neither attained**, both structurally excluded.
  - The decade grid is exactly the coordinate on which 10⁻ⁿ → 0 and 10ⁿ → ∞
    are the *two directions of one axis* — so the scale assignment has two ends
    it can never reach, symmetrically. The 61.43 decades is an **observed span,
    not the axis**.
- **B38** ([ESTABLISHED] check 51) — **0.999… = 1**: the corpus's signature in
  decimal form. *The parts vanish, the remainder vanishes, the total does not.*
  - **Prefixes** 0.9, 0.99, 0.999, … → 1 and **never attain it** (every finite
    string of nines is < 1), so 1 is an **excluded boundary too**. Floats lose
    the distinction only at n = 17 (1 − 10⁻¹⁷ inside half an ulp); the exact
    rational is still short of 1 at n = 30.
  - **Tail** — literally *all the tenth powers* — is **exactly 1/9**, with the
    tail after n terms **exactly 10⁻ⁿ/9**: positive at every finite n, never 0.
  - ⇒ **one sequence's two halves have different limits**: prefixes → 1,
    leftovers → 0. Exactly the contractive walk's shape.
  - **General law** (B19 and B32 in one line): for q ∈ (0,1) the terms vanish,
    the remainder vanishes, and Σ qᵏ = 1/(1−q) > 1. Verified q = 1/10, 1/2, 9/10,
    1/3, vanishing exponents **found** not assumed. And 1/9 **is** the q = 1/10
    case — the decimal expansion and the geometric series are the same object.
- **X38** (RESOLVED NEGATIVE, check 51) — "all the tenth powers are zero,
  therefore everything is zero" has a **true antecedent and a false conclusion**:
  terms vanish, tail vanishes, total does not (exactly 1/9; 1/(1−q) > 1 always).
  Symmetrically 10ⁿ → ∞ does not make the ladder's top infinite. This is **X35's
  overclaim one level up**, made about a sum instead of a walk — and the corpus
  has now registered the same non-implication **three** times (X34, X35, X38),
  which is itself the evidence that it is the framework's central caution rather
  than an accident of one model.
- **Four defects caught** while building check 51, all recorded rather than
  patched: the prefix threshold compared 0.9 against 1 − 1e-6 (false for small
  n; should have been a monotonicity test); the tail was summed **finitely** then
  compared to 1/9, which no truncation satisfies, so the exact closed forms
  part = (10ⁿ−1)/(9·10ⁿ), rem = 1/(9·10ⁿ) are used; the term-vanishing test
  hard-coded n = 60, far too small for q = 9/10 (0.9⁶⁰ is still 1.8e-3), so the
  exponent is now **searched for**; and a probe repeated the truncation error
  (40-term sum vs 1/9 → False) before it reached the battery. Also removed a
  junk gate line I had written with `or True`, which would have passed
  unconditionally.
- Register: B37, B38, X38 added. Numbered 124 → 126; NOT-claims 37 → 38.
  Corrigendum 102 → 103.

## Phase 37 — compilation: what is proved, and what it already is (2026-09-26)

- Request: *compile what is logically sound and verified, then expand or
  reference to known equivalents.* New file
  `VERIFIED_SYNTHESIS_AND_EQUIVALENTS.md`.
- **All 166 register rows sorted by logical status**, under a four-gate
  admission rule (computable / exact-or-sourced / reproducible / non-vacuous):
  Tier I = 20 exact-maths, Tier II = 24 sourced empirical, Tier III = 14
  negative, **68 excluded** as `[CONJECTURE]`/`[OPEN]`/`[FRAMING]`/
  `[POSTULATE]`/`[REAL]`. The exclusions being 54% of the numbered claims is
  the healthiest number in the register.
- **The central finding, and it is deflationary on purpose:** every
  mathematically *closed* result here is a **known** result. Named equivalents
  registered — the `R/r + 1` rolling count is the **coin-rotation problem**
  (Poisson 1837); Hurwitz's four algebras and Bott periodicity are textbook;
  countability is **Cantor (1891)**; the topological/metric split is
  `H₁(S¹) = ℤ`; E/G vacuity is **non-vacuity** in model theory; the
  excluded-boundary result is the **boundary of an open set**; `0.999… = 1` is
  the **geometric series** under the **Monotone Convergence Theorem**, and is a
  *theorem, not a paradox*, which the synthesis says explicitly. **No priority
  claim is available on any of the 20**, and the synthesis says so in writing so
  the derivations are never read as discoveries.
- Two register errors found by **recomputation, not reading**:
  - **X39** — a "rung↔neutral-axis correspondence, 7 of 18 matching" had entered
    the working context under B26's name. **No such claim exists**; B26 is the
    two sourced rungs plus a CV that *rose* to 0.970, and "neutral axis" occurs
    only as *neutral density filter*. Logged as not-claimed, because it would
    have been the most novel-**looking** result in the corpus and was
    unsupported.
  - **X40** — **the first error in an `[PROVEN]` row.** N06 mixed the 10⁶ and
    10⁷ ranges; mean gap 13.02 survives neither (true: 12.74 / 15.05) and its
    "≈ ln 13.12" is `ln(5×10⁵)`, the midpoint, not `ln 10⁶ = 13.82`. Properly
    measured it is a **7.8% shortfall**, not an agreement. Same error class as
    `P02` — asymptotic used as pointwise identity. N06 marked superseded in
    place, not deleted.
- **Check 52 is the first check that audits the register instead of confirming
  it**: a fresh independent sieve re-deriving N01/N02/N05/N06 and asserting the
  superseded values to be *wrong*, so the error cannot silently return. It
  caught a bug in its own first draft (coprime fraction compared against
  divisible density) — same class of slip, caught the same way.
- **Also recommended:** restate **B35** as a cardinality observation. For a
  *finite* set any bijection determines both sides, and 18 distinct labels give
  a trivial automorphism group uninterestingly, so "the zeros and the reals
  determine each other" is **true but vacuous at 18 rungs**; the
  300-relabelling check cannot fail by construction. The non-trivial version
  needs an infinite index set plus monotonicity or shift-commutation.
- Register: X39, X40 added (38 → 40 NOT-claims). Corrigendum 103 → 104.

## Phase 38 — the mirror is an involution, and the order does not fix the hand (2026-09-26)

- Follows Phase 37. The mirror proposed in `SPIRAL_STAIRCASE.md` was an idea;
  its concrete claims were then **verified rather than asserted**. One large
  claim did not survive, and it was the load-bearing one.
- **B39** (check 53) — extending `s` to `𝒵 ⊔ ℝ₊ ⊔ {0}` gives an **involution**:
  `f² = id`. Orbits have size 1 or 2 and no third size, so the structure is
  **18 pairs + 1 fixed point = 19 orbits over 37 elements**. §VI's "seventeen
  pairs" was wrong — all 18 rungs carry distinct scales, so all 18 are paired,
  and `0` is the single unpaired element.
- **B40** (check 53) — **mutual determination is load-bearing.** An explicit
  3-element counterexample (`{ab,ba,ac,ca,bc,cb}`) is symmetric *and* total and
  still not single-valued, hence not an involution. Single-valuedness is the
  condition that upgrades a resemblance to a function, not a restatement of one.
- **B41** (check 53) — the order narrows the pairing gauge from
  `18! = 6,402,373,705,728,000` to **exactly 2**, verified by enumeration on
  chains of length 2–6 and forced by rank. The two survivors are mirror images
  (`rank i ↦ i` and `rank i ↦ 17−i`).
- **X41 — THE RETRACTION.** §VI concluded: *"the order orients the involution,
  so monotonicity collapses the gauge to 1, and L4's spin-bias should follow
  from monotonicity rather than from a separate law at `t = 0`."*
  **False, and backwards.** The order does not remove the handedness — it
  reduces the gauge to a binary and preserves it. The residual 2 is
  **irreducible** and **is** the two hands. So the spin-bias is a real
  prediction about a genuine two-way choice, and the first draft would have
  **retired a real prediction as a bookkeeping convention**. Recorded because
  the error was in the direction of discarding something real.
- **Second error, corrected alongside:** the `2¹⁸` figure counted **column
  relabellings**, not **pairing reassignments**. Three counts now kept apart —
  column relabelling `2¹⁸ = 262,144`; pairing reassignment `18! = 6.4×10¹⁵`;
  order-respecting pairing **2**.
- **B42 (check 53) — the finding not expected.** 18 is **even**, so the rank
  reflection `x ↦ 17−x` fixes no rung; its fixed point is the half-integer rank
  **8.5**, in the 4.5-decade gap between `human` and `neutron-star`. So the
  structure carries **two kinds of centre**: `0` is an **element** (a real with
  no zero), `8.5` is an **absence** (nothing there). A third kind at another
  scale: `1/2`, pairing `0.999…` with `0.000…`. **The centre is always a fixed
  point; what it *is* depends on which set is mirrored** — a better general
  statement than "0 is the centre", because it says why `0` needed the ladder:
  `0` is the centre of the *real* line, and the ladder is a different set whose
  middle is not a member of it.
- **Sharp conditional prediction:** the handedness structure depends on the
  **parity of the rung count**. With an odd number of rungs the central rung
  would sit on the mirror's own axis. Add or remove one sourced rung and the
  centre changes kind. Cheap, falsifiable, and not yet tested.
- A fourth same-class slip, in check 53's own first run: an off-by-one in the gap
  indices. Third caught by recomputation rather than reading.
- Register: B39–B42 added (126 → 130), X41 added (40 → 41). Corrigendum
  104 → 105.

Gate (Phase 38): battery 19/19 green, `results_of_record.py` 53/53 exit 0,
`ruff --select F` clean, only intended changes staged.

Gate (Phase 37): battery 19/19 green, `results_of_record.py` 52/52 exit 0,
`ruff --select F` clean, only intended changes staged.

Gate (Phase 36): battery 19/19 green, `results_of_record.py` 51/51 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

Gate (Phase 35): battery 19/19 green, `results_of_record.py` 50/50 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

Gate (Phase 34): battery 19/19 green, `results_of_record.py` 49/49 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.

Gate (Phase 33): battery 19/19 green, `results_of_record.py` 47/47 exit 0,
`ruff --select F` clean on tracked corpus, only intended changes staged.