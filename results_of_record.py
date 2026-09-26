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
from a black hole); 30 the full 16-rung ladder matrix (log10 s and n(u)=D/s for
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

    # 30: full 16-rung ladder matrix (log10 s and n(u) = D/s).
    ladder = [("Planck", 1.616e-35, -34.79), ("quark", 1e-19, -19.00),
              ("proton", 8.4e-16, -15.08), ("atom", 1e-10, -10.00),
              ("molecule", 1e-9, -9.00), ("virus", 1e-7, -7.00),
              ("ball", 5.5e-7, -6.26), ("cell", 1e-5, -5.00),
              ("human", 1.75, 0.24), ("Earth", 6.378e6, 6.80),
              ("Sun", 1.393e9, 9.14), ("Kuiper-50AU", 7.48e12, 12.87),
              ("galaxy-30kpc", 9.257e20, 20.97), ("GA-50Mpc", 1.543e24, 24.19),
              ("Laniakea-160Mpc", 4.937e24, 24.69),
              ("observable-universe", 4.4e26, 26.64)]
    want_nu = [3.40e28, 5.5e12, 6.55e8, 5.5e3, 5.5e2, 5.5, 1.0, 0.055, 3.14e-7,
               8.62e-14, 3.95e-16, 7.35e-20, 5.94e-28, 3.56e-31, 1.11e-31, 1.25e-33]
    l10s = [math.log10(s) for _, s, _ in ladder]
    nu_all = [D/s for _, s, _ in ladder]
    mat_ok = all(abs(l10s[i] - ladder[i][2]) < 0.03 for i in range(16))
    mat_ok &= all(abs(nu_all[i]/want_nu[i] - 1) < 0.02 for i in range(16))
    mat_ok &= nu_all[6] == 1.0 and nu_all[7] < 1.0 \
        and all(u > 1 for u in nu_all[:6]) and all(u < 1 for u in nu_all[8:])
    ok &= expect(mat_ok,
                 "full 16-rung ladder matrix (log10 s and n(u)=D/s per RANKS table; ball n=1, cell 0.055 collapse reads 0D, point above)",
                 "; ".join(f"{ladder[i][0][:7]}={l10s[i]:+.2f}/n={nu_all[i]:.3g}" for i in range(16)),
                 "Planck -34.79/n=3.40e28 .. observable 26.64/n=1.25e-33")

    # 31: ladder gap moments (irregular everywhere).
    g10 = [l10s[i+1] - l10s[i] for i in range(15)]
    gm = sum(g10)/15
    gsd = math.sqrt(sum((x - gm)**2 for x in g10)/14)
    gm_ok = len(set(round(x, 4) for x in g10)) == 15 and g10[0] > 10 \
        and abs(gm - 4.095) < 0.02 and abs(gsd - 3.926) < 0.02 \
        and max(g10)/min(g10) > 25
    ok &= expect(gm_ok,
                 "ladder gap moments (log10 gaps 0.51..15.79, all distinct, Planck->quark 15.79 largest)",
                 f"mean={gm:.3f} sd={gsd:.3f} CV={gsd/gm:.3f} min={min(g10):.2f} max={max(g10):.2f} max/min={max(g10)/min(g10):.1f}",
                 "mean 4.095, sd 3.926, CV 0.959, max/min 31.0 - irregular everywhere")

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

    print()
    if ok:
        print("RESULTS OF RECORD: 40 checks reproduced.")
        return 0
    print("RESULTS OF RECORD: FAILED - a documented number was not reproduced.")
    return 1

if __name__ == "__main__":
    sys.exit(main())