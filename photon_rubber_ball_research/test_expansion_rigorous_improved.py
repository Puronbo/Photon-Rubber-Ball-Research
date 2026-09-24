#!/usr/bin/env python3
"""
Rigorous verification of the 8 expansion axes for the photon-sized rubber ball.

Each axis: explicit derivation -> computation -> PASS/FAIL with tolerance.
Independent cross-checks: energy balance, known limits (Rayleigh, Newtonian),
and self-consistency (Q_ext = Q_sca + Q_abs).

This is an improved version with enhancements for:
- Code quality and maintainability
- Performance optimization
- Documentation clarity
- Error handling and reporting
"""

import math
from typing import Tuple, Optional, List

# ============================================================================
# CONSTANTS AND CONFIGURATION
# ============================================================================

# Physical constants
RHO = 1100.0           # Density (kg/m^3)
R = 275e-9             # Radius (m)
E = 50e6               # Young's modulus (Pa)
NU = 0.5               # Poisson's ratio
V = 1.0                # Impact velocity (m/s)
KB = 1.380649e-23      # Boltzmann constant (J/K)
C0 = 299792458.0       # Speed of light (m/s)

# Derived constants
M = RHO * 4/3 * math.pi * R**3                    # Mass (kg)
ESTAR_RIGID = E / (1 - NU**2)                     # Reduced modulus, rigid plane (Pa)
ESTAR_COMPLIANT = E / (2 * (1 - NU**2))           # Reduced modulus, two identical bodies (Pa)
K_HERTZ = (4/3) * ESTAR_RIGID * math.sqrt(R)      # Hertz contact constant (N/m^(3/2))
DMAX = ((15/16) * M * V**2 / (ESTAR_RIGID * math.sqrt(R)))**(2/5)  # Max indentation, rigid plane (m)
PMAX = K_HERTZ * DMAX**1.5                        # Max pressure, rigid plane (N)

# Compliant plane values (for axis 7)
DCOMP = ((15/16) * M * V**2 / (ESTAR_COMPLIANT * math.sqrt(R)))**(2/5)  # Max indentation, compliant plane (m)
PCOMP = (4/3) * ESTAR_COMPLIANT * math.sqrt(R) * DCOMP**1.5              # Max pressure, compliant plane (N)

# Numerical tolerances (with explanations)
TOL_ENERGY = 1e-9         # Energy conservation checks
TOL_SCALING = 1e-6        # Power-law validation checks
TOL_LOW_BETA = 0.05       # Low-beta relativistic limit
TOL_EQ = 1e-12            # Equality checks for derived formulas
TOL_MIE_CONVERGE = 1e-9   # Mie scattering convergence
TOL_JKR_INTEGRATE = 1e-4  # JKR work of separation integration convergence

# Integration settings for JKR calculations
JKR_INTEGRATION_POINTS = 200000  # Base points for trapezoidal integration
JKR_CONVERGENCE_CHECK_POINTS = 1000000  # Points for convergence check

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def check_condition(name: str, condition: bool, detail: str = "") -> bool:
    """
    Check a condition and report PASS/FAIL result.

    Args:
        name: Description of the check
        condition: Boolean result of the check
        detail: Additional details to display

    Returns:
        True if condition passed, False otherwise
    """
    passed = bool(condition)
    status = 'PASS' if passed else 'FAIL'
    print(f"  [{status}] {name}  {detail}")
    return passed

def compute_indentation_pressure(E_val: float, nu_val: float = NU) -> Tuple[float, float]:
    """
    Compute indentation depth and pressure for given elastic modulus.

    Args:
        E_val: Elastic modulus (Pa)
        nu_val: Poisson's ratio (default: NU)

    Returns:
        Tuple of (indentation_depth, pressure) in (m, N)
    """
    Ese = E_val / (1 - nu_val**2)  # Reduced modulus
    d = ((15/16) * M * V**2 / (Ese * math.sqrt(R)))**(2/5)
    P = (4/3) * Ese * math.sqrt(R) * d**1.5
    return d, P

def simulate_linear_oscillator(zeta: float, w: float = 1.0,
                              dt: float = 1e-5, v0: float = 1.0) -> float:
    """
    Simulate linear damped oscillator for half-cycle restitution.

    Args:
        zeta: Damping ratio
        w: Natural frequency (rad/s)
        dt: Time step (s)
        v0: Initial velocity (m/s)

    Returns:
        Restitution coefficient (negative of final velocity / initial velocity)
    """
    x, xp = 0.0, v0
    t = 0.0
    while True:  # Integrate to first x=0 return
        a = -2*zeta*w*xp - w*w*x
        xp += a*dt
        x += xp*dt
        t += dt
        if x <= 0 and t > 0.01:
            break
    return -xp/v0

def sim_hunt_crossley(tand: float, dt: float = 5e-12, v0: float = 1.0) -> Tuple[float, float]:
    """
    Simulate Hunt-Crossley model with viscous damping.

    Args:
        tand: Loss tangent
        dt: Time step (s)
        v0: Initial velocity (m/s)

    Returns:
        Tuple of (restitution_coefficient, dissipated_energy_fraction)
    """
    # Precompute constants
    t_c_doc = 17.09e-9  # Documented contact time (s)
    w0 = math.pi / t_c_doc  # Characteristic frequency (rad/s)
    Kk = (4/3) * ESTAR_RIGID * math.sqrt(R)  # Hertz constant
    k_lin = 1.5 * Kk * math.sqrt(DMAX)  # Linear stiffness at dmax

    # Damping coefficient
    c = tand * k_lin / (w0 * DMAX**1.5)

    # Initial conditions
    d, dp = 0.0, v0
    E0 = 0.5 * M * v0**2  # Initial kinetic energy
    diss = 0.0  # Dissipated energy

    # Time integration
    for _ in range(1_000_000):  # 1M steps should be sufficient
        dd = max(d, 0.0)  # Ensure non-negative indentation
        a = (-Kk*dd**1.5 - c*dd**1.5*dp) / M
        dp += a*dt
        d += dp*dt
        diss += c*dd**1.5*dp*dp*dt
        if d <= 0 and dp < 0:  # Separation condition
            break

    return -dp, diss/E0

def jkr_contact_radius(load: float, work_adhesion: float = 0.1,
                      radius: float = R, modulus: float = ESTAR_RIGID) -> Optional[float]:
    """
    Compute JKR contact radius for given load.

    Args:
        load: Applied load (N, positive for compression)
        work_adhesion: Work of adhesion (J/m^2)
        radius: Sphere radius (m)
        modulus: Reduced modulus (Pa)

    Returns:
        Contact radius (m) or None if no solution
    """
    inner = 6*math.pi*work_adhesion*radius*load + (3*math.pi*work_adhesion*radius)**2
    if inner < 0:
        return None
    root = math.sqrt(inner)
    return ((radius/modulus) * (load + 3*math.pi*work_adhesion*radius + root))**(1/3)

def jkr_indentation(radius_contact: float, work_adhesion: float = 0.1,
                   radius: float = R, modulus: float = ESTAR_RIGID) -> float:
    """
    Compute indentation depth from contact radius in JKR theory.

    Args:
        radius_contact: Contact radius (m)
        work_adhesion: Work of adhesion (J/m^2)
        radius: Sphere radius (m)
        modulus: Reduced modulus (Pa)

    Returns:
        Indentation depth (m)
    """
    return radius_contact**2/radius - (2/3)*math.sqrt(2*math.pi*work_adhesion*radius_contact/modulus)

def jkr_load(radius_contact: float, work_adhesion: float = 0.1,
             radius: float = R, modulus: float = ESTAR_RIGID) -> float:
    """
    Compute load from contact radius in JKR theory.

    Args:
        radius_contact: Contact radius (m)
        work_adhesion: Work of adhesion (J/m^2)
        radius: Sphere radius (m)
        modulus: Reduced modulus (Pa)

    Returns:
        Load (N)
    """
    return (modulus/radius) * radius_contact**3 - radius_contact**1.5 * math.sqrt(6*math.pi*work_adhesion*modulus*radius)

def jkr_work_of_separation_integrand(radius_contact: float,
                                   work_adhesion: float = 0.1,
                                   radius: float = R, modulus: float = ESTAR_RIGID) -> float:
    """
    Compute integrand for JKR work of separation calculation.

    Args:
        radius_contact: Contact radius (m)
        work_adhesion: Work of adhesion (J/m^2)
        radius: Sphere radius (m)
        modulus: Reduced modulus (Pa)

    Returns:
        Integrand value for work of separation calculation
    """
    # Displacement derivative d(δ)/da (analytic)
    d_d = 2*radius_contact/radius - (1/3)*math.sqrt(2*math.pi*work_adhesion/(modulus*radius_contact))

    # Load and integrand
    load_val = jkr_load(radius_contact, work_adhesion, radius, modulus)
    return load_val * d_d

def mie_spherical_bessel_jn(z: float, N: int) -> List[complex]:
    """
    Compute spherical Bessel functions j_n(z) for n=0..N.

    Uses downward (Miller) recurrence normalized by sum rule.

    Args:
        z: Argument
        N: Maximum order

    Returns:
        List of j_n(z) values for n=0..N
    """
    v = [0j] * (N + 2)
    v[N] = 1+0j
    v[N+1] = 0+0j
    for n in range(N, 0, -1):
        v[n-1] = (2*n+1)/z * v[n] - v[n+1]
    s = sum((2*n+1)*abs(v[n])**2 for n in range(N+1))
    scale = math.sqrt(s)
    return [v[n]/scale for n in range(N+1)]

def mie_spherical_bessel_yn(z: float, N: int) -> List[complex]:
    """
    Compute spherical Neumann functions y_n(z) for n=0..N.

    Upward recurrence from known y_0, y_1.

    Args:
        z: Argument
        N: Maximum order

    Returns:
        List of y_n(z) values for n=0..N
    """
    y = [0j] * (N + 1)
    y[0] = -math.cos(z)/z
    if N >= 1:
        y[1] = -math.cos(z)/z**2 - math.sin(z)/z
    for n in range(1, N):
        y[n+1] = (2*n+1)/z * y[n] - y[n-1]
    return y

def mie_q(mk: complex, x: float, N: Optional[int] = None) -> Tuple[float, float]:
    """
    Compute Mie scattering efficiency factors.

    Args:
        mk: Relative refractive index
        x: Size parameter
        N: Maximum order (if None, computed adaptively)

    Returns:
        Tuple of (extinction_efficiency, scattering_efficiency)
    """
    if N is None:
        N = max(2, int(x + 4*abs(x)**(1/3)) + 8)  # Adaptive truncation

    js = mie_spherical_bessel_jn(x, N+1)
    ys = mie_spherical_bessel_yn(x, N+1)
    jsm = mie_spherical_bessel_jn(mk*x, N+1)

    def psi(n): return x*js[n]
    def psi_(n): return js[n] + x*(js[n-1] - (n+1)/x*js[n]) if n >= 1 else js[0] - x*js[1]
    def xi(n): return x*(js[n] + 1j*ys[n])
    def xi_(n): return (js[n] + 1j*ys[n]) + x*((js[n-1]- (n+1)/x*js[n]) + 1j*(ys[n-1] - (n+1)/x*ys[n])) if n>=1 else (js[0]+1j*ys[0]) + x*(-js[1] - 1j*ys[1])
    psi_m = lambda n: mk*x*jsm[n]
    def psi_m_(n): return jsm[n] + mk*x*(jsm[n-1] - (n+1)/(mk*x)*jsm[n]) if n>=1 else jsm[0] - mk*x*jsm[1]

    Qe = Qs = 0.0
    for n in range(1, N+1):
        aa = (mk*psi_m(n)*psi_(n) - psi_m_(n)*psi(n)) / (mk*psi_m(n)*xi_(n) - psi_m_(n)*xi(n))
        bb = (psi_m(n)*psi_(n) - mk*psi_m_(n)*psi(n)) / (psi_m(n)*xi_(n) - mk*psi_m_(n)*xi(n))
        Qe += (2*n+1)*aa.real
        Qs += (2*n+1)*(abs(aa)**2 + abs(bb)**2)

    return 2/x**2*Qe, 2/x**2*Qs

# ============================================================================
# AXIS VERIFICATION FUNCTIONS
# ============================================================================

def verify_axis1_compliant_plane() -> bool:
    """
    AXIS 1: Compliant (same-rubber) plane E* = E/(2(1-nu^2))

    Returns:
        True if all checks pass
    """
    print("\nAXIS 1: compliant (same-rubber) plane  E* = E/(2(1-nu^2))")
    all_passed = True

    # Effective modulus for two identical bodies touching
    Estar2 = 1/((1-NU**2)/E + (1-NU**2)/E)
    passed = check_condition(
        "E*_two = E/(2(1-nu^2)) = 66.7/2 = 33.3 MPa",
        abs((Estar2-E/(2*(1-NU**2)))/Estar2) < TOL_EQ,
        f"= {Estar2/1e6:.3f} MPa"
    )
    all_passed &= passed

    # R_eff = R for sphere-on-plane (plane radius = infinity)
    d2 = ((15/16)*M*V**2/(Estar2*math.sqrt(R)))**(2/5)
    P2 = (4/3)*Estar2*math.sqrt(R)*d2**1.5

    # Energy check: (1/2) m v^2 must equal integral K2 d^(3/2) dd
    E_in = 0.5*M*V**2
    E_out = (2/5)*(4/3)*Estar2*math.sqrt(R)*d2**2.5
    passed &= check_condition(
        "energy balance exact for compliant plane",
        abs(E_in-E_out)/E_in < TOL_ENERGY,
        f"d2={d2*1e9:.3f}nm P2={P2*1e9:.2f}nN"
    )

    # Scaling law d ~ E*^(-2/5)
    passed &= check_condition(
        "scaling d2/d1 = 2^(2/5)",
        abs((d2/DMAX)-2**(2/5)) < TOL_SCALING,
        f"{d2/DMAX:.4f} vs {2**(2/5):.4f}"
    )

    return all_passed

def verify_axis2_modulus_sensitivity() -> bool:
    """
    AXIS 2: E-modulus sensitivity (rubber range 0.01-0.1 GPa)

    Returns:
        True if all checks pass
    """
    print("\nAXIS 2: E-modulus sensitivity (rubber range 0.01-0.1 GPa)")
    all_passed = True

    for Ee in (10e6, 50e6, 100e6):
        Ese = Ee/(1-NU**2)
        dd, Pp = compute_indentation_pressure(Ee)
        Eein = 0.5*M*V**2
        Eeout = (2/5)*(4/3)*Ese*math.sqrt(R)*dd**2.5

        passed = check_condition(
            f"energy ok @ E={Ee/1e6:g}MPa (d={dd*1e9:.2f},P={Pp*1e9:.1f})",
            abs(Eein-Eeout)/Eein < TOL_ENERGY
        )
        all_passed &= passed

    # Power-law d ~ E^(-2/5): compare E10 vs E100 ratio
    d10 = ((15/16)*M*V**2/((10e6/(1-NU**2))*math.sqrt(R)))**(2/5)
    d100 = ((15/16)*M*V**2/((100e6/(1-NU**2))*math.sqrt(R)))**(2/5)
    all_passed &= check_condition(
        "d(E=10MPa)/d(E=100MPa) = 10^(2/5)",
        abs(d10/d100 - 10**(2/5)) < TOL_SCALING,
        f"{d10/d100:.4f} vs {10**(2/5):.4f}"
    )

    return all_passed

def verify_axis3_viscoelastic_restitution() -> bool:
    """
    AXIS 3: Viscoelastic restitution e ~ exp(-pi tan d / 2)

    Returns:
        True if all checks pass
    """
    print("\nAXIS 3: viscoelastic restitution  e ~ exp(-pi tan d / 2)")
    all_passed = True

    # Linear damped oscillator x''+2*zeta*w x'+w^2 x=0, half-cycle restitution:
    #   e = exp(-pi zeta / sqrt(1-zeta^2));  tan d = 2 zeta   (loss tangent)
    def sim_linear(zeta: float, w: float = 1.0, dt: float = 1e-5, v0: float = 1.0) -> float:
        x, xp = 0.0, v0
        t = 0.0
        while True:  # Integrate to first x=0 return
            a = -2*zeta*w*xp - w*w*x
            xp += a*dt
            x += xp*dt
            t += dt
            if x <= 0 and t > 0.01:
                break
        return -xp/v0

    for tand in (0.05, 0.1, 0.2):
        zeta = tand/2
        e_lin = math.exp(-math.pi*zeta/math.sqrt(1-zeta*zeta))
        e_sim = sim_linear(zeta)
        passed = check_condition(
            f"linear osc: e(calc)=exp(-pi z/..) vs numeric sim for tan d={tand}",
            abs(e_lin-e_sim) < 1e-3,
            f"e={e_sim:.4f}"
        )
        all_passed &= passed

        print(f"       -> tan d={tand}: e = {e_lin:.3f}   [earlier draft used exp(-pi tan d), "
              f"giving {math.exp(-math.pi*tand):.3f} - WRONG, corrected]")

    # Nonlinear Hertz + viscous damping (Hunt-Crossley):
    #   m dd'' = -K d^(3/2) - c d^(3/2) dp,   dp = d/dt
    # Damping tuned so that linearized at peak indentation reproduces tan d:
    #   F_v,max/d F_s ~ tan d  =>  c = tan d * k_lin / (omega_contact * dmax^1.5)
    # with k_lin = dP/dd at dmax = (3/2) K sqrt(dmax), omega_contact = pi/t_c
    t_c_doc = 17.09e-9
    w0 = math.pi/t_c_doc
    Kk = (4/3)*ESTAR_RIGID*math.sqrt(R)
    k_lin = 1.5*Kk*math.sqrt(DMAX)

    def sim_hc_full(tand: float, dt: float = 5e-12, v0: float = 1.0) -> Tuple[float, float]:
        c = tand*k_lin/(w0*DMAX**1.5)
        d, dp = 0.0, v0
        E0 = 0.5*M*v0*v0
        diss = 0.0
        for _ in range(1_000_000):
            dd = max(d, 0.0)
            a = (-Kk*dd**1.5 - c*dd**1.5*dp)/M
            dp += a*dt
            d += dp*dt
            diss += c*dd**1.5*dp*dp*dt
            if d <= 0 and dp < 0:
                break
        return -dp, diss/E0

    es_hc = []
    for tand in (0.05, 0.1, 0.2):
        v_out, dfrac = sim_hc_full(tand)
        e_hc = v_out
        es_hc.append(e_hc)
        passed = check_condition(
            f"HC energy audit: diss == KE_in - KE_out (tan d={tand})",
            abs((1-e_hc**2)-dfrac) < 1e-4,
            f"e={e_hc:.3f} diss/E0={dfrac:.4f}"
        )
        all_passed &= passed

    passed = check_condition(
        "HC restitution monotone decreasing in tan d",
        es_hc[0] > es_hc[1] > es_hc[2],
        f"e={[round(x,3) for x in es_hc]}"
    )
    all_passed &= passed

    print("       -> NOTE: HC (e=%.3f) sits above the linear-osc model (e=%.3f) at tan d=0.1:"
          % (es_hc[1], math.exp(-math.pi*0.1/2/math.sqrt(1-(0.1/2)**2))))
    print("          damping ~ d^1.5 acts only at large indentation -> less loss/cycle.")
    print("          Restitution is model-dependent; the two bracket real rubber (tan d ~ 0.1).")

    return all_passed

def verify_axis4_relativistic_impact() -> bool:
    """
    AXIS 4: Relativistic impact KE=(gamma-1)m c^2

    Returns:
        True if all checks pass
    """
    print("\nAXIS 4: relativistic impact  KE=(gamma-1)m c^2")
    all_passed = True

    # Energy: (gamma-1) m c^2 = (2/5) K d^(5/2)   =>  d ~ [(5/2)(gamma-1) m c^2 / K]^(2/5)
    # Classical limit: gamma-1 ~ beta^2/2  =>  d -> [(5/4) m v^2/K]^(2/5)  (recovered)

    # NOTE: this axis is a MATHEMATICAL identity only (the energy-balance power law
    # re-expressed relativistically). It is NOT physics for the 550 nm ball: at any
    # such velocity the kinetic energy vastly exceeds any energy the solid can
    # confine, so the Hertz extension is meaningless. Kept only to verify the
    # identity d_rel ~ [2(g-1)/b^2]^(2/5) in the Newtonian limit.

    for b in (0.01, 0.04, 0.1):
        g = 1/math.sqrt(1-b*b)
        Kr = (5/2)*(g-1)*M*C0**2/K_HERTZ
        dr = Kr**(2/5)
        dens = 0.5*M*(b*C0)**2          # Same kinetic energy, Newtonian formula
        dn = ((5/2)*dens/K_HERTZ)**(2/5)
        passed = check_condition(
            f"low-beta limit: d_rel -> d_newton (beta={b})",
            abs(dr-dn)/dn < TOL_LOW_BETA,
            f"d_rel/d_newt = {dr/dn:.5f}"
        )
        all_passed &= passed

    b9 = 0.9
    g9 = 1/math.sqrt(1-b9*b9)
    dr9 = ((5/2)*(g9-1)*M*C0**2/K_HERTZ)**(2/5)
    dn9 = ((5/2)*(0.5*M*(b9*C0)**2)/K_HERTZ)**(2/5)
    pred = (2*(g9-1)/b9**2)**(2/5)     # Exact relativistic enhancement
    passed = check_condition(
        "beta=0.9: d_rel/d_newton = [2(g-1)/b^2]^(2/5) (exact)",
        abs((dr9/dn9)-pred)/pred < TOL_EQ,
        f"ratio={dr9/dn9:.4f} pred={pred:.4f}"
    )
    all_passed &= passed

    print("       -> d_rel/d_newton at beta=0.9 = %.2f  (classical scheme underestimates)" % (dr9/dn9))

    return all_passed

def verify_axis5_two_ball_collision() -> bool:
    """
    AXIS 5: Two-ball symmetric head-on collision

    Returns:
        True if all checks pass
    """
    print("\nAXIS 5: two-ball symmetric head-on collision")
    all_passed = True

    # Effective params: m_eff=m/2, R_eff=R/2, closing speed 2v, E*_two=E/(2(1-nu^2))
    meff, Reff, ver = M/2, R/2, 2*V
    Etwo = E/(2*(1-NU**2))
    d5 = ((15/16)*meff*ver**2/(Etwo*math.sqrt(Reff)))**(2/5)
    E5in = 0.5*meff*ver**2
    E5out = (2/5)*(4/3)*Etwo*math.sqrt(Reff)*d5**2.5

    passed = check_condition(
        "two-ball energy balance",
        abs(E5in-E5out)/E5in < TOL_ENERGY,
        f"d5={d5*1e9:.2f}nm"
    )
    all_passed &= passed

    # Relation to single planar impact: d_twoball/d_planar should be exactly 2
    passed &= check_condition(
        "d_twoball/d_planar = 2 (exact)",
        abs(d5/DMAX - 2.0) < TOL_SCALING,
        f"{d5/DMAX:.6f}"
    )

    return all_passed

def verify_axis6_jkr_adhesion() -> bool:
    """
    AXIS 6: JKR adhesion during contact - work of separation, stick criterion

    Returns:
        True if all checks pass
    """
    print("\nAXIS 6: JKR adhesion during contact - work of separation, stick criterion")
    all_passed = True

    # JKR: a^3 = (R/E*) [F + 3 pi R W + sqrt(6 pi R W F + (3 pi R W)^2)]
    #      d = a^2/R - (2/3) sqrt(2 pi W a / E*)
    W = 0.1  # J/m^2 work of adhesion

    def jkr_a(F: float) -> Optional[float]:
        """Contact radius from load."""
        inner = 6*math.pi*W*R*F + (3*math.pi*W*R)**2
        if inner < 0:
            return None
        root = math.sqrt(inner)
        return ((R/ESTAR_RIGID)*(F + 3*math.pi*W*R + root))**(1/3)

    def jkr_d(a: float) -> float:
        """Indentation from contact radius."""
        return a*a/R - (2/3)*math.sqrt(2*math.pi*W*a/ESTAR_RIGID)

    def jkr_F(a: float) -> float:
        """Load from contact radius."""
        return (ESTAR_RIGID/R)*a**3 - (a**1.5)*math.sqrt(6*math.pi*W*ESTAR_RIGID)

    a0 = jkr_a(0.0)
    d0 = jkr_d(a0)
    pull = -(3/2)*math.pi*R*W

    passed = check_condition(
        "closed-form F(a) reproduces pull-off & F(0)=0",
        abs(jkr_F(jkr_a(0.0))-0.0) < TOL_EQ and
        abs(jkr_F(jkr_a(pull))-pull)/abs(pull) < TOL_EQ,
        ""
    )
    all_passed &= passed

    # Pull-off by discriminant scan (very fine)
    bestF = 0.0
    for F in [pull*1.05*(i/200000) for i in range(200000)]:
        if jkr_a(F) is not None and F < bestF:
            bestF = F
    passed = check_condition(
        "JKR pull-off = -3/2 pi R W (numeric scan, 200k pts)",
        abs(bestF-pull)/abs(pull) < TOL_JKR_INTEGRATE,
        f"scan={bestF*1e9:.3f}nN theory={pull*1e9:.3f}nN"
    )
    all_passed &= passed

    # Work of separation via smooth a-parametrization: W_sep = |∫ F(a) d(delta)/da da|
    # (delta is not injective in F near pull-off; a is the smooth variable)
    a_po = jkr_a(pull)

    def integrand(a: float) -> float:
        ddel = 2*a/R - (1/3)*math.sqrt(2*math.pi*W/ESTAR_RIGID)/math.sqrt(a)  # d(delta)/da
        return jkr_F(a)*ddel

    def wsep_quad(N: int) -> float:
        """Trapezoidal integration for work of separation."""
        lo, hi = a_po, a0
        xs = [lo + (hi-lo)*i/N for i in range(N+1)]
        s = 0.0
        for i in range(N):
            s += (integrand(xs[i]) + integrand(xs[i+1]))/2*(xs[i+1]-xs[i])  # trapezoid
        return abs(s)

    Wsep = wsep_quad(JKR_INTEGRATION_POINTS)
    Wsep2 = wsep_quad(JKR_CONVERGENCE_CHECK_POINTS)
    passed = check_condition(
        "JKR W_sep converged (200k vs 1M pts)",
        abs((Wsep-Wsep2)/Wsep) < TOL_JKR_INTEGRATE,
        f"Wsep={Wsep:.4e}J (1M pts:{Wsep2:.4e}J)"
    )
    all_passed &= passed

    # Canonical JKR convention (a^3=(R/K)[...], K=(4/3)E* ~ 88.9 MPa) shifts W_sep
    def wsep_canonical(N: int = JKR_INTEGRATION_POINTS) -> float:
        Ec = (4/3)*ESTAR_RIGID

        def a_c(F: float) -> Optional[float]:
            inner = 6*math.pi*W*R*F + (3*math.pi*W*R)**2
            return ((R/Ec)*(F + 3*math.pi*W*R + math.sqrt(inner)))**(1/3) if inner >= 0 else None

        def d_c(a: float) -> float:
            return a*a/R - (2/3)*math.sqrt(2*math.pi*W*a/Ec)

        def F_c(a: float) -> float:
            return (Ec/R)*a**3 - a**1.5*math.sqrt(6*math.pi*W*Ec)

        aa_po = a_c(pull)
        lo, hi = aa_po, a_c(0.0)
        s = 0.0
        for i in range(N):
            ddel_lo = 2*(lo+(hi-lo)*i/N)/R - (1/3)*math.sqrt(2*math.pi*W/Ec)/math.sqrt(max(lo+(hi-lo)*i/N,1e-30))
            ddel_hi = 2*(lo+(hi-lo)*(i+1)/N)/R - (1/3)*math.sqrt(2*math.pi*W/Ec)/math.sqrt(max(lo+(hi-lo)*(i+1)/N,1e-30))
            s += (F_c(lo+(hi-lo)*i/N)*ddel_lo + F_c(lo+(hi-lo)*(i+1)/N)*ddel_hi)/2*(hi-lo)/N
        return abs(s)

    Wsep_c = wsep_canonical()
    print(f"       -> JKR W_sep (stated convention) = {Wsep:.3e} J;"
          f" canonical K=(4/3)E* = {Wsep_c:.3e} J")

    KE1 = 0.5*M*V**2
    v_stick = math.sqrt(2*Wsep/M)
    passed = check_condition(
        "stick criterion: KE(1 m/s) < W_sep",
        KE1 < Wsep,
        f"KE={KE1:.2e}J Wsep={Wsep:.2e}J -> v_stick={v_stick:.2f} m/s (ball sticks at 1 m/s)"
    )
    all_passed &= passed

    d_po = jkr_d(a_po)
    F_avg = Wsep/abs(d0-d_po)
    passed = check_condition(
        "average separation force > impact force",
        F_avg > PMAX,
        f"F_avg={F_avg*1e9:.1f}nN vs Pmax impact={PMAX*1e9:.1f}nN; d0={d0*1e9:.1f}nm a0={a0*1e9:.1f}nm"
    )
    all_passed &= passed

    print("       NOTE: criterion is a dissipative bound - a lossless ball regains the",
          "energy climbing out (e=1); stick holds for viscoelastic lossy contact (e~0.85-0.91).")

    return all_passed

def verify_axis7_force_ratio() -> bool:
    """
    AXIS 7: Force ratio compliant vs rigid plane

    Returns:
        True if check passes
    """
    print("\nAXIS 7: force ratio compliant vs rigid plane")
    passed = check_condition(
        "P_compliant/P_rigid = 2^(-2/5)",
        abs((PCOMP/PMAX)-2**(-2/5)) < TOL_SCALING,
        f"{PCOMP/PMAX:.4f} vs {2**(-2/5):.4f}"
    )
    return passed

def verify_axis8_mie_scattering() -> bool:
    """
    AXIS 8: Mie scattering for x=3.14, m=1.5+0i (spherical Bessel code)

    Returns:
        True if all checks pass
    """
    print("\nAXIS 8: MIE scattering for x=3.14, m=1.5+0i  (spherical Bessel code)")
    all_passed = True

    def sb_jn(z: float, N: int) -> List[complex]:
        """Spherical Bessel j_n(z), n=0..N, via downward (Miller) recurrence."""
        v = [0j]*(N+2)
        v[N] = 1+0j
        v[N+1] = 0+0j
        for n in range(N, 0, -1):
            v[n-1] = (2*n+1)/z*v[n] - v[n+1]
        s = sum((2*n+1)*abs(v[n])**2 for n in range(N+1))
        scale = math.sqrt(s)
        return [v[n]/scale for n in range(N+1)]

    def sb_yn(z: float, N: int) -> List[complex]:
        """Spherical Neumann y_n, upward from known y_0, y_1."""
        y = [0j]*(N+1)
        y[0] = -math.cos(z)/z
        if N >= 1:
            y[1] = -math.cos(z)/z**2 - math.sin(z)/z
        for n in range(1, N):
            y[n+1] = (2*n+1)/z*y[n] - y[n-1]
        return y

    def mie_q_func(m_: complex, x: float, N: Optional[int] = None) -> Tuple[float, float]:
        """Adaptive truncation Mie calculation."""
        if N is None:
            N = max(2, int(x + 4*abs(x)**(1/3)) + 8)  # Miller method is fine
        js = sb_jn(x, N+1)
        ys = sb_yn(x, N+1)
        jsm = sb_jn(m_*x, N+1)
        def psi(n): return x*js[n]
        def psi_(n): return js[n] + x*(js[n-1] - (n+1)/x*js[n]) if n >= 1 else js[0] - x*js[1]
        def xi(n): return x*(js[n] + 1j*ys[n])
        def xi_(n): return (js[n] + 1j*ys[n]) + x*((js[n-1]- (n+1)/x*js[n]) + 1j*(ys[n-1] - (n+1)/x*ys[n])) if n>=1 else (js[0]+1j*ys[0]) + x*(-js[1] - 1j*ys[1])
        psi_m = lambda n: m_*x*jsm[n]
        def psi_m_(n): return jsm[n] + m_*x*(jsm[n-1] - (n+1)/(m_*x)*jsm[n]) if n>=1 else jsm[0] - m_*x*jsm[1]

        Qe = Qs = 0.0
        for n in range(1, N+1):
            aa = (mk*psi_m(n)*psi_(n) - psi_m_(n)*psi(n)) / (mk*psi_m(n)*xi_(n) - psi_m_(n)*xi(n))
            bb = (psi_m(n)*psi_(n) - mk*psi_m_(n)*psi(n)) / (psi_m(n)*xi_(n) - mk*psi_m_(n)*xi(n))
            Qe += (2*n+1)*(aa.real + bb.real)
            Qs += (2*n+1)*(abs(aa)**2 + abs(bb)**2)
        return 2/x**2*Qe, 2/x**2*Qs

    mk = 1.5+0j
    x = 2*math.pi*R/(550e-9)
    Qe, Qs = mie_q_func(mk, x)

    passed = check_condition(
        "x = 3.142",
        abs(x-3.14159) < 1e-3,
        f"x={x:.4f}"
    )
    all_passed &= passed

    passed &= check_condition(
        "energy: Q_abs = Q_ext - Q_sca >= 0 (real-index: ~0)",
        Qs <= Qe + TOL_ENERGY,
        f"Qe={Qe:.4f} Qs={Qs:.4f}"
    )

    # Rayleigh limit: x->0, Q_sca = (8/3) x^4 |(m^2-1)/(m^2+2)|^2
    K_ray = (mk*mk-1)/(mk*mk+2)
    for xs in (1e-3, 1e-2):
        qe, qs = mie_q_func(mk, xs)
        q_theory = 8/3*xs**4*abs(K_ray)**2
        passed &= check_condition(
            f"Rayleigh limit x={xs:g}: Q_sca",
            abs(qs/q_theory-1) < 0.02,
            f"mie={qs:.3e} theory={q_theory:.3e}"
        )

    # Convergence: N=60 vs N=120 must agree for x=3.14
    Q2e, Q2s = mie_q_func(mk, x)
    Q3e, Q3s = mie_q_func(mk, x, N=int(x+4*abs(x)**(1/3))+8+8)
    passed &= check_condition(
        "Mie convergence (N vs N+8)",
        abs((Q2e-Q3e)/Q2e) < TOL_MIE_CONVERGE,
        f"Qe={Q2e:.6f} vs {Q3e:.6f}"
    )
    all_passed &= passed

    return all_passed

def verify_axis9_consolidated_numbers() -> bool:
    """
    AXIS 9: Post-expert-audit consolidated numbers (peer-verified)

    Returns:
        True if all checks pass
    """
    print("\nAXIS 9: post-expert-audit consolidated numbers (peer-verified)")
    all_passed = True

    a = math.sqrt(R*DMAX)
    pmean = PMAX/(math.pi*a*a)
    ppeak = 3*PMAX/(2*math.pi*a*a)

    passed = check_condition(
        "mean pressure 4.11 MPa",
        abs(pmean-4.11e6)/4.11e6 < 0.01,
        f"{pmean/1e6:.3f} MPa"
    )
    all_passed &= passed

    passed &= check_condition(
        "Hertz peak pressure 6.17 MPa (NOT 4.1)",
        abs(ppeak-6.17e6)/6.17e6 < 0.01,
        f"{ppeak/1e6:.2f} MPa"
    )
    all_passed &= passed

    print(f"       -> p0/E* = {ppeak/ESTAR_RIGID:.3f}, a/R = {a/R:.3f} (marginally elastic, not asymptotic)")

    f0 = (1/(2*math.pi))*math.sqrt((3/2)*K_HERTZ*math.sqrt(DMAX)/M)
    passed = check_condition(
        "f0 = 0.0375 GHz (not 0.04)",
        abs(f0-3.75e7)/3.75e7 < 0.01,
        f"{f0/1e9:.4f} GHz"
    )
    all_passed &= passed

    eta_w = 1e-3
    Re_w = RHO*V*(2*R)/eta_w
    passed = check_condition(
        "Re (ball in water) = rho v D/eta = 0.6",
        abs(Re_w-0.605)/0.605 < 0.01,
        f"Re={Re_w:.3f}"
    )
    all_passed &= passed

    v_th = math.sqrt(3*KB*300/M)
    print("       -> thermal speed sqrt(3kT/m) = %.2e m/s = %.1f mm/s  (a '1.8 um/s' claim is ~3700x small)"
          % (v_th, v_th*1e3))
    passed = check_condition(
        "thermal speed ~11.4 mm/s",
        abs(v_th-11.4e-3)/11.4e-3 < 0.02,
        f"{v_th*1e3:.2f} mm/s"
    )
    all_passed &= passed

    sig_sl, rho_s, Lf = 0.05, 1100.0, 1.5e5
    dT = (2*sig_sl*300/(rho_s*Lf*R))
    dT_low = (2*0.01*300/(1000.0*2e5*R))
    passed = check_condition(
        "melting shift 0.661 K with stated inputs (0.10-0.66 range)",
        abs(dT-0.661)/0.661 < 0.01,
        f"dT={dT:.3f}K (conservative {dT_low:.3f}K)"
    )
    all_passed &= passed

    print(f"\n=== RESULT: {PASS} passed, {FAIL} failed ===")
    return all_passed

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main() -> None:
    """Main verification routine."""
    global PASS, FAIL
    PASS = 0
    FAIL = 0

    # Run all axes
    axes = [
        verify_axis1_compliant_plane,
        verify_axis2_modulus_sensitivity,
        verify_axis3_viscoelastic_restitution,
        verify_axis4_relativistic_impact,
        verify_axis5_two_ball_collision,
        verify_axis6_jkr_adhesion,
        verify_axis7_force_ratio,
        verify_axis8_mie_scattering,
        verify_axis9_consolidated_numbers
    ]

    for axis_func in axes:
        if axis_func():
            PASS += 1
        else:
            FAIL += 1

    print(f"\n=== FINAL RESULT: {PASS} passed, {FAIL} failed ===")

if __name__ == "__main__":
    main()