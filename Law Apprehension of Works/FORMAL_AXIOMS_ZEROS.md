# Formal Axioms: Zeros, Interconnection, Scale, Closure, Invariant

Minimal first-order skeleton of the framework "Zeros, Interconnection, Scale,
and Geometry" (MGS Puno, conceptual development with ChatGPT), plus the two
independence questions the framework states as its own central open problem
(Part X/XVI). Registered in CLAIM_REGISTER.md as F21 (framing) with real
anchors L12, A13, E05/E14; the arithmetic kernel is B19 (checks 36-38).

**Status:** [FRAMING] skeleton. The symbols below are *formal primitives of
this framework*, not physical entities. Nothing here establishes physics.
The two marked questions (Q27, Q28) are the framework's own open problems,
now sharpened and gated — not solved by fiat.

---

## 1. Primitives and sorts

- $\mathcal{Z} = \{Z_0, Z_1, \dots\}$ — reference states ("zeros").
- $\mathcal{R} \subseteq \mathcal{Z} \times \mathcal{Z}$ — binary relations
  (connections), written $Z_i \xrightarrow{R_{ij}} Z_j$.
- $F: \mathcal{Z} \to \mathcal{Z}$ — a transformation (a relation chosen as a
  function; composition is then available).
- $s: \mathcal{Z} \to \mathbb{R}_{>0}$ — a scale *assignment* (not a
  coordinate; scale exists only relative to a chosen relation).
- $q \in \mathbb{R}_{>0}$ — a scale factor; $s_{n+1} = q s_n$ on an orbit.
- $\Pi$ — a symbol reserved for an invariant. **No numerical value is
  assigned to $\Pi$ by this skeleton.**

No metric, no norm, no inner product, no time functional is among the
primitives. That absence is deliberate and is the reason Q27 and Q28 have the
answers they do.

---

## 2. Axioms A–G (the minimal set)

**A — Reference.** $\exists Z \in \mathcal{Z}$.

**B — Relation.** $R(Z_i, Z_j)$ exists between distinguishable references.

**C — Transformation.** $F: Z_i \mapsto Z_j$; relations may be ordered as
functions.

**D — Composition.** If $F_{AB}$ and $F_{BC}$ exist then $F_{BC} \circ F_{AB}$
exists on the shared node $Z_B$. (Paths follow; cycles become expressible.)

**E — Scale.** A transformation may carry a scale factor: $s_{n+1} = q s_n$.

**F — Closure.** Some $F$ have finite period: $\exists N>0:\ F^N(Z) = Z$; the
fundamental period is $N_\min = \min\{k>0 : F^k(Z) = Z\}$.

**G — Invariance.** Some property is preserved: $\exists T, X:\ T(X) = X$.

Everything else in the framework is *derived* from A–G plus stated conditions,
or it is a hypothesis (Part XIII of the source document).

---

## 3. Q27 — Does the zero relation force balanced geometry? [RESOLVED: NO, not without an extra condition]

The framework asks whether $\Delta r = \Delta z$ follows from A–G. It does not.

**Claim (independence).** For every $c \in \mathbb{R}_{>0}$, the model
$M_c = (r_n, z_n)_{n\ge 0}$ with $r_n = c\, q^n$, $z_n = q^n$ satisfies A–G
(with $F$ the shift $n \mapsto n+1$, scale $q$) and the self-similarity
condition $r_{n+1}/z_{n+1} = r_n/z_n = c$. Therefore $c$ is a free parameter
of the minimal skeleton, and the cone half-angle $\theta = \arctan c$ ranges
over all of $(0, \pi/2)$.

**Gated:** check 36 asserts $\arctan 2 \ne \pi/4$ while the $c=1$ case gives
$\tan(\pi/4)=1$; check 37 asserts the $c=2$ family is self-similar
($\arctan c = 1.1071$ rad) and records the family as a counterexample to
"self-similarity $\Rightarrow \pi/4$".

**What would close it.** An *extra* condition beyond A–G. The minimal one
found here: **isotropy of the elementary relation** — if the relation does not
prefer the axial direction over the radial one, then by symmetry the step
components are equal, $\Delta r = \Delta z$, hence $c=1$ and $\theta = \pi/4$.
Isotropy is an assumption, not a consequence; it is exactly the content of the
framework's Part X question. So:

$$\text{A--G} \;\nRightarrow\; c = 1, \qquad
\text{A--G} + \text{isotropy} \;\Rightarrow\; c = 1.$$

This is registered as **X27** (NOT-claim: "balanced geometry is forced by the
minimal axioms"). The framework's own refusal (Prop 10) is *correct and now
gated*, not merely asserted.

---

## 4. Q28 — Is $\Pi = \pi$? [RESOLVED: NO, not without a measure]

**Claim (topological vs. metric).** Rotational closure is the group
statement $R_{2\pi k} = I$ for $k \in \mathbb{Z}$ — an invariance of the
*orientation class* of a closed orbit. It requires no metric: winding number
$k$ is a homotopy invariant, and $R_{2\pi k} = I$ holds identically. This
establishes $T(\Pi) = \Pi$ in the group-theoretic sense (Axiom G) with
$\Pi$ = winding class.

The *numerical* value $\pi$ appears only when a measure is induced: arc length
$s = \rho\,\Delta\phi$, so a full turn is $2\pi\rho$, and the constant $\pi$ is
the ratio of circumference to diameter in that measure. No such measure is
among A–G.

**Gated:** check 38 asserts $R_{2\pi k} = (1, 0)$ for $k = 1, 2$ to machine
precision with no metric anywhere in the computation, and records that
assigning a number requires arc/diameter.

$$\text{A--G} \;\Rightarrow\; T(\Pi) = \Pi \;\text{ (topological)}, \qquad
\text{value}(\Pi) = \pi \;\Rightarrow\; \text{metric} \;(\text{not in A--G}).$$

This is registered as **X28** (NOT-claim: "$\Pi = \pi$"). The framework's own
Prop 17 is correct and now gated.

---

## 5. What is derived, what is still hypothesis

| Statement | Verdict | Anchor |
|---|---|---|
| A–G are satisfiable; $c$ free in $(0,\infty)$; $\theta = \arctan c$ | [ESTABLISHED] | check 36/37, B19 |
| Scaling alone never forces $\pi/4$ | [ESTABLISHED] (negation of X27) | check 36/37, B20 |
| Isotropy would force $\Delta r = \Delta z$ | [ESTABLISHED] as conditional | check 37 |
| Rotational closure = $R_{2\pi k}=I$, metric-free | [ESTABLISHED] | check 38, B21 |
| $\Pi = \pi$ | **[RESOLVED NEGATIVE]** — not a consequence of A–G (X28) | check 38, B21 |
| primes give discrete hierarchies $q = 1/p$ | [ESTABLISHED] arithmetic | check 36 |
| primes as "structural generator" (Part IX role 3) | **[RESOLVED NEGATIVE]** — nothing forces prime periods or prime scales; closure itself is optional (X29) | check 39, B22 |
| the relations fix the geometry | **[RESOLVED NEGATIVE]** — one network, continuum many geometries (X30) | check 40, B23 |
| space = interconnection of zeros; time = ordered transformations | [FRAMING] hypothesis | F21 (anchors L12, A13, E05) |
| time is an ordering of transformations | [FRAMING] — ordering alone does not give a metric on the order | F21 |

---

## 6. The one-line answer to the framework's central question (Part XVI)

> $F \stackrel{?}{\Rightarrow} (N, q, \theta, p, \Pi)$ — **no, under A–G nothing in
> the tuple is determined.** Axioms F and E *permit* a period $N$ and a scale
> $q$, but permit any value; Axiom G gives a topological $\Pi$; and $\theta$
> and $p$ are free parameters unless isotropy and a prime scale rule are added
> as extra assumptions. The framework's research program is therefore
> correctly identified as genuinely open — and now every specific gap is
> named, formalized, and gated (below).

**Adjacency rule (enforced):** no sentence above may be cited as physics.
The claimable core is B19–B23 + checks 36–40; the rest is framing.

---

## 7. The remaining symbols, closed (checks 39-40; B22, B23)

Part XVI lists five symbols. $\theta$ and $\Pi$ were settled in §3–§4; the
other three are settled here.

### 7.1 $N$ and $p$ need not be prime (B22, check 39)

Axiom F says *some* $F$ have finite period. It does not restrict the period.
The cyclic shift $\sigma_m(x) = (x+1) \bmod m$ on $\mathbb{Z}/m\mathbb{Z}$ has
**fundamental period exactly $m$ for every $m$** — prime or composite. Gated
witnesses: $m = 4, 6, 8, 9, 10, 12$ all give period $m$.

Axiom E likewise permits any $q > 0$; the composite contractive scales
$q = 1/4,\; 1/6,\; 1/9,\; 1/15$ are legal ($q^{50} < 10^{-30}$ for $q = 1/4$,
$< 10^{-58}$ for $q = 1/15$).

Closure is even **optional**: the successor $S(n) = n+1$ has no finite period
— no $N > 0$ with $S^N(0) = 0$ (the framework's own Prop 5, now gated).

$$\text{A--G} \;\nRightarrow\; N \text{ prime}, \qquad
\text{A--G} \;\nRightarrow\; q = 1/p .$$

So all three of the framework's prime roles (Part IX: period, scale,
generator) are *choices*. The framework's own summary — "prime structure is
presently a candidate structural property, not a physical law" — is correct
and now carries a gate. Registered **X29** (resolved negative).

### 7.2 The relations do not fix the geometry (B23, check 40)

A zero-network is combinatorial: path distance on a cycle $C_n$ is
$\lfloor n/2 \rfloor$, a pure integer, metric-free. Any Euclidean embedding
instead realises distance $d$ as the chord $2\rho\sin(\pi d/n)$, where $\rho$
is a **free positive parameter**.

Witness: $C_8$ is the *same graph* at $\rho = 1$ and $\rho = 2$ — neighbour
chord $0.765$ vs $1.531$, opposite chord $2.000$ vs $4.000$ — while path
distance stays $1$ and $4$ respectively. One relational structure, continuum
many geometries.

$$\text{relations} \;\nRightarrow\; \text{metric}, \qquad
\pi \text{ enters only at the embedding } 2\rho\sin(\pi d/n).$$

This is the same gauge lesson the corpus already holds for *positions*
(A13, L12) extended to *measurement itself*: the relations are the invariant
content, the geometry is a gauge choice. Registered **X30** (resolved
negative).

### 7.3 Status of Part XVI after this round

| Symbol | Forced by A–G? | Why |
|---|---|---|
| $N$ | **no** | any $m$ is a period of some $F$ (check 39) |
| $q$ | **no** | any $q > 0$; prime-reciprocals are a choice (check 39) |
| $\theta$ | **no** | $c \in (0,\infty)$ free; $\theta = \arctan c$ (check 37) |
| $p$ | **no** | nothing privileges primes (check 39) |
| $\Pi$ | only topologically | $R_{2\pi k} = I$; the *number* $\pi$ needs a measure (check 38) |

The framework's central question is therefore answered in the strongest
available way: **the minimal axiomatisation is honest, and every one of its
open consequences has been shown to be a genuine extra assumption rather
than a derivation in disguise.** That is the real result of this thread, and
it is the answer the framework itself asked for.

---

## 8. Axiom audit: how strong is A–G really? (check 41; B24)

Before using a skeleton to settle anything, it has to be asked whether the
skeleton *can* settle anything. Applied literally, A–G are weaker than the
framework intends.

| Axiom | As written | Content? | Why |
|---|---|---|---|
| A — Reference | $\exists Z$ | scaffolding | without it every other axiom is vacuously true |
| B — Relation | $R(Z_i,Z_j)$ exists | scaffolding | without it C, D, F, G cannot be stated |
| C — Transformation | $F: Z_i \mapsto Z_j$ | scaffolding | without it D has nothing to compose |
| D — Composition | $F_{BC}\circ F_{AB}$ exists | **yes** | a single-transformation system has no composable pair, so D is unsatisfiable while A, B, C, E, F, G all hold |
| E — Scale | a transformation *may* carry $s_{n+1} = qs_n$ | **none** | permissive: the constant scale $q = 1$ is always a witness |
| F — Closure | $\exists N>0: F^N(Z) = Z$ | **yes** | the successor $S(n) = n+1$ has no finite period, so F is independent of the rest |
| G — Invariance | $\exists T, X: T(X) = X$ | **none** | the identity $T = \mathrm{id}$ is always a witness |

So of seven axioms, **two (D, F) carry model-theoretic content, three are
scaffolding, and two are vacuous as stated.**

The fix is to state the intended, strengthened forms:

$$\text{E}' : \exists\, q \neq 1, \qquad \text{G}' : \exists\, T \neq \mathrm{id},\ X:\ T(X) = X .$$

Both are independent, and both are witnessed apart by the same model: the
successor map has no finite period (refutes F) **and** no fixed point under
any non-identity power (refutes G′). The constant-scale system satisfies E
but refutes E′.

**Consequence for the whole thread:** every independence result in §3, §4 and
§7 was proved against the *literal* A–G, so it remains valid a fortiori
against the strengthened A–G ∪ {E′, G′}. The framework's conclusions are
robust to this repair — but the framework's own Axioms E and G should be
restated, since as written they assert nothing. Registered **B24**.

---

## 9. Does A–G describe *this* corpus? (check 42; B25)

The strongest test of a framework is not internal consistency but whether it
describes the data the author already has. Applied to the corpus's own
18-rung rank-degree ladder, the answer splits:

- **A–D hold.** The ladder is a chain of distinguishable references, related
  by successive rungs, and paths along it compose. The relational and
  compositional content of the skeleton fits.
- **E fails.** Consecutive scale ratios are 15 distinct values, not one
  constant $q$: gap mean $4.096$ decades, sd $3.794$, CV $0.926$,
  $\max/\min = 31.3$. A geometric family would need every gap equal to the
  mean; the largest deviation is $11.7$ decades.
- **The prime-scale role fails outright.** $0$ of the $15$ steps match a
  prime-reciprocal $\log_{10}(1/p)$ for any prime $p < 60$.

$$\text{A--D} \;\checkmark\; \text{on the corpus ladder}, \qquad
\text{E} \;\times, \qquad \text{prime scale} \;\times .$$

This is an **applicability limit, not a contradiction**: the ladder is
irregular by design (its gaps are the "prime-gap-like" spacing of
RANKS_AND_DEGREES.md), so it was never a geometric family. What the check
establishes is that the framework's scale axiom describes an *idealised*
hierarchy, not the observed one — and the observed one is the only one this
corpus actually has evidence for. Registered **X31** (resolved negative) and
**B25**.

---

## 10. What each missing piece would cost

The five non-derivations of §7 are not gaps to be filled by assertion; each
is bought by one named extra assumption. The table also records whether this
corpus already contains that assumption.

| Wanted | Bought by | Already in this corpus? |
|---|---|---|
| $\theta = \pi/4$ | isotropy $\lvert\Delta r\rvert = \lvert\Delta z\rvert$ | **no** — A13 gives frame-*independence*, which is not isotropy |
| $\mathrm{value}(\Pi) = \pi$ | an induced arc/diameter measure | **yes, externally** — A12 supplies metric + connection from GR; it must be *imported*, not derived from zeros |
| $N$ prime | restricting the model class (5 of 11 periods in 2–12) | **no**, and the corpus's own ladder is non-geometric (§9) |
| $q = 1/p$ | the same restriction, applied to scale | **no** — 0 of 15 observed steps are prime-reciprocal |
| a metric | choosing an embedding (§4, §7.2) | **yes, externally** — same import as $\Pi$ |

The pattern is consistent and worth stating plainly: **the relational layer
of the framework is self-contained; the metric layer must be imported, and
this corpus's only route to a metric is A12's pseudo-Riemannian one.** The
framework is therefore not a competitor to the corpus's geometry — it is a
*pre-geometric* layer that would have to hand off to A12 at exactly the point
where B23 and B25 show the zeros go silent.

---

## 11. Where the boundary falls: pulsars and quasars (checks 43-44; B26-B28)

§10 prices the non-derivations abstractly. Two real objects test the
boundary directly, and they land on **opposite sides** of it — which is the
sharpest available evidence that the boundary is real and not an artefact of
the formalism.

### 11.1 A pulsar is the metric-free side (B27, check 43)

PSR B1929+10 has two timed observables, $P = 0.226518$ s and
$\dot P = 1.15661\times10^{-15}$ s/s (Taylor et al. 1993). From those two
numbers alone:

| Quantity | Formula | Computed | Published | Deviation |
|---|---|---|---|---|
| characteristic age | $\tau = P/2\dot P$ | 3.103 Myr | 3.09-3.1 Myr | **0.10%** |
| surface field | $B = 3.2\times10^{19}\sqrt{P\dot P}$ | $5.18\times10^{11}$ G | $0.51\times10^{12}$ G | **1.2%** |
| spin-down luminosity | $\dot E = 4\pi^2 I \dot P/P^3$ | $3.93\times10^{33}$ erg/s | $3.89\times10^{33}$ erg/s | **1.0%** |

Now read the formulas against the axiom list. $\tau = P/2\dot P$ is pure
period arithmetic — no $c$, no $R$, no metric, no norm. It uses exactly what
Axioms **F** (a finite period) and **G** (something preserved under the
transformation) already provide: a period and its drift. This is the
framework's relational layer, and nature hands it a three-million-year clock.

$\dot E$ and $B$, by contrast, embed $I$, $R$ and $c$. They are *not* in
A-G. And the pulsar's actual radiation requires a magnetic dipole — a symbol
the skeleton does not have at all.

### 11.2 A quasar is the metric-dependent side (B28, check 44)

A quasar's luminosity is anchored by the Eddington limit

$$L_{\rm Edd} = \frac{4\pi G M m_p c}{\sigma_T} = 1.257\times10^{38}\ \left(\frac{M}{M_\odot}\right)\ \text{erg s}^{-1},$$

which reproduces the published super-Eddington ratios of the two most
luminous quasars at $z > 3.5$ to 0.36%: J0341+1720 ($M = 6.73\times10^9$
$M_\odot$, $L_{\rm bol} = 2.32\times10^{48}$) gives $\lambda_{\rm Edd} = 2.742$
against a published 2.74, and J2125-1719 ($5.45\times10^9$, $2.07\times10^{48}$)
gives 3.021 against 3.01.

The decisive feature is not the number but its *shape*: $L_{\rm Edd} \propto M$
**only** because the capture radius is $r_g = GM/c^2$. That is a
Schwarzschild-metric object — exactly the import A12 supplies and exactly what
§4 and §7.2 showed the zeros cannot generate. Halving $M$ at fixed
$L_{\rm bol}$ doubles $\lambda_{\rm Edd}$ exactly.

### 11.3 The verdict

$$\underbrace{\text{pulsar}}_{\tau = P/2\dot P\ \text{metric-free}}
\ \Big|\ 
\underbrace{\text{quasar}}_{L_{\rm Edd} \propto M \text{ via } GM/c^2}
\ \text{— the boundary, in nature, in two objects.}$$

Neither object is "explained" by A-G, and this is registered as **X32**
(resolved negative) rather than spun. What the pair establishes is sharper
than a demonstration would be: **the same framework that cannot fix its own
angle or its own π has one object in nature where its relational layer is
exactly sufficient, and one where the missing metric is not optional.** Any
future version of the framework that claims predictive reach has to say which
side of that line it is on.

---

## 12. A turn that returns to zero: the period-3 sibling (B29, X33; check 45)

§11 fixed the boundary from outside. This section tests a proposal from the
inside: *what if the turn happens at rungs 4, 5 and 6 and goes back to zero,
like a triangle?* It is worth recording in full because the honest answer
splits the idea in half — one half is a real gap in the audit, the other half
does not close.

### 12.1 The idea is legal: Axiom G is a period-3 fixed point too

"Goes back to zero" is not an addition to the framework — it *is* Axiom G,
$\exists\, T, X$ with $T(X) = X$. A triangle is the period-3 instance of that
fixed point, and it is a perfectly good model: the cyclic shift
$\sigma_3(x) = (x+1) \bmod 3$ on $\mathbb{Z}/3\mathbb{Z}$ has fundamental
period exactly $3$ and returns to $0$.

And here is the gap. Check 39 probed the period question in order to *refute
primality*, so it tested only the composite set $\{4,6,8,9,10,12\}$ — all six
reproduce with period $= m$ exactly. The prime $3$ was never in the test set,
because a check designed to show "periods need not be prime" has no reason to
include one. So the triangle was not excluded by the framework; it was simply
never enumerated (**B29**). This is a coverage gap in the audit, and closing it
disturbs nothing — B22 already established that *no* period is forced.

### 12.2 The instantiation does not close: three coordinates, three failures

**(a) The ladder's own coordinate — degenerate.** Rungs 4, 5, 6 are atom,
molecule, virus, at $\log_{10} s = -10.00, -9.00, -7.00$. The three side
lengths are $1.00$, $2.00$ and $3.00$ decades, and

$$1 + 2 = 3 \quad \text{exactly}.$$

The triangle is degenerate. This is structural, not numerical: the ladder is
**one-dimensional**, so any three rungs are collinear and the enclosed area is
identically zero. What the walk actually traces is a there-and-back fold.

*(A trap worth naming: the gaps $1.00$ and $2.00$ are round because the corpus
defines molecule and virus at nominal $10^{-9}$ and $10^{-7}$ m. The $1$-$2$-$3$
pattern is a property of those nominal definitions, not of nature, and must not
be promoted into a pattern.)*

**(b) The turn-walk — rectangular.** The corpus's turn is $\pi/2$ (L06,
$i^4 = 1$). Three such turns is $270^\circ$, i.e. $-i$, which is **not** a
return; four are required. More decisively, a walk built only from quarter
turns carries four distinct leg directions $(+x, +y, -x, -y)$, so a closed
figure from it has four distinct vertices. It can close a rectangle; it can
never close a triangle. Making it triangular requires turning by $2\pi/3$
instead — period 3, which §12.1 shows is legal, and which is a *choice*.

**(c) The degree reading — self-defeating.** The corpus's one genuine
zero-event is the degree collapse at rung 8, and it is not free: $n(u) = 5.5 > 1$
at rung 6, so rung 6 reads degree 3; $n(u) = 1$ exactly at rung 7 (the ball's
own rung); $n(u) = 0.055 < 1$ at rung 8. The first 0D rung is therefore r8,
uniquely fixed by the committed $n(u)$ column. Relocating a zero to rung 6 would
put the corpus's own gauge object below its resolution limit.

### 12.3 Verdict

The framework permits the triangle; the corpus's ladder, turn angle and
resolution rule each independently prevent it from appearing *there*. That is a
real asymmetry worth keeping: **"a return to zero" is axiomatic (G), "this
triangle" is not (X33, resolved negative).** The constructive residue is B29 —
the period-3 fixed point is a legal structure the audit never enumerated — and
if the corpus ever wanted a closed figure to sit beside L08's committed open
spiral, the choice available is the turn angle, $2\pi/3$ rather than $\pi/2$.
That choice is permitted and entailed by nothing.

---

## 13. The exchange of threes (B30, X34; check 46)

§12 tested a *geometric* triangle and found it degenerate. The same intuition
recast as **block structure in the walk's step index** — grouping the steps
into threes, $\{1,2,3\}, \{4,5,6\}, \{7,8,9\}$ — turns out to be exactly right
about one thing and wrong about another. Both halves are worth having.

### 13.1 The exchange is real, and it is forced

The walk (L08) uses step lengths $L = 0, 1, 2, 3, 5, 7, 11, \dots$ — zero, one,
then the primes — with directions cycling $E, N, W, S$, period 4. Group the
steps three at a time and two things happen, neither of them fitted:

**The omitted direction cycles with period 4, not 3.** A block of three
consecutive steps uses three of the four directions and omits one. The omitted
one runs

$$S,\ W,\ N,\ E,\ S,\ W,\ \dots$$

so no two consecutive blocks agree until four blocks have passed — twelve
steps. The reason is $\gcd(3,4) = 1$: a block of 3 advances through a cycle
of 4 by an amount coprime to it, which is the standard reason two cycles of
length 3 and 4 never phase-align.

**The two axes trade places on every block.** Because $3$ is odd, a block of
three consecutive integers contains two of one index-parity and one of the
other, and even steps feed $x$ while odd steps feed $y$ in the corpus's exact
identity (B30's model reproduces the committed vertices $(3,5)$, $(-8,5)$,
$(-8,-8)$, $(9,11)$ and $r^2 = 202$ before any of this is tested). The
dominating parity therefore alternates:

| block | steps | directions | omitted | parity | x-steps | y-steps |
|---|---|---|---|---|---|---|
| 0 | 0,1,2 | E N W | S | E O E | **2** | 1 |
| 1 | 3,4,5 | S E N | W | O E O | 1 | **2** |
| 2 | 6,7,8 | W S E | N | E O E | **2** | 1 |
| 3 | 9,10,11 | N W S | E | O E O | 1 | **2** |

This is the "exchange" — the axes swapping which one they feed, block after
block, verified over 40 consecutive blocks. It is arithmetic, not structure
that was searched for, and it is metric-free.

### 13.2 The ladder closes into whole triples only at 18 rungs

$18 = 6 \times 3$ exactly, so the rung index partitions into six clean blocks.
$16$ — the ladder as it stood before the pulsar and quasar rungs were added —
did **not**: it left a remainder of one. So the whole-block structure is a
consequence of B26, not a property the corpus had before Phase 30. Worth
recording plainly, since it means those two rungs did more than add two sizes.

One caution against over-reading: the ladder's own gauge point, the ball at
$n(u) = 1$, is rung 7 — which sits *inside* block 2, not at a block boundary.
The blocks are an index convenience, not a claim about where the ladder's
physics changes.

### 13.3 But the blocks never return to zero

$X_{34}$ is the negative half, and it is unambiguous. The block endpoints are

$$(-2,1),\ (3,5),\ (9,-8),\ (-14,-18),\ (-24,19),\ (23,29),$$

with $r^2 = 5, 34, 145, 520, 937, 1370$ — **strictly increasing**. No boundary
falls on either axis. Over 400 prime steps the walk never revisits the origin
and never touches an axis again after step 2; the one origin hit is the
trivial zero-length first step $L_0 = 0$, which is not a closure. The reason
is not subtle: the step lengths are the primes and grow without bound, so the
endpoints diverge.

So the honest form of the intuition is:

$$\underbrace{\text{axes exchange}}_{\text{real, forced, period } 4}
\ \Big|\ 
\underbrace{\text{blocks return to zero}}_{\text{false - } r^2 \text{ monotone}}.$$

L08's open spiral stands, confirmed rather than overturned. The blocks swap
which axis they feed; they do not cycle back. A period-3 *turn* (§12.1) would
close such a loop — and that remains a choice, not a consequence.
