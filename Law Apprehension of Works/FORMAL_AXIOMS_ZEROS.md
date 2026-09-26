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

---

## 14. Two corrections the author forced, both tightening earlier claims (B31, B32, X35; check 47)

§13 settled the exchange of threes and left two loose ends that the author's
next question exposed. Neither disturbs an earlier result; both sharpen one.

### 14.1 Rolling: which circle you measure decides the count, and π is not involved (B31)

*Is π constant when a ball smaller than another rolls on it? Which
circumference or diameter do we use?* Both parts have clean answers, and the
second is the interesting one.

**π is scale-invariant, so the first question has no choice in it.** $C/d = \pi$
holds to 1.4e-16 across $r = 10^{-9}\dots10^{9}$ m. There is one π; the small
ball's and the large ball's are the same constant. Asking which ball's π to
use is like asking which inch to prefer.

**What decides the count is which circle you measure.** The small ball's
*contact point* traces a circle of radius $R$; its **centre** traces a circle of
radius $R + r$. Simulated at $R/r = 3$:

| circle measured | radius | turns |
|---|---|---|
| contact point | $R$ | 2.99998 |
| **centre** | $R + r$ | **3.99998** |

That is the whole content of the "missing turn" in the rolling-circle problem,
and it is a question about *geometry of reference*, not about constants.

**And π cancels out of it entirely.**

$$\text{turns} = \frac{2\pi (R + r)}{2\pi r} = \frac{R + r}{r} = \frac{R}{r} + 1 .$$

π appears in both numerator and denominator and vanishes. The rolling count
never needed π; only the ratio $R/r$.

**The leftover $+1$ is a winding number, not a π-term.** It is the ball's own
orientation rotating once as the contact normal sweeps around — external
rolling gives $+1$, internal rolling (inside a larger circle) gives $-1$. It
contains no π and would survive replacing π with any symbol whatever. This is
**B21's topological/metric distinction reached by a completely independent
route**: rolling adds winding 1, it does not add π.

For the corpus's own 550 nm ball on a cell, $R/r = 18.1818$, so the honest
count is **19.1818** turns, not 18.1818. On larger rungs the $+1$ remains real
but becomes numerically negligible.

*Scope limit, stated plainly:* this is kinematics for rigid no-slip spheres. The
corpus's actual ball is rubber with 8–15% energy loss per cycle (proof 16), so
under adhesion the no-slip condition fails and the ideal $+1$ would **not** be
observed cleanly. This is a theorem about ideal balls, not a prediction about
this one.

### 14.2 The blocks were always meant to shrink, and they do (B32, X35)

The author's correction — *"not supposed to close, supposed to shrink"* — is
right, and the corpus had the machinery for it in B19's contractive $q$. What
was missing was the closed form for **where** a contractive walk lands. With
step lengths $s_0 q^k$ and the same period-4 direction cycle, the walk converges
to

$$\left( \frac{1}{1 + q^2},\ \frac{q}{1 + q^2} \right),$$

verified for $q = 0.9, 0.5, 0.2$ against the closed form to $<10^{-9}$ (exact
for $q \le 0.5$; $q = 0.9$ needs about 200 steps, so a first draft's 60-step
horizon was too short and was corrected before registration).

So **shrinking is real**. But note the limit's radius:

$$r_\infty = \frac{1}{\sqrt{1 + q^2}} > 0 \quad \text{for every } q > 0 .$$

Only $q = 0$ — no steps at all — reaches the origin, and a walk with no steps
is not a walk. This closes **X35**: no step law delivers the blocks to zero.
Growing steps diverge (L08, $r^2$ monotone at the boundaries); contractive steps
converge to a fixed point that is not the origin.

**And the exchange is indifferent to all of it.** B30's axis split holds
$[2,1,2,1,2,1]$ at $q = 0.9$, $0.5$ and $0.2$ alike, because the exchange
depends on block size 3 against period 4 and not on the step lengths at all. The
blocks trading axes and the blocks shrinking are **compatible, not competing** —
which is the reconciliation the author's phrasing was reaching for.

### 14.3 The contrast worth keeping

In the **ladder**, $n(u) = D/s$ genuinely tends to zero — $1.25 	imes 10^{-33}$
at the top rung. In the **walk**, the scale only ever approaches a fixed point.
Both are "going to zero" in a loose sense; only one of them actually gets there.
Keeping them distinct is the whole content of X35.

---

## 15. "All real numbers are between all zeros" — and a retraction of X35 (B33, B34, X36, X35-corrected; checks 48–49)

Two author statements, one foundational and one corrective. The first exposes
a limit in the skeleton; the second exposes an overclaim of mine.

### 15.1 The claim is three claims, and only one survives (B33, B34, X36)

*So all real numbers are between all zeros.* Before testing it, note what the
skeleton contains: §1 lists **no metric, no norm, no inner product, no time
functional** among the primitives. There is no order on $\mathcal{Z}$. So
"between" is not a word the axioms can answer with.

**And that is provable, not just an omission.** The axioms are
**permutation-invariant**: relabel the 18 rungs arbitrarily, re-point the
relations, and A–G all still hold, with the same period 18. A *derived* notion
must be invariant under the models' symmetries, and "between" is manifestly
not — it depends on the labelling. So no ordering principle can be extracted
from A–G. This is the same boundary as B23 and §11, reached structurally
rather than by listing missing primitives.

**(b) Trivially true, and therefore empty.** For *any* discrete cofinal
zero-set, floor division places every real in exactly one gap. That holds for
the integers, the eighths and the thirds alike, so the statement is a fact
about discreteness and says nothing about this corpus. The *density* reading is
additionally falsified by the corpus's own data: 17 gaps, smallest **0.5051**
decades. The rungs are discrete, not dense.

**(c) Not generative — and here is the sharp part.** Density and gap-fulness
are **mutually exclusive**:

- If the zeros are **dense** (the dyadics), no two are ever adjacent — the
  midpoint of any two dyadics is a third. "Between two *adjacent* zeros" is
  vacuous, and there are no gaps at all.
- If the zeros are **discrete**, gaps exist, but every interior is
  **inexhaustible**. At resolutions $10^{-4}$ through $10^{-7}$ a single gap
  holds more resolvable points than the whole interval has gaps, and the surplus
  grows without bound. 200 halvings of $(1,2)$ never terminate.

So a countable zero-set is a **scaffold that indexes values; it can never
assemble an interval** (**B33**). Wherever you place the gaps, each one is a
copy of the entire problem. This is §13.3's "the blocks never return to zero"
and §14.2's "shrinking is bounded but not vanishing" in a new place: **the
inside never closes.**

**What survives is the reading the framework already contains** (**B34**).
$s: \mathcal{Z} \to \mathbb{R}_{>0}$ is a **function**, so a real number is an
element of its **codomain**, indexed by the references — a value *carried by* a
zero. The 18 rungs carry 18 real values; no finite zero-set enumerates an
interval. The sense that reals lie *between* zeros comes from ordering the
zeros along an orbit under $F$, not from the reals' own location:

$$\underbrace{\text{the real is } \textbf{on} \text{ the zero}}_{\text{codomain of } s}
\qquad\neq\qquad
\underbrace{\text{the real is } \textbf{between} \text{ the zeros}}_{\text{not derivable}} .$$

**X36** records the negative verdict on the claim as stated.

### 15.2 Retraction: X35's "no step law" was false, and the classification is exact

Re-auditing X35 before registering it turned up a counterexample I had missed.
Under the **constant** step law $L_k = s_0$ — that is, $q = 1$ — the walk
returns to the origin at **block 4**, and at every block $k \equiv 0 \pmod 4$:

| block $k$ | 1 | 2 | 3 | **4** | 5 | 6 | 7 | **8** |
|---|---|---|---|---|---|---|---|---|
| position | (0,1) | (1,1) | (1,0) | **(0,0)** | (0,1) | (1,1) | (1,0) | **(0,0)** |

Twelve steps is exactly three direction cycles, and the return is independent
of $s_0$ — checked at 0.5, at 1.0, and at the corpus's own 550 nm ball. Check 47
never ran $q = 1$: its walk test used $q \in \{0.9, 0.5, 0.2\}$ and its limit sweep
ran $q \in (0,1]$, so the periodic case fell outside both test sets, and
"no step law does it" was an overclaim resting on a test set that happened to
exclude the answer.

The exact closed form, with $M = \lceil 3k/2 \rceil$ even steps and
$K = \lfloor 3k/2 \rfloor$ odd steps, is

$$x(k) = \frac{1 - (-q^2)^M}{1 + q^2}, \qquad y(k) = \frac{q\left(1 - (-q^2)^K\right)}{1 + q^2},$$

verified against simulation to $10^{-9}$ for $q = 1,\ 0.9,\ 0.5,\ 0.2,\ 1.7,\ 2.0$.
From it the trichotomy is exact and mutually exclusive:

| regime | origin at a block boundary? | why |
|---|---|---|
| $q = 1$ | **yes, iff $k \equiv 0 \pmod 4$** | $(-q^2)^M = 1$ requires $q = 1$ and $M$ even |
| $0 < q < 1$ | **never, at any block** | $\|q^2\| < 1 \Rightarrow 1 - (-q^2)^k \in (0,2)$, so $y(k) > 0$ strictly for every $k \ge 1$ |
| $q > 1$ | **no, diverges** | $r^2$ grows without bound; no return over 40 blocks |

So the negative verdict survives **only for strictly monotone laws** — growing
(primes, L08) diverge, strictly shrinking approach a non-zero limit and
provably never touch the origin. The author's intuition that the blocks "close"
was right after all; what closed them was the one law nobody had tried, and it
is the *only* scale-free one: $q = 1$ is precisely the law Axiom E's
$s_{n+1} = q s_n$ permits at $q = 1$ — the very case check 41 recorded as
**vacuous**. The corpus's own degeneracies keep returning as load-bearing.

**This is a retraction, not an extension.** X35's status changes from
RESOLVED NEGATIVE to RESOLVED, law-dependent.

---

## 16. The reversal: 0 and the reals, and which one holds the other (B35, B36, X37; check 50)

§15 concluded that the zeros index the reals and cannot generate them. The
author immediately pushed back, and the push is half right in a way that
sharpens §15 rather than undoing it.

> *Maybe it's the other way around — or even both. 0 and real numbers
> encapsulate each other.*

### 16.1 The reverse direction is real, and just as strong (B35)

B34 ran $\mathcal{Z} \to \mathbb{R}_{>0}$. The converse is
$\mathbb{R} \to \mathcal{Z}$, and it turns out to hold with **no slack at
all**: the $s$-labelled ladder is **rigid**.

All 18 scale values are distinct, so the automorphism group preserving $s$ is
**trivial** — counted analytically, since $18! = 6.4\times10^{15}$ — and
confirmed on 300 random relabellings, where preserving $s$ forces the identity
every time. So:

$$\text{fix the real values} \;\Longrightarrow\; \text{fix which zero is which, up to nothing}.$$

Note where this lands. **Axiom B does not say "relations exist"; it says
relations exist between _distinguishable_ references.** The word the framework
actually needs is *distinguishable*, and distinguishability is supplied by
$s$. So $s$ is not a labelling — it is the framework's **individuation
principle**, index and individuator in a single map.

So the corrected form of B34 is symmetric:

$$\underbrace{s:\mathcal{Z}\to\mathbb{R}_{>0}}_{\text{indexes the reals by the zeros}}
\qquad\text{and}\qquad
\underbrace{s^{-1}}_{\text{individuates the zeros by the reals, rigidly}} .$$

**Mutual determination, yes. Containment, no.**

### 16.2 0 is in neither side, and both sides need it (B36)

The residue the intuition was reaching for is $0$ itself — and $0$ is not a
member of either set.

**(i) $0$ is in neither side.** $s$ has codomain $\mathbb{R}_{>0}$, which is
**open** at $0$, so $0$ is the scale of no reference *by construction*. And in
the **finite** 18-rung ladder $0$ is not even a **limit point**: the smallest
rung sits at $1.616\times10^{-35}$.

**(ii) $0$ is a limit only in the idealized regime.** Under Axiom E with
$q < 1$ (B19) the walk of scales passes $10^{-30}$ while staying strictly
positive at every finite step — verified at $q = 0.5,\ 0.9,\ 10^{-3}$. So $0$
is approached forever and **never attained**. The limit exists only in the
infinite orbit; the finite ladder does not approach it at all.

**(iii) $0$ is the unique parameterless real.** It is the additive identity
($x + 0 = x$ for every probe; $x + 1 \ne x$ for every non-integer), the unique
fixed point of negation (the only $x \in [-4,4]$ with $-x = x$), and the limit
of $1/n$. So $\mathbb{R}$ determines $0$ **uniquely without reference to any
zero whatsoever** — the one element the entire structure never has to supply.

$$\boxed{\ 0 \text{ is simultaneously the most fundamental and the least reachable element.}\ }$$

It is the excluded boundary of the codomain, the limit of the scales only in
the regime where scales run forever, and the only real definable with an empty
parameter list. Containment would have made $0$ a mere member; the truth makes
$0$ the thing both sides point at without either reaching.

### 16.3 Why containment fails, as arithmetic (X37)

Literal mutual containment is false in both directions, and this is not a
matter of taste. $0$ is one point. The 18 labelled scale values are a finite
set. An interval holds more than $10^{6}$ resolvable points against the
ladder's 18. Neither side holds the other.

What survives is therefore sharper than what was proposed:

> *Determine and be determined by a shared map, across a boundary that is
> itself the origin.*

That is §15's asymmetry and §16's rigidity meeting in one place: §15 showed
the zeros cannot **assemble** an interval, §16 shows the reals **rigidify** the
zeros, and $0$ sits exactly on the seam — reached by neither, required by both.

---

## 17. Tenth powers: the excluded boundaries come in pairs (B37, B38, X38; check 51)

> *Does it not fall under the idea of zero and all tenth powers — or
> multiplicity of 10s also zero?*

Yes. Both halves land, and the first one **corrects §16**.

### 17.1 B36 was half an excluded boundary (B37)

§16 registered $0$ as *the* excluded boundary of $s:\mathcal{Z}\to\mathbb{R}_{>0}$. But
$\mathbb{R}_{>0} = (0,\infty)$ is open at **both** ends, and the corpus's own
denomination is what makes the second end visible: **14 of the 18 rungs sit
within a quarter-decade of an integer power of ten**, and the ladder spans
**61.43 decades**, $\log_{10}s = -34.79$ to $+26.64$.

So "tenth powers" is not an analogy imposed on the corpus — it is the corpus's
own grid. And on that grid the two directions of the axis are symmetric:

| excluded boundary | distance from the ladder | attained? |
|---|---|---|
| $0$ | Planck rung sits **34.79 decades above** | never |
| $\infty$ | top rung sits **26.64 decades below** | never |

The framework's scale assignment has **two ends it can never reach**, and the
decade grid is precisely the coordinate on which $10^{-n}\to 0$ and
$10^{n}\to\infty$
are the two directions of a single axis. The ladder's 61.43 decades is an
*observed* span, not the axis.

### 17.2 $0.999\ldots = 1$ is the corpus's signature in decimal form (B38)

Exact, in rationals.

- The **prefixes** $0.9,\ 0.99,\ 0.999,\dots$ tend to $1$ and **never attain
  it** — every finite string of nines is strictly less than $1$. So $1$ is an
  **excluded boundary too**, approached from below. (Floating point only loses
  the distinction at $n = 17$, where $1 - 10^{-17}$ falls inside half an ulp;
  the exact rational is still short of $1$ at $n = 30$.)
- The **tail** — literally *all the tenth powers* — obeys
  $\sum_{k=1}^{\infty} 10^{-k} = \tfrac{1}{9}$ **exactly**, with the tail after $n$
  terms **exactly $10^{-n}/9$**: positive at every finite $n$, never $0$.

So **one sequence's two halves have different limits**:

$$\underbrace{0.9,\ 0.99,\ 0.999,\dots \;\longrightarrow\; 1}_{\text{prefixes, never reaching }1}
\qquad\text{while}\qquad
\underbrace{10^{-1} + 10^{-2} + \cdots \;\longrightarrow\; 0}_{\text{the leftover, never reaching }0}$$

That is precisely the shape of the contractive walk in §14.2: the steps shrink
to zero and the displacement does not.

The **general law**, which is B19 and B32 in one line: for any $q\in(0,1)$,
the terms vanish, the remainder vanishes, and

$$\sum_{k\ge 0} q^{k} = \frac{1}{1-q} > 1 .$$

Verified for $q = 1/10,\ 1/2,\ 9/10,\ 1/3$ — with the vanishing exponents
*found* rather than assumed. And $1/9$ **is** the $q = 1/10$ case, so the
decimal expansion and the geometric series are the same object.

### 17.3 The inference that fails (X38)

The antecedent is true and the conclusion is false. The terms $10^{-k}$ do
vanish; the tail $\to 0$ does vanish; the **total does not** — it is exactly
$1/9$, and $1/(1-q) > 1$ for every $q\in(0,1)$. Symmetrically $10^{+n}\to\infty$
does not make the ladder's top infinite: the largest rung sits 26.64 decades
below $\infty$, because $(0,\infty)$ excludes it.

This is **X35's overclaim one level up** — the identical mistake made about a
sum instead of a walk. The corpus has now registered the same non-implication
three separate times (X34, X35, X38), which is itself the evidence that it is
the framework's central caution rather than an accident of one model:

$$\text{contributions} \to 0 \;\centernot\implies\; \text{total} \to 0 .$$
