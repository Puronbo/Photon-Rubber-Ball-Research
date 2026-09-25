# STATE OF THE SCIENCE 2026
## (external reference for the thread; informational only)

Status: **INFORMATIONAL** — last researched 2026-09-25 via live web sources (dates/DOIs cited
inline; each bullet is independently verifiable). This file makes **no physics claims** for the
corpus, changes **no battery value**, and is framed like AUDIT_OF_THE_UNIVERSE: it records what
the external literature currently says, so the thread's speculation (LAW_A, RANKS, VERIFIED
linkage, POSSIBILITIES) can be written and read against a dated, cited baseline. Evidence labels:
**ESTABLISHED** = theorem/measured; **OPEN** = not resolved; **CONJECTURE** = believed/undecided;
**FRAMING** = the thread's own label, not external physics.

Where a claim here crosses into corpus physics, the corpus must go through the battery and
CORRIGENDUM. None of the numbers below is gate-asserted; do not cite them from
results_of_record.py.

---

## 1. Number-theory flask (nodes B1, C1, E1; battery checks 19-23 territory)

### 1.1 Bounded prime gaps — ESTABLISHED (theorem-level), twin primes still OPEN
- Zhang 2013: H1 < 7e7 (first finite unconditional bound). Polymath8a: 4680. Maynard 2014: 600,
  plus Hm < ∞ for all m. Polymath8b (2014): **H1 ≤ 246** unconditional; **H1 ≤ 6** under the
  Generalised Elliott–Halberstam conjecture, which is the **limit of the sieve method** (Selberg
  parity obstruction). As of 2026-09 no further unconditional improvement has been accepted; 246
  remains the state of the art. Source: Castryck, Tao, et al., "The bounded gaps between primes
  Polymath project — a retrospective," KU Leuven; Maynard, Ann. of Math. 181 (2015) 383–413.
- Battery relevance: check 19 (doubling 1,2,4,8) and check 21 (Euler) are math-fact asserts; the
  246-area is cited by the thread only as "the field brackets small prime gaps at 246" — that
  remains true.

### 1.2 Large prime gaps (lower bounds) — ESTABLISHED, with a NEW Aug-2026 preprint
- Westzynthius 1931: limsup g_n/log p_n = ∞. Rankin 1938 improved. Erdős's conjecture (2014):
  proven by Ford–Green–Konyagin–Tao and independently Maynard (both Ann. of Math. 2016); combined
  FGKMT 2018 (JAMS): g_n > c·(log p_n)(log log p_n)(log log log log p_n)/(log log log p_n)
  infinitely often.
- **Live development**: an Aug-2026 manuscript (authorship and role reported as an OpenAI
  "GPT-5.6 Sol" system) claims the improved bound g_n > c·(log p_n)(log log p_n)/(log log log log p_n)
  = G(X) ≫ (log X log₂X)/log₄X — a factor log₃X/(log₄X)² better than FGKMT — with a Lean
  formalization announced (B. Alexeev, Aug-2026). It is **not peer-reviewed** (as of 2026-09-25);
  treat as unverified preprint status, exactly as the corpus treats its own unverified items.
  If it survives review, it stiffens the large-gap side only; Cramér is a different (upper) claim.

### 1.3 Cramér's conjecture — OPEN; strong form widely DISBELIEVED
- Three forms: (a) g_n = O((log p_n)²); (b) limsup g_n/(log p_n)² = 1 (upthread "strong Cramér");
  (c) pointwise g_n < (log p_n)². All three unproven and undisproven.
- Known upper bounds: RH ⇒ g_n = O(√p_n·log p_n) (Cramér, conditional); best unconditional
  g_n = O(p_n^0.525) (Baker–Harman–Pintz 2001).
- Data vs the conjecture: the largest known Cramér–Shanks–Granville ratio
  g/(log p)² is **0.9206** (prime 1693182318746371); the record-merit gap (2017, Gapcoin,
  merit 41.9388) has CSG ratio only **0.2059**. So all known data sit below 1 — consistent with
  (c), far below the 1 of (b).
- Maier's theorem (1985) breaks the pure Cramér random model on short intervals; Granville's
  divisibility-corrected model gives limsup ≈ c ≥ 2e^(−γ) ≈ 1.1229 rather than 1. Majority reading
  (Granville, Pintz, Adleman–McCurley): the **strong form (limsup = 1) is likely false**; the
  O((log)²) order may still hold.

### 1.4 Prime-gap RECORDS (data, as of 2026-05) — ESTABLISHED (measured computations)
- Largest known gap with identified endpoints (probable primes): **16,045,848** after a
  385,713-digit PRP, merit 18.07 — A. Höglund, Mar-2024.
- Largest gap with **proven**-prime endpoints: **1,113,106** (merit 25.90, 18,662 digits) —
  Cami, Jansen, Andersen.
- Largest known **merit**: 41.9388 (gap 8350 after an 87-digit prime, Gapcoin 2017); second
  merit 40.246 (gap 42185402, 210 digits, R. Smith). Only two gaps with merit > 40 known.
- Largest maximal prime gap: **1,854** (85th maximal gap, after prime 101412319996363309069 —
  R. Smith, 2026). #maximal gaps up to the n-th prime is conjectured ≈ 2 ln n (ESTABLISHED belief).
- Thread consequence (RANKS "irregular prime-gap-like spacing", battery check 18): real prime
  gaps at any accessible log₁₀ height have merit ≈ 25-42 max and CSG < 1; the ladder's irregular
  log₁₀ step sizes (noise ~1-2 decades on a 60-decade backbone) are therefore *well within* the
  statistical norms of genuine prime-like spacing. The resemblance claim stays a resemblance
  (FRAMING), now backed by dated record data.

### 1.5 Euler's polynomial n²+n+41 — ESTABLISHED (theorem)
- n²+n+41 is prime for n = 0..39 and composite at n = 40 (= 41²) — battery check 21 (accurate).
- Rabinowitsch (1913): n²+n+A is prime for all 0 ≤ n ≤ A−2 **iff** Q(√(1−4A)) has class number 1.
  A = 41 corresponds to Q(√(−163)), class number 1 (Heegner–Stark). The odd lucky values
  A = 2,3,5,11,17,41 pair with Heegner numbers 7,11,19,43,67,163 respectively.
- Ulam spiral: the diagonal line-clustering that gives such polynomials its visual power has a
  partial explanation (certain binary quadratic forms) but **no complete theory** (OPEN as an
  explanation). The thread's use of 41 (B1 flask) is on solid theorem-level footing.

### 1.6 Doubling 1,2,4,8, Bott periodicity — ESTABLISHED (theorems)
- Hurwitz: real **normed** division algebras are only ℝ, ℂ, ℍ, 𝕆 (dim 1,2,4,8); Cayley–Dickson
  loses a property at each step (ℍ non-commutative; 𝕆 non-associative; 16-dim sedenions have zero
  divisors). Frobenius: the only finite-dim **associative** division algebras are ℝ, ℂ, ℍ.
- Bott periodicity: π_k of the stable groups is periodic with period 8 (real O) / 2 (complex U) —
  the 8-fold real period is the homotopy echo of the 1,2,4,8 chain. Also Adams: spheres S⁰,S¹,S³,S⁷
  are exactly the parallelizable spheres. (Battery checks 19-20 assert the doubling chain and the
  i-period-4 — both consistent with Bott.)
- Freudenthal–Tits magic square: exceptional groups F4,E6,E7,E8 built from pairs of division
  algebras with octonions on one side — the structural fact the thread's C2 note uses. Note the
  **physics** half (below) is NOT settled.

### 1.7 Octonion / E8 physics — SPECULATIVE (research program, not consensus)
- Live program: octonionic/trace-dynamics line (Adler trace dynamics; Chamseddine–Connes spectral
  action; split bioctonions; E8×E8 branching to SU(3)×E6 etc.; exceptional Jordan algebra
  eigenvalue constants; predictions of 6 forces incl. a "U(1)grav" MOND-like field). References:
  Inspire record "Trace dynamics, octonions and unification: an E8 × E8 ..." (Singh et al.).
- Formal obstacles: Distler & Garibaldi (J. Math. Phys. 2010) — "There is no E8 gauge theory" —
  a rigorous no-go against direct E8 GUTs realizing the standard fermion families; Lisi's earlier
  E8 proposal was never a completed theory. Status as of 2026: mathematically rich, physically
  unconvincing to the mainstream; keep the thread's C2 as FRAMING only.

---

## 2. Meter-flow flask (nodes M1-A; Mie, Hertz, JKR, thermal) — NO open item
- Hertz 1882 / Johnson–Kendall–Roberts 1971 / Mie 1908 / Dicke 1946 are textbook-verified and the
  corpus's use is battery-asserted (checks 1-16), including the circular-JKR scaling correction of
  corrigendum 76 (zero-load spot radius a ∝ R^(2/3), i.e. area ~ s^(4/3)). No research needed.

---

## 3. Self & center flask (nodes P1/P2, F/A) — the genuinely OPEN items

### 3.1 Hubble-tension — OPEN; unresolved as of 2026
- SH0ES (Cepheid–SN Ia ladder): H0 = 73.04 ± 1.04 (SH0ES-22; Riess et al. 2022). Planck base-ΛCDM:
  67.36 ± 0.54 (Planck 2020). A 2026 seven-route covariance review (Cepheid + TRGB + JAGB + Mira +
  SBF + TF + SNe II) gives 73.30 ± 0.92, i.e. **5.6σ above Planck**. DESI BAO (2025) sits near the
  Planck side (~68). Tension: **persistent, ~5-5.6σ, no accepted resolution**.
- Systematics being tested: JWST Cepheid crowding ruled out at 8.2σ (Riess 2024, >1000 Cepheids);
  TRGB route (Freedman/CCHP) yields ~69-70 and its champions argue part of the gap is ladder
  systematics; Pantheon+/CSP differences shift H0 by +2.0/+0.8 km/s/Mpc (2026 Chicago-Carnegie JWST
  TRGB paper). Campaign verdict (2026 reviews): more independent analysis needed; **not solved**.
- Corpus stance update: AUDIT_OF_THE_UNIVERSE's "open anomaly" wording is correct and current.

### 3.2 Great Attractor / Shapley / bulk flow — ESTABLISHED structures, anisotropic-flow anomaly OPEN
- The GA (Lynden-Bell 1987 inference) is now understood as largely the **Shapley supercluster**
  overdensity (l=311.5°, b=32.3°) plus the antipodal **Dipole Repeller** void (Hoffman et al. 2017):
  a gravitational dipole system driving local motion.
- Measured dipole bulk flow (Pantheon+ SNe Ia, 0.015 ≤ z ≤ 0.06; 2024): **132 ± 109 km/s toward
  (l,b) = (326.1°, 27.8°)**, i.e. toward Shapley, >99.9% confidence for the direction; effective
  depth ~103 Mpc; the antipode lands on the Dipole Repeller. (The velocity's huge relative error is
  itself worth honoring: direction significant, magnitude less so.)
- Larger scale: CosmicFlows-4 minimum-variance estimates (2023-2025, Phil. Trans. R. Soc. A 2025 /
  CF4++ 2025) find the bulk flow **grows** with radius instead of decaying — at R = 200 h⁻¹ Mpc the
  observed amplitude would occur in ΛCDM with only ~0.003% probability. This is an OPEN anomaly
  against the cosmological principle; the CF4++ group is currently hunting the homogeneity scale.
- **Crucial counterweight (honesty for node P1)**: none of this makes Shapley/GA a "center of the
  universe". The cosmological principle is tested by CMB isotropy (Planck: no preferred direction
  beyond the dipole; the dipole 369 km/s vertex (l,b) ≈ (264°, 48°) frame-of-the-Sun motion is
  innocuous), galaxy-survey large-scale homogeneity (volume-average density flat to ~1% above
  ~250 h⁻¹ Mpc), and BAO/CMB standard rulers. The thread's P1 "ascent toward center" is FRAMING:
  the universe has no observed center; the ladder's "center-ward" direction is a constructed
  coordinate, not a place.

### 3.3 Vacuum catastrophe (cosmological constant) — OPEN; the number is 56-122, not a clean 120
- Observed ρ_vac (Planck 2015): 5.96e-27 kg/m³ ≘ 3.35 GeV/m³. QFT zero-point estimate vs that:
  **50 to 122 orders** depending on method. Naive Planck-mass cutoff: ~120 (some citations 122-123)
  — the famous "worst prediction in physics". Lorentz-covariant regularizations (dimensional
  regularization/renormalization) reduce the mismatch to **~56-60 orders** (2026 AJP pedagogical
  article; Wikipedia current). Either way: an unresolved OPEN problem, no accepted mechanism, and
  the honest figure is a range with the naive-120 "widely repeated but method-dependent".
- Corpus note: if a narrative cites "~120 orders", it is citing the naive figure; the defensible
  range is 56-122. No corpus text currently makes this claim (verified by grep).

### 3.4 Quantum-gravity discreteness — OPEN, no evidence; stringent null limits
- No observational signature of spacetime discreteness has been confirmed (LQG/causal-set
  phenomenology remains untested in principle).
- Strong nulls from time-of-flight: GRB 221009A / LHAASO (Piran & Ofengeim, PRD 109 L081501, 2024):
  linear (n=1) LIV scale ≥ 5.9-6.2 E_Pl; quadratic (d=6) ≥ 5.8e-8 E_Pl.
- A minority analysis (Song & Ma, arXiv:2504.00918, 2025) claims E_LV ≈ 3.0e17 GeV (~10^-2 E_Pl)
  and 3.1σ rejection of dispersion-free vacuum from 17 GRB photons — controversial, not consensus,
  and the ≤7 TeV data can be explained without LIV (intrinsic multi-TeV prompt emission; e.g. the
  GRB 221009A prompt TeV component). Treat as a claim, not a result.

### 3.5 Dark-matter particle — OPEN
- As of 2026 no particle candidate detected: WIMP limits continue to deepen (LZ, XENONnT);
  axion windows remain partly unexplored; self-interaction bounds sharpen. Both WIMP and axion
  parameter space still open. POSSIBILITIES_AND_RELEVANCY's "unidentified DM particle" framing is
  accurate.

---

## 4. What the thread may rely on (dated, cited) — and what it must not

Solid (theorem or measured, dated above):
1. H1 ≤ 246 / H1 ≤ 6 (GEH, sieve-limit); 2. FGKMT large-gap lower bound (2018) + the unverified
   Aug-2026 preprint as preprint-only; 3. Cramér: all 3 forms unproven, strong form likely false,
   data CSG < 1 (max 0.9206); 4. gap records (16,045,848 PRP-end; 1,113,106 proven-end; merit
   41.94; maximal 1,854); 5. Euler n²+n+41 = Rabinowitsch ⁺ Heegner 163 (proved); 6.
   1,2,4,8 = Hurwitz/Frobenius/Adams + Bott 8-periodicity (proved); 7. Hubble tension live at
   5-5.6σ with no resolution (2026 reviews); 8. Shapley+DR dipole explains local bulk flow;
   CF4/CF4++ large-scale flow anomaly open; no universal center (cosmological principle intact);
   9. vacuum catastrophe real, 56-122 orders (method-dependent), open; 10. no QG discreteness
   evidence, LIV nulls strong; DM particle undetected.

Risky (do not assert as corpus physics):
- Any "center" claim for Shapley/GA/Laniakea; strong-Cramér exact constants; octonion/E8 physics
  unification; any vacuum-catastrophe "exactly 120"; LIV-scaled "3e17 GeV" claims; the Aug-2026
  preprint's bound before peer review.

---

## Sources (researched 2026-09-25; live-verified)
- 中文译本伴生文件：`STATE_OF_THE_SCIENCE_2026.zh.md`（canonical = 本英文原版；数字/编号出入
  以英文为准，修改须同步两端并经 corrigendum）。
- Wikipedia: Prime gap (records incl. 2026-05 maximal-gap 1854 and merit 41.94; CSG 0.9206);
  Cramér's conjecture (BHP upper bound, Maier/Granville/2e-γ, Aug-2026 preprint + Lean note);
  formula for primes (Rabinowitsch; not truncated detail on 41 yes via class number);
  cosmological constant problem (ρ_vac 5.96e-27 kg/m³; 50-122 orders; dimensional-reg ~56-60).
  Original pages carry revision timestamps 2026-09; data as-of dates given inline.
- Polymath/Maynard: Castryck, Tao et al., bounded-gaps retrospective (KU Leuven); Maynard, Ann.
  of Math. 181 (2015) 383-413; FGKMT, JAMS 31 (2018) 65-105.
- Hubble-tension 2026 reviews: "Chicago-Carnegie Hubble Program ... JWST TRGB" (ApJ, 2026);
  "Distance-ladder Measurements of H0" (RAA/1674-4527, 2026) [H0 = 73.30 ± 0.92, 5.6σ];
  Riess et al. 2022/2024; Planck 2020; DESI 2025.
- Bulk flow: "Bulk Flow Motion Detection with Pantheon+" (ApJ 965/…, 2024) [132 km/s, l=326, b=28,
  Shapley l=311.5/b=32.3, DR antipode]; "Challenges to the standard cosmological model from
  large-scale bulk flow estimates" (Phil. Trans. R. Soc. A 383, 2025) [0.003% at 200 h⁻¹ Mpc];
  "In search of the Local Universe dynamical homogeneity scale with CF4++" (A&A 2025).
- LIV/QG: Piran & Ofengeim, PRD 109 L081501 (2024); Song & Ma, arXiv:2504.00918 (2025) — as
  non-consensus; GRB 221009A LHAASO, Science Adv. 9 (2023).
- Octonion/E8: Singh et al., "Trace dynamics, octonions and unification" (INSPIRE record);
  Distler & Garibaldi, J. Math. Phys. 51 (2010) 062502 (no-go).
- Numbers embedded in this file (gap lengths, velocities, H0 values) are transcribed from the
  cited sources; where a transcription error is found, amend THIS file and add a corrigendum entry
  (same discipline as battery numbers, though this is informational only).