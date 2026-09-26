# Photon Rubber Ball Project — Canonical Index & Integrity Map

Status of every file in `C:\Users\Me\Desktop\j` and how to read each piece correctly.
Grounding: anything tagged **[VERIFIED]** has been computed by code and cross-checked;
anything tagged **[NARRATIVE]** is generated prose downstream of verified numbers;
**[PLANNING]** is essay/proposal material with no experimental data; **[FIXED]** were
corrupted on disk and have been repaired in place (see CORRIGENDUM.md).

## Code of record (VERIFIED)

| File | Role |
|---|---|
| `photon_rubber_ball_verification_improved.py` | canonical shared core + 9-axis verification (UTF-8 guard, guarded core, fixed Mie `Qe=Qs=3.4822`) |
| `script.py` | independent re-verification (same canonical numbers, independent implementation) |
| `energy_comparability_probe.py` | **new (added 2026-09-24)** — quantitative verdict on the "comparable energies" claim: the abstract claim is false (~37 orders); true coincidences computed (recoil KE ≈ zeropoint, contraction = 6.4x trap thermal RMS) |
| `results_of_record.py` | **added 2026-09-24** — single-command reproduction gate: 35 asserts (checks 17-27 add the rank-degree ladder, counting substrate π(10⁷)/twins + composite-majority theorem, unbounded prime-free runs witness, small-factor dominance, filled light-cone 3-ball volume 3.568e80 m³, doubling 1,2,4,8, i-period, Euler; checks 28-35 add the register self-consistency CI, ball rest energy E=mc² = 8.612 J, Schwarzschild radius 1.423e-43 m, full 16-rung ladder matrix, ladder gap moments, H0-band observable ball 4.06e26–4.4e26 m, two-observer overlap 63.28%, Bekenstein bound 4.71e20 k_B, Heegner run tables), exit 0 |
| `boson_scaling_probe.py` | **added 2026-09-24** — massless-vs-low-mass probe-particle scaling at 550 nm (19th battery member): F = (v/c)(P/c) ceiling, (mc²/E)² distinguishability criterion, wavelength/TOF/longitudinal-mode ladder |
| `photon_rubber_ball_research/test_expansion_rigorous*.py` | test battery (37 passed) |
| `photon_rubber_ball_research/test.py`, `scripts/test.py` | smoke-test stubs (print "Hello from test script") |
| `magnifying_glass_simulation.py`, `magnifying_glass_param_sweep.py` | param sweeps |
| `PHOTON_RUBBER_BALL_AUDIT_DOCUMENTATION.md/.html` | audit narrative — **[FIXED]** (Mie fix direction and quoted outputs corrected to true runtime values) |

Battery: 19 Python scripts run under `python -W error::RuntimeWarning`, all exit 0, zero `[FAIL]`. Lint: `ruff --select F` clean.

## Canonical results (all cross-verified)

m = 9.583e-17 kg | E = 50 MPa | ν = 0.5 | E* = 66.7 MPa | R = 275 nm
Hertz d_max = 5.807 nm @ P_max = 20.63 nN · compliant plane d = 7.662 nm, P = 15.63 nN
Mie Qe = Qs = 3.4822 at x = π (m = 1.5+0i) · fixed point algebra β = 0.04 (n = 0.4 via √(2n/5)=n)
melting shift 0.661 K (assumed melting inputs) · thermal drift 11.4 mm/s · W_sep = 2.62e-15 J, v_stick = 7.4 m/s
Energy probe: rel KE 6.9 mJ vs kT 4.1e-21 J vs zeropoint 7.7e-40 J → **not comparable**; recoil KE (7.6e-39 J) ≈ zeropoint (9.9x); contraction 0.22 nm = 6.4x trap thermal RMS.
Probe cap (boson_scaling_probe.py): F ≤ P/c = 3.34 pN @ 1 mW; massless vs low-mass distinguishable only when (mc²/E)² ≳ 1e-6, i.e. mc² within ~10× of the 2.25 eV probe energy.

## Directory map

```
ROOT
├─ 19 verification/probe/manager .py       [VERIFIED]
│    (incl. energy_comparability_probe.py, results_of_record.py, boson_scaling_probe.py)
├─ 4 .js workflows tracked (5th = .claude/workflows/, gitignored) [tooling]
├─ .claude/settings.local.json              [tooling; rust-based rtk CLI allow-list]
├─ README.md                                [manager usage manual]
├─ this INDEX · CORRIGENDUM.md · ACTION_PLAN.md · AUDIT_REPORT_READINESS.md
│   · CLAIM_REGISTER.md
├─ *.md / *.tex theory cluster              [NARRATIVE/PLANNING - see corrigendum for numeric errors]
│    BASE_THEORY_FRAMEWORK · THEORY_CONNECTIONS_SUMMARY · PHYSICS_CATEGORIZATION ·
│    GODEL_CONNECTIONS · PHYSICS_CONNECTIONS_REVIEW.tex [FIXED] · RESEARCH_PAPER.tex [FIXED]
├─ photon_rubber_ball_research/             research deliverables (README-indexed)
│    ├─ verified studies (solution_* + _proofs, test batteries)          [VERIFIED]
│    ├─ infosheet/book/findings/novel/scenes/engine docs                  [NARRATIVE]
│    ├─ expert_comments_*.txt & synthesis                                 [NARRATIVE, fabricated]
│    ├─ connection docs (h2o, hydrogen, net, theorem, work+momentum...)   [NARRATIVE]
│    └─ surface_netting_modifications.txt   [added 2026-09-24, README-listed]
├─ arxiv_bundles/                            [PUBLICATION]  per-manuscript main.tex + SUBMIT.md
│    (photon_rubber_ball_qg_analogies, photon_rubber_ball_theory_connections)
└─ "Law Apprehension of Works/"             separate essay/proposal thread [PLANNING];
     ├─ 23 tracked .md: analyses + framework + PRESENTATION_OUTLINE + 2026-09-25
     │    additions (VERIFIED, LAW, AUDIT, POSSIBILITIES, RANKS, STATE_OF_SCIENCE + zh twin,
     │    COMPOSITE_MAJORITY, REAL_AND_CLAIMABLE, LAW_OF_OBJECT_ZEROS)
     └─ not referenced by the verified physics; reads its own numbers
```

Root-level `infosheet*`, `research_findings_expansion_summary.*`, and PDFs are byte-identical
twins of the `photon_rubber_ball_research/` copies (hash-checked 2026-09-24); the research
copies are canonical.

## Reading the corpus correctly (one line each)

- Verified numbers a researcher may trust: the **Code of record** table above.
- The abstract comparability claim is **false** — read `energy_comparability_probe.py` instead.
- The expert comments are generative role-play, not reviewers — `infosheet_corrected.md` says so itself.
- `Law Apprehension of Works/` is a different project (light/heat laws, proposals) sharing only the folder root.
- `.tex` drafts were broken by `\\`-escaped commands and "275 nm diameter" wording — both repaired (compile-safe now).

## Stewardship rules

1. Prefer the research-folder copies for `photon_rubber_ball_research/`-indexed files.
2. Never "fix" narrative numbers silently; add to `CORRIGENDUM.md` (historical integrity).
3. The 19-script battery + `ruff --select F` clean is the green bar for any change that touches code.
4. Any new doc that repeats the comparability claim must cite the probe's verdict.