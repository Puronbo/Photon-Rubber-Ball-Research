#!/usr/bin/env python3
"""
Shatter Threshold Analysis for Photon Rubber Ball System

This script explores the conditions under which the photon-sized rubber ball
would shatter or fracture under high-energy impacts, connecting to fracture
mechanics, material failure limits, and potential analogies to gravitational
collapse or black hole formation.

Connections to unsolved theories:
- Quantum gravity and spacetime discreteness at Planck scales
- Black hole formation thresholds and hoop conjecture
- Quantum critical points and phase transitions
- Information loss in irreversible processes
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

# Material properties for rubber (approximate)
YIELD_STRESS = 10e6     # Yield stress (Pa) - typical for rubber
ULTIMATE_TENSILE_STRESS = 20e6  # Ultimate tensile stress (Pa)
FRACTURE_TOUGHNESS = 1000       # Fracture toughness (Pa·√m) - typical for rubber
DENSITY = 1100.0                # Density (kg/m³)
POISSON_RATIO = NU

# Derived quantities
VOLUME = 4/3 * math.pi * R**3
SURFACE_AREA = 4 * math.pi * R**2
E_STAR = E / (2 * (1 - NU**2))  # Effective modulus

# ============================================================================
# FRACTURE AND FAILURE ANALYSIS
# ============================================================================

def kinetic_impact_energy(velocity: float) -> float:
    """
    Calculate kinetic energy of impact.

    Args:
        velocity: Impact velocity (m/s)

    Returns:
        Kinetic energy (J)
    """
    return 0.5 * M * velocity**2

def relativistic_kinetic_energy(velocity: float) -> float:
    """
    Calculate relativistic kinetic energy.

    Args:
        velocity: Impact velocity (m/s)

    Returns:
        Relativistic kinetic energy (J)
    """
    if velocity >= C:
        return float('inf')
    gamma = 1.0 / math.sqrt(1.0 - (velocity**2 / C**2))
    return (gamma - 1.0) * M * C**2

def hoop_stress_from_impact(impact_pressure: float, radius: float = None,
                           wall_thickness: float = None) -> float:
    """
    Calculate hoop stress in spherical shell from internal pressure.

    For a sphere under uniform pressure, hoop stress = PR/(2t)
    Where P = pressure, R = radius, t = wall thickness

    Args:
        impact_pressure: Pressure from impact (Pa)
        radius: Sphere radius (m) - defaults to system radius
        wall_thickness: Effective wall thickness (m) - if None, uses radius

    Returns:
        Hoop stress (Pa)
    """
    if radius is None:
        radius = R
    if wall_thickness is None:
        wall_thickness = radius  # Simplified: treat as solid sphere with characteristic length

    return impact_pressure * radius / (2 * wall_thickness)

def impact_pressure_from_velocity(velocity: float, impact_time: float = None) -> float:
    """
    Estimate impact pressure from velocity and impact duration.

    Pressure = Force / Area
    Force = rate of momentum change = (momentum per impact) / (time between impacts)
    For single impact: F ≈ Δp / Δt

    Args:
        velocity: Impact velocity (m/s)
        impact_time: Impact duration (s) - if None, estimated from material properties

    Returns:
        Estimated impact pressure (Pa)
    """
    if impact_time is None:
        # Estimate impact time from material properties
        # Time for stress wave to cross sphere: t ≈ 2R / c_sound
        # Sound speed in rubber: c_sound ≈ sqrt(E/(ρ(1-ν²)))
        sound_speed = math.sqrt(E / (DENSITY * (1 - NU**2)))
        impact_time = 2 * R / sound_speed

    # Momentum change for elastic reflection: Δp = 2mv
    momentum_change = 2 * M * velocity

    # Average force during impact
    force = momentum_change / impact_time

    # Impact area (approximate as contact area)
    # For Hertz contact: a = (FR/E*)^(1/3) but we need iterative solution
    # Simplified: use geometric cross-section for estimation
    impact_area = math.pi * R**2

    return force / impact_area

def griffith_fracture_criterion(stress: float, crack_length: float = None,
                              surface_energy: float = None) -> bool:
    """
    Check if stress exceeds Griffith fracture criterion.

    Griffith criterion: σ_f = sqrt(2Eγ/(πa))
    where σ_f = fracture stress, E = Young's modulus,
          γ = surface energy, a = crack length

    Args:
        stress: Applied stress (Pa)
        crack_length: Characteristic crack length (m) - if None, uses atomic scale
        surface_energy: Surface energy (J/m²) - if None, estimated for rubber

    Returns:
        True if fracture should occur, False otherwise
    """
    if crack_length is None:
        # Atomic scale crack length
        crack_length = 0.3e-9  # 0.3 nm (approximate bond length)
    if surface_energy is None:
        # Surface energy for rubber (approximate)
        surface_energy = 0.05  # J/m² (typical for polymers)

    # Griffith fracture stress
    sigma_f = math.sqrt(2 * E * surface_energy / (math.pi * crack_length))

    return stress >= sigma_f

def yield_criterion(stress: float, yield_stress: float = None) -> bool:
    """
    Check if stress exceeds yield criterion.

    Args:
        stress: Applied stress (Pa)
        yield_stress: Yield stress (Pa) - if None, uses typical rubber value

    Returns:
        True if yielding should occur, False otherwise
    """
    if yield_stress is None:
        yield_stress = YIELD_STRESS

    return stress >= yield_stress

def ultimate_tensile_strength_criterion(stress: float,
                                      uts: float = None) -> bool:
    """
    Check if stress exceeds ultimate tensile strength.

    Args:
        stress: Applied stress (Pa)
        uts: Ultimate tensile stress (Pa) - if None, uses typical rubber value

    Returns:
        True if failure should occur, False otherwise
    """
    if uts is None:
        uts = ULTIMATE_TENSILE_STRESS

    return stress >= uts

def schwarzschild_condition(mass: float = None,
                           radius: float = None) -> bool:
    """
    Check if system meets Schwarzschild condition (black hole formation).

    Condition: R ≤ 2GM/c²

    Args:
        mass: Mass (kg) - if None, uses system mass
        radius: Radius (m) - if None, uses system radius

    Returns:
        True if Schwarzschild condition satisfied, False otherwise
    """
    if mass is None:
        mass = M
    if radius is None:
        radius = R

    schwarzschild_radius = 2 * G * mass / C**2
    return radius <= schwarzschild_radius

def hoop_conjecture_condition(mass: float = None,
                             circumference: float = None) -> bool:
    """
    Check if system meets hoop conjecture condition for black hole formation.

    Hoop conjecture: Black hole forms when mass is compressed into a region
    whose circumference in every direction is ≤ 4πM (in geometric units).

    In SI units: C ≤ 4πGM/c²

    Args:
        mass: Mass (kg) - if None, uses system mass
        circumference: Circumference (m) - if None, uses sphere circumference

    Returns:
        True if hoop conjecture condition satisfied, False otherwise
    """
    if mass is None:
        mass = M
    if circumference is None:
        circumference = 2 * math.pi * R  # Sphere circumference

    critical_circumference = 4 * math.pi * G * mass / C**2
    return circumference <= critical_circumference

def planck_density_condition(mass: float = None,
                           volume: float = None) -> bool:
    """
    Check if density reaches Planck density.

    Planck density: ρ_Planck = c^5/(ħG²) ≈ 5.16×10^96 kg/m³

    Args:
        mass: Mass (kg) - if None, uses system mass
        volume: Volume (m³) - if None, uses system volume

    Returns:
        True if Planck density condition satisfied, False otherwise
    """
    if mass is None:
        mass = M
    if volume is None:
        volume = VOLUME

    planck_density = C**5 / (HBAR * G**2)
    actual_density = mass / volume

    return actual_density >= planck_density

def calculate_shatter_thresholds():
    """Calculate various thresholds for shattering/failure."""
    print("=" * 70)
    print("SHATTER THRESHOLD ANALYSIS")
    print("Photon Rubber Ball System Under High-Energy Impacts")
    print("=" * 70)

    print("\nSystem Parameters:")
    print(f"  Sphere mass: {M:.3e} kg ({M / 1.660539e-27:.0f} amu)")
    print(f"  Sphere radius: {R*1e9:.1f} nm")
    print(f"  Volume: {VOLUME*1e24:.3f} nm³")
    print(f"  Density: {DENSITY:.1f} kg/m³")
    print(f"  Young's modulus: {E/1e6:.1f} MPa")
    print(f"  Yield stress: {YIELD_STRESS/1e6:.1f} MPa")
    print(f"  Ultimate tensile stress: {ULTIMATE_TENSILE_STRESS/1e6:.1f} MPa")
    print(f"  Fracture toughness: {FRACTURE_TOUGHNESS:.0f} Pa·√m")

    # 1. Conventional failure thresholds
    print("\n1. CONVENTIONAL FAILURE THRESHOLDS:")

    # Velocity for yield stress
    # Impact pressure ≈ ρv² for water hammer analogy (order of magnitude)
    # More accurately: for elastic impact, max pressure ∝ (Ev²ρ)^(1/3)
    # Using simplified relation: P ≈ ρv²
    v_yield = math.sqrt(YIELD_STRESS / DENSITY)
    v_uts = math.sqrt(ULTIMATE_TENSILE_STRESS / DENSITY)
    v_fracture_estimate = math.sqrt((FRACTURE_TOUGHNESS**2 * E) / (math.pi * DENSITY**3 * (0.3e-9)))  # Simplified

    print(f"  Velocity for yield stress (approx): {v_yield:.1f} m/s")
    print(f"  Velocity for UTS (approx): {v_uts:.1f} m/s")
    print(f"  Velocity for fracture estimate: {v_fracture_estimate:.1f} m/s")

    # Kinetic energies at these velocities
    ke_yield = 0.5 * M * v_yield**2
    ke_uts = 0.5 * M * v_uts**2
    ke_fracture = 0.5 * M * v_fracture_estimate**2

    print(f"  Kinetic energy at yield: {ke_yield:.3e} J")
    print(f"  Kinetic energy at UTS: {ke_uts:.3e} J")
    print(f"  Kinetic energy at fracture: {ke_fracture:.3e} J")

    # 2. Relativistic regime
    print("\n2. RELATIVISTIC REGIME:")
    print(f"  Speed of light: {C:.0f} m/s")
    print(f"  Rest mass energy: {M*C**2:.3e} J")
    print(f"  Velocity where KE_rel = 2*KE_classical: {C/math.sqrt(3):.0f} m/s")
    print(f"  Velocity where KE_rel = 10*KE_classical: {C*math.sqrt(0.99):.0f} m/s")

    # Velocity where relativistic corrections become significant (>1%)
    v_rel_1percent = C * math.sqrt(1 - (1/1.01)**2)
    print(f"  Velocity for 1% relativistic correction: {v_rel_1percent:.0f} m/s")

    # 3. Gravitational collapse analogs
    print("\n3. GRAVITATIONAL COLLAPSE ANALOGS:")
    schwarzschild_r = 2 * G * M / C**2
    hoop_circumference = 4 * math.pi * G * M / C**2
    planck_density = C**5 / (HBAR * G**2)

    print(f"  Schwarzschild radius: {schwarzschild_r*1e15:.3f} fm")
    print(f"  Actual radius: {R*1e9:.1f} nm")
    print(f"  Radius/Schwarzschild ratio: {R/schwarzschild_r:.3e}")
    print(f"  Hoop conjecture circumference: {hoop_circumference*1e9:.1f} nm")
    print(f"  Actual circumference: {2*math.pi*R*1e9:.1f} nm")
    print(f"  Circumference ratio: {(2*math.pi*R)/hoop_circumference:.3f}")
    print(f"  Planck density: {planck_density:.3e} kg/m³")
    print(f"  Actual density: {DENSITY:.3e} kg/m³")
    print(f"  Density ratio: {DENSITY/planck_density:.3e}")

    # Check conditions
    print("\n  Condition checks:")
    print(f"    Schwarzschild condition (R ≤ 2GM/c²): {schwarzschild_condition()}")
    print(f"    Hoop conjecture (C ≤ 4πGM/c²): {hoop_conjecture_condition()}")
    print(f"    Planck density (ρ ≥ ρ_Planck): {planck_density_condition()}")

    # 4. Impact velocity thresholds for various phenomena
    print("\n4. IMPACT VELOCITY THRESHOLDS:")

    # Thermal velocity at room temperature
    v_thermal = math.sqrt(3 * K_B * 300.0 / DENSITY)
    print(f"  Thermal velocity (300K): {v_thermal:.1f} m/s")

    # Sound velocity in material
    v_sound = math.sqrt(E_STAR / DENSITY)
    print(f"  Sound velocity in material: {v_sound:.1f} m/s")

    # Velocity where kinetic energy equals rest mass energy (classical)
    v_ke_eq_mc2 = math.sqrt(2 * C**2)  # From ½mv² = mc² → v = √2 c (unphysical, shows relativity needed)
    # Correct relativistic solution: (γ-1)mc² = mc² → γ = 2 → v = √3/2 c
    v_ke_rel_eq_mc2 = math.sqrt(3)/2 * C
    print(f"  Velocity where classical KE = mc²: {v_ke_eq_mc2:.0f} m/s ({v_ke_eq_mc2/C*100:.1f}% c) [>c ⇒ classical model invalid]")
    print(f"  Velocity where relativistic KE = mc²: {v_ke_rel_eq_mc2:.0f} m/s ({v_ke_rel_eq_mc2/C*100:.1f}% c)")

    # Velocity where momentum equals Planck momentum
    planck_momentum = math.sqrt(HBAR * C**3 / G)
    v_planck_momentum = planck_momentum / M
    print(f"  Velocity for Planck momentum: {v_planck_momentum:.0f} m/s ({v_planck_momentum/C*100:.1f}% c)")

    # 5. Energy density thresholds
    print("\n5. ENERGY DENSITY THRESHOLDS:")

    # Rest mass energy density
    rho_rest_energy = M * C**2 / VOLUME
    print(f"  Rest mass energy density: {rho_rest_energy:.3e} J/m³")

    # Planck energy density
    planck_energy_density = C**7 / (HBAR**2 * G**2)
    print(f"  Planck energy density: {planck_energy_density:.3e} J/m³")
    print(f"  Ratio (actual/Planck): {(M*C**2/VOLUME)/planck_energy_density:.3e}")

    # Yield energy density
    yield_energy_density = YIELD_STRESS  # Pa = J/m³
    print(f"  Yield energy density: {yield_energy_density:.3e} J/m³")
    print(f"  Ratio (yield/rest mass): {yield_energy_density/rho_rest_energy:.3e}")

    # 6. Time scales
    print("\n6. TIME SCALES:")

    # Light crossing time
    t_light = 2 * R / C
    print(f"  Light crossing time: {t_light*1e15:.3f} fs")

    # Planck time
    t_planck = math.sqrt(HBAR * G / C**5)
    print(f"  Planck time: {t_planck*1e45:.3e} s")

    # Characteristic mechanical time
    t_mech = R / v_sound
    print(f"  Mechanical response time: {t_mech*1e12:.3f} ps")

    # Impact duration estimate
    t_impact = 2 * R / v_sound  # Approximate
    print(f"  Estimated impact duration: {t_impact*1e12:.3f} ps")

    # 7. Scenario analysis
    print("\n7. SCENARIO ANALYSIS:")

    scenarios = [
        ("Typical laser tweezers", 1e-3, "m/s"),
        ("Sound wave in air", 340, "m/s"),
        ("Bullet impact", 800, "m/s"),
        ("Hypervelocity impact", 8000, "m/s"),
        ("Laser ablation plume", 1e4, "m/s"),
        ("Relativistic electron beam", 0.9*C, "m/s"),
        ("Ultra-relativistic proton", 0.99*C, "m/s"),
        ("Planck velocity", C, "m/s")
    ]

    print("  Scenario              | Velocity     | KE (J)       | Rel KE (J)   | Yield? | UTS? | Fracture? | Notes")
    print("  ----------------------|--------------|--------------|--------------|--------|------|-----------|-------")

    for label, velocity, unit in scenarios:
        if unit == "m/s" and velocity > C:
            velocity = C  # Cap at speed of light

        ke_classical = 0.5 * M * velocity**2
        if velocity < C:
            gamma = 1.0 / math.sqrt(1.0 - (velocity**2 / C**2))
            ke_rel = (gamma - 1.0) * M * C**2
        else:
            ke_rel = float('inf')

        # Estimate impact pressure and check failure
        impact_p = impact_pressure_from_velocity(velocity)
        hoop_stress = hoop_stress_from_impact(impact_p)
        yields = yield_criterion(hoop_stress)
        uts_fail = ultimate_tensile_strength_criterion(hoop_stress)

        # Fracture check (using estimated crack length)
        fracture_occurs = griffith_fracture_criterion(hoop_stress, crack_length=1e-9)  # 1 nm crack

        notes = []
        if velocity >= 0.1*C:
            notes.append("relativistic")
        if velocity >= 0.5*C:
            notes.append("highly relativistic")
        if ke_classical >= M*C**2:
            notes.append("KE > mc²")
        if schwarzschild_condition(M + ke_classical/C**2, R):  # Approximate mass increase
            notes.append("BH possible")

        note_str = ", ".join(notes) if notes else ""

        print(f"  {label:22} | {velocity:10.1f} | {ke_classical:12.3e} | {ke_rel:12.3e} | {str(yields):5} | {str(uts_fail):5} | {str(fracture_occurs):9} | {note_str}")

    # 8. Connections to unsolved theories
    print("\n" + "=" * 70)
    print("CONNECTIONS TO UNSOLVED THEORIES:")
    print("=" * 70)
    print("  ✓ Quantum Gravity & Spacetime Discreteness:")
    print("    Planck density/energy thresholds test limits of spacetime continuity")
    print("    Impact energies approaching Planck scale may reveal discreteness")
    print("    Black hole formation analogs via hoop conjecture and Schwarzschild condition")
    print("  ✓ Black Hole Formation & Thermodynamics:")
    print("    Hoop conjecture gives threshold for gravitational collapse")
    print("    Bekenstein-Hawking entropy applies if BH forms: S = kAc³/(4Għ)")
    print("    Hawking temperature: T = ħc³/(8πGMk_B)")
    print("  ✓ Quantum Critical Points & Phase Transitions:")
    print("    Yield point, fracture point as analogs to quantum phase transitions")
    print("    Critical exponents and scaling behavior near failure thresholds")
    print("  ✓ Information Loss & Irreversibility:")
    print("    Shattering represents irreversible information loss (fragment positions/momenta)")
    print("    Connection to black hole information paradox and unitary evolution")
    print("  ✓ High-Energy Quantum Gravity:")
    print("    Trans-Planckian effects in collider analogs")
    print("    Possible mini-black hole production in high-energy impacts")
    print("  ✓ Non-Equilibrium Thermodynamics:")
    print("    Shock wave formation, rarefaction waves, and entropy production")
    print("    Connection to fluctuation theorems in far-from-equilibrium regimes")
    print("  ✓ Cosmic Inflation & Phase Transitions:")
    print("    Rapid expansion analogs in post-impact dynamics")
    print("    Bubble nucleation and collision analogs in multiverse scenarios")

    # 9. Practical recommendations
    print("\n9. PRACTICAL RECOMMENDATIONS FOR EXPERIMENTAL EXPLORATION:")
    print("  • To study conventional failure: Impact velocities ~1-100 m/s")
    print("  • To study relativistic effects: Impact velocities > 0.01c (>3,000 km/s)")
    print("  • To approach BH analogs: Need densities > 10^20 kg/m³ (unachievable)")
    print("  • To study quantum gravity signatures: Impacts near Planck energy")
    print("    (requires ~10^19 GeV photons - currently infeasible)")
    print("  • Alternative approach: Use collective effects in many-sphere systems")
    print("    to simulate effective field theory or hydrodynamic analogs")
    print("  • Table-top analogies: Use fluid vortices, BECs, or optical systems")
    print("    to simulate effective metrics and horizons")

    return {
        'yield_velocity': v_yield,
        'uts_velocity': v_uts,
        'schwarzschild_radius': schwarzschild_r,
        'planck_density': planck_density,
        'light_crossing_time': t_light,
        'planck_time': t_planck
    }

if __name__ == "__main__":
    # Run the shatter threshold analysis
    results = calculate_shatter_thresholds()

    print("\n" + "=" * 70)
    print("Analysis complete. Results available in returned dictionary.")
    print("=" * 70)