#!/usr/bin/env python3
"""
Entropic Gravity Analogy for JKR Adhesion in Photon Rubber Ball System

This script explores whether the JKR adhesion energy (Axis 6) has an entropic
interpretation similar to Verlinde's entropic gravity theory, where gravity
emerges from entropy changes associated with information positions.

Connections to unsolved theories:
- Entropic gravity (Verlinde's hypothesis)
- Emergent spacetime and quantum entanglement (ER=EPR)
- Holographic principle and AdS/CFT correspondence
"""

import math
from photon_rubber_ball_verification_improved import LAMBDA_PHOTON

# ============================================================================
# CONSTANTS
# ============================================================================

# Physical constants
HBAR = 1.054571817e-34  # Reduced Planck constant (J·S)
BOLTZMANN_CONSTANT = 1.380649e-23  # J/K
C = 299792458.0         # Speed of light (m/s)
G = 6.67430e-11         # Gravitational constant (m³·kg⁻¹·s⁻²)

# System parameters (from main script)
M = 1100.0 * 4/3 * math.pi * (275e-9)**3  # Mass (kg)
R = 275e-9                              # Radius (m)
E = 50e6                                # Young's modulus (Pa)
NU = 0.5                                # Poisson's ratio

# JKR parameters (from Axis 6 in the improved script)
W_JKR = 0.1  # J/m² work of adhesion (from improved script Axis 6)

# ============================================================================
# JKR ADHESION ANALYSIS
# ============================================================================

def calculate_jkr_adhesion_energy() -> float:
    """
    Calculate the total JKR adhesion energy for the sphere-flat surface system.

    Returns:
        Total adhesion energy (J)
    """
    # For a sphere of radius R on a flat surface, the adhesion energy is:
    # E_adhesion = W_JKR × contact_area_at_pull_off
    # At pull-off, the contact radius a0 = (3πWR²/2E*)^(1/3)
    # But the total work of adhesion is simpler: W_JKR × π × a0²
    # Actually, the total energy to separate is W_JKR × area

    # From JKR theory, the pull-off force is F = -3/2 π R W
    # The work of adhesion is the integral of force over displacement
    # For a sphere, the total adhesion energy is:
    # E_adhesion = (3/2) π R W_JKR × Δz_0
    # Where Δz_0 is the equilibrium displacement at contact

    # Simpler approach: The work of adhesion W_JKR is energy per unit area
    # For a sphere, we need to multiply by the effective area
    # In JKR theory, the total adhesion energy is:
    # E_adhesion = 3/2 π R W_JKR × z_0
    # But this gets complicated. Let's use the standard result:

    # Actually, the JKR work of adhesion for sphere-flat is:
    # E_adhesion = 3/2 π R W_JKR × δ_0
    # Where δ_0 is the equilibrium approach

    # Alternatively, from the improved script's axis 6:
    # They calculate Wsep (work of separation) and compare to theoretical
    # Let's compute what the theoretical value should be

    # Standard JKR result: Work of adhesion = 3/2 π R W × Δz_0
    # But δ_0 = (W² R / E*²)^(1/3) or something similar

    # Let's use the values from the improved script's axis 6 verification
    # They state: "JKR W_sep (stated convention) = {Wsep:.3e} J"
    # And compare to theoretical: -3/2 π R W

    # So the theoretical work of adhesion is: E_theory = 3/2 π R W_JKR
    # This has units of J (since W_JKR is J/m², R is m)

    E_adhesion_theory = 1.5 * math.pi * R * W_JKR  # J
    return E_adhesion_theory

def entropic_gravity_entropy_change(
        mass: float = None,
        radius: float = None,
        displacement: float = None) -> float:
    """
    Calculate entropy change in Verlinde's entropic gravity model.

    In Verlinde's hypothesis, gravity emerges from entropy gradients:
    F Δx = T ΔS

    For a mass m approaching a screen with entropy S, the entropic force is:
    F = (T / ħ c) × (dS/dx) × (ħ c / 2π)  (simplified)

    More directly: When a mass m approaches a holographic screen by Δx,
    the entropy change is: ΔS = 2π k m c Δx / ħ

    Args:
        mass: Mass approaching the screen (kg)
        radius: Radius of mass (m) - used for screen area
        displacement: Displacement toward screen (m)

    Returns:
        Entropy change (J/K)
    """
    if mass is None:
        mass = M
    if radius is None:
        radius = R
    if displacement is None:
        # Use characteristic displacement - perhaps radius or Compton wavelength
        displacement = HBAR / (mass * C)  # Compton wavelength

    # Verlinde's entropy change for displacement Δx:
    # ΔS = 2π k m c Δx / ħ
    delta_S = 2 * math.pi * BOLTZMANN_CONSTANT * mass * C * displacement / HBAR
    return delta_S

def entropic_gravity_force(
        mass: float = None,
        radius: float = None,
        displacement: float = None,
        temperature: float = 300.0) -> float:
    """
    Calculate entropic gravity force.

    F = T ΔS / Δx

    Args:
        mass: Mass (kg)
        radius: Radius (m)
        displacement: Displacement (m)
        temperature: Temperature (K)

    Returns:
        Entropic force (N)
    """
    if displacement is None or displacement == 0:
        displacement = 1e-12  # Avoid division by zero

    delta_S = entropic_gravity_entropy_change(mass, radius, displacement)
    force = BOLTZMANN_CONSTANT * temperature * delta_S / displacement
    return force

def holographic_entropy_bound(
        radius: float = None) -> float:
    """
    Calculate holographic entropy bound for a sphere of given radius.

    The holographic principle states that the maximum entropy in a volume
    scales with the surface area, not the volume.

    S_max = k c³ A / (4 G ħ)
    where A is the surface area

    Args:
        radius: Radius of sphere (m)

    Returns:
        Maximum entropy (J/K)
    """
    if radius is None:
        radius = R

    # Surface area of sphere
    A = 4 * math.pi * radius**2  # m²

    # Holographic entropy bound
    S_max = BOLTZMANN_CONSTANT * C**3 * A / (4 * G * HBAR)
    return S_max

def beam_entropy_approximation(
        wavelength: float = None,
        power: float = 1.0) -> float:
    """
    Approximate entropy carried by an electromagnetic beam.

    This is a simplified model - photon entropy is subtle.
    For a coherent laser beam, entropy is low.
    For thermal radiation, entropy is higher.

    Args:
        wavelength: Wavelength (m)
        power: Power (W)

    Returns:
        Approximate entropy flux (J/K·s)
    """
    if wavelength is None:
        wavelength = LAMBDA_PHOTON

    # Photon energy
    E_photon = HBAR * 2 * math.pi * C / wavelength  # J (using ω = 2πc/λ)

    # Photon flux
    photon_flux = power / E_photon  # photons/s

    # For blackbody radiation, entropy per photon is ~3.6 k
    # For coherent state, entropy per photon is much lower
    # Let's use an intermediate value for estimation
    entropy_per_photon = 2.0 * BOLTZMANN_CONSTANT  # J/K per photon (approximate)

    # Entropy flux
    entropy_flux = photon_flux * entropy_per_photon  # J/K·s
    return entropy_flux

def run_entropic_gravity_analysis():
    """Run entropic gravity analogy analysis for JKR adhesion."""
    print("=" * 70)
    print("ENTROPIC GRAVITY ANALOGY FOR JKR ADHESION")
    print("Exploring connections to Verlinde's entropic gravity")
    print("=" * 70)

    print("\nSystem Parameters:")
    print(f"  Sphere mass: {M:.3e} kg ({M / 1.660539e-27:.0f} amu)")
    print(f"  Sphere radius: {R*1e9:.1f} nm")
    print(f"  Young's modulus: {E/1e6:.1f} MPa")
    print(f"  Work of adhesion (W_JKR): {W_JKR:.3f} J/m²")

    # Calculate JKR adhesion energy
    E_adhesion_jkr = calculate_jkr_adhesion_energy()
    print("\nJKR Adhesion Analysis:")
    print(f"  Theoretical JKR adhesion energy: {E_adhesion_jkr:.3e} J")
    print("  (from E = 3/2 π R W)")

    # Compare to entropic gravity predictions
    print("\nEntropic Gravity Analogy:")

    # 1. Entropic force approach
    # In entropic gravity: F = T ΔS / Δx
    # If we interpret the adhesive force as entropic, what entropy gradient would be needed?

    # JKR pull-off force: F_pull_off = -3/2 π R W
    F_pull_off = 1.5 * math.pi * R * W_JKR  # magnitude
    print(f"  JKR pull-off force magnitude: {F_pull_off:.3e} N")

    # What entropy gradient would produce this force at temperature T?
    # F = T |dS/dx|  =>  |dS/dx| = F / T
    T_room = 300.0  # K
    entropy_gradient_needed = F_pull_off / T_room
    print(f"  Required entropy gradient: {entropy_gradient_needed:.3e} J/K·m")
    print("  (for force F = T × dS/dx)")

    # 2. Holographic entropy bound comparison
    print("\nHolographic Entropy Bounds:")
    S_max = holographic_entropy_bound()
    print(f"  Maximum entropy (holographic bound): {S_max:.3e} J/K")
    print(f"  (for sphere of radius {R*1e9:.1f} nm)")

    # 3. Entropy change for characteristic displacements
    print("\nEntropy Changes for Characteristic Displacements:")
    displacements = [
        ("Compton wavelength", HBAR / (M * C)),
        ("Bohr radius", 5.29177210903e-11),
        ("Classical electron radius", 2.8179403227e-15),
        ("Sphere radius", R),
        ("1 nm", 1e-9),
        ("1 pm", 1e-12)
    ]

    for label, disp in displacements:
        if disp > 0:
            delta_S = entropic_gravity_entropy_change(displacement=disp)
            print(f"  {label:25} ({disp:.3e} m): ΔS = {delta_S:.3e} J/K")

    # 4. Work of adhesion from entropic perspective
    print("\nEntropic Work of Adhesion Estimation:")
    print("  If we imagine separating the sphere from surface by doing work against")
    print("  an entropic force, the work would be: W = ∫ F · dx")

    # For constant entropy gradient (approximation)
    characteristic_distance = R  # Use radius as characteristic separation distance
    entropic_work_estimate = F_pull_off * characteristic_distance
    print(f"  Constant force approximation: W = F × {characteristic_distance:.3e} m")
    print(f"  Entropic work estimate:     {entropic_work_estimate:.3e} J")
    print(f"  JKR adhesion energy:        {E_adhesion_jkr:.3e} J")
    print(f"  Ratio (entropic/JKR):       {entropic_work_estimate / E_adhesion_jkr:.3f}")

    # 5. Beam entropy connection (photons carrying information)
    print("\nPhoton Beam Entropy Connection:")
    print("  Considering the verification laser (550nm) as an information carrier:")

    # Typical optical tweezer power
    optical_power = 1e-3  # 1 mW (typical for tweezers)
    entropy_flux = beam_entropy_approximation(power=optical_power)
    print(f"  Optical power:              {optical_power:.3f} W")
    print(f"  Photon energy (550nm):      {6.62607015e-34 * 3e8 / 550e-9:.3e} J")
    print(f"  Photon flux:                {optical_power / (6.62607015e-34 * 3e8 / 550e-9):.2e} photons/s")
    print(f"  Entropy flux (approximate): {entropy_flux:.3e} J/K·s")

    # Over what time would this entropy match the adhesion entropy change?
    # For a characteristic displacement, what entropy does the beam carry?
    interaction_time = 1e-3  # 1 ms (typical measurement timescale)
    entropy_carried_in_time = entropy_flux * interaction_time
    print(f"  Entropy carried in {interaction_time*1e3:.1f} ms: {entropy_carried_in_time:.3e} J/K")

    # Compare to entropy needed for adhesion
    # If we think of adhesion as removing entropic freedom...
    # This is highly speculative, but let's see the scale
    print("\nSpeculative Connections to Unsolved Theories:")
    print("  ✓ Entropic Gravity (Verlinde):")
    print("    If adhesion has entropic origin, then F_adhesion = T ΔS/Δx")
    print("    This would connect surface tension to entropy gradients.")
    print("  ✓ ER=EPR & Quantum Entanglement:")
    print("    JKR adhesion might relate to entanglement entropy between")
    print("    sphere and surface degrees of freedom.")
    print("  ✓ Holographic Principle:")
    print("    The maximum entropy scales with surface area (R²), not volume (R³).")
    print("    Our system probes the mesoscopic regime where both might matter.")
    print("  ✓ Black Hole Analogies:")
    print("    The work of adhesion E_adhesion ∝ R connects to")
    print("    black hole surface gravity κ ∝ 1/R, though different scaling.")
    print("  ✓ Quantum Information & Measurement:")
    print("    Each photon in the verification beam carries information")
    print("    about the sphere's position - a continuous weak measurement.")

    return {
        'JKR_adhesion_energy': E_adhesion_jkr,
        'pull_off_force': F_pull_off,
        'holographic_entropy_bound': S_max,
        'entropy_gradient_needed': entropy_gradient_needed,
        'optical_entropy_flux': entropy_flux
    }

if __name__ == "__main__":
    # Run the entropic gravity analogy analysis
    results = run_entropic_gravity_analysis()

    print("\n" + "=" * 70)
    print("Analysis complete. Results available in returned dictionary.")
    print("=" * 70)