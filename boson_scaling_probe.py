#!/usr/bin/env python3
"""
Boson Scaling Probe: Massless vs Low-Mass Probe Particles for the
Photon-Sized Rubber Ball System (19th battery member)

The verification model uses a 550-nm photon beam (E = 2.25 eV) as the only
probe. This script quantifies how a low-mass (tiny but nonzero rest mass)
boson differs from a truly massless one at that same quantum energy E.

Key relation, exact: absorbed momentum flux is F = (p/E) P, and
p/E = v/c^2, v/c = sqrt(1 - (m c^2 / E)^2). Hence for a massive probe
F = (v/c) (P/c), saturating at the massless ceiling F = P/c only as
v -> c. Massless and low-mass probes are observationally identical when
the dimensionless pair (m c^2 / E)^2 is below experimental resolution;
deviations grow to percent level only when m c^2 approaches E.

Numbers follow the same constants as the verification battery; this table
is the ground truth for the probe-particle-type dimension.
"""

import math
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# ============================================================================
# CONSTANTS (same values as the verification battery)
# ============================================================================

C = 299792458.0
H = 6.62607015e-34
EV = 1.602176634e-19

WAVELENGTH = 550e-9
R = 275e-9
POWER = 1.0e-3

E_PHOTON = H * C / WAVELENGTH
RATE = POWER / E_PHOTON
F_CAP = POWER / C
BALL_DIAMETER = 2 * R

# ============================================================================
# SCALING FUNCTIONS
# ============================================================================

def gamma_beta(mass_energy):
    if mass_energy == 0.0:
        return 1.0
    xi = (mass_energy / E_PHOTON) ** 2
    if xi >= 1.0:
        return None
    return math.sqrt(1.0 - xi)

def de_broglie(mass_energy):
    numerator = H * C
    denominator = math.sqrt(max(E_PHOTON ** 2 - mass_energy ** 2, 0.0))
    return numerator / denominator

def transversal_time(beta):
    if beta is None:
        return None
    return BALL_DIAMETER / (beta * C)

# ============================================================================
# MAIN
# ============================================================================

def main():
    ladder = [
        ("massless photon", 0.0),
        ("photon-mass bound", 1e-18),
        ("1 meV", 1e-3),
        ("10 meV", 1e-2),
        ("0.1 eV", 0.1),
        ("1 eV", 1.0),
        ("2.24 eV (E minus 0.01 eV)", 2.24),
        ("2.26 eV (0.01 eV above E)", 2.26),
        ("5 eV", 5.0),
        ("10 eV", 10.0),
    ]

    t_photon = BALL_DIAMETER / C

    print("=" * 78)
    print("BOSON SCALING PROBE (550 nm probe, E = {:.4f} eV, P = 1 mW)".format(
        E_PHOTON / EV))
    print("=" * 78)
    print("  force-per-watt ceiling (every probe):  F = P/c = {:.4f} pN".format(
        F_CAP * 1e12))
    print("  photon rate at 1 mW: {:.4g} /s; per-quantum p = {:.4g} kg m/s".format(
        RATE, E_PHOTON / C))
    print()

    print("  mc^2 [eV]   (mc^2/E)^2   v/c     F [pN]   loss vs photon   lambda [m]")
    for name, mc2_ev in ladder:
        m2 = mc2_ev * EV
        beta = gamma_beta(m2)
        xi = (m2 / E_PHOTON) ** 2
        if beta is None:
            print("  {:16s} {:10.3e}  beyond threshold (E < mc^2: no ultra-rel. beam)".format(
                name, xi))
            continue
        force = beta * F_CAP * 1e12
        loss = (1.0 - beta) * 100.0
        wavelength = de_broglie(m2)
        print("  {:16s} {:10.3e}  {:.4f}   {:.4f}     {:.3f}%      {:.4g}".format(
            name, xi, beta, force, loss, wavelength))
    print()

    print("  time-of-flight across the ball (diameter 550 nm):")
    print("    photon     {:.4f} fs".format(t_photon * 1e15))
    for name, mc2_ev in ladder:
        m2 = mc2_ev * EV
        beta = gamma_beta(m2)
        if beta is None:
            continue
        delay = (transversal_time(beta) - t_photon) * 1e15
        if delay < 1e-6:
            print("    {:16s} {:.4f} fs  (delay {:.2e} fs, indistinguishable)".format(
                name, transversal_time(beta) * 1e15, delay))
        else:
            print("    {:16s} {:.4f} fs  (delay +{:.3f} fs)".format(
                name, transversal_time(beta) * 1e15, delay))
    print()

    print("  VERDICT on 'massless vs low-mass':")
    print("    distinguishing number is (mc^2/E)^2; identical when << 1e-6.")
    photon_bound_loss = 1 - gamma_beta(1e-18 * EV)
    print("    real-photon bound mc^2 = 1e-18 eV -> (mc^2/E)^2 = {:.1e}, "
          "loss {:.2e}% (unobservable)".format(
              (1e-18 * EV / E_PHOTON) ** 2, photon_bound_loss * 100))
    for mc2_ev in (1e-3, 0.1, 1.0):
        beta = gamma_beta(mc2_ev * EV)
        print("    mc^2 = {:5g} eV  -> v/c = {:.4f}, force-cap fraction {:.4f}, "
              "longitudinal mode ~ {:.2e}".format(
                  mc2_ev, beta, beta, ((mc2_ev * EV) / E_PHOTON) ** 2))
    print("    conclusion: massless and low-mass probes are interchangeable for")
    print("    force, rate, and wavelength until mc^2 is within ~10x of E = {:.2f} eV.".format(
        E_PHOTON / EV))

main()