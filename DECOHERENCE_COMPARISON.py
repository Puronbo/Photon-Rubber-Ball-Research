#!/usr/bin/env python3
"""
Decoherence Rate Comparison for Photon Rubber Ball System

This script compares different decoherence mechanisms in the photon rubber ball
system to explore connections to quantum gravity and foundational physics.

Connections to unsolved theories:
- Gravitational-induced decoherence (Penrose/Diósi models)
- Spacetime foam and quantum gravity phenomenology
- Environmental decoherence vs. intrinsic quantum gravity effects
"""

import math
from photon_rubber_ball_verification_improved import BOLTZMANN_CONSTANT

# ============================================================================
# FUNDAMENTAL CONSTANTS
# ============================================================================

# Physical constants (from main script)
HBAR = 1.054571817e-34  # Reduced Planck constant (J·S)
G = 6.67430e-11         # Gravitational constant (m³·kg⁻¹·s⁻²)
C = 299792458.0         # Speed of light (m/s)

# System parameters (from main script)
M = 1100.0 * 4/3 * math.pi * (275e-9)**3  # Mass (kg) - from improved script
R = 275e-9                              # Radius (m)
LAMBDA_PHOTON = 550e-9                  # Photon wavelength (m)

# ============================================================================
# DECOHERENCE MECHANISMS
# ============================================================================

def photon_scattering_decoherence_rate(photon_flux: float = 1e20) -> float:
    """
    Calculate decoherence rate due to photon scattering.

    Each photon scattering event localizes the sphere's position.
    Decoherence rate = scattering rate × localization strength²

    Args:
        photon_flux: Photon flux (photons·m⁻²·s⁻²)

    Returns:
        Decoherence rate (s⁻¹)
    """
    # Photon scattering cross-section (geometric approximation)
    # For Mie scattering with size parameter x=π, we use geometric cross-section
    sigma_scatt = math.pi * R**2  # Geometric cross-section (m²)

    # Scattering rate
    scattering_rate = photon_flux * sigma_scatt  # s⁻¹

    # Localization strength per scattering event
    # Momentum transfer per photon: Δp = h/λ
    photon_momentum = 6.62607015e-34 / LAMBDA_PHOTON  # J·s/m = kg·m/s
    # Position localization: Δx ≈ ħ/Δp (uncertainty principle)
    localizaton_strength = HBAR / photon_momentum  # m

    # Decoherence rate: Γ = rate × (localization strength / characteristic length)²
    # Using sphere radius as characteristic length
    decoherence_rate = scattering_rate * (localizaton_strength / R)**2

    return decoherence_rate

def gravitational_decoherence_penrose(mass: float = None,
                                     radius: float = None) -> float:
    """
    Calculate gravitational decoherence rate (Penrose model).

    Penrose's gravity-induced wavefunction collapse model:
    τ = ħ / E_G where E_G is gravitational self-energy

    Args:
        mass: Mass of object (kg) - defaults to system mass
        radius: Radius of object (m) - defaults to system radius

    Returns:
        Decoherence rate (s⁻¹)
    """
    if mass is None:
        mass = M
    if radius is None:
        radius = R

    # Gravitational self-energy for uniform sphere
    # E_G = (3/5) * G * M² / R
    E_G = (3/5) * G * mass**2 / radius

    # Decoherence rate (inverse of collapse time)
    # Γ = E_G / ħ
    decoherence_rate = E_G / HBAR

    return decoherence_rate

def gravitational_decoherence_diosi(mass: float = None,
                                   radius: float = None,
                                   r0: float = 1e-10) -> float:
    """
    Calculate gravitational decoherence rate (Diosi model).

    Diosi's model includes a length scale cutoff r0 to prevent divergence.

    Args:
        mass: Mass of object (kg) - defaults to system mass
        radius: Radius of object (m) - defaults to system radius
        r0: Length scale cutoff (m) - typical nuclear scale

    Returns:
        Decoherence rate (s⁻¹)
    """
    if mass is None:
        mass = M
    if radius is None:
        radius = R

    # Approximate for sphere: E_G ≈ G * M² / (radius + r0)
    E_G = G * mass**2 / (radius + r0)

    # Decoherence rate
    decoherence_rate = E_G / HBAR

    return decoherence_rate

def spacetime_foam_decoherence(energy: float = None,
                              length_scale: float = None,
                              model: str = 'holographic') -> float:
    """
    Calculate decoherence from spacetime foam models.

    Various quantum gravity models predict spacetime fluctuations
    that cause decoherence.

    Args:
        energy: Characteristic energy (J) - defaults to thermal energy
        length_scale: Characteristic length (m) - defaults to Compton wavelength
        model: 'holographic' or 'random_walk'

    Returns:
        Decoherence rate (s⁻¹)
    """
    if energy is None:
        # Use thermal energy as characteristic scale
        energy = BOLTZMANN_CONSTANT * 300.0  # J
    if length_scale is None:
        # Use Compton wavelength of the sphere
        length_scale = HBAR / (M * C)  # m

    l_pl = math.sqrt(HBAR * G / C**3)  # Planck length
    t_pl = l_pl / C                    # Planck time

    if model == 'holographic':
        # Holographic noise model (e.g., from AdS/CFT)
        # δl/l ~ (l_pl / l)^(2/3) where l_pl is Planck length
        strain = (l_pl / length_scale)**(2/3)
        # Decoherence rate: Γ ~ c * strain² / length_scale
        decoherence_rate = C * strain**2 / length_scale
    elif model == 'random_walk':
        # Random walk model of spacetime fluctuations
        # Each Planck time step gives random displacement ~ l_pl
        # Diffusion constant: D ~ l_pl² / t_pl
        D = l_pl**2 / t_pl
        # Decoherence rate for spatial superposition of size Δx:
        # Γ ~ D * (Δx / l_pl)² / l_pl²
        delta_x = length_scale  # Assume superposition over characteristic length
        decoherence_rate = D * (delta_x / l_pl)**2 / l_pl**2
    else:
        raise ValueError("Model must be 'holographic' or 'random_walk'")

    return decoherence_rate

def environmental_decoherence_gas_collisions(
        pressure: float = 1e-6,  # Pa (ultra-high vacuum)
        temperature: float = 300.0,  # K
        gas_mass: float = 6.63e-27  # kg (approximately H2)
    ) -> float:
    """
    Calculate decoherence rate from residual gas collisions.

    Args:
        pressure: Gas pressure (Pa)
        temperature: Temperature (K)
        gas_mass: Mass of gas particles (kg)

    Returns:
        Decoherence rate (s⁻¹)
    """
    # Gas number density
    n = pressure / (BOLTZMANN_CONSTANT * temperature)  # m⁻³

    # Thermal velocity of gas particles
    v_thermal = math.sqrt(3 * BOLTZMANN_CONSTANT * temperature / gas_mass)  # m/s

    # Collision cross-section (geometric)
    sigma_coll = math.pi * R**2  # m²

    # Collision rate
    collision_rate = n * v_thermal * sigma_coll  # s⁻¹

    # Momentum transfer per collision (approximate)
    delta_p = gas_mass * v_thermal  # kg·m/s

    # Position localization
    localizaton_strength = HBAR / delta_p  # m

    # Decoherence rate
    decoherence_rate = collision_rate * (localizaton_strength / R)**2

    return decoherence_rate

def run_decoherence_comparison():
    """Run complete decoherence rate comparison."""
    print("=" * 70)
    print("DECOHERENCE RATE COMPARISON ANALYSIS")
    print("Photon Rubber Ball System vs. Quantum Gravity Models")
    print("=" * 70)

    print("\nSystem Parameters:")
    print(f"  Sphere mass: {M:.3e} kg ({M / 1.660539e-27:.0f} amu)")
    print(f"  Sphere radius: {R*1e9:.1f} nm")
    print(f"  Photon wavelength: {LAMBDA_PHOTON*1e9:.0f} nm")
    print(f"  Compton wavelength: {HBAR/(M*C)*1e12:.3f} pm")
    print(f"  Planck mass: {math.sqrt(HBAR*C/G):.3e} kg")
    print(f"  System mass / Planck mass: {M / math.sqrt(HBAR*C/G):.3e}")

    # Calculate various decoherence rates
    print("\nDecoherence Rates (s⁻¹):")
    print("-" * 50)

    # 1. Photon scattering decoherence
    photon_flux_low = 1e15   # Low flux (weak measurement)
    photon_flux_high = 1e20  # High flux (strong measurement)
    gamma_photon_low = photon_scattering_decoherence_rate(photon_flux_low)
    gamma_photon_high = photon_scattering_decoherence_rate(photon_flux_high)
    print(f"  Photon scattering (low flux):  {gamma_photon_low:.3e} s⁻¹")
    print(f"  Photon scattering (high flux): {gamma_photon_high:.3e} s⁻¹")

    # 2. Gravitational decoherence (Penrose & Diosi)
    gamma_grav_penrose = gravitational_decoherence_penrose()
    gamma_grav_diosi = gravitational_decoherence_diosi()
    print(f"  Gravitational (Penrose):       {gamma_grav_penrose:.3e} s⁻¹")
    print(f"  Gravitational (Diosi, r0=1Å):  {gamma_grav_diosi:.3e} s⁻¹")

    # 3. Spacetime foam models
    gamma_foam_holo = spacetime_foam_decoherence(model='holographic')
    gamma_foam_rw = spacetime_foam_decoherence(model='random_walk')
    print(f"  Spacetime foam (holographic):  {gamma_foam_holo:.3e} s⁻¹")
    print(f"  Spacetime foam (random walk):  {gamma_foam_rw:.3e} s⁻¹")

    # 4. Environmental decoherence
    gamma_gas_uhv = environmental_decoherence_gas_collisions(pressure=1e-6)   # UHV
    gamma_gas_lv = environmental_decoherence_gas_collisions(pressure=1e-3)    # LV
    print(f"  Residual gas (1 μPa):          {gamma_gas_uhv:.3e} s⁻¹")
    print(f"  Residual gas (1 mPa):          {gamma_gas_lv:.3e} s⁻¹")

    # 5. Thermal decoherence (for reference)
    # Thermal decoherence rate: Γ_thermal ~ kT / ħ
    gamma_thermal = BOLTZMANN_CONSTANT * 300.0 / HBAR
    print(f"  Thermal (kT/ħ):                {gamma_thermal:.3e} s⁻¹")

    print("\n" + "=" * 70)
    print("COMPARISON AND INTERPRETATION")
    print("=" * 70)

    # Find dominant decoherence mechanism at different flux levels
    print(f"\nAt LOW photon flux ({photon_flux_low:.0f} photons/m²/s):")
    rates_low = [
        ("Photon scattering", gamma_photon_low),
        ("Gravitational (Penrose)", gamma_grav_penrose),
        ("Spacetime foam (holo)", gamma_foam_holo),
        ("Residual gas (1 μPa)", gamma_gas_uhv)
    ]
    rates_low_sorted = sorted(rates_low, key=lambda x: x[1], reverse=True)
    print(f"  Dominant: {rates_low_sorted[0][0]} ({rates_low_sorted[0][1]:.2e} s⁻¹)")
    if len(rates_low_sorted) > 1:
        print(f"  Second:   {rates_low_sorted[1][0]} ({rates_low_sorted[1][1]:.2e} s⁻¹)")

    print(f"\nAt HIGH photon flux ({photon_flux_high:.0f} photons/m²/s):")
    rates_high = [
        ("Photon scattering", gamma_photon_high),
        ("Gravitational (Penrose)", gamma_grav_penrose),
        ("Spacetime foam (holo)", gamma_foam_holo),
        ("Residual gas (1 μPa)", gamma_gas_uhv)
    ]
    rates_high_sorted = sorted(rates_high, key=lambda x: x[1], reverse=True)
    print(f"  Dominant: {rates_high_sorted[0][0]} ({rates_high_sorted[0][1]:.2e} s⁻¹)")
    if len(rates_high_sorted) > 1:
        print(f"  Second:   {rates_high_sorted[1][0]} ({rates_high_sorted[1][1]:.2e} s⁻¹)")

    # Quantum gravity sensitivity analysis
    print("\nQuantum Gravity Sensitivity:")
    print("  To detect gravitational decoherence, need:")
    print("    Photon scattering rate < Gravitational rate")
    print(f"  Required photon flux: < {gamma_grav_penrose / (math.pi * R**2 * (HBAR/(6.626e-34/LAMBDA_PHOTON/R))**2):.0f} photons/m²/s")
    print("  This corresponds to an intensity of:")
    photon_energy = 6.62607015e-34 * C / LAMBDA_PHOTON  # J per photon
    required_intensity = (gamma_grav_penrose / (math.pi * R**2 * (HBAR/(6.626e-34/LAMBDA_PHOTON/R))**2)) * photon_energy
    print(f"    {required_intensity:.3e} W/m²")
    print("  For comparison:")
    print("    Sunlight at Earth: ~1000 W/m²")
    print("    Strong laser: ~10⁶ W/m²")
    print(f"    Single photon/sec over 1μm²: ~{(6.626e-34*3e8/550e-9)/(1e-12):.3e} W/m²")

    # Spacetime foam sensitivity
    print("\nSpacetime Foam Sensitivity:")
    print("  Current experimental sensitivity to decoherence: ~10³-10⁶ s⁻¹")
    print(f"  Predicted spacetime foam rates: {gamma_foam_holo:.3e}-{gamma_foam_rw:.3e} s⁻¹")
    print("  To test quantum gravity models, need:")
    print(f"    Decoherence measurement precision < {min(gamma_foam_holo, gamma_foam_rw):.3e} s⁻¹")

    print("\nConnections to Unsolved Theories:")
    print("  ✓ Quantum Gravity Phenomenology:")
    print("    Comparison of decoherence mechanisms tests")
    print("    Penrose, Diosi, and spacetime foam models.")
    print("  ✓ Spacetime Discreteness:")
    print("    Foam models predict measurable effects at")
    print("    mesoscopic scales like our 275nm sphere.")
    print("  ✓ Measurement Problem in QM:")
    print("    Photon scattering decoherence vs. intrinsic")
    print("    gravity-induced collapse.")
    print("  ✓ Black Hole Information & Entropy:")
    print("    Gravitational self-energy connects to")
    print("    black hole thermodynamics via E_G ∝ M²/R.")

    return {
        'photon_scattering_low': gamma_photon_low,
        'photon_scattering_high': gamma_photon_high,
        'gravitational_penrose': gamma_grav_penrose,
        'gravitational_diosi': gamma_grav_diosi,
        'spacetime_foam_holo': gamma_foam_holo,
        'spacetime_foam_rw': gamma_foam_rw,
        'environmental_uhv': gamma_gas_uhv,
        'environmental_lv': gamma_gas_lv,
        'thermal': gamma_thermal
    }

if __name__ == "__main__":
    # Run the decoherence comparison
    results = run_decoherence_comparison()

    print("\n" + "=" * 70)
    print("Analysis complete. Results available in returned dictionary.")
    print("=" * 70)