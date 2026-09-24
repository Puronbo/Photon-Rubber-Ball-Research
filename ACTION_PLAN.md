# Action Plan — Goal Paths to Completion

Grounding: everything tagged **[VERIFIED]** in `PROJECT_INDEX.md` is trusted;
everything else is narrative and is tracked in `CORRIGENDUM.md` (never silently
rewritten). This document is the actionable layer: each goal path lists concrete
tasks with a **Done** criterion and current status. A closing gate runs
`results_of_record.py` + the 18-script battery + `ruff check --select F`.

## Verified foundations (fast facts)

- Canonical numbers are reproducible with one command: `python results_of_record.py` (16 checks, exit 0).
- Central abstract claim ("relativistic/quantum/thermal comparable at β=0.04") is **false** (~37 orders apart); true coincidences: per-photon recoil KE ≈ ball zeropoint (9.9×), JKR adhesion ≫ kT (6.3e5×), contraction 0.22 nm = 6.4× the trap thermal RMS.
- 18 Python scripts = code of record (all green under `-W error::RuntimeWarning`); `ruff --select F` clean.
- The `.md/.html/.txt` corpus is generated narrative; the expert comments are generative, not reviewers.

---

## Path 1 — Verification gate  (STATUS: DONE)

| Task | Done criterion | Status |
|---|---|---|
| 1.1 `results_of_record.py` reproduces + asserts the canonical table | 16/16 checks, exit 0 | DONE |
| 1.2 Added to the reproducible battery (16 → 17 → 18 runs) | full battery exit 0 | DONE |
| 1.3 The false abstract claim has a code-of-record replacement | `energy_comparability_probe.py` verdict | DONE |

## Path 2 — Text/document integrity  (STATUS: DONE)

| Task | Done criterion | Status |
|---|---|---|
| 2.1 Corrupt docs repaired in place | `[FIXED]` entries in `CORRIGENDUM.md` (audit-doc Mie narrative, fabricated outputs, 55 nm, truncated fragments) | DONE |
| 2.2 Both `.tex` compile | `pdflatex` exit 0 under TeX Live (row separators + `\keywords` + orphan `\\` fixed; diameter→radius) | DONE |
| 2.3 All `tracked` corrigendum entries closed by decision | decision recorded: **keep as corrigendum** (no narrative rewrite); numeric claims corrected only where unambiguous | DONE |
| 2.4 Canonical maps current | `PROJECT_INDEX.md` + `CORRIGENDUM.md` + `AUDIT_REPORT_READINESS.md` updated through Phase 6 | DONE |

## Path 3 — Science forward: decisive experiments  (STATUS: DEFINED; execution is off-computer)

Each is ordered by expected information gain. Feasibility numbers are computed at
the verified constants (m=9.58e-17 kg, k_trap=3.55 N/m, T=300 K, λ=550 nm).

### 3.1 Radiation-pressure spring-constant measurement  (most decisive first)
- Physics: a beam at power `P` exerts F = rate·p with rate = P/(hc/λ), p = h/λ.
- Numbers: 1 mW → 2.77e15 photons/s → F = 3.33 pN (absorbed) / 6.66 pN (reflected); static deflection Δx = F/k = **0.94 pm**, i.e. 36× **below** the trap thermal RMS (0.034 nm).
- Consequence: rotation—either raise power to **~360 mW** (10× thermal floor at k=3.55 N/m, absorbed), soften the trap, or time-average. This quantifies the trade-off the narrative docs never stated.
- **Done:** observed static deflection ≥ 10× thermal RMS, OR an explicit trap-softening/time-averaging design that reaches it. Source: `work_and_momentum_integrals.txt`, `photon_engine_research_paper.txt` (numbers corrected here).

### 3.2 JKR adhesion / pull-off
- Predicted W_sep = 2.62e-15 J, v_stick = 7.4 m/s (energy bound; lossless ball bounces). Measurable via AFM push-in/retract.
- **Done:** pull-off force within verified JKR prediction, with the dissipative-bound caveat stated.

### 3.3 Melting-shift calorimetry
- ΔT_m = 0.661 K is computed from **assumed** inputs (σ_sl, L_f, T_m) — the honest first step is measuring them.
- **Done:** material inputs measured; shift prediction re-derived from data, not assumption.

### 3.4 Fixed-point contraction (long horizon)
- Contraction at β=0.04 is 0.22 nm (6.4× trap RMS) but requires β≈0.04 = 12 000 km/s; experimental route needs >MeV acceleration — theory-only until then. **Done:** if/when a table-top relativistic-velocity source materializes (see `expert_comments_experimental.txt`).

## Path 4 — Publication  (STATUS: STRUCTURALLY READY, not submitted)

| Task | Done criterion | Status |
|---|---|---|
| 4.1 Manuscript compiles | `RESEARCH_PAPER.tex` → PDF, exit 0 | DONE |
| 4.2 Pre-submission integrity pass | abstract "comparable energies" replaced by `energy_comparability_probe.py` verdict; `0.08 eV`-class numbers corrected; fabricated-expert framing removed; "275 nm diameter" checked | OPEN |
| 4.3 Authorship/journal decision | explicit decision recorded here before submission | OPEN |

## Definition of completion

Closed when: Paths 1–2 done (already); Path 3 designs carry verified feasibility
numbers; Path 4.2/4.3 explicitly decided; final gate below is green.

Final gate: `python results_of_record.py` (exit 0) + 18-script battery (all exit 0,
zero `[FAIL]`) + `ruff check --select F` (clean) + `__pycache__` residual 0.

## Status log
- 2026-09-24 — Plan created; Paths 1–2 complete; Path 3 carries corrected feasibility numbers; Path 4.2/4.3 open by design (requires a human author's decisions); final gate run and green.
- 2026-09-24 — Final gate **passed**: `results_of_record.py` 16/16 (exit 0), battery **18/18** under `-W error::RuntimeWarning`, `ruff --select F` clean (whole folder), `__pycache__` residual 0. `PROJECT_INDEX.md`/`AUDIT_REPORT_READINESS.md`/`CORRIGENDUM.md` synced to Phase 6.