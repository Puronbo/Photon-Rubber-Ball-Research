# Photon Rubber-Ball Research

Physics research on a **photon-sized rubber ball**: r = 275 nm, E = 50 MPa,
nu = 0.5, mass 9.6e-17 kg — one solid object where impact, Mie scattering,
thermal motion, and relativistic recoil act at intermediate (5-100) micron-Hertz
scales. Everything here is independently re-verified, discrepancies are cataloged
in `CORRIGENDUM.md` (never silently fixed), and the numbers are tracked.

## THE PAPER (the head)

- **`Photon_Rubber_Ball_PAPER.pdf`** — the compiled main manuscript (this is the
  head document of the repository; compiled from `RESEARCH_PAPER.tex`, exit 0).
- `RESEARCH_PAPER.tex` — LaTeX source: 9 verification axes + 5 theory extensions
  (quantum thermodynamics, decoherence, entropic gravity, black-hole analogies,
  fluctuation-dissipation), feasibility quantified in §5.
- `PHYSICS_CONNECTIONS_REVIEW.tex` — the connections review companion paper.

**Verified and mathematically backed.** Every number in the paper is reproduced
by the 19-script battery (`results_of_record.py` = 16 assert-style checks, exit
0; full battery green under `-W error::RuntimeWarning`). The mathematical backing
is explicit: the verified results fall on proven theorems — the prime-number
distribution (PNT), dimension-cap theorems (Frobenius, Hurwitz), Euler's
π/2-rotation period-4 (`i⁴ = 1`), Buckingham's π-theorem's dimensional factoring, and the
fluctuation-dissipation/Jarzynski/Crooks equalities — mapped node-by-node in
`Law Apprehension of Works/VERIFIED_COMPONENT_LINKAGE.md` (PROVEN vs CONJECTURE
labels, never conflated). Open conjectures (Riemann, Goldbach, Cramér gaps,
twin primes, Hardy-Littlewood quadratics) are cited as open, not used as proof.

## What to trust (verified foundation)

The canonical numbers are reproducible with a single command:

```bash
python results_of_record.py      # 16 checks, exit 0
```

The "comparable energies" abstract claim is **false** (~37 orders of magnitude
apart; see `CORRIGENDUM.md` entry 1). What survives as genuinely coincident:
per-photon recoil KE ~ ball zeropoint (9.9x), JKR adhesion >> kT (6.3e5x), and
the trap contraction 0.22 nm = 6.4x the trap thermal RMS. The 19-script battery
runs green under `python -W error::RuntimeWarning`; lint standard is
`ruff --select F` clean.

| Quantity | Value |
|---|---|
| mass M | 9.583e-17 kg |
| E*, E*_two | 66.7 / 33.3 MPa |
| Hertz d_max / P_max (rigid plane) | 5.807 nm / 20.63 nN |
| compliant plane d / P | 7.662 nm / 15.63 nN |
| thermal speed sqrt(3kT/m) | 11.4 mm/s |
| Mie Qe = Qs (x=pi, m=1.5+0i) | 3.4822 |
| melting shift | 0.661 K (assumed inputs) |

## Repository map (everything, organized)

```
├─ HEAD: Photon_Rubber_Ball_PAPER.pdf      the compiled paper (verified & math-backed)
├─ manuscripts/                            RESEARCH_PAPER.tex + PHYSICS_CONNECTIONS_REVIEW.tex
│                                          (pdflatex/xelatex, TeX Live 2026 exit 0)
├─ verified science (19 .py)               -- the code of record, runnable
│  ├─ photon_rubber_ball_verification_improved.py   9-axis battery (canonical core)
│  ├─ results_of_record.py                           reproduction gate: asserts the table
│  ├─ energy_comparability_probe.py                  verdict on the core claim
│  ├─ script.py · BLACK_HOLE_ANALOGIES.py · SHATTER_THRESHOLD_ANALYSIS(_EXPANDED).py
│  ├─ FLUCTUATION_DISSIPATION_CONNECTION.py · ENTROPIC_GRAVITY_ANALOGY.py
│  ├─ DECOHERENCE_COMPARISON.py · QUANTUM_THERMODYNAMICS_EXTENSION.py
│  ├─ COGNITIVE_UNIVERSE_MODEL.py · magnifying_glass_*.py · boson_scaling_probe.py
│  └─ photon_rubber_ball_research/         twin canonical copies + 37 tests
├─ verification & honesty                  PROJECT_INDEX.md (canonical map: start here)
│  │                                      CORRIGENDUM.md (70-entry catalog, 1 [FALSE], n [FIXED])
│  │                                      AUDIT_REPORT_READINESS.md (Phase 1-8.3 gate results)
│  │                                      ACTION_PLAN.md (Paths 1-4 to completion)
├─ the generated corpus (narrative)        .md / .html / .pdf / .txt twin documents
│      AUDIT_DOCUMENTATION · theory & connections · black-hole & shatter threads ·
│      fictional_lab_scene · research papers for novel · infosheets · surfaces
├─ arxiv_bundles/                          submission-ready staging (main.tex + PDF +
│      SUBMIT.md each; uploading needs your arXiv account/endorsement)
├─ tooling                                 ai_script_manager_final.py (launcher) ·
│      expert_audit_develop*.js worker fan-out · magnifying_glass_workflow.js
├─ scripts/                                manager targets (incl. scripts/test.py)
├─ logs/ · experiment_logs/                runtime logs (gitignored)
└─ Law Apprehension of Works/              planning thread (informational, NOT physics):
       VERIFIED_COMPONENT_LINKAGE.md (nodes A0-F1; theorem/conjecture linkage)
       LAW_OF_CENTER_ASCENT.md (law-craft, postulates flagged REAL vs POSTULATE)
       + GREAT_ATTRACTOR_REACTOR_ANALYSIS.md · SYNTHESIS_OF_ALL_WORK.md · ...
```

## Quickstart

```bash
# single-command reproduction gate
python results_of_record.py

# the full 19-script battery (all exit 0 under -W error::RuntimeWarning)
python photon_rubber_ball_verification_improved.py
python script.py
python energy_comparability_probe.py
# ... any other runner in the tree

# lint standard
ruff check . --select F

# compile the head paper
pdflatex -halt-on-error RESEARCH_PAPER.tex
```

## Stewardship rules

1. `photon_rubber_ball_research/` copies are canonical; the root copies mirror them.
2. Never silently rewrite narrative numbers — only `CORRIGENDUM.md` records changes.
3. The 19-script battery + `ruff --select F` clean is the green bar for any code change.
4. Path to completion and open publication tasks: `ACTION_PLAN.md` (Paths 1-4).
5. The Law Apprehension of Works thread is planning material: informational only,
   never citable as measured physics without a battery step (corrigendum 25/57 policy).

## Publication status

Both `.tex` manuscripts compile under TeX Live 2026 and passed the Phase-8
pre-submission integrity pass (corrigendum 42-44): no experiment is claimed to
have been run, energy scales are stated as ~37 orders apart (corrected), feasibility
is quantified in §5, and "expert audit" means automated code review. Co-authorship
is recorded (M.G.S. Puno + Claude Code Assistant, corrigendum 45); arXiv bundles
are staged in `arxiv_bundles/` — uploading requires your own arXiv
account/endorsement (see each bundle's `SUBMIT.md`). The head PDF is compiled
from the same source and is byte-current with both bundles' stage.