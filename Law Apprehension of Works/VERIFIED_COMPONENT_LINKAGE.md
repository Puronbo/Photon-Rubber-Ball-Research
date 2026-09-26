# VERIFIED COMPONENT LINKAGE

Planning-thread note (informational, not verified-numerics corpus). Everything
below marked VERIFIED was checked numerically on 2026-09-25 or is already part
of the battery/canonical set; nodes marked FRAMING are philosophical stance and
must never be cited as corpus fact. The point of this file: every "real"
component links to the next through a verified edge, with no dangling claims.

## Self-gauge lemma (complete, added 2026-09-25)

Definition. Every object O defines its own rest frame F_O. In F_O the object sits
at its own origin: position x(O) = 0, and its proper extent is degenerate
supp(O) = {0}, i.e. size(O) = 0. This is a gauge fix, not physics.

Measuring with an integer line. Choose an external unit u. The lattice
L_u = {k*u | k in {0,1,2,...}} reads O's diameter as

    D_O = n_O(u) * u                       (n_O = integer lattice count)

and its volume with shape factor c (sphere c = pi/6, cube c = 1, ...) is

    V_O = c * (n_O(u) * u)^d .

Completeness (three factors). Volume is well defined iff all three are specified:
    n_O  <- counting   (Layer B; any integer lattice suffices; primes are a sparse
                        texture choice, never required for the value)
    u    <- unit       (Layer D; minted by h, c, k_B, G, moduli: u = 1 nm, lambda,
                        hbar/(mc), (kT/E)*r, ...)
    c    <- geometry   (dimensionless shape factor)
Without u the "volume" is a dimensionless number n^3; without c it misses shape.
Hence an object's self-0 is a gauge statement, NOT a measured size.

Invariance (this is the completion; ties to corrigendum 70). D_O = n_O(u)*u is
unit-invariant, so n_O(u) ~ 1/u. Verified on the ball, D = 550 nm:
    u = 1 nm   -> n = 550        -> V = (pi/6)*(550 nm)^3 = 8.71e-20 m^3
                                    (density 1100 kg/m^3 * V = 9.58e-17 kg == m, battery ✓)
    u = 1 um   -> n = 0.55 < 1   -> sub-unit, reads as a point   (entry 70 boundary ✓)
    u = 50 Mpc -> n = 3.56e-31   -> point                       (entry 70 ratio ✓)
Self-consistency: the proper frame always gives n = 0, u-free -> size zero by gauge =
the 0D point (A1). The whole size-at-scale ladder (A2) is just the function n(u) read
at different lattices.

## The linked chain

    A0 self-gauge lemma (object = 0 in its own frame)             [VERIFIED math]
       |  formal reason A1 holds; gives n_O(u)*u = D invariance
       v
    A1 0D point (Hausdorff dim 0, measure 0)                 [VERIFIED, trivial]
       |
       | correction boundary: a 550 nm ball is NOT a point at
       | molecular scales; point-like only above ~um
       v
A2 size-at-scale ladder (CORRIGENDUM entry 70)           [VERIFIED]
        D/Earth       = 8.62e-14
        D/50 Mpc      = 3.56e-31
        D/1 nm molec  = 5.5e+02
        D/0.1 nm atom = 5.5e+03
        rank x degree (RANKS_AND_DEGREES.md, checks 17-18): the same
        ladder read as (rank, degree) - n(u) >= 1 keeps an object's
        native degree; n(u) < 1 collapses its reading to a 0D point.
        |
        | the same counting substrate appears inside the ball:
       v
    B1 primes = irreducible positions of the line            [VERIFIED]
       ladder 0,1,primes; partial sums S12 =
       0,1,3,6,11,18,29,42,59,78,101,130
       NOT triangular beyond T3 (T4=10 != S5=11)             [correction]
       PNT: pi(1e6)=78498 (N/lnN 7.8% off, asymptotic);
       p_500000=7368787 (n*ln n 12.3% off);
       mean gap near 5e5 = 13.02 vs ln = 13.12;
       max gap 154 <= Cramer (ln 1e7)^2 = 260  [CONJECTURE, evidence only]
       |
       | link: ~5.6e10 counted atoms in the ball = B applied to E
       v
    C1 pi/2 turn = multiplication by i, period 4            [VERIFIED]
       i^n real cycle = 1,0,-1,0,1,0,-1,0
       |
       | link: adding anticommuting units = doubling dims
       v
    C2 Cayley-Dickson dims 1,2,4,8 (R,C,H,O)                 [VERIFIED]
       physical space = 3+1 real signature; dims DO NOT
       climb like primes (caps at 4 for physics)
       |
        | correction: prime turn-walk is an OPEN SPIRAL,
        | not nested square rings. Verified vertices: endpoint
        | after steps 0..19 = (9,11), r^2 = 202; (-8,5) at step 6,
        | r^2 = 89; (3,5) after the 6 steps 0,1,2,3,5,7, r^2 = 34.
        | r^2 = (sum of E-W steps)^2 + (sum of N-S steps)^2 and
        | is NOT the sum of squares of ladder terms (the earlier
        | draft claim was false from step 3 on; corrigendum 74).
       v
    D1 constants meter the axes; h->0 deletes quantum sizes  [VERIFIED mapping]
       ZPE->0, L_P->0, lambda_C->0, dx*dp->0
       survivors: P/c = 3.3356 pN @ 1 mW (classical radiation
       pressure), k_B*T trap RMS 0.034 nm, JKR/material sizes
       |
       | link: survivors are exactly what the battery measures
       v
    E1 the ball at the molecular rung                         [VERIFIED]
       D=550 nm, R=275 nm, m=9.583e-17 kg, E=50 MPa, nu=0.5
       Hertz d=5.807 nm @ 20.63 nN; compliant 7.662 nm @ 15.63 nN
       v_th=11.4 mm/s; Qe=Qs=3.4822; contraction 0.08% (0.22 nm)
       trap RMS 0.034 nm; melting shift 0.661 K
       |
       | link: the genuine coincidences (CORRIGENDUM entry 1)
       v
    E2 recoil KE ~= ZPE (9.9x); JKR >> k_B*T (6.3e5x);         [VERIFIED]
       full energies ~37 orders apart; per-photon momentum
       2h/lambda = 1.246e-27 kg*m/s (1064 nm)
       |
       | link: those scales are exactly A2's endpoints
       v
F1 A2 closes back to A1: the ball is all-but-a-point at     [VERIFIED]
        50 Mpc (3.56e-31), 8.6e-14 of Earth, a colloid at
        molecular rungs (same numbers as A2)

## Ranks and degrees (formal coordinates, added 2026-09-25)

In RANKS_AND_DEGREES.md the ladder is made explicit as two axes:

    RANK   the rung index (position "how high") - 0 datum/point, then upward.
           Substrate: B1's primes-indexed ladder (irregular gaps, PNT mean).
    DEGREE the dimensionality of the reading - 0 point, 1 line, 2 plane,
           3 solid; algebraic tail 1,2,4,8 (Frobenius/Hurwitz, C2); spatial
           physics caps at 3+1.

Coherence with the chain:
    ranks   use B1's counting substrate (positions index the ladder),
    degrees use C2's theorem caps (1,2,4,8 PROVEN; 3+1 physical, empirical),
    collapse is A2 read above an object's own rung (n(u) < 1 -> degree 0),
    datum invariance is A0 (rank 0, degree 0 never changes - Law L1's rest).
    OPEN-SPIRAL correction (C2): the pi/2 turn-walk is a spiral, not rings.

Verified numbers (results_of_record checks 17-27): n(u) profile D=550 nm;
log10 ladder -34.79,...,+26.64 with irregular gaps; pi(1e7)=664579;
twins <1e7 = 58980; composite-majority theorem (S(n) = n-1-2*pi(n) >= 0 for
n >= 9, first strict majority n=10, ties {1,9,11,13}, S(1e7)=8670841);
unbounded prime-free runs (witness 201!+2..201!+201); small-factor dominance
(#<=1e7 with a factor in {2,3,5,7} = 7714287, coprime to 210 = 2285713);
filled light-cone = observable 3-ball at R = 4.4e26 m, V = 3.568e80 m^3,
~4.10e99 canonical balls (register L10/E15, observed-ball only);
doubling 1,2,4,8; i period 4; Euler n^2+n+41 primes n=0..39 failing at
n=40 (=41^2).

Extension-round numbers (checks 28-35): register self-consistency CI (per-letter
IDs contiguous; B18 L12 N7 E16 A16 F20 P7 G9 + X26, matching the Count line);
ball rest energy E = mc^2 = 8.612 J (1 mW beam for 2.4 h); Schwarzschild radius
2GM/c^2 = 1.423e-43 m (ball ~36.3 orders from a black hole, diameter 36.59);
full 18-rung ladder matrix (log10 -34.79..+26.64 and n(u) = 3.40e28..1.25e-33, with sourced neutron-star 1.239e4 m and quasar-BLR 2.590e15 m rungs);
gap moments mean 4.095, sd 3.926, CV 0.959, max/min 31.0 (irregular everywhere);
H0-band observable ball R = 4.06e26..4.4e26 m, V = 2.80e80..3.568e80 m^3,
fill = 3.2e99..4.1e99 (central value is a band); two-observer overlap at
separation R/2 = 63.28% of each ball's volume (mutually-visible core);
Bekenstein bound 4.71e20 k_B, ~8.2e9x the Dulong-Petit thermal entropy
(ball far below its information limit); Euler n^2+n+b prime-run table
(b,run) = (2,1),(3,2),(5,4),(11,10),(17,16),(41,40), champion -163.

Framework-kernel numbers (check 36, "Zeros, Interconnection, Scale, and
Geometry"): tan(pi/4) = 1 with cos = sin at pi/4 (balanced r = z -> cone
half-angle pi/4); general slope c = atan(2) = 1.1071 rad != pi/4 (scaling
never fixes the angle); contractive (1/2)^200 ~ 6.2e-61 (s_0 q^n -> 0);
prime scales 1/p for p = 2,3,5,7,11 distinct in (0,1); rotational closure
cos 2pi = 1, sin 2pi = 0.

Open-problem resolutions (checks 37-38, FORMAL_AXIOMS_ZEROS.md): X27
independence — for every c > 0 the model r_n = c*q^n, z_n = q^n satisfies
minimal axioms A–G with r/z invariant (c = 2 gives atan(c) = 1.1071 rad !=
pi/4), so c is a free parameter and self-similarity never entails pi/4;
isotropy would be the extra assumption forcing c = 1. X28 topology vs measure
— R_{2pi k} = (1, 0) for k = 1, 2 to machine precision with no metric in the
expression, so T(Pi) = Pi is metric-free while value(Pi) = pi requires an
induced arc/diameter measure.

Part XVI's remaining symbols, closed (checks 39-40): N is not forced prime —
the cyclic shift on Z/m has fundamental period exactly m for every m, so
composite periods 4,6,8,9,10,12 are models of Axiom F; q is not forced
prime-reciprocal — q = 1/4, 1/6, 1/9, 1/15 are legal contractive scales
(q^50 = 7.9e-31 for 1/4, 1.6e-59 for 1/15); closure is optional — the
successor S(n) = n+1 has no finite period (no N > 0 with S^N(0) = 0).
Geometry is not fixed by the relations: C_8 path distance (diam 4) is
metric-free while the chord metric gives neighbour 0.765 at rho = 1 and
1.531 at rho = 2 for the same graph, opposite chord 2.000 vs 4.000, and
scales exactly linearly with the free radius.

Axiom audit and applicability (checks 41-42): of A-G only D and F carry
model-theoretic content - A, B, C are non-vacuity scaffolding, E is vacuous
as stated (q = 1 is a witness) and G is vacuous as stated (T = id is a
witness); the strengthened E' (q != 1) and G' (T != id) are independent, both
refuted by the successor map, which has no finite period and no fixed point.
Against the corpus's own 18-rung ladder, A-D hold but E fails - 17 distinct
ratios, gap mean 4.096 decades, CV 0.926, max/min 31.3 - and 0 of 15 steps
are prime-reciprocal, so the scale axiom is an idealisation rather than a
description of the observed hierarchy.

Pulsar and quasar, the two objects that bracket the boundary (checks 43-44):
PSR B1929+10 from P = 0.226518 s and Pdot = 1.15661e-15 s/s alone gives
tau = P/2Pdot = 3.103 Myr (published 3.09-3.1, dev 0.10%), B = 3.2e19
sqrt(P Pdot) = 5.180e11 G (published 0.51e12, dev 1.16%), Edot = 4 pi^2 I
Pdot/P^3 = 3.929e33 erg/s (published 3.89e33, dev 0.99%, I = 1e45 g cm^2) -
tau is metric-free, B and Edot embed I, R and c. L_Edd = 4 pi G M m_p c /
sigma_T = 1.2573e38 erg/s per solar mass gives lambda_Edd = 2.742 (published
2.74) for J0341+1720 (M = 6.73e9 Msun, L_bol = 2.32e48) and 3.021 (published
3.01) for J2125-1719 (M = 5.45e9, L_bol = 2.07e48), and is linear in M only
via the Schwarzschild radius GM/c^2. Ladder rungs: neutron star 1.239e4 m
(PSR J0740+6620, R = 12.39 km, Riley et al. 2021), quasar BLR 2.590e15 m
(100-day reverberation lag, Kaspi et al. 2000); gaps 17 distinct, mean 3.614,
sd 3.504, CV 0.970. A period-3 return is a legal model of F and G (sigma_3 on Z/3 has
fundamental period exactly 3) that check 39 never probed, having tested only the composite
set {4,6,8,9,10,12}; but the proposed triangle at rungs 4-6 closes nowhere - degenerate in
the 1D ladder (sides 1.00 + 2.00 = 3.00 decades), rectangular under the pi/2 turn (three
quarter turns = 270 deg, not a return; four distinct leg directions), and the corpus's one
real zero-event is r8, fixed by the ball's n = 1 at r7. Grouping the walk's steps in threes
against the period-4 direction cycle makes the axes trade places every block (omitted
direction cycles S,W,N,E with period 4 since gcd(3,4)=1; 3 is odd so the dominant
step-index parity alternates 2/1, 1/2 over 40 blocks), and 18 rungs divide into exactly
six triples where 16 did not - but the blocks never return: r^2 at boundaries is 5, 34,
145, 520, 937, 1370, strictly increasing, no boundary on an axis, no origin return in
400 prime steps.

## Theorems and conjectures per layer (label PROVEN / CONJECTURE — never conflate)

A0 self-gauge:
  PROVEN   Gauge/coordinate freedom (diffeomorphism invariance of field laws; GR is
           background-independent). "Position and size zero in own frame" is a gauge
           fix, exactly the freedom these theorems guarantee.
  PROVEN   Buckingham Pi theorem (1914): every physical relation reduces to
           dimensionless groups -> why "volume = count * unit^d" splits as it does.
  (operational): proper frame reading n = 0, u-free is by construction, not conjecture.

B1 primes:
  PROVEN   Prime Number Theorem (Hadamard & de la Vallee Poussin 1896; elementary:
           Erdos & Selberg 1949). pi(x) ~ x/ln x; pi(1e6)=78498 vs 72382 is its 7.8%
           asymptotic error. Consequence: mean gap ~ ln p (observed 13.02 vs 13.12).
  PROVEN   Euclid (c.300 BCE): infinitely many primes. Dirichlet AP (1837):
           primes in arithmetic progressions. Chebyshev 1850: Bertrand's postulate.
  PROVEN   Green-Tao (2004): primes contain arbitrarily long arithmetic progressions.
  CONJECTURE Riemann hypothesis (1859): exact pi(x) - Li(x) error from zeta zeros.
           Open. Different proofs of rest of PNT family irreducible to it.
  CONJECTURE Cramer (1936): maximal gap ~ (ln p)^2. My verified max gap 154 below 1e7
           vs (ln 1e7)^2 = 260 is EVIDENCE, not proof. (corrected label)
  CONJECTURE Goldbach (1742); twin primes/de Polignac; Legendre (prime between n^2 and
           (n+1)^2). Note: bounded prime gaps <= 246 are PROVEN (Maynard 2013,
           Polymath 8b 2014) but infinitude of twin primes is still open.
CONJECTURE Hardy-Littlewood (1923): density of primes among quadratics like
            n^2+n+41. Its primality for n=0..39 and failure at 40 (=41^2) is PROVEN
            computation but the density law (why Ulam diagonals are rich) is conjecture.
            (gate-asserted: results_of_record check 21)

C2 doubling/dimensions:
  PROVEN   Frobenius (1877): only real associative finite division algebras are
           R, C, H -> the "doubling" chain cannot extend associatively past H.
  PROVEN   Hurwitz (1898): only normed division algebras are R, C, H, O (caps at 8).
PROVEN   Bott periodicity (1959): Clifford algebra repetitions of period 8
            (the O/8D tail of the chain repeats).
  PROVEN   i period 4 (i^2=-1, i^4=1) — Euler formula.
            (gate-asserted: results_of_record checks 19-20)
  (empirical): observed space is 3+1 real. The chain capping at 8D is THEOREM-proven;
           space being 3(+1)D is an empirical fact, not a theorem.

E2 / physics connections (the corpus's theory-extension layer):
  PROVEN   Fluctuation-dissipation theorem (Callen & Welton 1951); Jarzynski equality
           (1997); Crooks (1999) — the FDT connection file's foundation, battery-tested.
  CONJECTURE Verlinde entropic gravity (2010); quantum-gravity-induced decoherence
           sizes; black-hole analog thermodynamics at microscale — analogical, open.
  PROVEN (numeric) the "genuine coincidences": recoil KE ~= ZPE (9.9x),
           JKR >> k_BT (6.3e5x), 37 orders of magnitude hierarchy (corrigendum 1).

Crucial discipline: PNT, Frobenius, Hurwitz, Pi theorem give the frame our checks
reproduced; Cramer, Goldbach, RH, twin primes, Hardy-Littlewood give the frame's
open edges (the ladder's irregularity is EXACTLY where the conjectures live).

## Closed loop

A0 -> A1 -> A2 -> B1 -> D1 -> E1 -> E2 -> F1 -> back to A2/A1 (and A0 via D_O invariance).
Ranks-and-degrees coordinates interleave the loop: rank positions (A2 -> B1 substrate),
degree caps (C2 -> doubling/i-period), collapse (F1 / A2 at high rung).
Every edge is a verified number or a correction recorded above.
No node in the loop depends on an unverified claim.

## FRAMING (never cited as corpus fact)

- "consciousness = the action in space": process-ontology stance
  (Whitehead/enactivism); no experiment in this project or physics
  generally measures it. Kept here as framing only.
- "count to the next prime, turn pi/2" as a SINGLE law: rejected.
  Primes (positions, ~n ln n), doubling (dimensions, powers of 2),
  constants (scale meter, dimensionless ratios) are three laws of
  different growth; splicing them is poetic, not structural.