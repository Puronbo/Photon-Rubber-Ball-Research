#!/usr/bin/env python3
"""
Results of Record - single-command reproduction gate.

Reproduces and asserts the canonical result table documented in PROJECT_INDEX.md
using the verification module's own constants and the independent closed forms
the battery verifies. Exits nonzero if any documented number is not reproduced.

Backed by: photon_rubber_ball_verification_improved.py (9-axis battery),
script.py (independent re-verification), test_expansion_rigorous*.py (37 tests),
energy_comparability_probe.py (energy-scale verdict).
"""

import math
import sys

import photon_rubber_ball_verification_improved as core

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

KB = 1.380649e-23
HBAR = 1.054571817e-34
C0 = 299792458.0

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

    print()
    if ok:
        print("RESULTS OF RECORD: 16 checks reproduced.")
        return 0
    print("RESULTS OF RECORD: FAILED - a documented number was not reproduced.")
    return 1

if __name__ == "__main__":
    sys.exit(main())