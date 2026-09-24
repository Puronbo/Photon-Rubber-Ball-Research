#!/usr/bin/env python3
"""
Expanded Shatter Threshold Analysis for Photon Rubber Ball System

This script expands on the shatter threshold analysis with more detailed
fracture mechanics, viscoelastic effects, quantum gravity connections,
and expanded scenario exploration for the photon-sized rubber ball system
under high-energy impacts.

Connections to unsolved theories:
- Quantum gravity and spacetime discreteness
- Black hole formation and information paradox
- Quantum critical points and universality classes
- Non-equilibrium thermodynamics and fluctuation theorems
- Cosmological phase transitions and inflationary analogs
"""

import math
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# ============================================================================
# CONSTANTS
# ============================================================================

# Physical constants
HBAR = 1.054571817e-34  # Reduced Planck constant (J·S)
G = 6.67430e-11         # Gravitational constant (m³·kg⁻¹·s⁻¹)
C = 299792458.0         # Speed of light (m/s)
K_B = 1.380649e-23      # Boltzmann constant (J/K)

# System parameters (from improved script)
M = 1100.0 * 4/3 * math.pi * (275e-9)**3  # Mass (kg)
R = 275e-9                              # Radius (m)
E = 50e6                                # Young's modulus (Pa)
NU = 0.5                                # Poisson's ratio
DENSITY = 1100.0                        # Density (kg/m³)

# Material properties for rubber (more detailed)
YIELD_STRESS = 10e6     # Yield stress (Pa)
ULTIMATE_TENSILE_STRESS = 20e6  # Ultimate tensile stress (Pa)
FRACTURE_TOUGHNESS = 1000       # Fracture toughness (Pa·√m)
CHARACTERISTIC_FLAW = 100e-9    # Characteristic pre-existing flaw size (m)
POISSON_RATIO = NU

# Viscoelastic parameters (from Axis 3)
TANDELTA = 0.1          # Loss tangent
RELAXATION_TIME = 1e-3  # Stress relaxation time (s)

# Derived quantities
VOLUME = 4/3 * math.pi * R**3
SURFACE_AREA = 4 * math.pi * R**2
E_STAR = E / (2 * (1 - NU**2))  # Effective modulus
SHEAR_MODULUS = E / (2 * (1 + NU))  # Shear modulus
# NU = 0.5 is incompressible, making the longitudinal (constrained) modulus
# formally infinite; clamp (1-2*NU) so sound-speed math stays finite.
LONGITUDINAL_MODULUS = E * (1 - NU) / ((1 + NU) * max(1 - 2 * NU, 1e-3))  # Bulk modulus

# Characteristic velocities
SOUND_SPEED_LONGITUDINAL = math.sqrt(LONGITUDINAL_MODULUS / DENSITY)
SOUND_SPEED_SHEAR = math.sqrt(SHEAR_MODULUS / DENSITY)
THERMAL_VELOCITY = math.sqrt(3 * K_B * 300.0 / DENSITY)

# ============================================================================
# FRACTURE MECHANICS MODELS
# ============================================================================

def griffith_fracture_stress(crack_length: float,
                           surface_energy: float = 0.05) -> float:
    """
    Griffith fracture stress for brittle fracture.

    σ_f = sqrt(2Eγ/(πa))

    Args:
        crack_length: Crack length (m)
        surface_energy: Surface energy (J/m²)

    Returns:
        Fracture stress (Pa)
    """
    return math.sqrt(2 * E * surface_energy / (math.pi * crack_length))

def irwin_oplastic_modification(crack_length: float,
                              yield_stress: float = None) -> float:
    """
    Irwin's plastic zone modification to Griffith criterion.

    Effective crack length: a_eff = a + r_p
    where r_p = (1/(2π)) * (K_IC / σ_y)^2 is plastic zone size

    Args:
        crack_length: Original crack length (m)
        yield_stress: Yield stress (Pa)

    Returns:
        Effective crack length (m)
    """
    if yield_stress is None:
        yield_stress = YIELD_STRESS

    # Approximate fracture toughness
    K_IC = FRACTURE_TOUGHNESS * math.sqrt(math.pi)  # Convert to standard units

    # Plastic zone size (plane stress)
    r_p = (1/(2*math.pi)) * (K_IC / yield_stress)**2

    return crack_length + r_p

def viscoelastic_fracture_enhancement(strain_rate: float,
                                    base_toughness: float = None) -> float:
    """
    Enhancement of fracture toughness due to viscoelastic effects.

    Based on time-temperature superposition and strain rate effects.

    Args:
        strain_rate: Strain rate (1/s)
        base_toughness: Base fracture toughness (Pa·√m)

    Returns:
        Enhanced fracture toughness (Pa·√m)
    """
    if base_toughness is None:
        base_toughness = FRACTURE_TOUGHNESS

    # Williams-Landel-Ferry (WLF) equation for time-temperature shift
    # Simplified: toughness increases with strain rate up to a point
    reference_rate = 1.0  # 1/s reference
    if strain_rate <= reference_rate:
        return base_toughness
    else:
        # Power-law increase (simplified)
        enhancement = 1.0 + 0.5 * math.log10(strain_rate / reference_rate)
        return base_toughness * min(enhancement, 3.0)  # Cap enhancement

def critical_impact_energy_for_fracture(impact_angle: float = 0.0) -> float:
    """
    Calculate critical impact energy for fracture initiation.

    Uses energy balance: Impact energy = Surface energy created + Plastic work + Elastic waves

    Args:
        impact_angle: Impact angle from normal (0° = normal, 90° = grazing)

    Returns:
        Critical impact energy (J)
    """
    # Normalized angular factor (grazing impacts less damaging)
    angular_factor = math.cos(impact_angle)**2

    # Assume pre-existing flaw distribution
    # Characteristic flaw size from processing: 100 nm (typical for rubbers)

    # Griffith energy for creating two new surfaces
    surface_energy_per_area = 0.05  # J/m²
    new_surface_area = 4 * math.pi * R**2  # For complete fragmentation (conservative)
    surface_energy = surface_energy_per_area * new_surface_area

    # Plastic work estimate (simplified)
    yield_strain = YIELD_STRESS / E
    plastic_work = 0.5 * YIELD_STRESS * yield_strain * VOLUME

    # Elastic wave energy (energy radiated away)
    # Fraction of impact energy that goes into elastic waves
    wave_fraction = 0.3  # Empirical for impacts

    # Total energy required: surface + plastic + waves/(1-wave_fraction)
    # Rearranged: E_impact = (surface + plastic) / (1 - wave_fraction)
    base_energy = (surface_energy + plastic_work) / (1 - wave_fraction)

    return base_energy * angular_factor

def strain_rate_from_impact(velocity: float,
                          impact_duration: float = None) -> float:
    """
    Estimate strain rate from impact parameters.

    Args:
        velocity: Impact velocity (m/s)
        impact_duration: Impact duration (s) - if None, estimated

    Returns:
        Strain rate (1/s)
    """
    if impact_duration is None:
        # Estimate from sound transit time
        impact_duration = 2 * R / SOUND_SPEED_LONGITUDINAL

    # Approximate strain: ΔL/L ≈ v*t / R for impact
    # Strain rate ≈ strain / time ≈ (v*t/R) / t = v/R
    return velocity / R

def quantum_gravity_length_scale_from_impact(velocity: float) -> float:
    """
    Estimate effective length scale probed by impact that could
    reveal quantum gravity effects.

    Based on uncertainty principle: Δx ≈ ħ / Δp
    Where Δp is momentum transfer in impact

    Args:
        velocity: Impact velocity (m/s)

    Returns:
        Effective length scale (m)
    """
    # Momentum transfer for elastic reflection
    momentum_transfer = 2 * M * velocity

    # Uncertainty in position
    delta_x = HBAR / momentum_transfer

    return delta_x

def holographic_entropy_bound_violation_check(energy_density: float) -> bool:
    """
    Check if energy density violates holographic entropy bound.

    Bekenstein bound: S ≤ 2πk_B E R / (ħ c)
    Violated when entropy density exceeds bound

    Args:
        energy_density: Energy density (J/m³)

    Returns:
        True if bound violated, False otherwise
    """
    # Maximum entropy density from Bekenstein bound
    # S_max/V ≤ 2πk_B (ρc²) R / (ħ c V) = 2πk_B ρ R c / (ħ V)
    # For sphere: V = 4/3 π R³ → S_max/V ≤ (3/2) k_B ρ c / (ħ R)
    max_entropy_density = 1.5 * K_B * DENSITY * C / (HBAR * R)

    # Actual entropy density (approximate: S ≈ E/T for relativistic gas)
    # Using temperature equivalent: T_eq = E/(k_B N) where N = number of particles
    # For order of magnitude: S ≈ k_B per particle when E ≈ k_B T per particle
    # So S/V ≈ k_B * (number density) = k_B * (ρ / m_proton)
    actual_entropy_density = K_B * DENSITY / (1.67e-27)  # Very rough estimate

    return actual_entropy_density > max_entropy_density

def planck_scale_probing_velocity() -> float:
    """
    Calculate velocity needed to probe Planck scale lengths.

    From uncertainty principle: Δx ≈ ħ / (m v) for non-relativistic
    Set Δx = ℓ_Planck = sqrt(ħG/c³)

    Returns:
        Velocity (m/s)
    """
    planck_length = math.sqrt(HBAR * G / C**3)
    # Non-relativistic approximation: v = ħ / (m * Δx)
    v_nonrel = HBAR / (M * planck_length)

    # Relativistic correction needed if v approaches c
    if v_nonrel > 0.1 * C:
        # Solve relativistically: p = γmv = ħ / Δx
        # γv = ħ / (m Δx)
        target = HBAR / (M * planck_length)
        # v = c * target / sqrt(c^2 + target^2)
        v_rel = C * target / math.sqrt(C**2 + target**2)
        return v_rel
    else:
        return v_nonrel

def expanded_shatter_analysis():
    """Run expanded shatter threshold analysis."""
    print("=" * 80)
    print("EXPANDED SHATTER THRESHOLD ANALYSIS")
    print("Photon Rubber Ball System: Fracture, Viscoelasticity, and Quantum Gravity")
    print("=" * 80)

    print("\nSystem Parameters:")
    print(f"  Mass: {M:.3e} kg | Radius: {R*1e9:.1f} nm | Density: {DENSITY:.1f} kg/m³")
    print(f"  Young's Modulus: {E/1e6:.1f} MPa | Shear Modulus: {SHEAR_MODULUS/1e6:.1f} MPa")
    print(f"  Yield Stress: {YIELD_STRESS/1e6:.1f} MPa | UTS: {ULTIMATE_TENSILE_STRESS/1e6:.1f} MPa")
    print(f"  Fracture Toughness: {FRACTURE_TOUGHNESS:.0f} Pa·√m | Loss Tangent: {TANDELTA}")

    # 1. Detailed Fracture Analysis
    print("\n1. FRACTURE MECHANICS ANALYSIS:")
    print("   Crack Length (m)   | Griffith σ_f (MPa) | Irwin σ_f (MPa) | Notes")
    print("   -------------------|--------------------|-----------------|-------")

    crack_lengths = [1e-12, 1e-10, 1e-9, 1e-8, 1e-7, 1e-6, 1e-5]
    for a in crack_lengths:
        sigma_g = griffith_fracture_stress(a) / 1e6
        a_eff = irwin_oplastic_modification(a)
        sigma_i = griffith_fracture_stress(a_eff) / 1e6
        notes = ""
        if a < 1e-9:
            notes = "atomic scale"
        elif a > 1e-6:
            notes = "visible flaw"
        print(f"   {a:10.0e} | {sigma_g:17.1f} | {sigma_i:15.1f} | {notes}")

    # 2. Viscoelastic Effects
    print("\n2. VISCOELASTIC EFFECTS ON FRACTURE:")
    strain_rates = [1e-3, 1e-1, 1e1, 1e3, 1e5]
    print("   Strain Rate (1/s) | Base Toughness (Pa√m) | Enhanced Toughness (Pa√m) | Enhancement")
    print("   ------------------|-----------------------|---------------------------|------------")
    for rate in strain_rates:
        base = FRACTURE_TOUGHNESS
        enhanced = viscoelastic_fracture_enhancement(rate, base)
        enhancement = enhanced / base
        print(f"   {rate:10.1f} | {base:22.0f} | {enhanced:26.0f} | {enhancement:10.1f}×")

    # 3. Impact Angle Dependence
    print("\n3. IMPACT ANGLE DEPENDENCY:")
    angles = [0, 15, 30, 45, 60, 75, 90]
    print("   Angle (°) | Angular Factor | Relative Fracture Energy")
    print("   ----------|----------------|--------------------------")
    for angle in angles:
        factor = math.cos(math.radians(angle))**2
        print(f"   {angle:9.0f} | {factor:13.3f} | {factor:25.3f}")

    # 4. Critical Energy Calculations
    print("\n4. CRITICAL IMPACT ENERGIES FOR FRACTURE:")
    angles_deg = [0, 30, 60]
    print("   Angle (°) | Critical Energy (J) | Equivalent Velocity (m/s)")
    print("   ----------|---------------------|---------------------------")
    for angle in angles_deg:
        energy_crit = critical_impact_energy_for_fracture(math.radians(angle))
        # Velocity for equivalent energy (non-relativistic)
        v_equiv = math.sqrt(2 * energy_crit / M)
        print(f"   {angle:9.0f} | {energy_crit:20.3e} | {v_equiv:26.1f}")

    # 5. Strain Rate and Viscoelastic Fracture
    print("\n5. STRAIN RATE DEPENDENT FRACTURE THRESHOLD:")
    impact_velocities = [1, 10, 100, 1000, 10000]  # m/s
    print("   Impact v (m/s) | Strain Rate (1/s) | Fracture Toughness (Pa√m) | Notes")
    print("   ---------------|-------------------|---------------------------|-------")
    for v in impact_velocities:
        strain_rate = strain_rate_from_impact(v)
        toughness = viscoelastic_fracture_enhancement(strain_rate)
        notes = ""
        if strain_rate > 1e4:
            notes = "high rate"
        elif strain_rate < 1e-1:
            notes = "quasi-static"
        print(f"   {v:15.0f} | {strain_rate:16.1f} | {toughness:26.0f} | {notes}")

    # 6. Quantum Gravity Probing
    print("\n6. QUANTUM GRAVITY PROBING CAPABILITIES:")
    test_velocities = [1, 100, 1000, 10000, 1e5, 1e6, 1e7, 0.001*C, 0.01*C, 0.1*C]
    print("   Impact v (m/s)   | Momentum Transfer (kg·m/s) | Δx (m)          | ℓ_Planck (m)   | Ratio")
    print("   -----------------|----------------------------|-----------------|----------------|------")
    planck_length = math.sqrt(HBAR * G / C**3)
    for v in test_velocities:
        if v >= C:
            v = 0.99 * C  # Cap below c
        momentum = 2 * M * v  # Elastic reflection
        delta_x = HBAR / momentum
        ratio = delta_x / planck_length
        print(f"   {v:15.0f} | {momentum:28.3e} | {delta_x:16.3e} | {planck_length:15.3e} | {ratio:5.2f}")

    # 7. Expanded Scenario Analysis
    print("\n7. EXPANDED SCENARIO ANALYSIS:")
    print("   Scenario                     | v (m/s)     | E_kin (J)     | E_rel (J)     | Fracture? | Viscoel. Enh. | QG Scale (m)    | Notes")
    print("   ---------------------------|-------------|---------------|---------------|-----------|---------------|-----------------|-----------------------")

    scenarios = [
        ("Optical tweezers", 1e-3),
        ("Brownian motion", THERMAL_VELOCITY),
        ("Sound in air", 340),
        ("Ultrasonic cleaning", 20),
        ("Water droplet impact", 10),
        ("Sand particle impact", 100),
        ("Bullet impact", 800),
        ("Hypervelocity impact", 8000),
        ("Laser ablation", 1e4),
        ("Railgun projectile", 2e4),
        ("Meteorite impact", 2e4),
        ("Relativistic electron", 0.9*C),
        ("Ultra-relativistic proton", 0.99*C),
        ("LHC proton beam", 0.999999*C),
        ("Planck energy photon", C)  # Though this is a photon, not massive particle
    ]

    for label, velocity in scenarios:
        if velocity >= C:
            velocity = 0.999 * C

        # Kinetic and relativistic energy
        ke_classical = 0.5 * M * velocity**2
        if velocity < C:
            gamma = 1.0 / math.sqrt(1.0 - (velocity**2 / C**2))
            ke_rel = (gamma - 1.0) * M * C**2
        else:
            ke_rel = float('inf')

        # Fracture assessment
        strain_rate = strain_rate_from_impact(velocity)
        fracture_toughness = viscoelastic_fracture_enhancement(strain_rate)
        # Estimate if fracture occurs (simplified)
        impact_pressure = DENSITY * velocity**2  # Water hammer approx
        hoop_stress = impact_pressure * R / (2 * R)  # Simplified for sphere
        fracture_occurs = hoop_stress > (fracture_toughness**2 * E / (math.pi * CHARACTERISTIC_FLAW**2))**0.5  # Simplified

        # Viscoelastic enhancement
        enhancement = viscoelastic_fracture_enhancement(strain_rate, 1.0)  # Relative enhancement

        # Quantum gravity scale probed
        qg_scale = quantum_gravity_length_scale_from_impact(velocity)

        notes = []
        if velocity > SOUND_SPEED_LONGITUDINAL:
            notes.append("supersonic")
        if velocity > 0.01*C:
            notes.append("relativistic")
        if enhancement > 2.0:
            notes.append("VE strong")
        if qg_scale < 1e-18:
            notes.append("QG scale")

        note_str = ", ".join(notes)

        print(f"   {label:29} | {velocity:10.1f} | {ke_classical:12.3e} | {ke_rel:12.3e} | {str(fracture_occurs):9} | {enhancement:12.1f}× | {qg_scale:16.2e} | {note_str}")

    # 8. Expanded Connections to Unsolved Theories
    print("\n" + "=" * 80)
    print("EXPANDED CONNECTIONS TO UNSOLVED THEORIES:")
    print("=" * 80)
    print("  ✓ Quantum Gravity & Spacetime Foam:")
    print("    - Impact energies probe spacetime structure via uncertainty principle")
    print("    - Planck scale accessibility: Δx ≈ ħ/Δp from impact momentum transfer")
    print("    - Spacetime foam models predict modifications to dispersion relations")
    print("    - High-energy impacts may reveal decoherence from quantum geometry")
    print("  ✓ Black Hole Formation & Information Paradox:")
    print("    - Hoop conjecture: C ≤ 4πGM/c² gives collapse threshold")
    print("    - Apparent horizon formation in relativistic impacts")
    print("    - Information scattering in fragmentation vs. unitary evolution")
    print("    - Fragmentation entropy vs. Bekenstein-Hawking entropy")
    print("  ✓ Quantum Critical Points & Universality:")
    print("    - Yield point, fracture point as quantum phase transitions")
    print("    - Critical exponents and scaling near failure thresholds")
    print("    - Universality classes connecting rubber fracture to other systems")
    print("    - Renormalization group flow in viscoelastic fracture")
    print("  ✓ Non-Equilibrium Thermodynamics & Fluctuation Theorems:")
    print("    - Fragmentation as irreversible process with entropy production")
    print("    - Work distributions from impact ensembles test Jarzynski equality")
    print("    - Measurement back-action in fragment tracking")
    print("    - Shock wave dynamics and entropy gradients")
    print("  ✓ Cosmological Phase Transitions & Inflation:")
    print("    - Rapid expansion analogs in post-impact dynamics")
    print("    - Bubble nucleation and collision in fragmentation")
    print("    - Reheating analogs from elastic wave thermalization")
    print("    - Topological defect formation in crack networks")
    print("  ✓ High-Energy Quantum Gravity & Trans-Planckian Physics:")
    print("    - Lorentz invariance violation tests from dispersion modifications")
    print("    - Modified dispersion relations from quantum gravity effects")
    print("    - Possible mini-black hole or string ball production analogs")
    print("  ✓ Complex Systems & Emergent Phenomena:")
    print("    - Self-organized criticality in fracture networks")
    print("    - Avalanche statistics and power-law distributions")
    print("    - Connection to sandpile models and crackling noise")
    print("    - Emergent geometry from entanglement in fragmented states")

    # 9. Practical Experimental Recommendations
    print("\n9. PRACTICAL EXPERIMENTAL RECOMMENDATIONS:")
    print("  • Low-energy regime (v < 10 m/s): Study viscoelastic effects, ")
    print("    strain-rate dependent fracture, and quantum measurement back-action")
    print("  • Ultrasonic regime (10 < v < 100 m/s): Probe fracture initiation, ")
    print("    crack propagation, and sound wave emission")
    print("  • Hypervelocity regime (100 < v < 1000 m/s): Investigate shock ")
    print("    formation, melting thresholds, and plasma creation")
    print("  • Relativistic regime (v > 0.001c): Explore relativistic ")
    print("    effects, time dilation in decay products, and aberration")
    print("  • Ultra-relativistic regime (v > 0.1c): Investigate ")
    print("    relativistic shock waves, particle production analogs,")
    print("    and effective metric modifications")
    print("  • Quantum gravity regime (v > 0.01c): Where Δx approaches ")
    print("    femtometer scale, testing spacetime discreteness models")
    print("  • Planck scale regime (v > 0.9c): Where impact energies ")
    print("    approach Planck scale - currently infeasible but valuable")
    print("    for theoretical framework development")
    print("  • Alternative approaches:")
    print("    - Use laser-induced stress waves instead of particle impacts")
    print("    - Employ pulsed lasers for controlled energy deposition")
    print("    - Use nanoparticle aggregates to simulate effective media")
    print("    - Employ optical tweezers for precise manipulation and measurement")

    return {
        'yield_strain': YIELD_STRESS / E,
        'fracture_energy_scaling': critical_impact_energy_for_fracture(0.0),
        'quantum_gravity_scale_at_1km_s': quantum_gravity_length_scale_from_impact(1000.0),
        'planck_probing_velocity': planck_scale_probing_velocity()
    }

if __name__ == "__main__":
    # Run the expanded shatter threshold analysis
    results = expanded_shatter_analysis()

    print("\n" + "=" * 80)
    print("Analysis complete. Results available in returned dictionary.")
    print("=" * 80)