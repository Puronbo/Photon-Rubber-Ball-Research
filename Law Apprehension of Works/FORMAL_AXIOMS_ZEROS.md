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
| Scaling alone never forces $\pi/4$ | [ESTABLISHED] (negation of X27) | check 36/37 |
| Isotropy would force $\Delta r = \Delta z$ | [ESTABLISHED] as conditional | check 37 |
| Rotational closure = $R_{2\pi k}=I$, metric-free | [ESTABLISHED] | check 38 |
| $\Pi = \pi$ | [OPEN] — needs a derivation | X28 |
| primes give discrete hierarchies $q = 1/p$ | [ESTABLISHED] arithmetic | check 36 |
| primes as "structural generator" (Part IX role 3) | [OPEN] / [FRAMING] | C-thread, no check |
| space = interconnection of zeros; time = ordered transformations | [FRAMING] hypothesis | F21 (anchors L12, A13, E05) |
| time is an ordering of transformations | [FRAMING] — ordering alone does not give a metric on the order | F21 |

---

## 6. The one-line answer to the framework's central question (Part XVI)

> $F \stackrel{?}{\Rightarrow} (N, q, \theta, p, \Pi)$ — *no* under A–G. The
> minimal skeleton yields $N$ and $q$ (from F and E) and topological $\Pi$
> (from G), but $\theta$ and $p$ are *free parameters* unless isotropy and a
> scale rule are added. The framework's research program is therefore
> correctly identified as genuinely open — and now the two specific gaps are
> named, formalized, and gated.

**Adjacency rule (enforced):** no sentence above may be cited as physics.
The claimable core is B19 + checks 36-38; the rest is framing.
