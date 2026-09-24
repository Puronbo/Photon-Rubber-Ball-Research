# Corrigendum — Documented discrepancies vs the verified numbers

Compiled 2026-09-24 after reading the entire corpus. "Verified" = computed by the
17-script code battery (see PROJECT_INDEX.md). Entries marked **[FIXED]** were
repaired in place the same day; all others are tracked here without silent rewriting
(historical integrity). The single most important correction is entry 1.

## The central claim

| # | Doc / site | As written | Verified truth | Status |
|---|---|---|---|---|
| 1 | `research_paper_findings.txt` abstract; `work_and_momentum_integrals.txt` §4.2 | "at β=0.04 relativistic, quantum, and thermal energy scales become comparable" | rel KE 6.9 mJ vs kT 4.1e-21 J vs ball zeropoint 7.7e-40 J — ~37 orders apart (run `energy_comparability_probe.py`) | tracked |
| 2 | `work_and_momentum_integrals.txt` §6 Ex.2 | s = ½(F/m)t² ≈ 5e-6 m (F=8e-25 N, 1 s) | ≈ 4e-9 m | tracked |
| 3 | `h2o_and_photon_connections.txt` / `hydrogen_atom_photon_bath.txt` §1 | retroactive citation of `surface_netting_modifications.txt` (created 2026-09-24) | file now exists; citation created-to-order | tracked |

## Numbers off in the narrative layer

| # | Doc / site | As written | Verified | Status |
|---|---|---|---|---|
| 4 | `expert_comments_thermal.txt:41`, `expert_comments_quantum.txt:34`, `synthesis:16` | "relativistic energy gain ~0.08 eV" at β=0.04 | (γ−1)mc² = 6.9 mJ ≈ 4e16 eV | tracked |
| 5 | `expert_comments_quantum.txt:34` | "quantum zero-point energy ~0.08 eV" | ball confinement ħ²/(2mR²) = 7.7e-40 J; 0.08 eV implies ~2 nm confinement | tracked |
| 6 | `photon_engine_concept.txt` §2.1, `photon_engine_research_paper.txt` §2.2 | "size parameter x = 2πr/λ ≈ 1" | x = π ≈ 3.14 (the actual verified scattering regime) | tracked |
| 7 | engine concept, engine paper, `work_and_momentum_integrals.txt` §6, hydrogen table | m ≈ 8.7e-17 kg | 9.583e-17 kg | tracked |
| 8 | multiple docs | v_th = √(kT/m) ≈ 2e-3 m/s | 6.7e-3 (computed); thermal drift 11.4 mm/s | tracked |
| 9 | `research_paper_findings.txt` §5.3 | ΔT_m ≈ 5.5 K (r=275 nm) | 0.661 K | tracked |
| 10 | `photon_engine_research_paper.txt` §3.2, concept §3.2 | "to 1 m/s needs ~7e10 photons ≈ 0.04 s" | 25 µs at full beam; ~3 yr at own interception rate 6.7e2 s⁻¹ | tracked |
| 11 | `photon_engine_concept.txt` §5.1, engine paper §5.1 | "~kT/λ ≈ 4 pN" | kT/550 nm ≈ 7.5 fN | tracked |
| 12 | `hydrogen_atom_photon_bath.txt` §1 | ω₀ = 4.13e15 Hz (Lyman-α, 121.6 nm); Γ ≈ 2π·8.2 MHz | c/λ = 2.47e15 Hz; Γ=2π·99 MHz consistent with its own τ≈1.6 ns | tracked |
| 13 | `research_paper_findings.txt` §2.2 | (n²·5)/2 = 50β² | (n²·5)/2 = 250β² (self-contradicts its §2.3) | tracked |
| 14 | `research_paper_findings.txt` §8.5 | ">1000 mm: Optical microscopy" | >1000 nm | tracked |
| 15 | `research_paper_findings.txt` §2 | "fifty-five nanometers, ten billion atoms" | diameter 550 nm | **[FIXED]** in both scenes |
| 16 | `expert_comments_thermal.txt:24` | surface deformation 5–50 nm | d_max = 5.807 nm | tracked |
| 17 | `expert_comments_relativity.txt:28` | contraction "relativistic effects begin to be measurable" | 0.22 nm vs trap thermal RMS 0.034 nm (6.4x) but below imaging resolution | tracked |
| 18 | `expert_comments_relativity.txt:21` | volume contraction factor "γ, not 1/γ" complaint | corrected in manuscripts per reviewer note | tracked |
| 19 | `theorem_connections.txt` | Banach: "unique fixed point n*=0.4, contraction everywhere" | not a contraction near 0 (|T'| diverges); fixed points are 0 AND 0.4 | tracked |
| 20 | `PHOTON_RUBBER_BALL_AUDIT_DOCUMENTATION.md`:24,71 (`.html`:180,247) | "Qe should be aa.real only, not aa.real+bb.real"; "now uses only aa.real" | the bug was omitting the `b_n` term; the fix sums aa+bb (Qe=Qs=3.4822) — described backwards | **[FIXED]** |
| 21 | same docs:125/126 (`.html`:333/334) | "= 33.300 MPa"; "d2=198.910 nm P2=132.80 nN" | 33.333 MPa; d2=7.662 nm P2=15.63 nN | **[FIXED]** |
| 22 | `PHYSICS_CONNECTIONS_REVIEW.tex:32`, `RESEARCH_PAPER.tex` abstract:52 | "275 nm diameter …" | radius 275 nm (diameter 550 nm) | **[FIXED]** |
| 23 | both `.tex` files | literal `\\`-escaped commands (`\\textbf`, `\\begin{itemize}`) → wouldn't compile | single backslash | **[FIXED]** |

## Process-layer notes (not numeric)

| # | Doc / site | Note |
|---|---|---|
| 24 | `expert_comments_*.txt` (5), `synthesis_of_expert_perspectives.txt` | generative role-play "expert" reviews; synthesis misattributes quotes (e.g., "Multi-scale framework required" appears in no individual file) and drops the thermal expert's hedges. `infosheet_corrected.md` disavows the expert layer outright. Treat as narrative. |
| 25 | `Law Apprehension of Works/` | `REAL_IMAGINARY_NUMBERS_ANALYSIS.md` §3.1 and `WHAT_EVERYTHING_MEANS_CONCRETELY.md` flip the real=viral/dissipative convention; `CONNECTION_AUDIT.md` rates Orch-OR/IIT/Gödelian "NOT CONNECTABLE" and entropic gravity "SPECULATIVE" while the presentation foregrounds them; axis numbering differs between SYNTHESIS and presentation/proposal; "pN/√N" should be "pN/√Hz"; `RESEARCH_PROPOSAL.md` budget lines sum ≈$2.7M vs stated $2.45M. Essay/planning thread — no data. |
| 26 | `UNIFIED_CONNECTIONS_FRAMEWORK.md`:339,372 | truncated fragments "forconsistency", "symmeinformation theory" | **[FIXED]** |
| 27 | `big_bang_style_scene.txt:31` / `.html:32`, `fictional_lab_scene.txt:5` / `.html:6` | "fifty-five nanometers" (55 nm) | **[FIXED]** to 550 nm |
| 28 | `logs/test_20260923_061950.log` | empty log, kept (benign named-empty) | — |
| 29 | `PHOTON_RUBBER_BALL_AUDIT_DOCUMENTATION` | claims "all numerical results identical" while its own (now fixed) Mie narrative contradicted itself | **[FIXED]** |

## Verified values a reader may rely on

m=9.583e-17 kg · E*=66.7 MPa · d_max=5.807 nm @20.63 nN · compliant d=7.662 nm P=15.63 nN ·
Qe=Qs=3.4822 (x=π, m=1.5+0i) · β=0.04 algebra (n=0.4) · melting 0.661 K · 11.4 mm/s ·
W_sep=2.62e-15 J, v_stick=7.4 m/s · recoil KE 7.6e-39 J ≈ zeropoint 7.7e-40 J (9.9x).