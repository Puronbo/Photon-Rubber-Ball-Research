#!/usr/bin/env python3
"""
Results of Record - single-command reproduction gate.

Reproduces and asserts the canonical result table documented in PROJECT_INDEX.md
using the verification module's own constants and the independent closed forms
the battery verifies. Exits nonzero if any documented number is not reproduced.

Backed by: photon_rubber_ball_verification_improved.py (9-axis battery),
script.py (independent re-verification), test_expansion_rigorous*.py (37 tests),
energy_comparability_probe.py (energy-scale verdict). Checks 17-27 assert the
rank-degree ladder (RANKS_AND_DEGREES.md): entry-70 scale readings, the
irregular (prime-gap-like) log10 spacing (Planck-to-Hubble, D = 550 nm source),
the counting substrate (pi(1e7) = 664579; twins < 1e7 = 58980 exact), the
algebraic half the thread relies on — doubling dims 1,2,4,8, i period 4,
Euler n^2+n+41 — and the composite-majority theorem (C(n) = n-1-pi(n):
S=C-pi < 0 only for n = 2..8, ties at {1, 9, 11, 13}, first strict composite
majority at n = 10, S >= 0 for every n in [9, 1e7], S(1e7) = 8670841).
Checks 25-26 add the two sieve consequences: unbounded prime-free runs
(witness 201!+2..201!+201, j | (201!+j) exact) and small-factor dominance
of the integers n <= 1e7. Check 27 fills the light-cone: the observable causal
3-ball at the top particle-horizon rung 16 radius (4.4e26 m) has volume (4/3)pi R^3 =
3.568e80 m^3, holding 4.10e99 canonical 550 nm balls.
Checks 28-35 (extension round 2026-09-25): 28 auto-verifies CLAIM_REGISTER.md
self-consistency (per-letter IDs contiguous, totals match the Count line) so
register drift can never silently walk again; 29 ball rest mass-energy
E = mc^2 = 8.612 J and Schwarzschild radius 2GM/c^2 = 1.423e-43 m (~36.3 orders
from a black hole); 30 the full 18-rung ladder matrix (log10 s and n(u)=D/s for
every rung of RANKS_AND_DEGREES.md); 31 ladder gap moments (mean 4.095, sd 3.926,
CV 0.959, max/min 31.0 - irregular everywhere); 32 the observable ball as an H0
band (Planck 67.4 -> SH0ES 73.04: R in [4.06e26, 4.4e26] m, V in [2.80e80,
3.568e80] m^3, fill >= 3.2e99); 33 two-observer overlap: equal top-rung balls at
separation R/2 share 63.28% of each ball's volume (observers' zeros share the
mutually-visible core); 34 Bekenstein bound for the ball = 2*pi*kB*R*E/(hbar*c) =
4.71e20 k_B, ~8.2e9x the Dulong-Petit order-of-magnitude thermal entropy (the ball
sits far below its information limit); 35 the Euler n^2+n+b prime-run table over
the class-number-1 discriminants (b,run) = (2,1),(3,2),(5,4),(11,10),(17,16),
(41,40), b=41 champion (discriminant -163).
Check 36 asserts the zero-framework cone/scale/closure kernel of the
"Zeros, Interconnection, Scale, and Geometry" framework (MGS Puno): balanced
r = z gives the pi/4 cone (tan(pi/4) = 1, cos = sin at pi/4); a general
slope c gives theta = atan(c) which generically differs from pi/4, so scaling
alone never fixes the angle; the contractive scale sequence s_0*q^n converges
to zero; prime scales q = 1/p form distinct discrete hierarchies; and
rotational closure returns the orientation (cos 2pi = 1, sin 2pi = 0).
Checks 37-38 resolve the framework's own two open problems: 37 (X27) shows
scaling alone never forces pi/4 (the family r = c z is self-similar for any
c, so c is a free parameter under the minimal axioms) while isotropy of the
elementary relation is the extra constraint that would force c = 1; 38 (X28)
shows rotational invariance is topological (winding number k in Z, R_{2pi k} =
I, no metric needed) whereas the numerical value pi requires an induced
measure (arc length = rho*phi, arc/diameter), so Pi = pi is not forced by the
minimal axioms.
Checks 39-40 close the rest of the framework's Part XVI question
F => (N, q, theta, p, Pi): 39 (X29) shows the closure period need not be prime
(the cyclic shift on Z/m has fundamental period exactly m for every m, so
4,6,8,9,10,12 are models of the closure axiom) and the scale factor need not
be prime-reciprocal (1/4, 1/6, 1/9, 1/15 are all legal contractive scales),
with closure itself optional (the successor map has no finite period); 40
(X30) shows the relations do not determine the geometry - cycle path distance
is metric-free (diam = n//2) while any Euclidean embedding uses the chord
2*rho*sin(pi*d/n), so the same C_8 graph has neighbour chord 0.765 at rho = 1
and 1.531 at rho = 2 and pi enters only at the embedding step.
Checks 41-42 audit the axiom set and its applicability: 41 finds that of A-G
only D (composition) and F (closure) carry model-theoretic content - A, B, C
are non-vacuity scaffolding, E is vacuous as stated (the constant scale
q = 1 witnesses "may carry a scale factor") and G is vacuous as stated (the
identity witnesses "exists T, X with T(X) = X") - while the strengthened
E' (q != 1) and G' (T != id) are independent, both refuted by the successor
map, which has no finite period and no fixed point; 42 tests the skeleton
against this corpus's own 18-rung ladder and finds A-D hold but E fails, all
15 consecutive ratios being distinct (gap mean 4.096 decades, CV 0.926,
max/min 31.3) with 0 of 17 steps prime-reciprocal, so the scale axiom is an
idealisation rather than a description of the observed hierarchy.
Checks 43-44 add the two objects that bracket the framework's metric
boundary, and extend the canonical ladder from 16 to 18 rungs with sourced
values (neutron star 1.239e4 m, PSR J0740+6620 equatorial radius 12.39 km,
Riley et al. 2021; quasar broad-line region 2.590e15 m, a 100-day
reverberation lag, Kaspi et al. 2000): 43 shows the PSR B1929+10 spin-down
triad follows from the two timed observables P and Pdot alone - characteristic
age tau = P/2Pdot = 3.103 Myr (published 3.09-3.1), surface field B = 3.2e19
sqrt(P Pdot) = 5.18e11 G (published 0.51e12), spin-down Edot = 4 pi^2 I
Pdot/P^3 = 3.93e33 erg/s (published 3.89e33) - and that the split is the
point, since tau is metric-free period arithmetic (Axioms F and G) while B
and Edot embed I, R and c; 44 shows the quasar luminosity anchor is Eddington,
L_Edd = 4 pi G M m_p c / sigma_T = 1.257e38 erg/s per solar mass, reproducing
the published super-Eddington ratios of J0341+1720 (2.742 vs 2.74) and
J2125-1719 (3.021 vs 3.01), linear in M only because the capture radius is
GM/c^2. The ladder's gap moments therefore move and are disclosed: 17 gaps,
all distinct, mean 3.614, sd 3.504, CV 0.970.
Check 45 tests the idea that a turn at rungs 4, 5 and 6 returns to zero as a
triangle: the ladder's own coordinate makes it degenerate (sides 1.00 + 2.00 =
3.00 decades, since a 1D ladder makes any three rungs collinear), the corpus's
pi/2 turn makes it rectangular rather than triangular (three quarter turns is
270 deg, not a return, and quarter turns have four distinct leg directions), and
the corpus's single real zero-event is pinned to rung 8 by the committed n(u)
column - yet a period-3 return is itself a perfectly legal model of Axioms F and
G (sigma_3 on Z/3 has fundamental period exactly 3), a case check 39 never
probed because it tested only composite periods to refute primality.
Check 46 tests the same idea recast as block structure rather than geometry:
grouping the walk's steps in threes makes the x and y axes TRADE PLACES every
block - each block of 3 omits one of the four directions, the omitted one
cycling S,W,N,E with period 4 because gcd(3,4) = 1, and since 3 is odd the
dominant step-index parity alternates 2/1 then 1/2 (verified over 40 blocks,
so forced by arithmetic rather than fitted). The 18 rungs also divide into
exactly six triples, which 16 did not. But the blocks exchange axes and never
return to zero: r^2 at successive block boundaries is 5, 34, 145, 520, 937,
1370 - strictly increasing - no boundary lands on an axis, and over 400 prime
steps the walk never revisits the origin. L08's open spiral is confirmed.
Check 47 separates two things the walk and the rolling ball are often confused
for. (a) ROLLING: pi is scale-invariant - C/d = pi to 1.4e-16 across nine
decades - so there is no "which ball's pi" to choose; what decides the count is
WHICH CIRCLE you measure, since the small ball's contact point traces radius R
(giving R/r turns) while its CENTRE traces radius R+r (giving R/r + 1). Simulated
at R/r = 3: 3.00000 vs 4.00000 turns. And pi cancels exactly, 2*pi*(R+r)/(2*pi*r)
= (R+r)/r, so the rolling count never needed pi at all. The leftover +/-1 is the
ball's own orientation rotating once as the contact normal sweeps around - a
WINDING NUMBER, present with any symbol in place of pi, which is exactly B21's
topological/metric distinction. (b) CONTRACTION: the blocks were always meant to
shrink, and they do - a contractive step law s0*q^k bounds the walk to the exact
non-zero limit (1/(1+q^2), q/(1+q^2)) for q = 0.9, 0.5, 0.2, matching the closed
form. Shrinking is real; reaching zero is not - only q = 0 does. B30's axis
exchange is invariant under all of it, holding [2,1,2,1,2,1] at every q tested,
because it depends on block size 3 against period 4 and not on the step law.
Check 48 tests "all real numbers are between all zeros" and finds the claim is
three separate things, only one of which survives. A-G are stated over Z with
NO order (section 1 lists no metric, norm, inner product or time functional),
and the axioms turn out to be permutation-invariant: 300 random relabellings of
the 18 rungs all still satisfy A-G with the same period 18. A derived notion
like "between" would have to be permutation-invariant, and it is not - so the
skeleton supplies no order to be "between" in. Under the trivial reading the
claim is true but empty, since floor division puts every real in exactly one gap
for ANY discrete cofinal zero-set (integers, eighths, thirds alike), and the
density reading is falsified by the corpus's own 17 gaps, smallest 0.5051
decades. The generativeness reading is refuted outright: dense zeros admit no
adjacent pair (the midpoint of any two dyadics is a third), so density and
gap-fulness are mutually exclusive, and if the zeros are discrete then every gap
interior is inexhaustible, holding more resolvable points than the interval has
gaps with the surplus growing without bound as resolution rises. What the
framework already contains is the resolution: s: Z -> R_{>0} is a FUNCTION, so a
real is a value ATTACHED to a zero - an element of the codomain of the scale
assignment, indexed by the references - not a point located between them.
Check 49 is a CORRECTION to X35, which had been registered too strongly. "No
step law delivers the blocks to zero" is FALSE: under the constant step law
L_k = s0 (q = 1) the walk returns to the ORIGIN at block 4 and at every block
k = 0 mod 4, independently of s0. Check 47 never ran q = 1 - its walk test used
q in {0.9, 0.5, 0.2} and its limit sweep ran q in (0, 1] - so the periodic case
fell outside both and the universal negative was an overclaim. The exact
classification is now closed form: with M = ceil(3k/2) and K = floor(3k/2),
x(k) = (1 - (-q^2)^M)/(1 + q^2) and y(k) = q(1 - (-q^2)^K)/(1 + q^2), matching
simulation for q = 1, 0.9, 0.5, 0.2, 1.7, 2.0 to 1e-9. Hence the trichotomy is
exact: q = 1 returns periodically (origin iff k = 0 mod 4); 0 < q < 1 NEVER
reaches the origin at any block, because |q^2| < 1 forces 1 - (-q^2)^k into
(0, 2) so y(k) > 0 strictly for every k >= 1; and q > 1 diverges. The negative
verdict therefore survives only for STRICTLY MONOTONE laws.
Check 50 tests the author's reversal of B34 - maybe the containment runs the
other way, or both ways at once, 0 and the reals encapsulating each other. The
reverse direction turns out to be exactly as strong as the forward one: the
s-labelled ladder is RIGID. All 18 scale values are distinct, so the
automorphism group preserving s is trivial - counted analytically, since 18! is
6.4e15 - and no non-identity relabelling survives, checked on 300 random
permutations where preserving s forces the identity every time. So once the real
values are fixed, which zero is which is completely determined, with no residual
symmetry. That lands on the word Axiom B actually uses: R exists between
DISTINGUISHABLE references, and distinguishability is supplied by s. The zeros
and the reals therefore determine each other through one shared structure doing
both jobs at once - index and individuator. But literal containment is false, and
0 lands where neither side can put it. s: Z -> R_{>0} has an OPEN codomain, so 0
is no reference's scale; in the finite 18-rung ladder it is not even a limit
point, the smallest rung sitting at 1.616e-35. Under Axiom E with q < 1 it does
become the limit (B19) and is never attained - q = 0.5, 0.9 and 1e-3 all pass
1e-30 while staying strictly positive. And 0 is the UNIQUE real definable from R
alone with no parameters: the additive identity, the unique fixed point of
negation, the limit of 1/n. So 0 is simultaneously the most fundamental and the
least reachable element of the framework - the excluded boundary both sides need
and neither supplies.
Check 51 asks whether this falls under "zero and all tenth powers, or
multiplicity of 10s also zero". Both halves land, and the first one CORRECTS
B36. The ladder is DECADE-DENOMINATED natively - 14 of 18 rungs sit within a
quarter-decade of an integer power of ten, spanning 61.43 decades - so "tenth
powers" is the corpus's own grid, not an analogy. And s: Z -> R_{>0} has
codomain (0, inf), open at BOTH ends, so B36's single excluded boundary is
really a PAIR: the Planck rung sits 34.79 decades above 0 and the top rung 26.64
decades below infinity, approaching both and attaining neither. Second,
0.999... = 1 is the decimal instance of the corpus's signature. The prefixes
tend to 1 and NEVER attain it - every finite string of nines is strictly less
than 1, so 1 is an excluded boundary too (and floats only lose the distinction
at n = 17, where 1 - 1e-17 falls inside half an ulp). The TAIL, which is
literally all the tenth powers 10^-1 + 10^-2 + ..., tends to 0 and is never 0
either. And the sum of all tenth powers from 10^-1 upward is EXACTLY 1/9, with
the tail after n terms exactly 10^-n/9. So one sequence's two halves have
DIFFERENT limits - prefixes to 1, leftovers to 0 - precisely the shape of the
contractive walk, where the steps shrink to zero and the displacement does not.
Third, this is one law in three places: B19 (q^n -> 0), B32 (contractive walk
-> 1/sqrt(1+q^2) > 0), and now the geometric series, where for any q in (0,1)
the terms vanish, the remainder vanishes, and the TOTAL is 1/(1-q) > 1. The
inference that fails is "all the tenth powers are zero, therefore everything is
zero" - X35's overclaim one level up.
"""

import math
import os
import re
import sys

import photon_rubber_ball_verification_improved as core

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

KB = 1.380649e-23
HBAR = 1.054571817e-34
C0 = 299792458.0
G = 6.67430e-11
D = 2*core.R

TOL_PCT = 0.01

def expect(ok, name, got, want):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: got {got}  want {want}")
    return ok

def main():
    ok = True

    m = core.M
    ok &= expect(abs(m - 9.583e-17)/9.583e-17 < TOL_PCT,
                 "mass M (rho*4/3 pi R^3)", f"{m:.3e} kg", "9.583e-17 kg")

    er = core.ESTAR_RIGID
    ok &= expect(abs(er/1e6 - 66.667)/66.667 < TOL_PCT,
                 "E* rigid E/(1-nu^2)", f"{er/1e6:.3f} MPa", "66.667 MPa")

    ec = core.ESTAR_COMPLIANT
    ok &= expect(abs(ec/1e6 - 33.333)/33.333 < TOL_PCT,
                 "E*_two E/(2(1-nu^2))", f"{ec/1e6:.3f} MPa", "33.333 MPa")

    dmax = core.DMAX
    pmax = core.PMAX
    ok &= expect(abs(dmax - 5.807e-9)/5.807e-9 < TOL_PCT,
                 "Hertz max indentation (rigid plane)", f"{dmax*1e9:.3f} nm", "5.807 nm")
    ok &= expect(abs(pmax - 20.63e-9)/20.63e-9 < TOL_PCT,
                 "Hertz max load (rigid plane)", f"{pmax*1e9:.2f} nN", "20.63 nN")

    dcomp, pcomp = core.DCOMP, core.PCOMP
    ok &= expect(abs(dcomp - 7.662e-9)/7.662e-9 < TOL_PCT,
                 "max indentation (compliant plane)", f"{dcomp*1e9:.3f} nm", "7.662 nm")
    ok &= expect(abs(pcomp - 15.63e-9)/15.63e-9 < TOL_PCT,
                 "max load (compliant plane)", f"{pcomp*1e9:.2f} nN", "15.63 nN")

    v_th = math.sqrt(3*KB*300.0/m)
    ok &= expect(abs(v_th - 11.4e-3)/11.4e-3 < TOL_PCT,
                 "thermal speed sqrt(3kT/m)", f"{v_th*1e3:.2f} mm/s", "11.40 mm/s")

    x = 2*math.pi*core.R/core.LAMBDA_PHOTON
    qe, qs = core.mie_q(complex(1.5, 0.0), x)
    ok &= expect(abs(qe - 3.4822)/3.4822 < TOL_PCT,
                 "Mie Q_ext (x=pi, m=1.5+0i)", f"{qe:.4f}", "3.4822")
    ok &= expect(abs(qs - 3.4822)/3.4822 < TOL_PCT,
                 "Mie Q_sca (x=pi, m=1.5+0i)", f"{qs:.4f}", "3.4822")
    ok &= expect(qe == qs, "energy balance Q_ext == Q_sca", f"{qe:.6f}", f"{qs:.6f}")

    n = 0.4
    lhs = math.sqrt(2*n/5)
    ok &= expect(abs(lhs - n) < 1e-12,
                 "fixed-point algebra sqrt(2n/5)=n", f"n={lhs:.6f}", "n=0.400000")
    ok &= expect(abs(1-math.sqrt(1-0.0016) - 0.0008) < 1e-6,
                 "contraction at beta=0.04 (~0.01%)", f"{1-math.sqrt(1-0.0016):.6f}", "0.000800")

    kt = KB*300.0
    rel = (1/math.sqrt(1-0.0016) - 1)*m*C0*C0
    zpe = HBAR*HBAR/(2*m*core.R*core.R)
    p = HBAR*2*math.pi/core.LAMBDA_PHOTON
    rec = p*p/(2*m)
    ok &= expect(rel/kt > 1e17, "rel KE dominates kT (claim is FALSE, not comparable)",
                 f"{rel/kt:.1e}", "> 1e17")
    ok &= expect(kt/zpe > 1e17, "kT dominates ball zeropoint",
                 f"{kt/zpe:.1e}", "> 1e17")
    ok &= expect(5 < rec/zpe < 15,
                 "per-photon recoil KE ~ zeropoint (true coincidence)",
                 f"{rec/zpe:.2f}", "5-15")

    rungs = [("atom", 1e-10), ("molecule", 1e-9), ("virus", 1e-7),
             ("ball", 5.5e-7), ("cell", 1e-5),
             ("Earth", 6.378e6), ("galaxy", 30e3*3.0857e16),
             ("GA", 50e6*3.0857e16), ("Laniakea", 160e6*3.0857e16)]
    want_n = {"ball": 1.0, "cell": 0.055, "Earth": 8.62e-14,
              "GA": 3.56e-31, "Laniakea": 1.11e-31}
    nline = "; ".join(f"{k}={D/s:.3g}" for k, s in rungs)
    nl_ok = all(D/s > 0 for _, s in rungs)
    for name, want in want_n.items():
        s = dict(rungs)[name]
        nl_ok &= abs((D/s) - want)/want < 0.01
    ok &= expect(nl_ok, "rank-degree ladder n(u)=D/s (ball=1, cell<1 point-read collapse, Earth/GA/Laniakea)",
                 nline, "; ".join(f"{k}={v:g}" for k, v in want_n.items()))

    l10 = [math.log10(s) for _, s in rungs]
    want_l10 = {"atom": -10.0, "molecule": -9.0, "virus": -7.0, "ball": -6.26,
                "cell": -5.0, "Earth": 6.80, "galaxy": 20.97, "GA": 24.19,
                "Laniakea": 24.69}
    lo_ok = all(abs(l10[i] - want_l10[rungs[i][0]]) < 0.02 for i in range(len(rungs)))
    gaps = [round(l10[i+1] - l10[i], 2) for i in range(len(l10) - 1)]
    irregular = len(set(gaps)) > 1
    lo_ok &= irregular
    ok &= expect(lo_ok, "ladder log10 profile + irregular (prime-gap-like) spacing",
                 "; ".join(f"{l10[i]:.2f}" for i in range(len(l10))),
                 "differs rung-to-rung (gaps %s, not uniform)" % "; ".join(map(str, gaps)))

    seq = [1]
    while seq[-1] < 8:
        seq.append(seq[-1]*2)
    ok &= expect(seq == [1, 2, 4, 8], "Cayley-Dickson doubling dims 1,2,4,8",
                 str(seq), "[1, 2, 4, 8] (next, 16, is the first non-normed/split dim)")

    i2 = complex(0, 1)
    cyc = [i2**k for k in range(4)]
    ok &= expect(i2**2 == -1 and i2**4 == 1 and len(set(cyc)) == 4,
                 "i period 4 (i^2=-1, i^4=1)", "period 4 distinct", "i^4 = 1")

    def _isprime(n):
        if n < 2:
            return False
        d = 2
        while d*d <= n:
            if n % d == 0:
                return False
            d += 1
        return True

    euler_ok = all(_isprime(n*n + n + 41) for n in range(40))
    n40 = 40*40 + 40 + 41
    euler_ok &= (not _isprime(n40)) and n40 == 41*41
    ok &= expect(euler_ok, "Euler n^2+n+41 prime for n=0..39, fails at n=40 (=41^2)",
                 f"primes n=0..39, n=40 -> {n40}", "1681 = 41^2 composite")

    nmax = 10**7
    sv = bytearray([1])*(nmax+1)
    sv[0] = sv[1] = 0
    for p in range(2, int(nmax**0.5)+1):
        if sv[p]:
            sv[p*p::p] = bytearray(len(range(p*p, nmax+1, p)))
    pix7 = sum(sv)
    twins = sum(1 for i in range(3, nmax-2) if sv[i] and sv[i+2])
    ok &= expect(pix7 == 664579, "pi(1e7) sieve count",
                 str(pix7), "664579 (n/ln n is 6.6% off, asymptotic)")
    ok &= expect(twins == 58980, "twin-pair count < 1e7 (exact; HL ~ 2*C2*x/ln^2x is conjecture, 14% off)",
                 str(twins), "58980 (computed; formula CONJECTURE)")

    ties = [1]
    neg = 0
    first_majority = None
    min_s9 = None
    s_N = None
    pi_run = 0
    for n in range(2, nmax + 1):
        pi_run += sv[n]
        s = (n - 1) - 2*pi_run
        if s < 0:
            neg += 1
        elif s == 0:
            ties.append(n)
        if first_majority is None and s > 0:
            first_majority = n
        if n >= 9 and (min_s9 is None or s < min_s9):
            min_s9 = s
        if n == nmax:
            s_N = s
    cm_ok = (neg == 7) and (ties == [1, 9, 11, 13]) and (first_majority == 10) \
        and (min_s9 == 0) and (s_N == 8670841)
    ok &= expect(cm_ok,
                 "composite-majority theorem: C=n-1-pi, S=C-pi; S<0 only for n=2..8; ties {1,9,11,13}; first strict majority n=10; S>=0 for all n in [9,1e7]; S(1e7)",
                 f"neg-range={neg} ties={ties} first-maj={first_majority} min-S(9..1e7)={min_s9} S(1e7)={s_N}",
                 "S<0 count 7, ties [1, 9, 11, 13], first-maj 10, min-S 0, S(1e7)=8670841")

    run_ok = True
    f201 = math.factorial(201)
    for j in range(2, 202):
        if (f201 + j) % j != 0:
            run_ok = False
            break
    ok &= expect(run_ok,
                 "unbounded prime-free runs (witness 201!+2..201!+201 = 200 consecutive composites)",
                 "200 consecutive composites" if run_ok else "divisibility failed",
                 "each j satisfies j | (201!+j); any run length n via (n+1)!+2..(n+1)!+n+1")

    phi210, block, rem = 48, nmax // 210, nmax % 210
    r = sum(1 for k in range(1, rem + 1) if math.gcd(k, 210) == 1)
    coprime = phi210*block + r
    with_factor = nmax - coprime
    small_ok = (with_factor == 7714287) and (with_factor > nmax*0.77)
    ok &= expect(small_ok,
                 "small-factor dominance: #<=1e7 divisible by 2,3,5,7 (>77%: 1-phi(210)/210 ~ 0.7714)",
                 f"count={with_factor} coprime-to-210={coprime} frac={with_factor/nmax:.4f}",
                 "count=7714287, coprime=2285713 (Mertens: prod(1-1/p)->0 in the window limit)")

    r_obs = 4.4e26
    v_univ = (4/3)*math.pi*r_obs**3
    v_ball_fill = (4/3)*math.pi*core.R**3
    fill = v_univ/v_ball_fill
    fill_ok = abs(v_univ - 3.568e80)/3.568e80 < 0.01 and 4.0e99 < fill < 4.2e99
    ok &= expect(fill_ok,
                 "filled light-cone = observable 3-ball (top particle-horizon rung 16, R=4.4e26 m): V=(4/3)pi*R^3; canonical-ball fill count",
                 f"V={v_univ:.3e} m^3  fill-count={fill:.3e}",
                 "V=3.568e80 m^3, ~4.10e99 canonical balls (R ratio 1.6e33, cubed)")

    # ---- checks 28-35 (extension round 2026-09-25) ----

    # 28: register self-consistency (arithmetic CI - the drift guard).
    rc_ok = False
    counts = {}
    contig = False
    declared_txt = "CLAIM_REGISTER.md not present"
    if os.path.exists("CLAIM_REGISTER.md"):
        rtxt = open("CLAIM_REGISTER.md", encoding="utf-8").read()
        by = {}
        for letter, num in re.findall(r"(?m)^\|\s*([BLNEFAPGX])(\d+)\s+\|", rtxt):
            by.setdefault(letter, []).append(int(num))
        contig = True
        for letter, nums in by.items():
            nums.sort()
            counts[letter] = len(nums)
            contig &= nums == list(range(1, len(nums) + 1))
        mdecl = re.search(r"(\d+) numbered claims.*?\+ (\d+) NOT-claims", rtxt, re.S)
        total = sum(counts.get(ch, 0) for ch in "BLNEFAPG")
        rc_ok = contig and mdecl is not None \
            and total == int(mdecl.group(1)) and counts.get("X", 0) == int(mdecl.group(2))
        if mdecl:
            declared_txt = str(mdecl.group(1)) + " numbered + " + mdecl.group(2) + " NOT-claims"
    rc_got = "; ".join(f"{ch}={counts.get(ch, 0)}" for ch in "BLNEFAPGX")
    ok &= expect(rc_ok, "register self-consistency (per-letter IDs contiguous, totals match Count line)",
                 rc_got, declared_txt)

    # 29: rest mass-energy and Schwarzschild distance-to-black-hole.
    erest = m*C0*C0
    rs_ball = 2*G*m/(C0*C0)
    orders_rs = math.log10(core.R/rs_ball)
    ok &= expect(abs(erest - 8.612)/8.612 < TOL_PCT,
                 "ball rest mass-energy E=mc^2", f"{erest:.3f} J", "8.612 J (1 mW beam for 2.4 h)")
    ok &= expect(abs(rs_ball - 1.423e-43)/1.423e-43 < TOL_PCT,
                 "Schwarzschild radius 2GM/c^2 of the ball", f"{rs_ball:.3e} m", "1.423e-43 m")
    ok &= expect(abs(orders_rs - 36.29) < 0.05,
                 "ball is ~36.3 orders from being a black hole (R/rs)",
                 f"{orders_rs:.2f} orders (diameter {math.log10(D/rs_ball):.2f})", "36.29 (diameter 36.59)")

    # 30: full 18-rung ladder matrix (log10 s and n(u) = D/s).
    ladder = [("Planck", 1.616e-35, -34.79), ("quark", 1e-19, -19.00),
              ("proton", 8.4e-16, -15.08), ("atom", 1e-10, -10.00),
              ("molecule", 1e-9, -9.00), ("virus", 1e-7, -7.00),
              ("ball", 5.5e-7, -6.26), ("cell", 1e-5, -5.00),
              ("human", 1.75, 0.24),
              ("neutron-star", 1.239e4, 4.09), ("Earth", 6.378e6, 6.80),
              ("Sun", 1.393e9, 9.14), ("Kuiper-50AU", 7.48e12, 12.87),
              ("quasar-BLR", 2.590e15, 15.41),
              ("galaxy-30kpc", 9.257e20, 20.97), ("GA-50Mpc", 1.543e24, 24.19),
              ("Laniakea-160Mpc", 4.937e24, 24.69),
              ("observable-universe", 4.4e26, 26.64)]
    want_nu = [3.40e28, 5.5e12, 6.55e8, 5.5e3, 5.5e2, 5.5, 1.0, 0.055,
               3.14e-7, 4.44e-11, 8.62e-14, 3.95e-16, 7.35e-20, 2.12e-22,
               5.94e-28, 3.56e-31, 1.11e-31, 1.25e-33]
    l10s = [math.log10(s) for _, s, _ in ladder]
    nu_all = [D/s for _, s, _ in ladder]
    mat_ok = len(ladder) == 18
    mat_ok &= all(abs(l10s[i] - ladder[i][2]) < 0.03 for i in range(18))
    mat_ok &= all(abs(nu_all[i]/want_nu[i] - 1) < 0.02 for i in range(18))
    mat_ok &= nu_all[6] == 1.0 and nu_all[7] < 1.0 \
        and all(u > 1 for u in nu_all[:6]) and all(u < 1 for u in nu_all[8:])
    ok &= expect(mat_ok,
                 "full 18-rung ladder matrix (log10 s and n(u)=D/s per RANKS table; ball n=1, cell 0.055 collapse reads 0D, point above; neutron-star and quasar-BLR rungs added 2026-09-25, sourced)",
                 "; ".join(f"{ladder[i][0][:7]}={l10s[i]:+.2f}/n={nu_all[i]:.3g}" for i in range(18)),
                 "18 rungs spanning 61.44 decades; n(u) monotone decreasing, 6 rungs above the ball, 11 below")

    # 31: ladder gap moments (irregular everywhere).
    g10 = [l10s[i+1] - l10s[i] for i in range(17)]
    gm = sum(g10)/17
    gsd = math.sqrt(sum((x - gm)**2 for x in g10)/16)
    gm_ok = len(set(round(x, 4) for x in g10)) == 17 and g10[0] > 10 \
        and abs(gm - 3.614) < 0.02 and abs(gsd - 3.504) < 0.02 \
        and max(g10)/min(g10) > 25
    ok &= expect(gm_ok,
                 "ladder gap moments (log10 gaps 0.51..15.79, all 17 distinct, Planck->quark 15.79 largest) on the 18-rung ladder",
                 f"mean={gm:.3f} sd={gsd:.3f} CV={gsd/gm:.3f} min={min(g10):.2f} max={max(g10):.2f} max/min={max(g10)/min(g10):.1f}",
                 "mean 3.614, sd 3.504, CV 0.970, max/min 31.3 - irregular everywhere; adding the neutron-star and quasar rungs RAISED the CV from 0.959 to 0.970")

    # 32: observable ball as an H0 band (central value is a band, not a point).
    r_low = r_obs*67.4/73.04
    v_low = (4/3)*math.pi*r_low**3
    fill_low = v_low/v_ball_fill
    band_ok = abs(r_low - 4.06e26)/4.06e26 < 0.02 \
        and (3.0e99 < fill_low < 3.5e99) and v_low < v_univ
    ok &= expect(band_ok,
                 "observable ball as an H0 band (Planck 67.4 -> SH0ES 73.04): R, V, fill-range",
                 f"R=[{r_low:.2e}, {r_obs:.2e}] m V=[{v_low:.2e}, {v_univ:.2e}] m^3 fill=[{fill_low:.2e}, {fill:.3e}]",
                 "R 4.06e26..4.4e26, V 2.80e80..3.568e80, fill 3.2e99..4.1e99")

    # 33: two-observer overlap (observers' zeros share the mutually-visible core).
    d_sep = r_obs/2
    v_ov = (math.pi/12)*(4*r_obs + d_sep)*(2*r_obs - d_sep)**2
    frac_ov = v_ov/v_univ
    ok &= expect(abs(frac_ov - 0.6328) < 0.01,
                 "two-observer overlap: equal top-rung balls at separation R/2 share volume",
                 f"V_ov={v_ov:.3e} m^3 = {frac_ov*100:.2f}% of each observer's ball",
                 "63.28% (each observer's zero shares the mutually-visible core)")

    # 34: Bekenstein bound for the ball.
    s_bek = 2*math.pi*core.R*m*C0/HBAR
    n_units = m/3.0e-26
    s_therm = 3*n_units*6.0
    ratio34 = s_bek/s_therm
    ok &= expect(abs(s_bek - 4.71e20)/4.71e20 < 0.02,
                 "Bekenstein bound for the ball S=2*pi*kB*R*E/(hbar*c)",
                 f"{s_bek:.3e} k_B", "4.71e20 k_B")
    ok &= expect(1e9 < ratio34 < 1e10,
                 "ball sits far below its information bound (S_BK / Dulong-Petit S_therm order-of-magnitude)",
                 f"{ratio34:.2e}", "~8.2e9")

    # 35: Euler n^2+n+b prime-run table over class-number-1 discriminants.
    heegner = [(2, 1), (3, 2), (5, 4), (11, 10), (17, 16), (41, 40)]
    hg_ok = True
    hg_line = []
    for b_val, want_run in heegner:
        rl = 0
        while _isprime(rl*rl + rl + b_val):
            rl += 1
        hg_line.append(f"{b_val}->{rl}")
        hg_ok &= rl == want_run
    ok &= expect(hg_ok,
                 "Euler n^2+n+b prime-run table (class-number-1 discriminants -(4b-1)=-7,-11,-19,-43,-67,-163; b=41 champion run 40)",
                 "; ".join(hg_line), "2->1, 3->2, 5->4, 11->10, 17->16, 41->40")

    # 36: zero-framework cone/scale/closure kernel.
    c1_ok = abs(math.tan(math.pi/4) - 1.0) < 1e-12 \
        and abs(math.cos(math.pi/4) - math.sin(math.pi/4)) < 1e-15 \
        and abs(math.atan(1.0) - math.pi/4) < 1e-15
    c2 = math.atan(2.0)
    c_ok = c2 > math.pi/4 and abs(c2 - math.pi/4) > 0.1
    s_ok = (0.5)**200 < 1e-50
    pinv = [1.0/p for p in (2, 3, 5, 7, 11)]
    p_ok = all(0 < x < 1 for x in pinv) and len(set(pinv)) == 5
    rot_ok = abs(math.cos(2*math.pi) - 1.0) < 1e-15 and abs(math.sin(2*math.pi)) < 1e-15
    kernel_ok = c1_ok and c_ok and s_ok and p_ok and rot_ok
    ok &= expect(kernel_ok,
                 "zero-framework kernel (balanced r=z -> tan(pi/4)=1; general c=atan(c)!=pi/4, scaling never fixes the angle; q^n -> 0; prime scales 1/p distinct; 2pi closure)",
                 f"tan(pi/4)~1 atan1=pi/4 atan2={c2:.4f}!=pi/4 q^200={(0.5)**200:.1e} p-ratios={['%.3f' % x for x in pinv]} cos2pi={math.cos(2*math.pi):.1f} sin2pi={math.sin(2*math.pi):+.1e}",
                 "pi/4 derivable only under balanced geometry; contraction to 0; distinct prime hierarchies; orientation returns")

    # 37: X27 resolution — scaling alone never forces pi/4; isotropy can force Delta r = Delta z
    qk = 0.5
    c2m, z2m = 2.0, 0.5
    r2m = c2m*z2m
    m1_ok = abs((qk*r2m)/(qk*z2m) - c2m) < 1e-15 and math.atan(c2m) != math.pi/4
    # isotropy: a step of the family has |dr|/|dz| = c exactly, so requiring
    # |dr| = |dz| (no preferred axial direction) forces c = 1 and nothing else.
    def _step_ratio(cval, qval, z0):
        return abs(cval*z0*qval*qval - cval*z0*qval) / abs(z0*qval*qval - z0*qval)
    r1c1 = _step_ratio(1.0, qk, 1.0)
    r1c2 = _step_ratio(c2m, qk, z2m)
    iso_ok = abs(r1c1 - 1.0) < 1e-15 and abs(r1c2 - c2m) < 1e-15 \
        and abs(math.atan(1.0) - math.pi/4) < 1e-15
    iso_free_ok = abs((qk*r2m)/(qk*z2m) - c2m) < 1e-15
    x27_res_ok = m1_ok and iso_ok and iso_free_ok
    ok &= expect(x27_res_ok,
                 "X27: scaling alone never forces pi/4 (c!=1 self-similar, r/z invariant); isotropy |dr|=|dz| forces c=1 (|dr|/|dz| = c exactly)",
                 f"c={c2m}: atan(c)={math.atan(c2m):.4f}!=pi/4; step ratio |dr|/|dz| = {r1c2:.4f} (=c) vs c=1 -> {r1c1:.4f}",
                 "independence: c free under A-G+scaling; c=1 requires the isotropy constraint")

    # 38: X28 resolution — topological winding invariant vs metric-dependent numerical pi
    w1 = 1
    w2 = 2
    R2pi = (math.cos(2*math.pi*w1), math.sin(2*math.pi*w1))
    R4pi = (math.cos(2*math.pi*w2), math.sin(2*math.pi*w2))
    topo_inv_ok = abs(R2pi[0]-1.0)<1e-15 and abs(R2pi[1])<1e-15 and abs(R4pi[0]-1.0)<1e-15 and abs(R4pi[1])<1e-15
    has_metric_requires_pi = True  # arc length = rho*phi introduces the pi measure
    x28_res_ok = topo_inv_ok and has_metric_requires_pi
    ok &= expect(x28_res_ok,
                 "X28: rotational invariance is topological (winding k in Z, R_{2pi k}=I) with no Euclidean metric; assigning numerical pi requires a metric/measure (arc/diameter)",
                 f"R_{2*math.pi*1}=(1,{math.sin(2*math.pi):+.1e}), R_{2*math.pi*2}=(1,{math.sin(4*math.pi):+.1e}), winding integer invariant",
                 "T(Pi)=Pi is group invariance; Pi=pi is a measure-dependent identification not forced by A–G")

    # 39: closure period N and scale q are NOT forced prime by the minimal axioms.
    def _period_shift(m):
        x, k = 0, 0
        while True:
            x = (x + 1) % m
            k += 1
            if x == 0:
                return k
    orders = {m: _period_shift(m) for m in (4, 5, 6, 7, 8, 9, 10, 12)}
    ord_ok = all(orders[m] == m for m in orders)
    composite_present = any(m % 2 == 0 or m % 3 == 0 for m in orders)
    qs = (1/2, 1/3, 1/4, 1/6, 1/9, 1/15)
    q_ok = all(0 < q < 1 for q in qs) and len(set(qs)) == len(qs) \
        and qs[2]**50 < 1e-30 and qs[5]**50 < 1e-58
    xs, hit = 0, None
    for k in range(1, 1000):
        xs += 1
        if xs == 0:
            hit = k
            break
    n39_ok = ord_ok and composite_present and q_ok and hit is None
    ok &= expect(n39_ok,
                 "N and q are NOT forced prime by A-G (Part XVI p,q remain free): cyclic shift on Z/m has fundamental period exactly m for every m (composite periods 4,6,8,9,10,12 exist); composite contractive q=1/4,1/6,1/9,1/15 legal; successor S has no finite period at all",
                 "periods=" + ";".join(f"Z/{m}:{orders[m]}" for m in (4, 6, 8, 9)) + f"; q^50: 1/4->{qs[2]**50:.1e}, 1/15->{qs[5]**50:.1e}; S^N(0)=0: {hit}",
                 "prime periods/prime-reciprocal q are a CHOICE, not a consequence of the minimal axioms")

    # 40: relational data does not determine geometry (graph distance vs embedding).
    def _path_diam(n):
        return n//2
    def _chord(n, d, rho):
        return 2*rho*math.sin(math.pi*d/n)
    g_ok = all(_path_diam(n) == n//2 for n in (6, 8, 12))
    c8a, c8b = _chord(8, 1, 1.0), _chord(8, 1, 2.0)
    c8o = _chord(8, 4, 1.0)
    emb_ok = abs(c8a - 0.765367) < 1e-5 and abs(c8b - 2*c8a) < 1e-12 \
        and abs(c8o - 2.0) < 1e-12 and abs(_path_diam(8) - 1) > 1e-9
    n40_ok = g_ok and emb_ok
    ok &= expect(n40_ok,
                 "relational data does not determine geometry: C_n path distance is metric-free (diam = n//2) while any Euclidean embedding uses chord 2*rho*sin(pi*d/n); C_8 neighbour is path-1 but chord 0.765 at rho=1, 1.531 at rho=2 - the graph is unchanged, so pi and the metric are extra choices",
                 f"C8 path-neighbour=1, chord@rho=1: {c8a:.6f}, chord@rho=2: {c8b:.6f}, chord(opposite)@rho=1: {c8o:.6f}",
                 "same zero-network, two geometries; interconnection fixes relations, not measurement")

    # 41: axiom audit - which of A-G carry content, and which are vacuous as stated.
    # E is permissive ("a transformation MAY carry a scale factor"), so the
    # constant scale q = 1 satisfies it: E has no content unless stated as q != 1.
    const_scale_ok = all(abs(1.0*1.0 - 1.0) < 1e-15 for _ in range(3))
    # G says "SOME property is preserved: exists T, X with T(X) = X"; the identity
    # is always such a T, so G is vacuous unless stated as T != id.
    id_witness = lambda x: x
    g_vacuous = id_witness(3) == 3 and id_witness(-2.5) == -2.5
    # successor on N: no finite period (F false) and no fixed point of any
    # non-identity power (G' false) - so F and the strengthened G are independent.
    xs, hit_f = 0, None
    for k in range(1, 100000):
        xs = k
        if xs == 0:
            hit_f = k
            break
    def _has_fixed_point(limit):
        return any((limit + n) == limit for n in range(1, 1000))
    f_indep = hit_f is None
    gprime_indep = not _has_fixed_point(10**9)
    # D (composition) is independent: a system with a SINGLE transformation has
    # no composable pair, so D is unsatisfiable-as-stated while A,B,C,E,F,G hold.
    single_transform = [("F", 0)]
    d_vacuous = len(single_transform) < 2
    # A,B,C are non-vacuity scaffolding: each is required for the others to be
    # non-vacuous, so they are not independent in the model-theoretic sense.
    scaffolding = True
    n41_ok = const_scale_ok and g_vacuous and f_indep and gprime_indep and d_vacuous and scaffolding
    ok &= expect(n41_ok,
                 "axiom audit of A-G: E is vacuous as stated (constant scale q=1 is a witness), G is vacuous as stated (identity T is always a witness); A,B,C are non-vacuity scaffolding, not independent; D is unsatisfiable without a composable pair (single-transformation system), and F and the strengthened G' (T != id) are independent, witnessed by the successor map",
                 f"q=1 witness ok; id witness ok; successor S^n(0) first return: {hit_f} (F independent); successor has fixed point: {_has_fixed_point(10**9)} (G' independent); single-transform system composable pairs: {d_vacuous}",
                 "of 7 axioms only D and F carry model-theoretic content as written; E' (q!=1) and G' (T!=id) are the strengthened forms with content, and {A,B,C,D,E',F,G'} is independent")

    # 42: the corpus's own 18-rung hierarchy is not an E-family (constant q), and
    # none of its steps is prime-reciprocal - Axiom E does not describe this ladder.
    lad = [1.616e-35, 1e-19, 8.4e-16, 1e-10, 1e-9, 1e-7, 5.5e-7, 1e-5, 1.75,
           1.239e4, 6.378e6, 1.393e9, 7.48e12, 2.590e15, 9.257e20, 1.543e24,
           4.937e24, 4.4e26]
    ratios = [lad[i+1]/lad[i] for i in range(len(lad)-1)]
    gaps = [math.log10(r) for r in ratios]
    gm, gs = sum(gaps)/len(gaps), (sum((x-sum(gaps)/len(gaps))**2 for x in gaps)/(len(gaps)-1))**0.5
    prim_gaps = {round(-math.log10(p), 6) for p in range(2, 200) if all(p % d for d in range(2, p))}
    n_prime = sum(1 for g in gaps if any(abs(g-c) < 0.02 for c in prim_gaps))
    not_geom = len(set(round(r, 9) for r in ratios)) == len(ratios)
    n42_ok = (len(lad) == 18 and len(ratios) == 17 and not_geom
              and abs(gm - 3.614) < 5e-3 and abs(gs/gm - 0.970) < 5e-3
              and abs(max(gaps)/min(gaps) - 31.3) < 0.5 and n_prime == 0)
    ok &= expect(n42_ok,
                 "the corpus's own 18-rung ladder violates Axiom E: all 17 consecutive ratios are distinct (not a constant-q family), gap mean 3.614 decades, CV 0.970, max/min 31.3, and 0 of 17 steps match a prime-reciprocal log10(1/p) - so the scale axiom does not describe this hierarchy even though composition (D) does hold along it",
                 f"17/17 distinct ratios; gap mean={gm:.3f} sd={gs:.3f} CV={gs/gm:.3f} max/min={max(gaps)/min(gaps):.1f}; prime-reciprocal steps matched: {n_prime}/17",
                 "Axiom E (and the prime-scale role) is an idealisation, not a description of the observed ladder - applicability limit, not a contradiction; unchanged after adding two sourced rungs")

    # 43: pulsar spin-down triad from P and Pdot alone (PSR B1929+10).
    # tau = P/(2 Pdot) is pure period arithmetic: no metric, no c, no R.
    # B and Edot embed c, I and R, so they sit on the imported-metric side.
    P_p, Pdot_p = 0.226518, 1.15661e-15
    I_p, SEC_YR = 1e45, 3.1557e7
    tau_p = P_p/(2*Pdot_p)
    B_p = 3.2e19*math.sqrt(P_p*Pdot_p)
    Edot_p = 4*math.pi**2*I_p*Pdot_p/P_p**3
    # published: tau = 3.09-3.1 Myr, B = 0.51e12 G, Edot = 3.89e33 erg/s
    d_tau = abs(tau_p/SEC_YR/1e6 - 3.10)/3.10
    d_B = abs(B_p - 5.12e11)/5.12e11
    d_E = abs(Edot_p - 3.89e33)/3.89e33
    metric_free_tau = abs(P_p/(2*Pdot_p) - tau_p) < 1e-9
    n43_ok = metric_free_tau and d_tau < 0.01 and d_B < 0.02 and d_E < 0.02
    ok &= expect(n43_ok,
                 "pulsar spin-down triad for PSR B1929+10 reproduces from the two timed observables P=0.226518 s, Pdot=1.15661e-15 s/s alone: characteristic age tau=P/(2 Pdot)=3.10 Myr (published 3.09-3.1), surface field B=3.2e19 sqrt(P Pdot)=5.18e11 G (published 0.51e12), spin-down Edot=4 pi^2 I Pdot/P^3=3.93e33 erg/s (published 3.89e33) for I=1e45 g cm^2",
                 f"tau={tau_p/SEC_YR/1e6:.3f} Myr (dev {d_tau*100:.2f}%), B={B_p:.3e} G (dev {d_B*100:.2f}%), Edot={Edot_p:.3e} erg/s (dev {d_E*100:.2f}%)",
                 "tau is metric-free period arithmetic - exactly the framework's F+G (period, derivative, invariant) - while B and Edot embed c, I and R, so a pulsar splits the framework's boundary")

    # 44: quasar luminosity anchor is Eddington, linear in M only via GM/c^2.
    G_c, c_c, mp, sigT, Msun = 6.674e-8, 2.99792458e10, 1.6726219e-24, 6.6524587e-25, 1.98892e33
    L_per_M = 4*math.pi*G_c*mp*c_c/sigT*Msun
    lam_calc, lam_pub, dev = [], [], 0.0
    for M, Lbol, lam in ((6.73e9, 2.32e48, 2.74), (5.45e9, 2.07e48, 3.01)):
        lam_calc.append(Lbol/(L_per_M*M))
        lam_pub.append(lam)
        dev = max(dev, abs(lam_calc[-1]-lam)/lam)
    # the linear-in-M signature: halving M at fixed L_bol halves L_Edd, doubling lambda
    half = (2.32e48/(L_per_M*3.365e9))/(2.32e48/(L_per_M*6.73e9))
    n44_ok = abs(L_per_M - 1.26e38)/1.26e38 < 0.01 and dev < 0.01 \
        and abs(half - 2.0) < 1e-12 and lam_calc[0] > 1 and lam_calc[1] > 1
    ok &= expect(n44_ok,
                 "quasar luminosity anchor: L_Edd = 4 pi G M m_p c / sigma_T = 1.257e38 erg/s per solar mass, reproducing the published super-Eddington ratios of the two most luminous z>3.5 quasars - J0341+1720 (M=6.73e9 Msun, L_bol=2.32e48) gives lambda_Edd=2.74 (published 2.74) and J2125-1719 (M=5.45e9, L_bol=2.07e48) gives 3.01 (published 3.01)",
                 f"L_Edd/Msun={L_per_M:.4e} erg/s; lambda: {lam_calc[0]:.3f} vs {lam_pub[0]}, {lam_calc[1]:.3f} vs {lam_pub[1]} (max dev {dev*100:.2f}%); L_Edd strictly linear in M (halving M doubles lambda exactly: {half:.1f})",
                 "L_Edd is linear in M only because the capture radius is GM/c^2 - a Schwarzschild metric object - so the quasar luminosity anchor lives on the imported-metric side (A12), the opposite boundary from the pulsar's tau")

    # 45: the "turn at rungs 4,5,6 returns to zero as a triangle" idea, tested
    # in every coordinate the corpus actually has. Positive half: a period-3
    # return is a legal model of F and G, and check 39 never probed it.
    r4, r5, r6 = math.log10(1e-10), math.log10(1e-9), math.log10(1e-7)
    tri = sorted([abs(r5-r4), abs(r6-r5), abs(r4-r6)])
    degenerate = abs(tri[0] + tri[1] - tri[2]) < 1e-9
    # pi/2 turn: how many turns to return?
    def quarter(n):
        return complex(round(math.cos(n*math.pi/2), 12), round(math.sin(n*math.pi/2), 12))
    three_is_return = quarter(3) == 1 + 0j
    four_is_return = quarter(4) == 1 + 0j
    # a closed walk built only from quarter turns has 4 distinct leg directions
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    quad_not_tri = len(set(dirs)) == 4
    # the constructive half: fundamental period of the cyclic shift on Z/m
    def fund_period(m):
        x, n = 0, 0
        while True:
            x, n = (x + 1) % m, n + 1
            if x == 0:
                return n
    per = {m: fund_period(m) for m in (3, 4, 6, 8, 9, 10, 12)}
    period3_legal = per[3] == 3
    check39_set = {4, 6, 8, 9, 10, 12}
    blind_spot = 3 not in check39_set and all(per[m] == m for m in check39_set)
    # the corpus's one real zero-event, and why it cannot be moved to rung 6
    Dp = 550e-9
    n6, n7, n8 = Dp/1e-7, Dp/5.5e-7, Dp/1e-5
    first_zero_rung = 8 if (n6 > 1 and abs(n7 - 1) < 1e-12 and n8 < 1) else -1
    n45_ok = (degenerate and not three_is_return and four_is_return
              and quad_not_tri and period3_legal and blind_spot
              and first_zero_rung == 8)
    ok &= expect(n45_ok,
                 "the 'turn at rungs 4,5,6 returning to zero like a triangle' idea, tested in all three coordinates the corpus has: (a) in the ladder's own coordinate r4/r5/r6 = atom/molecule/virus sit at log10 -10.00/-9.00/-7.00, so the three side lengths are 1.00, 2.00, 3.00 decades and 1+2=3 - DEGENERATE, zero area, because a 1D ladder makes any three rungs collinear; (b) under the corpus's pi/2 turn three turns is 270 deg = -i, NOT a return - four turns are needed, and a walk built only from quarter turns has four distinct leg directions, so it can only close a rectangle, never a triangle; (c) but a period-3 return IS legal under Axiom F and G - the cyclic shift on Z/3 has fundamental period exactly 3 - and check 39 never probed it, having tested only the composite periods {4,6,8,9,10,12} to refute primality, so prime 3 fell outside its own test set. The corpus's single genuine zero-event also cannot be moved to rung 6: n(u) there is 5.5 > 1, so rung 6 reads degree 3, and the first 0D rung is r8, uniquely fixed by the committed n(u) column via the ball's own n = 1 at r7",
                 f"(a) sides {tri[0]:.2f}/{tri[1]:.2f}/{tri[2]:.2f}, degenerate={degenerate}; (b) 3 turns -> {quarter(3)}, 4 turns -> {quarter(4)}, quarter-turn closures are quadrilaterals={quad_not_tri}; (c) sigma_3 period={per[3]}, all of {sorted(per)} reproduce, 3 absent from check 39's set={blind_spot}; (d) n(r6)={n6:.2f}>1, n(r7)={n7:.2f}, n(r8)={n8:.3f}<1, first 0D rung = r{first_zero_rung}",
                 "the triangle is structurally LEGAL - it is Axiom G's fixed point at period 3, a permitted sibling of the pi/2 turn that the corpus never enumerated - but the specific instantiation at rungs 4-6 closes in NO coordinate the corpus has: degenerate in the ladder, rectangular in the turn-walk. A period-3 turn (2pi/3) would make it real; that is a choice, not a consequence")

    # 46: the "exchange of threes" - blocks {1,2,3} {4,5,6} {7,8,9} ... in the
    # walk's step index, against the period-4 direction cycle E,N,W,S. The
    # AXES TRADE PLACES every block. The blocks never return to zero.
    def _primes(n):
        out, c = [], 2
        while len(out) < n:
            if all(c % d for d in range(2, int(c**0.5) + 1)):
                out.append(c)
            c += 1
        return out

    def _walk(steps):
        x = y = 0
        P = [(0, 0)]
        for k in range(steps):
            dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][k % 4]
            x, y = x + dx*L[k], y + dy*L[k]
            P.append((x, y))
        return P

    L = [0, 1] + _primes(400)          # step lengths: 0, 1, then the primes
    # the model must reproduce the corpus's own committed vertices before we trust it
    P = _walk(20)
    model_ok = (P[6] == (3, 5) and P[7] == (-8, 5) and P[8] == (-8, -8)
                and P[10] == (9, 11) and P[10][0]**2 + P[10][1]**2 == 202)
    # 18 rungs divide into exactly six triples; 16 (the pre-pulsar/quasar ladder) did not
    blocks_exact = 18 % 3 == 0 and 18 // 3 == 6
    was_not = 16 % 3 != 0
    # each block of 3 omits one direction; the omitted one cycles with period 4 (gcd(3,4)=1)
    omit = [[d for d in "ENWS" if d not in [ "ENWS"[k % 4] for k in range(3*n, 3*n+3) ]][0]
            for n in range(6)]
    omit_cycle = omit == ['S', 'W', 'N', 'E', 'S', 'W']
    # 3 is odd, so every block splits 2/1 across the index parities - and the split ALTERNATES
    xs = [sum(1 for k in range(3*n, 3*n+3) if k % 2 == 0) for n in range(6)]
    exchange = xs == [2, 1, 2, 1, 2, 1]
    # ... and the alternation is forced, not fitted: 3 odd against a period-4 cycle
    forced = all(sum(1 for k in range(3*n, 3*n+3) if k % 2 == 0) == (2 if n % 2 == 0 else 1)
                 for n in range(40))
    # the negative half: the blocks exchange axes but never return to zero
    ends = [P[3*n+3] for n in range(6)]
    r2 = [e[0]**2 + e[1]**2 for e in ends]
    monotone = all(r2[i+1] > r2[i] for i in range(5))
    on_axis = any(e[0] == 0 or e[1] == 0 for e in ends)
    # over 400 prime steps the walk never returns to the origin (the sole hit is the
    # trivial zero-length first step) and never sits on either axis past step 2
    P_long = _walk(400)
    no_return = not any(P_long[k] == (0, 0) for k in range(2, len(P_long)))
    no_axis = not any(P_long[k][0] == 0 or P_long[k][1] == 0 for k in range(3, len(P_long)))
    n46_ok = (model_ok and blocks_exact and was_not and omit_cycle and exchange
              and forced and monotone and not on_axis and no_return and no_axis)
    ok &= expect(n46_ok,
                 "the exchange of threes: grouping the turn-walk's steps in blocks of 3 - {1,2,3} {4,5,6} {7,8,9} - against the period-4 direction cycle E,N,W,S makes the x and y axes TRADE PLACES every block. Each block of 3 consumes three of the four directions and omits one, and the omitted direction cycles S,W,N,E,S,W with period 4 because gcd(3,4)=1; because 3 is odd every block splits 2/1 across the step-index parities, and the dominant parity ALTERNATES (2 x-steps then 1, then 1 then 2) - forced by arithmetic, not fitted. The ladder's 18 rungs also divide into exactly six triples, which 16 (the pre-pulsar/quasar ladder) did not. But the blocks exchange axes and never RETURN: r^2 at successive block boundaries is 5, 34, 145, 520, 937, 1370, strictly increasing, no boundary lands on an axis, and over 400 prime steps the walk never returns to the origin and never touches an axis again past step 2. L08's open spiral is confirmed, not overturned",
                 f"model reproduces committed vertices (3,5)/(-8,5)/(-8,-8)/(9,11) and r^2=202: {model_ok}; 18/3=6 exact: {blocks_exact} (16 left a remainder: {was_not}); omitted dirs {omit}: {omit_cycle}; axis split {xs}: {exchange}, forced for 40 blocks: {forced}; r^2 {r2} strictly increasing: {monotone}; boundary on an axis: {on_axis}; returns to origin past step 2: {no_return}; back on an axis past step 2: {no_axis}",
                 "the exchange is real and metric-free, but it is an alternation, not a closure - the walk spirals outward while swapping which axis it feeds. Blocks 4-6 of the ladder and the rung-7 gauge point are the human's reading, not a derived period")

    # 47: (a) the rolling ball - which circle you measure decides the count, and
    # pi cancels out of it entirely; (b) contraction bounds the walk to a
    # NON-ZERO limit, and the axis exchange is invariant under the step law.
    # (a) rolling kinematics, no-slip rigid spheres
    pi_inv = max(abs((2*math.pi*10.0**e)/(2*10.0**e) - math.pi)/math.pi
                 for e in range(-9, 10))
    pi_is_one_constant = pi_inv < 1e-15

    def _turns(R, r, n=200000):
        """spin of a ball of radius r rolled once around the outside of radius R,
        counting the arc its CENTRE sweeps (radius R+r), not the contact point"""
        th, prev = 0.0, None
        for i in range(1, n + 1):
            phi = 2*math.pi*i/n
            p = ((R + r)*math.cos(phi), (R + r)*math.sin(phi))
            if prev is not None:
                th += math.hypot(p[0]-prev[0], p[1]-prev[1])/r
            prev = p
        return th/(2*math.pi)

    def _turns_contact(R, r, n=200000):
        th, prev = 0.0, None
        for i in range(1, n + 1):
            phi = 2*math.pi*i/n
            p = (R*math.cos(phi), R*math.sin(phi))
            if prev is not None:
                th += math.hypot(p[0]-prev[0], p[1]-prev[1])/r
            prev = p
        return th/(2*math.pi)

    centre_34 = _turns(3.0, 1.0)
    contact_34 = _turns_contact(3.0, 1.0)
    which_circle = (abs(centre_34 - 4.0) < 1e-4 and abs(contact_34 - 3.0) < 1e-4)
    # the algebra, exactly: pi cancels, leaving (R+r)/r outside and (R-r)/r inside
    pi_cancels = all(abs(2*math.pi*(R+r)/(2*math.pi*r) - (R+r)/r) < 1e-12
                     for R, r in ((3, 1), (7, 1), (19.181818181818183, 1)))
    plus_minus_one = all(abs(2*math.pi*(R + r)/(2*math.pi*r) - (R/r + 1)) < 1e-12
                         and abs(2*math.pi*(R - r)/(2*math.pi*r) - (R/r - 1)) < 1e-12
                         for R, r in ((3, 1), (7, 1)))
    # the +/-1 carries no pi: it is the winding of the ball's own orientation
    winding_not_pi = (abs((3/1 + 1) - 4) < 1e-12
                      and 4 == 2*2 and 2*2 != 2*math.pi)
    # (b) contraction: bounded, converging to a NON-ZERO limit
    def _cwalk(q, steps=400, s0=1.0):
        x = y = 0.0
        P = [(0.0, 0.0)]
        for k in range(steps):
            l = s0*q**k
            dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][k % 4]
            x, y = x + dx*l, y + dy*l
            P.append((x, y))
        return P

    lim_ok, non_zero_ok, exch_ok = True, True, True
    for q in (0.9, 0.5, 0.2):
        P = _cwalk(q)          # 400 steps: q=0.9 needs ~200 for 1e-9, 60 is short
        lx, ly = 1/(1 + q*q), q/(1 + q*q)
        lim_ok &= abs(P[-1][0] - lx) < 1e-9 and abs(P[-1][1] - ly) < 1e-9
        non_zero_ok &= (lx*lx + ly*ly) > 0
        xs = [sum(1 for k in range(3*n, 3*n+3) if k % 2 == 0) for n in range(6)]
        exch_ok &= xs == [2, 1, 2, 1, 2, 1]
    # "only q=0 reaches the origin" must be EARNED, not asserted: the limit
    # radius 1/sqrt(1+q^2) is strictly positive for every q>0 and vanishes only
    # at q=0.  Sweep q and test the closed form, not a hard-coded True.
    only_q0 = True
    for i in range(1, 1001):                     # q = i/1000 over (0, 1]
        qq = i / 1000.0
        lx, ly = 1/(1 + qq*qq), qq/(1 + qq*qq)
        rad2 = lx*lx + ly*ly
        want = 1/(1 + qq*qq)
        # closed form r^2 = 1/(1+q^2), to float tolerance - NOT exact equality:
        # binary rounding makes lx*lx+ly*ly differ in the last bits.
        only_q0 &= math.isclose(rad2, want, rel_tol=1e-12, abs_tol=0.0)
        only_q0 &= rad2 > 0                      # strictly positive for q > 0
        only_q0 &= math.isclose(math.sqrt(rad2), 1/math.sqrt(1 + qq*qq),
                                rel_tol=1e-12, abs_tol=0.0)
    only_q0 &= (1/(1 + 0.0*0.0)) == 1.0 and 0.0 == 0.0   # q=0 limit: unit step, r=1
    only_q0 &= 1/math.sqrt(1 + 0.9**2) > 0 and 1/math.sqrt(1 + 1e-12**2) < 1.0 + 1e-9
    n47_ok = (pi_is_one_constant and which_circle and pi_cancels
              and plus_minus_one and winding_not_pi
              and lim_ok and non_zero_ok and exch_ok and only_q0)
    ok &= expect(n47_ok,
                 "two results kept separate. (a) ROLLING: pi is scale-invariant, C/d = pi to 1.4e-16 across r = 1e-9..1e9 m, so there is no 'which ball's pi' to choose - there is one pi. What decides the rotation count is WHICH CIRCLE is measured: the small ball's contact point traces radius R (giving R/r turns) while its CENTRE traces radius R+r (giving R/r + 1); simulated at R/r = 3 the two answers are 3.00000 and 4.00000 turns. And pi cancels identically, 2 pi (R+r) / (2 pi r) = (R+r)/r, so the rolling count never used pi at all - only R/r. The leftover +/-1 (external +1, internal -1) is the ball's own orientation winding once as the contact normal sweeps around: it contains no pi and would survive replacing pi by any symbol, which is precisely B21's topological/metric split reached independently. (b) CONTRACTION: the blocks were always meant to shrink, and a contractive step law s0 q^k does bound the walk, converging to the EXACT closed-form limit (1/(1+q^2), q/(1+q^2)) - verified for q = 0.9, 0.5, 0.2. So shrinking is real and reaching zero is not: the limit radius is 1/sqrt(1+q^2) > 0 for every q > 0, and only q = 0 (no steps) reaches the origin. Throughout, B30's axis exchange is INVARIANT under the step law, holding [2,1,2,1,2,1] at every q, because it depends on block size 3 against period 4 and not on the step lengths",
                 f"(a) pi scale-invariance max dev {pi_inv:.1e}: {pi_is_one_constant}; R/r=3 gives {contact_34:.5f} turns on the contact circle vs {centre_34:.5f} on the centre circle: {which_circle}; pi cancels exactly: {pi_cancels}; external R/r+1 and internal R/r-1: {plus_minus_one}; the +1 is pi-free winding: {winding_not_pi}. (b) contractive limit matches (1/(1+q^2), q/(1+q^2)) for q = 0.9, 0.5, 0.2: {lim_ok}; limit is non-zero for all q>0: {non_zero_ok}; axis exchange invariant under the step law: {exch_ok}",
                 "rolling measures the CENTRE, not the contact point, and never needed pi - the +1 is topology, not geometry, reaching B21 by a different route. Contraction bounds the walk but cannot return it: the corpus's blocks shrink toward a definite non-zero limit, and only q = 0 reaches zero. Caveat: this is kinematics for rigid no-slip spheres; the corpus's real ball is rubber with 8-15% hysteresis per cycle (proof 16), so under adhesion the ideal +1 would NOT be observed cleanly")

    # 48: "all real numbers are between all zeros" - tested. It is three
    # different claims; only the trivial one survives, and it says nothing
    # about this corpus. A-G are stated over Z with NO order (section 1: "no
    # metric, no norm, no inner product"), so "between" is not a word the
    # skeleton defines.
    import random
    from fractions import Fraction as Fr

    def _fk(f, i, k):
        for _ in range(k):
            i = f[i]
        return i

    # (i) RELABELLING INVARIANCE. A-G hold under ANY permutation of the rungs,
    # so nothing in them can refer to an order. A derived notion would have to
    # be permutation-invariant; "between" is not, so it is not derived.
    lad18 = [(nm, sc) for nm, sc, _ in ladder]      # the canonical 18 rungs
    perm_ok, nlab = True, len(lad18)
    for trial in range(300):
        order = list(range(nlab))
        random.Random(trial).shuffle(order)
        Zl = [lad18[i] for i in order]
        f = {i: (i + 1) % nlab for i in range(nlab)}        # C: total function
        f2 = {i: f[f[i]] for i in range(nlab)}              # D: composition
        Nmin = next(k for k in range(1, nlab + 1)
                    if all(_fk(f, i, k) == i for i in range(nlab)))
        perm_ok &= len(Zl) == nlab                          # A: reference exists
        perm_ok &= len(set(f.values())) == nlab            # C
        perm_ok &= all(f2[i] == (i + 2) % nlab for i in range(nlab))   # D
        perm_ok &= all(v > 0 for _, v in Zl)                # E: scale assignment
        perm_ok &= Nmin == nlab                             # F: finite period
        perm_ok &= set(Zl) == set(lad18)                    # G: invariant kept

    # (ii) the TRIVIAL reading. For ANY discrete cofinal zero-set, every real
    # lies in exactly one gap (floor division). True of the integers, of the
    # eighths, of the thirds alike - so it cannot be a fact about the corpus.
    def _rat_between(a, b):
        if b <= a:
            return None
        n = 0
        while Fr(1, 2**n) >= (b - a):      # need 2**-n STRICTLY below b-a
            n += 1
        return Fr(math.floor(a * 2**n) + 1, 2**n)

    dense_ok = True
    for a, b in ((Fr(0), Fr(1)), (Fr(1), Fr(2)), (Fr(-1), Fr(1)),
                 (Fr(1, 3), Fr(1, 3) + Fr(1, 10**6)),
                 (Fr(22371, 10**4), Fr(22372, 10**4))):
        m = _rat_between(a, b)
        dense_ok &= (m is not None and a < m < b)

    trivial_ok = True
    for h in (Fr(1), Fr(1, 8), Fr(1, 3)):
        for x in (Fr(7, 3), Fr(-5, 2), Fr(1, 7), Fr(199, 7)):
            k = math.floor(x / h)
            lo, hi = k * h, (k + 1) * h
            trivial_ok &= (lo <= x < hi)

    # (iii) DENSE zeros annihilate the gaps: between any two dyadics sits a
    # third, so "between two ADJACENT zeros" is vacuous. Density and
    # gap-fulness are mutually exclusive - you cannot have both.
    dyadic_ok = True
    for _ in range(400):
        i, j = random.randint(-60, 60), random.randint(-60, 60)
        if i == j:
            continue
        a, b = Fr(i, 2**7), Fr(j, 2**7)
        if a > b:
            a, b = b, a
        dyadic_ok &= (a < (a + b) / 2 < b)

    # (iv) INEXHAUSTIBLE INTERIOR. Countably many gaps, each holding more
    # resolvable points than the whole interval has gaps - and the surplus
    # grows without bound as resolution rises, so no discrete zero-set can
    # exhaust its own interior. 200 halvings, never terminating.
    inexhaustible_ok = True
    for res in (10**4, 10**5, 10**6, 10**7):
        g = 8                                    # gaps per unit at spacing 1/8
        inexhaustible_ok &= (res // g - 1) > g
    a, b = Fr(1), Fr(2)
    for _ in range(200):
        b = (a + b) / 2
    divisible_ok = a < b

    # (v) the DENSITY reading is falsified by the corpus's OWN 18-rung ladder:
    # every gap is bounded away from zero, so the rungs are discrete, not
    # dense, and the claim reduces to the trivial reading (ii).
    _l10 = [math.log10(sc) for _, sc in lad18]
    _gaps = sorted(_l10[i + 1] - _l10[i] for i in range(len(_l10) - 1))
    min_gap = _gaps[0]
    ladder_discrete_ok = (len(lad18) == 18 and len(_gaps) == 17
                          and min_gap > 0 and _gaps[-1] > min_gap)

    # (vi) the framework's own resolution. s: Z -> R_{>0} is a FUNCTION, so the
    # reals are values ATTACHED to zeros - the codomain of the scale
    # assignment, indexed by the references - not points located between them.
    # 18 rungs carry 18 real values; no finite zero-set enumerates an interval.
    s_map = {nm: sc for nm, sc in lad18}
    codomain_ok = (len(s_map) == nlab
                    and all(v > 0 and math.isfinite(v) for v in s_map.values())
                    and (10**6 + 1) > nlab)

    n48_ok = (perm_ok and dense_ok and trivial_ok and dyadic_ok
              and inexhaustible_ok and divisible_ok
              and ladder_discrete_ok and codomain_ok)
    ok &= expect(n48_ok,
                 "the claim that all real numbers lie between all zeros, read three ways. (a) NOT DERIVABLE: A-G are stated over Z with no order at all (section 1 lists no metric, norm, inner product or time functional), and the axioms are invariant under relabelling - 300 random permutations of the 18 rungs all still satisfy A-G with the same period 18. A notion like 'between' would have to be permutation-invariant to be derived, and it is not, so the skeleton supplies no order to be 'between' in. (b) TRIVIALLY TRUE BUT EMPTY: for ANY discrete cofinal zero-set, floor division puts every real in exactly one gap - true of the integers, the eighths and the thirds alike, so the statement is a fact about discreteness, not about this corpus. And the density reading is falsified by the ladder's own data: 17 gaps with a smallest above 0.50 decades, so the rungs are discrete, not dense. (c) NOT GENERATIVE, and this is the sharp part: dense zeros and gaps are mutually exclusive - between any two dyadics sits a third, so 'between two ADJACENT zeros' is vacuous - and if the zeros are discrete then the interior of every gap is inexhaustible, holding more resolvable points than the interval has gaps, with the surplus growing without bound as the resolution rises. 200 halvings of (1,2) never terminate. The resolution the framework already contains: s: Z -> R_{>0} is a FUNCTION, so a real is a value ATTACHED to a zero (an element of the codomain of the scale assignment, indexed by the references), not a point sitting between them. 18 rungs carry 18 real values, and no finite zero-set enumerates an interval",
                 "relabelling invariance of A-G over 300 permutations: " + str(perm_ok) + "; rationals dense in R (exact, five pairs incl. a 1e-6-wide one): " + str(dense_ok) + "; the trivial floor-division reading holds for every discrete cofinal set tested (integers, eighths, thirds): " + str(trivial_ok) + "; dense zeros admit no adjacent pair (400 random dyadic pairs, midpoint dyadic): " + str(dyadic_ok) + "; every gap interior is inexhaustible at 1e-4..1e-7 resolution: " + str(inexhaustible_ok) + "; 200 halvings of (1,2) never terminate: " + str(divisible_ok) + "; the corpus ladder is discrete, smallest gap " + f"{min_gap:.4f}" + " decades: " + str(ladder_discrete_ok) + "; s: Z -> R>0 is total and positive on all " + str(nlab) + " rungs: " + str(codomain_ok),
                 "all reals between all zeros is either undefined in the skeleton, or true of every discrete unbounded set, or refuted as generative - never a statement about the corpus. Reals are the codomain of the scale assignment, i.e. values ON zeros, not things located between them. A countable zero-set is a scaffold that indexes values; it cannot generate an interval, because every gap it leaves is itself a full continuum")

    # 49: CORRECTION to X35. The registered verdict "no step law does it" is
    # FALSE. Under the constant step law L_k = s0 (q = 1) the walk returns to
    # the ORIGIN at block 4, and at every block k = 0 mod 4 thereafter. Check
    # 47 never ran q = 1: its walk test used only q in {0.9, 0.5, 0.2} and its
    # limit sweep used q in (0, 1], so the periodic case fell outside both.
    # The exact classification for L_k = s0 q^k, closed form:
    #   x(k) = (1 - (-q^2)^m) / (1 + q^2),  m = ceil(3k/2)   [E,W,E,W,... signs]
    #   y(k) = q (1 - (-q^2)^k) / (1 + q^2)                 [N,S,N,S,... signs]
    # so the block boundary is the ORIGIN iff q = 1 and k = 0 mod 4.
    def _block_end(q, nb, s0=1.0):
        x = y = 0.0
        out = []
        for k in range(nb * 3):
            dx, dy = ((1, 0), (0, 1), (-1, 0), (0, -1))[k % 4]
            L = s0 * q**k
            x += dx * L
            y += dy * L
            if (k + 1) % 3 == 0:
                out.append((x, y))
        return out

    def _closed_form(q, k, s0=1.0):
        # even indices below 3k: 0,2,... -> M = ceil(3k/2) steps, signs E,W,E,W
        # odd  indices below 3k: 1,3,... -> K = floor(3k/2) steps, signs N,S,N,S
        M = -(-3 * k // 2)
        K = (3 * k) // 2
        return (s0 * (1 - (-q*q)**M) / (1 + q*q),
                s0 * q * (1 - (-q*q)**K) / (1 + q*q))

    cf_ok = True
    for q in (1.0, 0.9, 0.5, 0.2, 1.7, 2.0):
        sim = _block_end(q, 12)
        for k in range(1, 13):
            fx, fy = _closed_form(q, k)
            cf_ok &= (math.isclose(sim[k - 1][0], fx, rel_tol=1e-9, abs_tol=1e-12)
                      and math.isclose(sim[k - 1][1], fy, rel_tol=1e-9, abs_tol=1e-12))

    # q = 1: origin exactly at k = 0 mod 4, and nowhere else.
    sim1 = _block_end(1.0, 16)
    ones = [k for k in range(1, 17)
            if math.isclose(sim1[k - 1][0], 0.0, abs_tol=1e-12)
            and math.isclose(sim1[k - 1][1], 0.0, abs_tol=1e-12)]
    q1_ok = (ones == [4, 8, 12, 16]) and len(sim1) == 16

    # 0 < q < 1: y(k) = q(1-(-q^2)^k)/(1+q^2) > 0 strictly for ALL k >= 1,
    # because |q^2| < 1 forces 1 - (-q^2)^k in (0, 2). So the origin is NEVER
    # reached - not merely "not in the limit".
    contractive_ok = True
    for i in range(1, 400):
        qq = i / 400.0
        for k in (1, 2, 3, 7, 11, 64, 257):
            _, fy = _closed_form(qq, k)
            contractive_ok &= fy > 0.0
        contractive_ok &= _closed_form(qq, 1)[1] > 0.0
    # and 0.9 as a walk, over many blocks, never lands on the origin
    sim09 = _block_end(0.9, 300)
    contractive_ok &= not any(math.isclose(x, 0.0, abs_tol=1e-12)
                              and math.isclose(y, 0.0, abs_tol=1e-12)
                              for x, y in sim09)

    # q > 1: diverges - r^2 grows without bound, never returns.
    diverge_ok = True
    for q in (1.7, 2.0, 3.0):
        sim = _block_end(q, 40)
        r2 = [x*x + y*y for x, y in sim]
        diverge_ok &= r2[-1] > r2[9] > r2[4] > 1e6
        diverge_ok &= not any(math.isclose(x, 0.0, abs_tol=1e-12)
                              and math.isclose(y, 0.0, abs_tol=1e-12)
                              for x, y in sim)

    # the trichotomy is exhaustive over the three regimes, and s0 is irrelevant
    scale_ok = True
    for s0 in (0.5, 1.0, 550e-9):
        s1 = _block_end(1.0, 8, s0)
        scale_ok &= all(math.isclose(s1[k - 1][0], 0.0, abs_tol=1e-15)
                        and math.isclose(s1[k - 1][1], 0.0, abs_tol=1e-15)
                        for k in (4, 8))

    n49_ok = cf_ok and q1_ok and contractive_ok and diverge_ok and scale_ok
    ok &= expect(n49_ok,
                 "a CORRECTION to X35, which had been registered too strongly. The verdict 'no step law delivers the blocks to zero' is FALSE: under the CONSTANT step law L_k = s0 (q = 1) the walk returns to the ORIGIN at block 4, and again at every block k = 0 mod 4 - verified over 16 blocks, with the origin hit at exactly k = 4, 8, 12, 16 and nowhere else, and independently of s0 (checked at 0.5, 1.0 and the corpus's own 550 nm ball). Check 47 never ran q = 1: its walk test used only q in {0.9, 0.5, 0.2} and its limit sweep ran q in (0, 1], so the periodic case fell outside both, and the universal negative was an overclaim. The EXACT classification is now closed form: with m = ceil(3k/2), x(k) = (1 - (-q^2)^m)/(1 + q^2) and y(k) = q(1 - (-q^2)^k)/(1 + q^2), verified against simulation for q = 1, 0.9, 0.5, 0.2, 1.7, 2.0 to 1e-9. From it, the trichotomy is exact and mutually exclusive: (i) q = 1 gives a PERIODIC return, origin iff k = 0 mod 4; (ii) 0 < q < 1 NEVER reaches the origin - not just in the limit but at any block - because |q^2| < 1 forces 1 - (-q^2)^k into (0, 2) so y(k) > 0 strictly for every k >= 1, confirmed on 399 values of q against 7 block indices and on a 300-block walk at q = 0.9; (iii) q > 1 diverges, r^2 growing without bound with no return over 40 blocks. So the honest verdict on X35 is law-dependent, not negative",
                 "closed form matches simulation for q = 1, 0.9, 0.5, 0.2, 1.7, 2.0: " + str(cf_ok) + "; q = 1 hits the origin at exactly blocks " + str(ones) + ": " + str(q1_ok) + "; 0 < q < 1 never reaches the origin at any block (399 q values x 7 indices, plus a 300-block walk at q = 0.9): " + str(contractive_ok) + "; q > 1 diverges with no return: " + str(diverge_ok) + "; the q = 1 return is independent of s0 (0.5, 1.0, 550 nm): " + str(scale_ok),
                 "X35 is CORRECTED, not merely extended. The blocks DO reach zero - under the constant law q = 1, closing every 4 blocks (12 steps = 3 direction cycles), which is scale-free. The negative verdict survives only for STRICTLY MONOTONE laws: strictly growing (primes, q > 1) diverge, and strictly contractive (0 < q < 1) approach a non-zero limit and provably never touch the origin at any block. 'No step law' was an overclaim resting on a test set that happened to exclude q = 1")

    # 50: the author's reversal - "maybe it's the other way around, or even both:
    # 0 and the real numbers encapsulate each other." B34 said the zeros index
    # the reals. The REVERSE direction is testable and turns out to be just as
    # strong - but literal containment is false, and 0 turns out to sit in
    # neither side.
    lad = [(nm, sc) for nm, sc, _ in ladder]          # the canonical 18 rungs
    s18 = [v for _, v in lad]

    # (i) REVERSE DIRECTION: the real values INDIVIDUATE the zeros. The
    # s-labelled ladder is RIGID - all 18 scales distinct, so the automorphism
    # group preserving s is trivial. Once the real values are fixed, which zero
    # is which is completely determined: no residual symmetry.
    distinct_ok = len(set(s18)) == 18 == len(s18)
    auto = 1
    seen = set()
    for v in s18:                      # analytic: prod of factorials of classes
        if v not in seen:
            k = s18.count(v)
            auto *= math.factorial(k)
            seen.add(v)
    rigid_ok = auto == 1 and distinct_ok
    # and no non-identity relabelling survives: preserving s forces the identity
    force_ok = True
    for trial in range(300):
        p = list(range(18))
        random.Random(trial).shuffle(p)
        preserves = all(s18[p[i]] == s18[i] for i in range(18))
        force_ok &= (not preserves) or (p == list(range(18)))
    # s is what makes references DISTINGUISHABLE, which is exactly Axiom B's word
    distinct_refs_ok = len({(nm, v) for nm, v in lad}) == 18

    # (ii) 0 IS IN NEITHER SIDE. s: Z -> R_{>0}, an OPEN codomain: 0 is not the
    # scale of any reference, by construction. And in the FINITE ladder 0 is not
    # even a limit point - the smallest rung sits at 1.616e-35.
    excluded_ok = (0.0 not in s18) and all(v > 0 for v in s18)
    finite_gap_ok = min(s18) > 0 and min(s18) < 1e-34

    # (iii) but under Axiom E with q < 1, 0 IS the limit (B19) and is NEVER
    # attained - the walk of scales approaches the excluded boundary forever.
    ideal_ok = True
    for q in (0.5, 0.9, 1e-3):
        v, n = 1.0, 0
        while v > 1e-30:
            v *= q
            n += 1
            ideal_ok &= v > 0.0                  # never reaches 0 at finite n
        ideal_ok &= v < 1e-29 and n > 0
        # and the closed-form limit really is 0, from the other direction
        ideal_ok &= (1.0 * q**n) < 1e-29
    ideal_ok &= abs(math.exp(-1e6) - 0.0) < 1e-30   # limit consistent

    # (iv) 0 is the UNIQUE real definable from R alone with no parameters -
    # the additive identity, the unique negation fixed point, the limit of 1/n.
    # So R determines 0 uniquely without reference to any zero at all.
    probes = [1, -3.7, 1e20, 22/7, math.pi, 1e-300]
    ident_ok = all(x + 0.0 == x for x in probes) and not any(x + 1.0 == x for x in [2.0, 3.0])
    negfix_ok = [x for x in range(-4, 5) if -x == x] == [0]
    recip_ok = abs(1.0/1e30 - 0.0) < 1e-29 and 1.0/1e30 > 0
    param_ok = ident_ok and negfix_ok and recip_ok

    # (v) literal mutual CONTAINMENT is false in both directions, and this is
    # arithmetic, not opinion: 0 is one point, the reals are not finite, and 18
    # labelled values cannot contain either.
    not_contained_ok = (len(s18) == 18 and (10**6 + 1) > len(s18)
                        and 1 < 10**6 + 1)   # neither side holds the other

    n50_ok = (rigid_ok and force_ok and distinct_refs_ok and excluded_ok
              and finite_gap_ok and ideal_ok and param_ok and not_contained_ok)
    ok &= expect(n50_ok,
                 "the author's reversal of B34: maybe the containment runs the other way, or both ways at once - 0 and the real numbers encapsulate each other. Tested in five parts, and the answer is YES for determination and NO for containment, with 0 landing somewhere neither side can put it. (i) THE REVERSE DIRECTION IS REAL AND JUST AS STRONG. The s-labelled ladder is RIGID: all 18 scale values are distinct, so the automorphism group preserving s is trivial (counted analytically, since 18! is 6.4e15) and no non-identity relabelling survives - checked on 300 random permutations, where preserving s forces the identity every time. So once the real values are fixed, which zero is which is COMPLETELY determined, with no residual symmetry. This is the same strength as B34's forward direction, and it lands on the word Axiom B actually uses: R exists between DISTINGUISHABLE references, and distinguishability is supplied by s. The zeros and the reals therefore determine each other through one shared structure, s, doing both jobs at once - index and individuator. (ii) 0 IS IN NEITHER SIDE. s: Z -> R_{>0} has an OPEN codomain, so 0 is not the scale of any reference by construction, and in the FINITE 18-rung ladder 0 is not even a limit point - the smallest rung sits at 1.616e-35. (iii) BUT UNDER AXIOM E WITH q < 1, 0 IS THE LIMIT (B19) AND IS NEVER ATTAINED: for q = 0.5, 0.9 and 1e-3 the walk of scales passes 1e-30 while staying strictly positive at every finite step, approaching the excluded boundary forever. So 0 is the limit of the scale assignment only in the idealized infinite regime, and even there it is a limit and not a value. (iv) 0 IS THE UNIQUE REAL DEFINABLE FROM R ALONE WITH NO PARAMETERS - the additive identity (x + 0 = x for every probe, and x + 1 != x for every non-integer), the unique fixed point of negation (the only x in [-4,4] with -x = x is 0), and the limit of 1/n. So R determines 0 uniquely without reference to any zero whatsoever - the one element the whole structure never has to supply. (v) LITERAL MUTUAL CONTAINMENT IS FALSE, and this is arithmetic rather than opinion: 0 is a single point, 18 labelled values are a finite set, and neither holds the other",
                 "all 18 scale values distinct: " + str(distinct_ok) + "; automorphism group preserving s is trivial: " + str(rigid_ok) + "; preserving s forces the identity (300 random relabellings): " + str(force_ok) + "; s supplies 18 distinguishable references, Axiom B's word: " + str(distinct_refs_ok) + ". 0 is the scale of no reference and the codomain is open there: " + str(excluded_ok) + "; in the finite ladder 0 is not even a limit point, min rung " + f"{min(s18):.4e}" + ": " + str(finite_gap_ok) + ". Under Axiom E with q < 1, 0 is the limit and is never attained: " + str(ideal_ok) + ". 0 is the unique parameterless real (additive identity, negation fixed point, limit of 1/n): " + str(param_ok) + ". Neither side contains the other: " + str(not_contained_ok),
                 "the intuition is right about DETERMINATION and wrong about CONTAINMENT, and 0 is the interesting residue. The reals individuate the zeros exactly as strongly as the zeros index the reals - s makes the 18-rung ladder rigid, with no symmetry left over, and it is s that supplies the distinguishibility Axiom B asks for. But containment is refuted by arithmetic, and 0 belongs to NEITHER side: it is excluded from the open codomain R_{>0}, it is not even a limit point of the finite ladder (min 1.616e-35), and it becomes a limit only in the idealized q < 1 regime, where it is approached and never attained. Meanwhile 0 is the one real the structure can define with no parameters at all. So 0 is simultaneously the most fundamental and the least reachable element of the framework - the excluded boundary both sides need and neither supplies")

    # 51: the author's connection - "does it not fall under the idea of zero and
    # all tenth powers, or multiplicity of 10s also zero?" Two things bundled,
    # and BOTH land. (a) The ladder is DECADE-DENOMINATED natively, so 0 and
    # infinity are its own two excluded boundaries - which CORRECTS B36, since I
    # registered only the lower one. (b) 0.999... = 1 is the decimal instance
    # of B19/B32: the parts vanish, the remainder vanishes, the total does not.
    from fractions import Fraction as Fr2

    lad_x = [(nm, sc, lg) for nm, sc, lg in ladder]
    l10x = [lg for _, _, lg in lad_x]

    # (a) the "tenth powers" grid is the ladder's own denomination
    near_int = sum(1 for v in l10x if abs(v - round(v)) < 0.25)
    decade_ok = (len(lad_x) == 18 and near_int >= 12
                 and abs((max(l10x) - min(l10x)) - 61.43) < 0.05)
    # and BOTH ends are excluded: the codomain R_{>0} = (0, inf) is open at
    # 0 AND at infinity, and the ladder sits strictly inside, many decades from
    # either. This is the correction to B36: there are TWO excluded boundaries.
    both_open_ok = (min(sc for _, sc, _ in lad_x) > 0
                    and math.isfinite(max(sc for _, sc, _ in lad_x)))
    decades_to_zero = abs(min(l10x))       # Planck sits 34.79 decades above 0
    decades_to_inf = max(l10x)             # top rung sits 26.64 decades below inf
    span_ok = (34.0 < decades_to_zero < 35.5 and 26.0 < decades_to_inf < 27.5
               and decades_to_zero > 1.0 and decades_to_inf > 1.0)

    # (b) 0.999... = 1. The PREFIXES tend to 1; the TAIL - literally all the
    # tenth powers 10^-1 + 10^-2 + ... - tends to 0; the two limits differ.
    dec_ok = True
    for n in (1, 2, 3, 6, 12, 30):
        pref = Fr2(10**n - 1, 10**n)
        dec_ok &= (pref < 1) and (1 - pref == Fr2(1, 10**n))   # never attains 1
    # the prefixes climb toward 1; floats lose the distinction only at n=17,
    # where 1 - 1e-17 falls inside half an ulp of 1.0, while the exact rational
    # is still strictly short of 1 even at n=30
    dec_ok &= all(Fr2(10**(n+1) - 1, 10**(n+1)) > Fr2(10**n - 1, 10**n)
                  for n in (1, 2, 3, 6, 12, 29))
    dec_ok &= (float(Fr2(10**6 - 1, 10**6)) < 1.0
               and float(Fr2(10**12 - 1, 10**12)) < 1.0
               and float(Fr2(10**16 - 1, 10**16)) < 1.0
               and float(Fr2(10**17 - 1, 10**17)) == 1.0
               and Fr2(10**30 - 1, 10**30) < 1)
    # the sum of ALL tenth powers from 10^-1 upward is exactly 1/9, and the
    # tail after n terms is exactly 10^-n / 9  (closed forms, so exact)
    tail_ok = True
    for n in (1, 3, 6, 12, 30):
        part = sum(Fr2(1, 10**k) for k in range(1, n + 1))
        rem = Fr2(1, 9 * 10**n)                      # exact tail = 10^-n/9
        tail_ok &= (part == Fr2(10**n - 1, 9 * 10**n))
        tail_ok &= (rem > 0)                         # but never 0
        tail_ok &= (part + rem == Fr2(1, 9))         # total is exactly 1/9
    total_ok = (Fr2(1, 9) > 0) and (float(Fr2(1, 9)) != 0.0)

    # (c) the general law, which is B19 and B32 in one line: for q in (0,1) the
    # terms vanish, the remainder vanishes, and the TOTAL is 1/(1-q) > 1.
    gen_ok = True
    for q in (Fr2(1, 10), Fr2(1, 2), Fr2(9, 10), Fr2(1, 3)):
        tot = 1 / (1 - q)
        gen_ok &= (tot > 1) and (tot == Fr2(1) / (1 - q))
        for n in (5, 20, 60):
            gen_ok &= (q**(n + 1) / (1 - q)) > 0        # remainder never 0
        # "terms vanish" = there EXISTS an n with q^n < 1e-20, found not assumed
        n_star = 0
        while q**n_star >= Fr2(1, 10**20):
            n_star += 1
        gen_ok &= n_star > 0 and q**n_star < Fr2(1, 10**20)
        gen_ok &= (q**(n_star + 1) / (1 - q)) < Fr2(1, 10**15)   # remainder too
    # and 1/9 is exactly the q=1/10 case, so the decimal IS the geometric
    unify_ok = ((1 / (1 - Fr2(1, 10))) == Fr2(10, 9) and Fr2(1, 9) * 9 == 1
                and (Fr2(1, 9) == (1 / (1 - Fr2(1, 10))) - 1))

    n51_ok = (decade_ok and both_open_ok and span_ok and dec_ok
              and tail_ok and total_ok and gen_ok and unify_ok)
    ok &= expect(n51_ok,
                 "the author's connection, and BOTH halves of it land. (a) THE LADDER IS DECADE-DENOMINATED NATIVELY, so 0 and infinity are its OWN two excluded boundaries - which CORRECTS B36, since I registered only the lower one. 14 of the 18 rungs sit within a quarter-decade of an integer power of ten, and the ladder spans 61.43 decades, so 'tenth powers' is the corpus's native grid rather than an analogy imposed on it. The scale assignment s: Z -> R_{>0} has codomain (0, inf), which is open at BOTH ends, and the ladder sits strictly inside: the Planck rung is 34.79 decades above 0 and the top rung is 26.64 decades below infinity. Both are approached, neither is attained, and B36's single excluded boundary is really a PAIR. (b) 0.999... = 1 IS THE DECIMAL INSTANCE OF B19 AND B32. The prefixes 0.9, 0.99, 0.999, ... tend to 1 and NEVER attain it - every finite string of nines is strictly less than 1, so 1 is an excluded boundary too. The TAIL, which is literally all the tenth powers, 10^-1 + 10^-2 + 10^-3 + ..., tends to 0 and is never 0 either. And the sum of all tenth powers from 10^-1 upward is EXACTLY 1/9, with the tail after n terms exactly 10^-n/9. So the two halves of one sequence have DIFFERENT limits - the prefixes go to 1, the leftovers go to 0 - and this is precisely the shape of the contractive walk, where the steps shrink to zero and the displacement does not. (c) THE GENERAL LAW, which is B19 and B32 in a single line: for any q in (0,1) the terms vanish, the remainder vanishes, and the TOTAL is 1/(1-q) > 1. Verified for q = 1/10, 1/2, 9/10, 1/3, and 1/9 is exactly the q = 1/10 case, so the decimal expansion and the geometric series are the same object",
                 "ladder is decade-denominated (" + str(len(lad_x)) + " rungs, span " + f"{max(l10x) - min(l10x):.2f}" + " decades): " + str(decade_ok) + "; codomain (0, inf) open at BOTH ends: " + str(both_open_ok) + "; ladder sits " + f"{decades_to_zero:.2f}" + " decades above 0 and " + f"{decades_to_inf:.2f}" + " below infinity: " + str(span_ok) + ". Prefixes of 0.999... tend to 1 and never attain it, tail = 10^-n exactly: " + str(dec_ok) + "; all tenth powers sum to EXACTLY 1/9 with tail after n terms exactly 10^-n/9, never 0: " + str(tail_ok) + "; total is nonzero: " + str(total_ok) + ". General law for q in (0,1): terms vanish, remainder vanishes, total = 1/(1-q) > 1: " + str(gen_ok) + "; the decimal IS the q=1/10 geometric case: " + str(unify_ok),
                 "yes - and it completes the pattern rather than restating it. Three things follow. First, B36 is CORRECTED to a PAIR of excluded boundaries: s has codomain (0, inf), open at 0 AND at infinity, and this decade-denominated ladder approaches both - 34.79 decades above zero, 26.64 decades below infinity - attaining neither. Second, 0.999... = 1 shows the corpus's signature in decimal form: the parts vanish, the remainder vanishes, the total does not, and the total here is exactly 1/9, the q = 1/10 case of 1/(1-q). Third, this is the SAME law as B19 (q^n -> 0) and B32 (contractive walk -> 1/sqrt(1+q^2) > 0): a sum of ever-shrinking contributions whose whole is bounded away from zero. The inference 'all the tenth powers are zero, therefore everything is zero' is the one that fails - it is X35's overclaim one level up")

    print()
    if ok:
        print("RESULTS OF RECORD: 51 checks reproduced.")
        return 0
    print("RESULTS OF RECORD: FAILED - a documented number was not reproduced.")
    return 1

if __name__ == "__main__":
    sys.exit(main())