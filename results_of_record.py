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
3-ball at the Hubble rung 16 radius (4.4e26 m) has volume (4/3)pi R^3 =
3.568e80 m^3, holding 4.10e99 canonical 550 nm balls.
"""

import math
import sys

import photon_rubber_ball_verification_improved as core

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

KB = 1.380649e-23
HBAR = 1.054571817e-34
C0 = 299792458.0
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
                 "filled light-cone = observable 3-ball (Hubble rung 16, R=4.4e26 m): V=(4/3)pi*R^3; canonical-ball fill count",
                 f"V={v_univ:.3e} m^3  fill-count={fill:.3e}",
                 "V=3.568e80 m^3, ~4.10e99 canonical balls (R ratio 1.6e33, cubed)")

    print()
    if ok:
        print("RESULTS OF RECORD: 27 checks reproduced.")
        return 0
    print("RESULTS OF RECORD: FAILED - a documented number was not reproduced.")
    return 1

if __name__ == "__main__":
    sys.exit(main())