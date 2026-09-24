#!/usr/bin/env python3
"""
Fluctuation-Dissipation Connections in Photon Rubber Ball System

This script explores connections between the viscoelastic restitution model
(Axis 3) and fluctuation-dissipation theorems, with implications for
quantum dissipation, quantum Brownian motion, and unsolved theories in
quantum gravity and cosmology.

Connections to unsolved theories:
- Quantum dissipation and decoherence in black hole horizons
- Cosmic viscosity and dark energy analogies
- Fluctuation-dissipation relations in quantum gravity
- Emergent spacetime from entanglement and dissipation
"""

import math
from photon_rubber_ball_verification_improved import C, G

# ============================================================================
# CONSTANTS
# ============================================================================

# Physical constants
HBAR = 1.054571817e-34  # Reduced Planck constant (J·S)
K_B = 1.380649e-23      # Boltzmann constant (J/K)

# System parameters (from improved script)
M = 1100.0 * 4/3 * math.pi * (275e-9)**3  # Mass (kg)
R = 275e-9                              # Radius (m)
E = 50e6                                # Young's modulus (Pa)
NU = 0.5                                # Poisson's ratio

# Viscoelastic parameters (from Axis 3 in improved script)
TANDELTA_VALUES = (0.05, 0.1, 0.2)  # Loss tangent values

# ============================================================================
# FLUCTUATION-DISSIPATION THEOREM
# ============================================================================

def hunt_crossley_dissipation_coefficient(tand: float, E_star: float, R: float, v_impact: float = 1.0) -> float:
    """
    Calculate effective dissipation coefficient from Hunt-Crossley model.

    The Hunt-Crossley model for viscoelastic restitution:
    F = k * x^n + d * x^n * dx/dt
    where d is related to the loss tangent.

    Args:
        tand: Loss tangent (dimensionless)
        E_star: Effective elastic modulus (Pa)
        R: Sphere radius (m)
        v_impact: Impact velocity (m/s)

    Returns:
        Dissipation coefficient (kg/s)
    """
    # From the improved script's Axis 3 implementation:
    # restitution coefficient e = exp(-pi * tand / 2)
    # For small tand, e ≈ 1 - pi*tand/2
    # Energy loss per collision: ΔE/E₀ = 1 - e² ≈ pi*tand (for small tand)

    # Effective dissipation coefficient for harmonic oscillator approximation:
    # γ = (energy loss per radian) / (energy stored)
    # For Hertzian contact with exponent 3/2, the relationship is more complex

    # Simplified approach: use equivalent viscous damping
    # For a harmonic oscillator, quality factor Q = 1/tand (approximately)
    # And γ = ω₀/Q where ω₀ is natural frequency

    # Effective stiffness for contact (approximate)
    # For spherical contact: k* ≈ 2E*√(Rδ) but we need characteristic value
    # Use stiffness at typical indentation: δ₀ ≈ (mv²/E*)^(2/5) * R^(1/5)
    characteristic_velocity = v_impact
    characteristic_indentation = (M * characteristic_velocity**2 / E_star)**(2/5) * R**(1/5)
    k_eff = 2 * E_star * math.sqrt(R * characteristic_indentation)

    # Natural frequency
    omega_0 = math.sqrt(k_eff / M)

    # Dissipation coefficient: γ = tand * ω_0 (for small tand)
    gamma = tand * omega_0

    return gamma

def fluctuation_dissipation_theorem(gamma: float, temperature: float = 300.0, omega: float = None) -> dict:
    """
    Calculate fluctuation-dissipation relations.

    Classical FDT: ⟨x²⟩ = 2k_BT γ / (m²ω₄) for damped harmonic oscillator
    Quantum FDT: includes zero-point fluctuations and tanh(ħω/2k_BT) factor

    Args:
        gamma: Dissipation coefficient (kg/s)
        temperature: Temperature (K)
        omega: Angular frequency (rad/s) - if None, uses characteristic frequency

    Returns:
        Dictionary of FDT relations and comparisons
    """
    if omega is None:
        # Use characteristic frequency from contact mechanics
        E_star = E / (2 * (1 - NU**2))
        characteristic_indentation = (M * 1.0**2 / E_star)**(2/5) * R**(1/5)  # For v=1 m/s
        k_eff = 2 * E_star * math.sqrt(R * characteristic_indentation)
        omega = math.sqrt(k_eff / M)

    # Classical mean square displacement (from equipartition and dissipation)
    # For damped harmonic oscillator in thermal equilibrium:
    # ⟨x²⟩_classical = k_BT / k_eff
    # But we can also express via dissipation:
    # ⟨x²⟩ = (2k_BT gamma) / (m^2 omega^4)  [for specific oscillator model]

    k_eff = M * omega**2
    x2_classical = K_B * temperature / k_eff

    # Quantum correction factor
    # Quantum FDT: S_xx(ω) = (2hbar / pi) * [n(ω,T) + 1/2] * Im[χ(ω)]
    # where n(ω,T) = 1/(exp(hbar*omega/k_BT) - 1) is Bose-Einstein distribution
    # and chi(ω) is susceptibility

    # For harmonic oscillator: Im[chi(omega)] = gamma * omega / [(omega_0^2 - omega^2)^2 + (gamma*omega)^2]
    # At resonance (omega = omega_0): Im[chi(omega_0)] = 1/gamma

    # Quantum mean square displacement:
    # ⟨x²⟩_quantum = (hbar / (pi * m * gamma)) * ∫ [n(ω,T) + 1/2] * (gamma^2 * omega^2) / [(omega_0^2 - omega^2)^2 + (gamma*omega)^2] domega
    # Simplified approximation at low damping:
    # ⟨x²⟩_quantum ≈ (hbar / (2 * m * omega_0)) * coth(hbar * omega_0 / (2 * k_BT))

    hbar_omega = HBAR * omega
    coth_arg = hbar_omega / (2 * K_B * temperature)
    if coth_arg > 20:  # Avoid overflow in coth for large arguments
        coth_val = 1.0  # coth(x) → 1 as x → ∞
    elif coth_arg < 1e-10:
        coth_val = 2 / coth_arg  # coth(x) ≈ 1/x for small x
    else:
        coth_val = 1.0 / math.tanh(coth_arg)  # coth(x) = 1/tanh(x)

    x2_quantum = (HBAR / (2 * M * omega)) * coth_val

    # Zero-point contribution
    x2_zpe = HBAR / (2 * M * omega)  # Ground state width squared

    # Thermal contribution
    x2_thermal = x2_quantum - x2_zpe

    # Classical limit (high T or low omega): coth(x) ≈ 1/x
    # Then ⟨x²⟩_quantum ≈ k_BT / (m * omega^2) = k_BT / k_eff

    return {
        'gamma': gamma,
        'omega': omega,
        'temperature': temperature,
        'x2_classical': x2_classical,
        'x2_quantum': x2_quantum,
        'x2_zpe': x2_zpe,
        'x2_thermal': x2_thermal,
        'quantum_correction_factor': x2_quantum / x2_classical if x2_classical > 0 else 0,
        'zero_point_fraction': x2_zpe / x2_quantum if x2_quantum > 0 else 0
    }

def johnson_nyquist_noise(resistance: float = None, temperature: float = 300.0, bandwidth: float = 1e3) -> float:
    """
    Calculate Johnson-Nyquist noise voltage.

    V_rms = sqrt(4 * k_B * T * R * Δf)

    Args:
        resistance: Electrical resistance (Ohms) - if None, uses mechanical analog
        temperature: Temperature (K)
        bandwidth: Frequency bandwidth (Hz)

    Returns:
        RMS noise voltage (V)
    """
    if resistance is None:
        # Mechanical analog: resistance -> damping coefficient
        # Voltage -> velocity, Current -> force
        # Then: ⟨v²⟩ = 4 * k_B * T * gamma * Δf
        gamma = hunt_crossley_dissipation_coefficient(tand=0.1, E_star=E/(2*(1-NU**2)), R=R)
        resistance = gamma  # Mechanical analog

    vrms = math.sqrt(4 * K_B * temperature * resistance * bandwidth)
    return vrms

def quantum_shot_noise(current: float = None, bandwidth: float = 1e3) -> float:
    """
    Calculate quantum shot noise.

    I_shot = sqrt(2 * e * I * Δf)

    For mechanical analog: force noise from discrete impulses

    Args:
        current: Analogous "current" (impulse rate * momentum transfer) - if None, uses photon impact rate
        bandwidth: Frequency bandwidth (Hz)

    Returns:
        RMS noise amplitude (N for force analog)
    """
    if current is None:
        # Estimate from photon impacts
        # Photon momentum transfer per photon: 2*h/lambda (for reflection)
        photon_momentum = 2 * 6.62607015e-34 / 550e-9  # kg*m/s
        # Assume photon flux of 1e20 photons/m2/s (typical for measurement)
        photon_flux = 1e20  # photons/m2/s
        cross_section = math.pi * R**2  # m2
        impact_rate = photon_flux * cross_section  # impacts/s
        current = impact_rate * photon_momentum  # N (equivalent to force from continuous stream)

    # Shot noise: sqrt(2 * q * I * delta_f)
    # For mechanical analog with momentum transfer q per event:
    q = 2 * 6.62607015e-34 / 550e-9  # Momentum transfer per photon
    shot_noise = math.sqrt(2 * q * current * bandwidth)
    return shot_noise

def caldeira_leggett_decoherence(temperature: float = 300.0, coupling: float = None) -> float:
    """
    Estimate decoherence rate from Caldeira-Leggett model.

    Quantum Brownian motion model for decoherence:
    Gamma_phi = (2 * gamma * k_BT) / (hbar^2) * (delta_x)^2  [for high T]
    where gamma is damping coefficient, delta_x is superposition size

    Args:
        temperature: Temperature (K)
        coupling: Coupling strength - if None, uses gravitational coupling

    Returns:
        Decoherence rate (1/s)
    """
    if coupling is None:
        # Gravitational coupling strength for superposition of size delta_x
        # Energy difference: Delta_E ≈ G * M^2 * delta_x / R^3  (for gradient)
        # But simpler: use dimensionless gravitational coupling
        # alpha_g = G * M^2 / (hbar * c)
        coupling = G * M**2 / (HBAR * C)

    # Get dissipation coefficient
    gamma = hunt_crossley_dissipation_coefficient(tand=0.1, E_star=E/(2*(1-NU**2)), R=R)

    # Characteristic superposition size (use Compton wavelength or zero-point motion)
    E_star = E / (2 * (1 - NU**2))
    characteristic_indentation = (M * 1.0**2 / E_star)**(2/5) * R**(1/5)
    k_eff = 2 * E_star * math.sqrt(R * characteristic_indentation)
    omega_0 = math.sqrt(k_eff / M)
    delta_x = math.sqrt(HBAR / (M * omega_0))  # Zero-point motion

    # High temperature limit: Gamma_phi = (2 * gamma * k_BT) / (hbar^2) * (delta_x)^2
    gamma_phi = (2 * gamma * K_B * temperature) / (HBAR**2) * (delta_x**2)

    return gamma_phi

def run_fluctuation_dissipation_analysis():
    """Run fluctuation-dissipation connection analysis."""
    print("=" * 70)
    print("FLUCTUATION-DISSIPATION CONNECTIONS ANALYSIS")
    print("Viscoelastic Restitution (Axis 3) to Quantum Dissipation")
    print("=" * 70)

    print("\nSystem Parameters:")
    print(f"  Sphere mass: {M:.3e} kg")
    print(f"  Sphere radius: {R*1e9:.1f} nm")
    print(f"  Young's modulus: {E/1e6:.1f} MPa")
    print(f"  Loss tangent values: {TANDELTA_VALUES}")

    # Effective modulus
    E_star = E / (2 * (1 - NU**2))
    print(f"  Effective modulus E*: {E_star/1e6:.1f} MPa")

    # Analyze each loss tangent value
    print("\n1. HUNT-CROSSLEY MODEL PARAMETERS:")
    print("   tand | restitution e | gamma (kg/s) | omega_0 (rad/s)")
    print("   -----|---------------|--------------|----------------")

    results_tand = []
    for tand in TANDELTA_VALUES:
        # Restitution coefficient
        e = math.exp(-math.pi * tand / 2)

        # Dissipation coefficient
        gamma = hunt_crossley_dissipation_coefficient(tand, E_star, R)

        # Characteristic frequency
        characteristic_indentation = (M * 1.0**2 / E_star)**(2/5) * R**(1/5)
        k_eff = 2 * E_star * math.sqrt(R * characteristic_indentation)
        omega_0 = math.sqrt(k_eff / M)

        results_tand.append({'tand': tand, 'e': e, 'gamma': gamma, 'omega_0': omega_0})
        print(f"   {tand:5.3f} | {e:13.6f} | {gamma:12.6e} | {omega_0:14.3f}")

    # 2. Fluctuation-Dissipation Theorem Analysis
    print("\n2. FLUCTUATION-DISSIPATION THEOREM:")
    print("   Temperature: 300.0 K")
    print(f"   Thermal energy kT: {K_B * 300:.3e} J")
    print("   | tand | ⟨x²⟩_classical (m²) | ⟨x²⟩_quantum (m²) | Quantum/Classical |")
    print("   |------|---------------------|---------------------|-------------------|")

    fdt_results = []
    for tand in TANDELTA_VALUES:
        gamma = hunt_crossley_dissipation_coefficient(tand, E_star, R)
        characteristic_indentation = (M * 1.0**2 / E_star)**(2/5) * R**(1/5)
        k_eff = 2 * E_star * math.sqrt(R * characteristic_indentation)
        omega_0 = math.sqrt(k_eff / M)

        fdt = fluctuation_dissipation_theorem(gamma, temperature=300.0, omega=omega_0)
        fdt_results.append(fdt)

        print(f"   | {tand:4.3f} | {fdt['x2_classical']:20.3e} | {fdt['x2_quantum']:20.3e} | {fdt['quantum_correction_factor']:16.3f} |")

    # 3. Noise Analogies
    print("\n3. NOISE ANALOGIES:")

    # Johnson-Nyquist noise (thermal)
    gamma_sample = hunt_crossley_dissipation_coefficient(tand=0.1, E_star=E_star, R=R)
    vn_rms = johnson_nyquist_noise(resistance=gamma_sample, temperature=300.0, bandwidth=1e3)
    print("  Johnson-Nyquist noise (mechanical analog):")
    print(f"    RMS velocity noise: {vn_rms:.3e} m/s (in 1 kHz bandwidth)")
    print(f"    Equivalent force noise: {vn_rms * M:.3e} N")

    # Shot noise (quantum)
    fn_shot = quantum_shot_noise(bandwidth=1e3)
    print("  Quantum shot noise (force analog):")
    print(f"    RMS force noise: {fn_shot:.3e} N (in 1 kHz bandwidth)")

    # Compare noise sources
    print("  Noise comparison at 300K, 1 kHz BW:")
    print(f"    Thermal (J-N):     {vn_rms * M:.3e} N")
    print(f"    Quantum (shot):    {fn_shot:.3e} N")
    print(f"    Ratio shot/J-N:    {fn_shot / (vn_rms * M) if vn_rms * M > 0 else 0:.3f}")

    # 4. Caldeira-Leggett Decoherence Estimate
    print("\n4. CALDEIRA-LEGGETT DECOHERENCE ESTIMATE:")
    gamma_phi = caldeira_leggett_decoherence(temperature=300.0)
    print(f"  Decoherence rate (QBM model): {gamma_phi:.3e} s⁻¹")
    print(f"  Decoherence time: {1/gamma_phi if gamma_phi > 0 else float('inf'):.3e} s")

    # Compare to other decoherence rates from previous analysis
    # Gravitational decoherence (Penrose)
    E_G = (3/5) * 6.67430e-11 * M**2 / R
    gamma_grav = E_G / HBAR
    print(f"  Gravitational decoherence (Penrose): {gamma_grav:.3e} s⁻¹")
    print(f"  Ratio (QBM/Grav): {gamma_phi / gamma_grav if gamma_grav > 0 else 0:.3f}")

    # 5. Connections to Unsolved Theories
    print("\n" + "=" * 70)
    print("CONNECTIONS TO UNSOLVED THEORIES:")
    print("=" * 70)
    print("  ✓ Quantum Dissipation & Black Hole Horizons:")
    print("    Viscoelastic dissipation analogs to horizon viscosity")
    print("    Membrane paradigm and fluid-gravity correspondence")
    print("  ✓ Cosmic Viscosity & Dark Energy:")
    print("    Bulk viscosity in cosmological fluids")
    print("    Analogies to effective field theory of dark energy")
    print("  ✓ Fluctuation-Dissipation in Quantum Gravity:")
    print("    FDT constraints on graviton self-energy")
    print("    Hierarchy problem and cosmological constant")
    print("  ✓ Emergent Spacetime from Entanglement:")
    print("    Dissipation as entanglement entropy production")
    print("    Tensor network renormalization and RG flow")
    print("  ✓ Measurement Problem & Continuous Spontaneous Localization:")
    print("    Dissipative collapse models (Diòsi-Penrose)")
    print("    Connection to gravitational decoherence estimates")

    return {
        'tand_results': results_tand,
        'fdt_results': fdt_results,
        'noise_analogies': {
            'johnson_nyquist_rms_force': vn_rms * M,
            'shot_noise_rms_force': fn_shot
        },
        'decoherence_qbm': gamma_phi,
        'decoherence_gravitational': gamma_grav
    }

if __name__ == "__main__":
    # Run the fluctuation-dissipation analysis
    results = run_fluctuation_dissipation_analysis()

    print("\n" + "=" * 70)
    print("Analysis complete. Results available in returned dictionary.")
    print("=" * 70)