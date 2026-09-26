# VERIFIED SYNTHESIS AND KNOWN EQUIVALENTS

*Compiled 2026-09-26. Scope: every claim in `CLAIM_REGISTER.md` (126 numbered +
40 NOT-claims) sorted by **logical status**, each paired with the **standard
result it already is**. The point of this document is not to advertise the
corpus. It is to establish, claim by claim, exactly which results here are the
corpus's own and which are textbook — so that nothing in the register is
mistaken for novelty, and nothing genuine is buried among the rest.*

---

## 0. The admission rule

A claim enters this compilation only if it passes **all four** gates:

| gate | test |
|---|---|
| **A. Computable** | the claim is decidable by a finite calculation, not an interpretation |
| **B. Exact or sourced** | arithmetic is exact (rational/algebraic), or every input number carries a citation |
| **C. Reproducible** | it is in `results_of_record.py` and passes (52/52, exit 0) |
| **D. Non-vacuous** | the calculation could have come out otherwise, and did, somewhere in the record |

Anything failing **A** is *framing* and is excluded from §1–§3 regardless of how
inspiring it sounds. This is the register's own `P07` relevancy rule applied to
the corpus itself: **a connection is never a validation.**

| tier | meaning | count |
|---|---|---|
| **I** | exact mathematics, closed, no physical input | 20 |
| **II** | sourced empirical, arithmetic gated | 24 |
| **III** | negative results — refutations with witnesses or models | 14 |
| **—** | excluded: `[CONJECTURE]` `[OPEN]` `[FRAMING]` `[POSTULATE]` `[REAL]` | 68 |
| | **total** | **126** |

---

## 1. Tier I — exact mathematics, closed

All twenty entries are computable with no physical input whatsoever. **Every one
of them is a known result.** The corpus derives them; it does not originate
them. Listed with the theorem each already is.

### 1.1 The order/combinatorics cluster (B22, B30, B29)

| claim | check | known equivalent |
|---|---|---|
| `N` and `p` need not be prime; the prime-scale role fails | 39 | **ℤ/nℤ is cyclic with generator 1 for every n** (Dummit & Foote, *Abstract Algebra*). "Cyclic for all n" makes "only for prime n" false by one line. |
| blocks of 3; axes exchange; closes into whole triples only at 18 | 46 | **coset structure of ℤ/3ℤ** plus the arithmetic fact 3 ∣ 18. The "axis exchange" is a coordinate rotation — an element of the symmetry group acting on the labelling, not a new mechanism. |
| a period-3 return is a *legal* model of Axioms F/G | 45 | **ℤ₃ as a model**; existential axioms are witnessed by the cyclic group. Textbook model theory. |

### 1.2 The topology-vs-geometry cluster (B20–B24, B33, B34)

This is the strongest cluster in the corpus, and it is **standard topology**.

| claim | check | known equivalent |
|---|---|---|
| rotational closure is topological; `Π = π` is **not** forced | 38 | **H₁(S¹) = ℤ** — the winding number is the integral of a closed 1-form, computable without any metric. Recovering `π` requires arc length, i.e. an *additional* structure. Textbook: Bott & Tu, *Differential Forms in Algebraic Topology*, ch. 4. |
| the axioms are satisfied by a 2-parameter family `rₙ = c·qⁿ` | 37 | **Model-theoretic independence / non-completeness.** An axiom system admitting a free-parameter family of models is not categorical. Standard logic. |
| the zero-network does not determine geometry | 40 | **An abstract graph carries no metric.** Many embeddings of one graph; graph-reconstruction counterexamples are classical. |
| Axioms E and G are **vacuous as written**; E′, G′ refuted by the successor map | 41 | **Vacuity of an existentially quantified axiom** (witness: the identity, the constant map). E′/G′ fail because `n ↦ n+1` has no fixed point and no finite period — the standard countermodel. This is the best piece of formal work in the corpus and it is *routine* model theory. |
| reals are values **attached to** zeros, not points between them | 48 | **Cardinality.** ∣ℤ₊∣ = ℵ₀ < 2^ℵ₀ = ∣ℝ∣ (Cantor, 1891). A countable index cannot generate an uncountable set — it can only *label* one, once a labelling map is supplied. The corpus's own conclusion, and it is Cantor's theorem. |
| gaps are topological, not geometric | 48 | **Order type.** ℚ has order type ℚ and its placement in ℝ is extra data. The Cantor set is the standard counterexample to "position is determined by order". |

### 1.3 The kinematic cluster (B31, B32) — a known puzzle, correctly solved

| claim | check | known equivalent |
|---|---|---|
| a circle of radius `r` rolling externally round a fixed circle of radius `R` turns `R/r + 1` times; **π is not an independent input** | 47 | **The coin-rotation problem**, posed by Poisson (1837). Standard result: external `(R+r)/r = R/r + 1`; internal `(R−r)/r = R/r − 1`. The famous case is a coin round an identical coin: **2**, not 1. |
| the same count as a **winding number** of the tangent frame | 47 | **Degree of the Gauss map**; in the language of fibre bundles, the **first Stiefel–Whitney number**. This is *the* classical case where a topological invariant answers a kinematic question. |
| the blocks of three shrink; exact closed form `1/√(1+q²)` | 47 | **The geometric series**: `Σ_{k≥0}(−q²)^k = 1/(1+q²)`, then a square root. Textbook. |

**Honest note on the `+1`.** The corpus registers this as a discovery. It is
not. It is a 190-year-old puzzle, and the `+1` is precisely the part that
puzzles people — the rolling circle picks up one extra rotation because its own
frame returns to itself after the contact arc is exhausted. The corpus got it
right, and got right *why* `π` drops out (both circumference and contact arc
carry a factor π, so only the ratio survives). Citing Poisson costs the corpus
nothing and protects it from an avoidable priority dispute.

### 1.4 The boundary cluster (B36, B37, B38)

| claim | check | known equivalent |
|---|---|---|
| `0` is excluded from `s(𝒵)`; limit only under `q < 1` | 50 | **An open set contains no boundary point.** `∂(0,∞) = {0, ∞}`. Textbook general topology. |
| the excluded boundary is a **pair**, `{0, ∞}` | 51 | Same. The correction B36 → B37 is the correction of a half-truth, and the corrected statement is the definition of boundary of an open interval. |
| the ladder is decade-native: 14/18 rungs within ¼ decade of `10ⁿ` | 51 | **A logarithmic grid.** The empirical part (14/18) is corpus measurement; the structural part is the standard observation that a quantity spanning 61 decades is *naturally* read in decades. |
| `0.999… = 1`; `Σ_{k≥1}10^{-k} = 1/9`; tail after `n` terms exactly `10^{-n}/9` | 51 | **The geometric series** `Σq^k = 1/(1−q)`, evaluated at `q = 1/10`. |
| terms vanish, remainder vanishes, total `1/(1−q) > 1` | 51 | **Monotone Convergence Theorem** (Levi). Because the terms are non-negative, the interchange `Σ lim = lim Σ` is *legitimately* available — so this is a **theorem, not a paradox**, and the corpus should say so. |

**A precision the corpus should adopt.** "The parts vanish but the total does
not" is sometimes heard as a failure of limits. It is not. For a positive-term
series MCT *guarantees* the limit/sum interchange, and the content is the
mundane, standard statement that **a countable union of negligible sets need
not be negligible** — the measure-theoretic version being that in a non-atomic
space every countable set has measure zero while the whole space does not. That
is the honest equivalent. It is a smaller claim than "a paradox", and a true one.

### 1.5 The structure cluster (B19, L05–L11)

| claim | check | known equivalent |
|---|---|---|
| cone/scale/closure kernel; `n(u) < 1 ⇒ 0` | 36 | **A valuation / degree function.** `n(u) = ⌊log u⌋` is exactly the standard *order function* of Gröbner-basis theory, and the "collapse to 0 below the top grade" is what a floor does. The object is a **sharp monoid** with a ℤ-grading. |
| Cayley–Dickson doubling `1,2,4,8`; `Cl(0,8)`; Bott period 8 | 19 | **Cayley–Dickson construction**; **Hurwitz (1901)**: the alternative normed composition algebras are exactly ℝ, ℂ, ℍ — so the sequence stops at 4, which is a *theorem about why it stops*. **Bott periodicity** with `w₂(C) = 1` gives period 8. The register already marks this `[ESTABLISHED]-theorem` (E12). |
| `i` has period 4 = the `π/2` turn | 20 | `i⁴ = 1`. Elementary. |
| `n²+n+41` prime for `n = 0..39`, fails at `n = 40` | 21 | **Euler's polynomial**; the failure is `1681 = 41²`, and 41 is a **Rabinowitsch/Heegner** number (class number one). Register already marks `[ESTABLISHED]-theorem` (E12). |
| the prime turn-walk is an **open** spiral, `r² = (ΣE−W)² + (ΣN−S)²` | — | Arithmetic: net displacement of a walk with per-step drift. `r²` is a squared net-displacement identity. No theorem is claimed and none is needed. |
| the filled light-cone is the observable **3-ball**, radius = particle horizon | 27 | **The causal past of a spacetime event in 3+1 Minkowski space is a 3-ball.** Standard (Hawking & Ellis; Wald §2). Register already marks `[ESTABLISHED]-external` (E15). |
| spatial physics caps at 3(+1) | — | **Empirical, not a theorem.** No no-go theorem forbids `d > 4`; what exists are specific difficulties (4D Yang–Mills confinement). The register correctly says `[PROVEN] empirical cap`. Keep it a cap. |
| the zero-to-horizon window is recursive | 17–18 | **Definitional.** It is the *reading* procedure applied at each scale (L12/L03), not a physical law. The corpus's own `X21` already says exactly this. |

### 1.6 The number-theory cluster (N01–N06) — all textbook, all honestly labelled

| claim | check | known equivalent |
|---|---|---|
| `π(10⁷) = 664,579`; `n/ln n` 6.6% off | 22 | **Prime Number Theorem.** The 6.6% gap is the expected `ln ln x` correction. |
| twins `< 10⁷` = 58,980 exact; Hardy–Littlewood 50,822 | 23 | **Hardy–Littlewood prime-tuples heuristic.** Verified exact: the twin count is right. **The "14% off" needs its denominator stated** — 13.8% relative to the *observation*, **16.1% relative to the *prediction***. The second is the honest figure for how far the heuristic sits from the data. A 16% deviation at `x = 10⁷` is entirely unremarkable for an asymptotic heuristic, and the register's `[PROVEN]-exact; formula [CONJECTURE]` split is correct. |
| composite majority `S(n) = C − π ≥ 0` for `n ≥ 9` | 24 | Elementary, and the first strict majority is a finite check. Honest. |
| unbounded prime-free runs, witness `201!+2 … 201!+201` | 25 | **Euclid's factorial construction.** Classical. |
| 7,714,287 of `n ≤ 10⁷` divisible by 2,3,5,7 (2,285,713 coprime to 210) | 26 | **Inclusion–exclusion / the wheel sieve.** Density estimate `10⁷·(1−½)(1−⅓)(1−⅕)(1−⅐) = 7,714,285.7`; exact count **7,714,287** — agrees to 6 significant figures but is **not** the floor, because `10⁷ = 47619·210 + 10` leaves a partial period contributing a boundary term of **+2**. Re-verified here by two independent methods (periodic count and brute force). Textbook. |
| `π(10⁶) = 78,498`; `p₅₀₀₀₀₀ = 7,368,787`; max gap 154 ≤ `(ln 10⁷)² = 260` | linkage B1 | **Cramér's conjecture** for the `O(√x)` gap bound — correctly marked `[CONJECTURE]`, and the inequality is the right *shape* of the claim. `π(10⁶)` and `p₅₀₀₀₀₀` verified exact by sieve. The max gap 154 **is** the correct `10⁷` record (at `p = 4,652,353`). **But this row mixes ranges — see §5.3.** |

---

## 2. Tier II — sourced empirical, arithmetic gated

Every input here carries a citation. Every one of these is a **textbook formula
correctly instantiated**.

| claim | check | known equivalent |
|---|---|---|
| `M = 9.583e-17 kg` from `ρ` and `R` | 1 | `ρ·(4/3)πR³`. Arithmetic. |
| `E* = 66.667 MPa` (rigid pair) | 2–3 | **Hertzian reduced modulus** `E* = E/(1−ν²)`. Hertz (1882). |
| Hertz `d_max = 5.807 nm @ 20.63 nN` | 4–5 | **Hertz contact theory**, textbook. |
| compliant-plane `d = 7.662 nm @ 15.63 nN` | 6–7 | **JKR theory** — Johnson, Kendall & Roberts (1971), `a ∝ P^{1/3}`. |
| thermal speed `√(3kT/m) = 11.4 mm/s` | 8 | **Equipartition.** One degree of freedom. Textbook. |
| Mie `Q_e = Q_s = 3.4822` at `x = π` | 9–11 | **Mie scattering** (Bohren & Huffman). The `Q_e = Q_s` equality is **energy conservation**, so it is a check on the code, not a discovery. |
| FDT fixed point `n = 0.4`; trap contraction 0.22 nm | 12–14, probe | **Fluctuation–Dissipation Theorem** (Kubo 1966). |
| JKR adhesion ≫ `kT`; radiation-pressure cap `P/c` | probe | Standard scaling; `F ≤ P/c` is momentum-flux bookkeeping. |
| ZPE vs `kT` vs relativistic KE ratios | 14–16 | **Quantum harmonic oscillator** ZPE `½ħω`; equipartition. |
| **pulsar triad from two timed observables** | 43 | `τ = P/(2Ṗ)`; `B = 3.2e19√(PṖ)` G; `Ė = 4π²IṖ/P³`. All standard — Hobbs et al. (2015), *Living Rev. Relativ.* **18**, 21. Reproduced to 0.10%, 1.2%, 1.0%. |
| **quasar anchor is Eddington, linear in `M`** | 44 | `L_Edd = 4πGMm_p c/σ_T` — strictly linear in `M`, hence `L/L_Edd ∝ 1/M`. The BLR radius from Kaspi et al. (2000), *ApJ* **535**, 62, with `R ∝ L^0.70`. |
| 16 → 18 sourced rungs; CV **rises** 0.959 → 0.970 | 30–31, 42 | Honest strengthening: adding two non-cherry-picked canonical rungs made the *irregularity* claim stronger. This is the correct scientific move and it is rare in this literature. |

**The one caveat that matters here.** The pulsar and quasar entries are the
corpus's most impressive *empirical* work, and they are also the place where the
`X32` caveat bites hardest: the spin-down relations are **known relations**, so
reproducing them from `P` and `Ṗ` demonstrates that the framework's *metric-free*
side and the *metric-dependent* side meet cleanly on a real object. It does
**not** show the framework *explains* pulsars. `X32` already says this, and the
compilation confirms the register is right to say it.

---

## 3. Tier III — negative results

These are the corpus's **strongest and most genuinely its own** results. A
refutation with a named witness is hard to steal and hard to mistake for
textbook — because the *witness* is new even when the *method* is standard.

| refutation | check | the equivalent that already exists | what is new |
|---|---|---|---|
| balanced geometry not forced by the zero relation | 37 | independence (standard) | the specific 2-parameter model family `c·qⁿ` |
| `Π ≠ π` without a measure | 38 | `H₁(S¹) = ℤ` (standard) | the explicit proof that the reserved invariant is not π |
| prime structure not forced | 39 | ℤ/nℤ cyclic (standard) | tying it to the *specific* prime-scale role in the ladder |
| the network does not fix geometry | 40 | graphs carry no metric (standard) | applying it to the zero-ladder |
| **Axioms E and G are vacuous as written** | 41 | non-vacuity (standard) | the audit of *this* axiom set, and the corrected E′/G′ |
| **the scale axiom does not describe this corpus's own ladder** — 0/15 gaps match `log₁₀(1/p)` | 42 | falsification (Popper) | the negative result on the framework's own flagship hypothesis |
| **"energies are comparable" — FALSE, ~37 orders** | corr. 1 | dimensional analysis | the retraction, logged not deleted |
| **"size = 0 at all scales" — FALSE** | corr. 70 | the point-like limit | the retraction |
| rungs 4,5,6 do **not** close a triangle | 45 | — | a specific failed instantiation, all three coordinates |
| the blocks of three do **not** return to zero | 46 | — | the specific walk |
| **X35 retracted** — "no step law delivers zero" was false; `q = 1` returns at `k ≡ 0 mod 4` | 49 | — | **the retraction itself**, with the exact closed form |
| "all reals are between all zeros" | 48 | countability (Cantor) | the three-way split into three claims |
| "0 and the reals encapsulate each other" | 50 | boundary of an open set | containment refuted *as arithmetic* |
| "all tenth powers zero ⇒ everything zero" | 51 | geometric series + MCT | naming the inference as a named fallacy |

**On X35 — the corpus's most valuable single act.** Registering a claim, testing
it, finding it **false**, and *publicly retracting it with the corrected
classification attached* is the behaviour the entire rest of the literature
should be copied on. The retraction is also the one result here with no
textbook equivalent at all, because textbooks do not usually contain a
self-correction.

---

## 4. The novelty ledger — honest accounting

| category | n | what may be claimed |
|---|---|---|
| exact mathematics that is **standard** | 20 | *derivation and application.* **No priority claim is available on any of these.** |
| empirical instantiation of standard formulas | 24 | *correct instantiation with sourced inputs.* No priority claim. |
| negative results by standard methods | 11 | *the witness and the specific instantiation.* Weak but real priority on the witness. |
| **errors this compilation found and logged** | 2 (X39, X40) | **genuinely the corpus's own** — see §5 |
| self-correction / retraction discipline | 1 (X35) | **genuinely the corpus's own** |
| governance, reproducibility, no-experiment honesty | 9 (G) | **genuinely the corpus's own** |
| specification of a coherent, exactly-solvable model | 1 | *the specification is the contribution* — see below |
| excluded (conjecture / open / framing / postulate) | 68 | **nothing** |

### 4.1 The one defensible mathematical contribution

Not a theorem. **A specification.** The corpus has built a model that is
simultaneously:

- **exactly solvable** (all 18 scale values, all block positions, the `q = 1`
  classification — closed forms, no numerics), and
- **falsifiable**, and it has already falsified one of its own hypotheses (0/15
  prime-gap matches) and one of its own published claims (X35).

A framework that is exactly solvable, that makes a sharp prediction, and whose
sharpest prediction **failed against its own data** — and which recorded the
failure — is worth more than a framework that agrees with everything. That
verdict is the corpus's own, and it is the correct one.

### 4.2 What must never be claimed

- That the `R/r + 1` rolling count, Hurwitz's four algebras, Bott periodicity,
  Cantor's uncountability, `H₁(S¹) = ℤ`, Monotone Convergence, the PNT, JKR,
  Hertz, Mie, Kubo, Eddington luminosity, or pulsar spin-down are new. **They
  are not.** They are *correctly used*, which is a different and sufficient
  virtue.
- That the ladder "explains" pulsars or quasars. **X32 forbids it** and the
  compilation confirms the prohibition.
- That any of the 68 excluded claims is established. They are not, and gate **A**
  of the admission rule is why.

---

## 5. Two findings from compiling this

### 5.1 B35's strength is overstated

B35 registers mutual determination between the zeros and the reals via `s`, on
the grounds that the 18 scale values are distinct so `Aut(s)` is trivial. Both
statements are **true**. Neither carries the weight the register places on them:

- For a **finite** set, *any* bijection determines both sides. Eighteen distinct
  labels give a trivial automorphism group for the uninteresting reason that a
  discrete set with no structure has no automorphisms to speak of. The
  implication "`fix the reals` ⇒ `fix which zero is which`" is therefore **true
  but vacuous** at 18 rungs.
- The same is true of the elegant `300 random relabellings` check: for a set
  with all-distinct labels, preserving `s` forces the identity *by construction*.
  The experiment cannot fail, so it confirms nothing.

**What would make it non-trivial:** an **infinite** index set, plus a structural
requirement beyond distinctness — for instance that `s` be *monotone*, or
commute with a shift, or extend to a self-map of the ladder. Then "the reals
determine the zeros" becomes a rigidity theorem with content. As registered, it
is a correct observation about cardinality wearing the clothes of a result.
**Recommend: restate B35 as a cardinality observation, and open a new claim for
the monotone/shift-commuting version.**

### 5.2 A phantom claim in the working context

The context summary carried into this session asserted a "rung↔neutral-axis
mapping" attributed to B26, with "7 of 18 rungs matching." **No such claim
exists.** `B26` is the addition of two sourced rungs (neutron star, quasar BLR)
and the finding that adding them *strengthened* the irregularity claim
(CV 0.959 → 0.970). "Neutral axis" appears in the corpus only as *neutral density
filter* in two experimental-procedure lines.

The claim is not merely unregistered — it is **unsupported**, and it would have
been the corpus's most novel-looking empirical result. It is recorded here as
`X39`: **RESOLVED NEGATIVE — there is no neutral-axis correspondence in this
corpus; the assertion was a context error and is not claimed.** It is logged so
that if it resurfaces it is recognised as an error rather than re-derived.

### 5.3 A real arithmetic error: N06 mixes two ranges

`N06` is the one row in the number-theory block that **does not survive
re-verification**, and the error is a range mix rather than a wrong method.
Every number in it was recomputed from a fresh sieve of `n ≤ 10⁷`:

| quantity | register | measured | verdict |
|---|---|---|---|
| `π(10⁶)` | 78,498 | 78,498 | **correct** |
| `p₅₀₀₀₀₀` | 7,368,787 | 7,368,787 | **correct** |
| max gap, `p < 10⁶` | *(not stated)* | **114** at `p = 492,113` | — |
| max gap, `p < 10⁷` | 154 | **154** at `p = 4,652,353` | **correct — for `10⁷`** |
| Cramér bound `(ln 10⁷)²` | 260 | 259.8 | **correct — for `10⁷`** |
| **mean gap** | **13.02** | **12.74** (`p<10⁶`) / **15.05** (`p<10⁷`) | **WRONG under either reading** |
| **"≈ ln 13.12"** | 13.12 | `ln 10⁶ = 13.82`, `ln 10⁷ = 16.12` | **WRONG** |

Two distinct faults:

1. **The mean gap 13.02 matches nothing.** The defensible value for `p < 10⁶` is
   **12.74**; for `p < 10⁷` it is **15.05**. Scanning every natural window, the
   closest is **13.06** over complete gaps with left endpoint in `[10⁵, 10⁶)` —
   so 13.02 is not a rounding of any standard choice. The quoted figure is
   unattributable.
2. **The logarithm is the wrong one.** `13.12 = ln(5×10⁵)` — the **midpoint** of
   the interval, not `ln(10⁶) = 13.82`. Comparing a mean gap against the log of
   the *midpoint* rather than the endpoint is not a standard convention, and it
   is the comparison that makes "mean gap ≈ ln" look like a PNT confirmation.
   Measured properly, `12.74` vs `ln 10⁶ = 13.82` is a **7.8% shortfall**, not
   an agreement.

The row also quotes `π(10⁶)` and `p₅₀₀₀₀₀` (both `10⁶`-scale) beside a max gap
of 154 and a Cramér bound of 260 (both `10⁷`-scale), so a reader cannot tell
which range the mean gap belongs to. **Recommend: restate N06 as two rows,
`10⁶` and `10⁷`, with the mean gap computed as `(p_last − 2)/(π − 1)`, and drop
the `≈ ln` phrasing entirely** — the correct statement is the PNT's
`g(x) ~ ln x`, an *asymptotic*, not an identity to be checked at one cutoff.
Logged as `X40`.

**Why this is recorded rather than quietly patched.** It is the first error this
compilation has found in an `[PROVEN]` row, and it is exactly the error class the
corpus warns about elsewhere: an asymptotic used as a pointwise identity, which
is the same shape as the vacuum-catastrophe fallacy the register already files
under `P02`. The corpus's own rule — retract, log, re-verify — applies here too,
and it applies to `[PROVEN]` rows with the same force as to published claims.

---

## 6. What is excluded, and why

68 claims fail gate **A** and are excluded from the synthesis:

- **`[CONJECTURE]` (10)** — Cramér, octonion/E8 unification, DM identity, the
  entropic-gravity extension layer. Named conjectures, correctly labelled.
- **`[OPEN]` (13)** — vacuum catastrophe, bulk-flow anomaly, DM non-detection,
  inflation/baryogenesis origin, the start, hard problem of consciousness.
  Genuine open problems of physics, correctly labelled.
- **`[FRAMING]` (7)** — "size = 0 at all scales" as a *shape* claim; "the law is
  a solution"; "the edges are the same as the center"; the closure cycle.
  Interpretive, not computable. **This is not a criticism** — a framework needs a
  layer that says what it *means*. It is simply not evidence, and gate **A**
  keeps it out of the synthesis.
- **`[POSTULATE]` (4)** — P2 centre grows, P5 primal tornado, P3 ascent push,
  L4 handedness. Assumptions. The register is explicit that P5's spin-bias
  signature is **not established**.
- **`[REAL]` / naming only (3)** — the Local Group bound behind F04/L3. The
  *observation* is real; the *lock condition* built on it is a postulate.
- **Cosmology desk-reference (A, E series, 32)** — Hubble tension, prime-gap
  records, horizon topology. Real external facts, but they are **inputs and
  context, not results of this framework**. The register already says so.

**The exclusions are the healthiest part of the register.** 68 of 126 numbered
claims are honestly marked as not-established, and 38 further claims are
recorded as NOT-claims — a corpus that had *no* `[OPEN]` or `[FRAMING]` entries
would be far less trustworthy, not more.

---

## 7. One-line verdict

> **Every result in this corpus that is mathematically *closed* is a known
> result; every result that is *genuinely its own* is a negative one.** The
> framework's value lies not in its theorems — which are standard — but in
> (a) an exactly-solvable specification that is falsifiable and has already
> failed one of its own predictions, (b) a retraction discipline that has
> already corrected one published claim and, in this compilation, **two more
> register rows**, and (c) a governance record in which 68 of 126 claims are
> honestly marked as not established.

The mathematics is the scaffolding. The honesty is the contribution. The
compilation exists so that the scaffolding is never mistaken for more — and so
that when a `[PROVEN]` row turns out to be wrong, as `N06` did, the same
machinery that retracted `X35` catches it.

---

## Appendix — what was re-verified, and how

Nothing in §1–§2 was taken on trust from the register. The following were
recomputed independently while writing this document:

| quantity | method | result |
|---|---|---|
| `π(10⁷)` | Eratosthenes sieve to `10⁷` | 664,579 — **matches** |
| `π(10⁶)`, `p₅₀₀₀₀₀` | same sieve | 78,498 / 7,368,787 — **match** |
| twins `< 10⁷` | same sieve | 58,980 — **matches** |
| Hardy–Littlewood prediction | `2C₂x/ln²x`, `C₂ = 0.66016…` | 50,822 — **matches** |
| n ≤ 10⁷ divisible by 2,3,5,7 | periodic count over `mod 210` **and** brute force | 7,714,287 both ways — **matches** |
| `n/ln n` at `10⁷` | — | 620,421, **6.64%** low — register's 6.6% **matches** |
| mean prime gap, `p<10⁶` | sieve | **12.74** — register's 13.02 **does not match** |
| mean prime gap, `p<10⁷` | sieve | **15.05** — register's 13.02 **does not match** |
| max gap, `p<10⁶` / `p<10⁷` | sieve | **114** / **154** — register's 154 is the `10⁷` value |
| ball mass `M` | `ρ·(4/3)πR³` with module constants `ρ=1100`, `R=275 nm` | 9.5825e-17 kg — register's 9.583e-17 **matches** |
| ball-energy ratios (B09–B11) | **not re-verified** — the check's own `T` and `v` were not traced, so the register's figures are reported here as-is and unendorsed | — |

**Method note.** `B01` was nearly logged as a 1000× error on the strength of a
guessed density and radius; tracing the module's actual constants showed the
register correct. That is the second time in this corpus's history that a
plausible-looking error dissolved on inspection (the first was check 51's
`q = 0.9` horizon). The lesson generalises and is worth stating plainly:
**a compilation that re-derives is worth more than one that reads.** The one
genuine error it did find, `N06`, was found by recomputation and not by reading.
