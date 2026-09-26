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
