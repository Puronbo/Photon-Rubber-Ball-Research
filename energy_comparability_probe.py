#!/usr/bin/env python3
"""
Energy Comparability Probe for Photon-Sized Rubber Ball System

The research documents repeat the abstract claim: "at beta = 0.04, relativistic,
quantum, and thermal energy scales become comparable." This script tests that
claim quantitatively with the ball's actual verified parameters and reports the
true energy ratios at the fixed point, plus the honest comparisons that DO hold:

- per-photon recoil kinetic energy vs the ball's confinement (zero-point) scale
- length contraction vs the optical-trap thermal position floor
- JKR adhesion energy vs the trap's quantum and thermal scales

Numbers computed here are ground truth from the same constants used by the
16-script verification battery; doc-side claims that disagree with this table
are cataloged in CORRIGENDUM.md.
"""

import math
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# ============================================================================
# CONSTANTS (same values as the verification battery)
# ============================================================================

HBAR = 1.054571817e-34
KB = 1.380649e-23
C = 299792458.0
G = 6.67430e-11

RHO = 1100.0
R = 275e-9
E = 50e6
NU = 0.5
WAVELENGTH = 550e-9
TEMP = 300.0
TRAP_K = 3.55
W_SEP = 2.62e-15
BETA_FIXED = 0.04

M = RHO * 4/3 * math.pi * R**3

# ============================================================================
# ENERGY TERMS
# ============================================================================

def rel_ke(beta):
    return (1/math.sqrt(1 - beta**2) - 1) * M * C**2

def zpe_ball(radius):
    return HBAR**2 / (2 * M * radius**2)

def photon_recoil_ke():
    p = HBAR * 2*math.pi / WAVELENGTH
    return p**2 / (2*M)

def trap_phonon():
    return HBAR * math.sqrt(TRAP_K / M)

def kt_energy():
    return KB * TEMP

def gravitational_binding():
    return G * M**2 / R

def quote_pair(a, b):
    return max(a, b) / min(a, b) if b > 0 else float("inf")

# ============================================================================
# GEOMETRIC EFFECTS AT THE FIXED POINT
# ============================================================================

def contraction(radius, beta):
    return radius * (1 - math.sqrt(1 - beta**2))

def thermal_position_rms():
    return math.sqrt(KB * TEMP / TRAP_K)

# ============================================================================
# MAIN
# ============================================================================

def main():
    kt = kt_energy()
    rel = rel_ke(BETA_FIXED)
    zpe = zpe_ball(R)
    rec = photon_recoil_ke()
    phonon = trap_phonon()
    grav = gravitational_binding()

    print("=" * 72)
    print("ENERGY COMPARABILITY PROBE (ball-verified parameters)")
    print("=" * 72)
    print(f"  mass                 M  = {M:.3e} kg")
    print(f"  radius               R  = {R:.3e} m")
    print(f"  fixed point          beta = {BETA_FIXED:.4f}  (n=0.4)")
    print()
    print("  energy scale                         J                vs kT(300K)")
    rows = [
        ("kT (thermal)", kt),
        ("rel. kinetic (gamma-1)mc2", rel),
        ("ball zero-point hbar2/2mR2", zpe),
        ("per-photon recoil p2/2m", rec),
        ("trap phonon hbar*sqrt(k/m)", phonon),
        ("JKR adhesion W_sep", W_SEP),
        ("self-gravity Gm2/R", grav),
    ]
    for name, val in rows:
        if name == "kT (thermal)":
            print(f"  {name:28s} {val:12.3e}   (reference 1.0e+00)")
        elif val > kt:
            print(f"  {name:28s} {val:12.3e}   kT is {val/kt:.1e} x BELOW")
        else:
            print(f"  {name:28s} {val:12.3e}   kT is {kt/val:.1e} x ABOVE")
    print()
    print("  VERDICT on doc claim 'relativistic/quantum/thermal comparable at 0.04':")
    print(f"    largest:smallest of the first three = {quote_pair(rel, min(zpe, kt)):.1e} "
          f"(~{math.log10(quote_pair(rel, min(zpe, kt))):.0f} orders of magnitude)  -> NOT comparable")
    print()
    print("  COMPARISONS THAT DO HOLD:")
    print(f"    per-photon recoil KE / zero-point = {quote_pair(rec, zpe):.2f}  "
          f"(same ~1e-39 J energy family)")
    print(f"    JKR adhesion W_sep / kT          = {quote_pair(W_SEP, kt):.1e} "
          "(adhesion far exceeds thermal energy)")
    print(f"    trap phonon / kT                  = {quote_pair(phonon, kt):.1e} "
          "(hbar*sqrt(k/m) sits 2e5 x below kT: the trap's COM motion is classical)")
    print()
    print("  GEOMETRY AT beta=0.04:")
    print(f"    length contraction        {contraction(R, BETA_FIXED)*1e9:.3f} nm")
    print(f"    trap thermal position RMS {thermal_position_rms()*1e9:.3f} nm")
    print(f"    optical resolution floor  {WAVELENGTH/1000*1e9:.1f} nm  (lambda/1000)")
    print(f"    verdict: contraction is {contraction(R, BETA_FIXED)/thermal_position_rms():.1f} x "
          "the trap thermal floor, well below imaging resolution")

main()