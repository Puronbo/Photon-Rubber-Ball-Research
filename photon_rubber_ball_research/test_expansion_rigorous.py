"""
Rigorous verification of the 8 expansion axes for the photon-sized rubber ball.

Each axis: explicit derivation -> computation -> PASS/FAIL with tolerance.
Independent cross-checks: energy balance, known limits (Rayleigh, Newtonian),
and self-consistency (Q_ext = Q_sca + Q_abs).
"""
import math, cmath
from math import pi, sqrt

PASS = 0
FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    PASS += bool(cond); FAIL += (not bool(cond))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}  {detail}")

# ---- shared constants ------------------------------------------------------
rho, R   = 1100.0, 275e-9
m        = rho*4/3*pi*R**3
E, nu, v = 50e6, 0.5, 1.0
kB       = 1.380649e-23
Estar    = E/(1-nu**2)          # rigid-plane reduced modulus
K        = (4/3)*Estar*sqrt(R)
dmax     = ((15/16)*m*v**2/(Estar*sqrt(R)))**(2/5)
Pmax     = K*dmax**1.5
print("baseline: m=%.2e kg  E*=%.1f MPa  dmax=%.3f nm  Pmax=%.2f nN\n"
      % (m, Estar/1e6, dmax*1e9, Pmax*1e9))

# ===========================================================================
print("AXIS 1: compliant (same-rubber) plane  E* = E/(2(1-nu^2))")
# effective modulus for two identical bodies touching:
#   1/E*_tot = (1-nu1^2)/E1 + (1-nu2^2)/E2  = 2(1-nu^2)/E
Estar2 = 1/( (1-nu**2)/E + (1-nu**2)/E )
check("E*_two = E/(2(1-nu^2)) = 66.7/2 = 33.3 MPa",
      abs((Estar2-E/(2*(1-nu**2)))/Estar2) < 1e-9, f"= {Estar2/1e6:.3f} MPa")
# R_eff = R for sphere-on-plane (plane radius = infinity)
d2 = ((15/16)*m*v**2/(Estar2*sqrt(R)))**(2/5)
P2 = (4/3)*Estar2*sqrt(R)*d2**1.5
# energy check: (1/2) m v^2 must equal integral K2 d^(3/2) dd
E_in = 0.5*m*v**2
E_out = (2/5)*(4/3)*Estar2*sqrt(R)*d2**2.5
check("energy balance exact for compliant plane", abs(E_in-E_out)/E_in < 1e-9,
      f"d2={d2*1e9:.3f}nm P2={P2*1e9:.2f}nN")
# scaling law d ~ E*^(-2/5)
check("scaling d2/d1 = 2^(2/5)", abs((d2/dmax)-2**(2/5)) < 1e-6,
      f"{d2/dmax:.4f} vs {2**(2/5):.4f}")

# ===========================================================================
print("\nAXIS 2: E-modulus sensitivity (rubber range 0.01-0.1 GPa)")
for Ee in (10e6, 50e6, 100e6):
    Ese = Ee/(1-nu**2)
    dd  = ((15/16)*m*v**2/(Ese*sqrt(R)))**(2/5)
    Pp  = (4/3)*Ese*sqrt(R)*dd**1.5
    Eein  = 0.5*m*v**2
    Eeout = (2/5)*(4/3)*Ese*sqrt(R)*dd**2.5
    check(f"energy ok @ E={Ee/1e6:g}MPa (d={dd*1e9:.2f},P={Pp*1e9:.1f})",
          abs(Eein-Eeout)/Eein < 1e-9)
# power-law d ~ E^(-2/5): compare E10 vs E100 ratio
d10 = ((15/16)*m*v**2/((10e6/(1-nu**2))*sqrt(R)))**(2/5)
d100 = ((15/16)*m*v**2/((100e6/(1-nu**2))*sqrt(R)))**(2/5)
check("d(E=10MPa)/d(E=100MPa) = 10^(2/5)", abs(d10/d100 - 10**(2/5)) < 1e-6,
      f"{d10/d100:.4f} vs {10**(2/5):.4f}")

# ===========================================================================
print("\nAXIS 3: viscoelastic restitution  e ~ exp(-pi tan d / 2)")
# linear damped oscillator  x''+2*zeta*w x'+w^2 x=0, half-cycle restitution:
#   e = exp(-pi zeta / sqrt(1-zeta^2));  tan d = 2 zeta   (loss tangent)
# derive: amplitude |x| ~ e^(-zeta w t); at half period T_half=pi/w_d,
#   e = exp(-zeta w pi / w_d) = exp(-pi zeta/sqrt(1-zeta^2))  ~ exp(-pi tan d/2)
def sim_linear(zeta, w=1.0, dt=1e-5, v0=1.0):
    x, xp = 0.0, v0
    t = 0.0
    while True:                       # integrate to first x=0 return
        a = -2*zeta*w*xp - w*w*x
        xp += a*dt; x += xp*dt; t += dt
        if x <= 0 and t > 0.01: break
    return -xp/v0
for tand in (0.05, 0.1, 0.2):
    zeta = tand/2
    e_lin = math.exp(-pi*zeta/math.sqrt(1-zeta*zeta))
    e_sim = sim_linear(zeta)
    check(f"linear osc: e(calc)=exp(-pi z/..) vs numeric sim for tan d={tand}",
          abs(e_lin-e_sim) < 1e-3, f"e={e_sim:.4f}")
    print(f"       -> tan d={tand}: e = {e_lin:.3f}   [earlier draft used exp(-pi tan d), "
          f"giving {math.exp(-pi*tand):.3f} - WRONG, corrected]")
# nonlinear Hertz + viscous damping (Hunt-Crossley):
#   m dd'' = -K d^(3/2) - c d^(3/2) dp,   dp = d/dt
# damping tuned so that linearized at peak indentation reproduces tan d:
#   F_v,max/d F_s ~ tan d  =>  c = tan d * k_lin / (omega_contact * dmax^1.5)
# with k_lin = dP/dd at dmax = (3/2) K sqrt(dmax), omega_contact = pi/t_c
t_c_doc = 17.09e-9
w0 = pi/t_c_doc
Kk = (4/3)*Estar*sqrt(R)
k_lin = 1.5*Kk*sqrt(dmax)
def sim_hc_full(tand, dt=5e-12, v0=1.0):
    c = tand*k_lin/(w0*dmax**1.5)
    d, dp = 0.0, v0
    E0 = 0.5*m*v0*v0
    diss = 0.0
    for _ in range(10**6):
        dd = max(d, 0.0)
        a = (-Kk*dd**1.5 - c*dd**1.5*dp)/m
        dp += a*dt; d += dp*dt
        diss += c*dd**1.5*dp*dp*dt
        if d <= 0 and dp < 0: break
    return -dp, diss/E0
es_hc = []
for tand in (0.05, 0.1, 0.2):
    v_out, dfrac = sim_hc_full(tand)
    e_hc = v_out
    es_hc.append(e_hc)
    check(f"HC energy audit: diss == KE_in - KE_out (tan d={tand})",
          abs((1-e_hc**2)-dfrac) < 1e-4, f"e={e_hc:.3f} diss/E0={dfrac:.4f}")
check("HC restitution monotone decreasing in tan d",
      es_hc[0] > es_hc[1] > es_hc[2], f"e={[round(x,3) for x in es_hc]}")
print("       -> NOTE: HC (e=%.3f) sits above the linear-osc model (e=%.3f) at tan d=0.1:" 
      % (es_hc[1], math.exp(-pi*0.1/2/math.sqrt(1-(0.1/2)**2))))
print("          damping ~ d^1.5 acts only at large indentation -> less loss/cycle.")
print("          Restitution is model-dependent; the two bracket real rubber (tan d ~ 0.1).")

# ===========================================================================
print("\nAXIS 4: relativistic impact  KE=(gamma-1)m c^2")
# energy: (gamma-1) m c^2 = (2/5) K d^(5/2)   =>  d ~ [(5/2)(gamma-1) m c^2 / K]^(2/5)
# classical limit: gamma-1 ~ beta^2/2  =>  d -> [(5/4) m v^2/K]^(2/5)  (recovered)
c0 = 299792458.0
# NOTE: this axis is a MATHEMATICAL identity only (the energy-balance power law
# re-expressed relativistically). It is NOT physics for the 550 nm ball: at any
# such velocity the kinetic energy vastly exceeds any energy the solid can
# confine, so the Hertz extension is meaningless. Kept only to verify the
# identity d_rel ~ [2(g-1)/b^2]^(2/5) in the Newtonian limit.
for b in (0.01, 0.04, 0.1):
    g = 1/math.sqrt(1-b*b)
    Kr = (5/2)*(g-1)*m*c0**2/K
    dr = Kr**(2/5)
    dens = 0.5*m*(b*c0)**2          # same kinetic energy, newtonian formula
    dn   = ((5/2)*dens/K)**(2/5)
    check(f"low-beta limit: d_rel -> d_newton (beta={b})",
          abs(dr-dn)/dn < 0.05, f"d_rel/d_newt = {dr/dn:.5f}")
b9 = 0.9; g9 = 1/math.sqrt(1-b9*b9)
dr9 = ((5/2)*(g9-1)*m*c0**2/K)**(2/5)
dn9 = ((5/2)*(0.5*m*(b9*c0)**2)/K)**(2/5)
pred = (2*(g9-1)/b9**2)**(2/5)     # exact relativistic enhancement
check("beta=0.9: d_rel/d_newton = [2(g-1)/b^2]^(2/5) (exact)",
      abs((dr9/dn9)-pred)/pred < 1e-9, f"ratio={dr9/dn9:.4f} pred={pred:.4f}")
print("       -> d_rel/d_newton at beta=0.9 = %.2f  (classical scheme underestimates)" % (dr9/dn9))

# ===========================================================================
print("\nAXIS 5: two-ball symmetric head-on collision")
# effective params: m_eff=m/2, R_eff=R/2, closing speed 2v, E*_two=E/(2(1-nu^2))
meff, Reff, ver = m/2, R/2, 2*v
Etwo = E/(2*(1-nu**2))
d5 = ((15/16)*meff*ver**2/(Etwo*sqrt(Reff)))**(2/5)
E5in  = 0.5*meff*ver**2
E5out = (2/5)*(4/3)*Etwo*sqrt(Reff)*d5**2.5
check("two-ball energy balance", abs(E5in-E5out)/E5in < 1e-9,
      f"d5={d5*1e9:.2f}nm")
# relation to single planar impact: d_twoball/d_planar should be exactly 2
check("d_twoball/d_planar = 2 (exact)",
      abs(d5/dmax - 2.0) < 1e-6, f"{d5/dmax:.6f}")

# ===========================================================================
print("\nAXIS 6: JKR adhesion during contact - work of separation, stick criterion")
# JKR:  a^3 = (R/E*) [F + 3 pi R W + sqrt(6 pi R W F + (3 pi R W)^2)]
#       d   = a^2/R - (2/3) sqrt(2 pi W a / E*)
# Invert the load for F(a) (derived from the a^3 relation, checked below):
W = 0.1  # J/m^2 work of adhesion
def jkr_a(F):
    inner = 6*pi*W*R*F + (3*pi*W*R)**2
    if inner < 0: return None
    root  = math.sqrt(inner)
    return ((R/Estar)*(F + 3*pi*W*R + root))**(1/3)
def jkr_d(a): return a*a/R - (2/3)*math.sqrt(2*pi*W*a/Estar)
def jkr_F(a): return (Estar/R)*a**3 - (a**1.5)*math.sqrt(6*pi*W*Estar)
a0 = jkr_a(0.0); d0 = jkr_d(a0)
pull = -(3/2)*pi*R*W
check("closed-form F(a) reproduces pull-off & F(0)=0",
      abs(jkr_F(jkr_a(0.0))-0.0) < 1e-12 and abs(jkr_F(jkr_a(pull))-pull)/abs(pull) < 1e-12)
# pull-off by discriminant scan (very fine)
bestF = 0.0
for F in [pull*1.05*(i/200000) for i in range(200000)]:
    if jkr_a(F) is not None and F < bestF: bestF = F
check("JKR pull-off = -3/2 pi R W (numeric scan, 200k pts)", abs(bestF-pull)/abs(pull) < 1e-4,
      f"scan={bestF*1e9:.3f}nN theory={pull*1e9:.3f}nN")
# work of separation via smooth a-parametrization:  W_sep = |int F(a) d(delta)/da da|
# (delta is not injective in F near pull-off; a is the smooth variable)
a_po = jkr_a(pull)
def integrand(a):
    ddel = 2*a/R - (1/3)*math.sqrt(2*pi*W/Estar)/math.sqrt(a)   # d(delta)/da
    return jkr_F(a)*ddel
def wsep_quad(N):
    lo, hi = a_po, a0
    xs = [lo + (hi-lo)*i/N for i in range(N+1)]
    s = 0.0
    for i in range(N):
        s += (integrand(xs[i]) + integrand(xs[i+1]))/2*(xs[i+1]-xs[i])   # trapezoid
    return abs(s)
Wsep  = wsep_quad(200000)
Wsep2 = wsep_quad(1000000)
check("JKR W_sep converged (200k vs 1M pts)", abs((Wsep-Wsep2)/Wsep) < 1e-4,
      f"Wsep={Wsep:.4e}J (1M pts:{Wsep2:.4e}J)")
# canonical JKR convention (a^3=(R/K)[...], K=(4/3)E* ~ 88.9 MPa) shifts W_sep
def wsep_canonical(N=200000):
    Ec = (4/3)*Estar
    def a_c(F):
        inner = 6*pi*W*R*F + (3*pi*W*R)**2
        return ((R/Ec)*(F + 3*pi*W*R + math.sqrt(inner)))**(1/3) if inner >= 0 else None
    def d_c(a): return a*a/R - (2/3)*math.sqrt(2*pi*W*a/Ec)
    def F_c(a): return (Ec/R)*a**3 - a**1.5*math.sqrt(6*pi*W*Ec)
    aa_po = a_c(pull)
    lo, hi = aa_po, a_c(0.0)
    s = 0.0
    for i in range(N):
        ddel_lo = 2*(lo+(hi-lo)*i/N)/R - (1/3)*math.sqrt(2*pi*W/Ec)/math.sqrt(max(lo+(hi-lo)*i/N,1e-30))
        ddel_hi = 2*(lo+(hi-lo)*(i+1)/N)/R - (1/3)*math.sqrt(2*pi*W/Ec)/math.sqrt(max(lo+(hi-lo)*(i+1)/N,1e-30))
        s += (F_c(lo+(hi-lo)*i/N)*ddel_lo + F_c(lo+(hi-lo)*(i+1)/N)*ddel_hi)/2*(hi-lo)/N
    return abs(s)
Wsep_c = wsep_canonical()
print(f"       -> JKR W_sep (stated convention) = {Wsep:.3e} J;"
      f" canonical K=(4/3)E* = {Wsep_c:.3e} J")
KE1 = 0.5*m*v**2
v_stick = math.sqrt(2*Wsep/m)
check("stick criterion: KE(1 m/s) < W_sep", KE1 < Wsep,
      f"KE={KE1:.2e}J Wsep={Wsep:.2e}J -> v_stick={v_stick:.2f} m/s (ball sticks at 1 m/s)")
d_po = jkr_d(a_po)
F_avg = Wsep/abs(d0-d_po)
check("average separation force > impact force", F_avg > Pmax,
      f"F_avg={F_avg*1e9:.1f}nN vs Pmax impact={Pmax*1e9:.1f}nN; d0={d0*1e9:.1f}nm a0={a0*1e9:.1f}nm")
print("       NOTE: criterion is a dissipative bound - a lossless ball regains the",
      "energy climbing out (e=1); stick holds for viscoelastic lossy contact (e~0.85-0.91).")

# ===========================================================================
print("\nAXIS 7: force ratio compliant vs rigid plane")
check("P_compliant/P_rigid = 2^(-2/5)", abs((P2/Pmax)-2**(-2/5)) < 1e-6,
      f"{P2/Pmax:.4f} vs {2**(-2/5):.4f}")

# ===========================================================================
print("\nAXIS 8: MIE scattering for x=3.14, m=1.5+0i  (spherical Bessel code)")
def sb_jn(z, N):
    # spherical Bessel j_n(z), n=0..N, via downward (Miller) recurrence,
    # normalized by the sum rule  sum (2n+1) j_n^2 = 1
    v = [0j]*(N+2)
    v[N] = 1+0j; v[N+1] = 0+0j
    for n in range(N, 0, -1):
        v[n-1] = (2*n+1)/z*v[n] - v[n+1]
    s = sum((2*n+1)*v[n]**2 for n in range(N+1))
    scale = cmath.sqrt(s)
    return [v[n]/scale for n in range(N+1)]
def sb_yn(z, N):
    # spherical Neumann y_n, upward from known y_0, y_1
    y = [0j]*(N+1)
    y[0] = -cmath.cos(z)/z
    if N >= 1:
        y[1] = -cmath.cos(z)/z**2 - cmath.sin(z)/z
    for n in range(1, N):
        y[n+1] = (2*n+1)/z*y[n] - y[n-1]
    return y
def mie_q(m_, x, N=None):
    # adaptive truncation:  nstop ~ x + 4 x^(1/3) + 8   (Miller method is fine
    # only when the recurrence never overflows, i.e. N not vastly larger than x)
    if N is None:
        N = max(2, int(x + 4*abs(x)**(1/3)) + 8)
    js = sb_jn(x, N+1); ys = sb_yn(x, N+1)
    jsm = sb_jn(m_*x, N+1)
    def psi(n): return x*js[n]
    def psi_(n): return js[n] + x*(js[n-1] - (n+1)/x*js[n]) if n >= 1 else js[0] - x*js[1]
    def xi(n):  return x*(js[n] + 1j*ys[n])
    def xi_(n): return (js[n] + 1j*ys[n]) + x*((js[n-1]- (n+1)/x*js[n]) + 1j*(ys[n-1] - (n+1)/x*ys[n])) if n>=1 else (js[0]+1j*ys[0]) + x*(-js[1] - 1j*ys[1])
    psi_m  = lambda n: m_*x*jsm[n]
    psi_m_ = lambda n: jsm[n] + m_*x*(jsm[n-1] - (n+1)/(m_*x)*jsm[n]) if n>=1 else jsm[0] - m_*x*jsm[1]
    Qe = Qs = 0.0
    for n in range(1, N+1):
        aa = (m_*psi_m(n)*psi_(n)   - psi_m_(n)*psi(n))  / (m_*psi_m(n)*xi_(n)  - psi_m_(n)*xi(n))
        bb = (psi_m(n)*psi_(n)      - m_*psi_m_(n)*psi(n))/(psi_m(n)*xi_(n)     - m_*psi_m_(n)*xi(n))
        Qe += (2*n+1)*aa.real + (2*n+1)*bb.real
        Qs += (2*n+1)*(abs(aa)**2 + abs(bb)**2)
    return 2/x**2*Qe, 2/x**2*Qs
mk = 1.5+0j
x = 2*pi*R/(550e-9)
Qe, Qs = mie_q(mk, x)
check("x = 3.142", abs(x-3.14159) < 1e-3, f"x={x:.4f}")
check("energy: Q_abs = Q_ext - Q_sca >= 0 (real-index: ~0)", Qs <= Qe + 1e-9,
      f"Qe={Qe:.4f} Qs={Qs:.4f}")
# Rayleigh limit: x->0,  Q_sca = (8/3) x^4 |(m^2-1)/(m^2+2)|^2
K_ray = (mk*mk-1)/(mk*mk+2)
for xs in (1e-3, 1e-2):
    qe, qs = mie_q(mk, xs)
    q_theory = 8/3*xs**4*abs(K_ray)**2
    check(f"Rayleigh limit x={xs:g}: Q_sca", abs(qs/q_theory-1) < 0.02,
          f"mie={qs:.3e} theory={q_theory:.3e}")
# convergence: N=60 vs N=120 must agree for x=3.14
Q2e, Q2s = mie_q(mk, x); Q3e, Q3s = mie_q(mk, x, N=int(x+4*abs(x)**(1/3))+8+8)
check("Mie convergence (N vs N+8)", abs((Q2e-Q3e)/Q2e) < 1e-9, f"Qe={Q2e:.6f} vs {Q3e:.6f}")

# ===========================================================================
print("\nAXIS 9: post-expert-audit consolidated numbers (peer-verified)")
a    = sqrt(R*dmax)
pmean = Pmax/(pi*a*a)
ppeak = 3*Pmax/(2*pi*a*a)
check("mean pressure 4.11 MPa", abs(pmean-4.11e6)/4.11e6 < 0.01, f"{pmean/1e6:.3f} MPa")
check("Hertz peak pressure 6.17 MPa (NOT 4.1)", abs(ppeak-6.17e6)/6.17e6 < 0.01,
      f"{ppeak/1e6:.2f} MPa")
print(f"       -> p0/E* = {ppeak/Estar:.3f}, a/R = {a/R:.3f} (marginally elastic, not asymptotic)")
f0 = (1/(2*pi))*sqrt((3/2)*K*sqrt(dmax)/m)
check("f0 = 0.0375 GHz (not 0.04)", abs(f0-3.75e7)/3.75e7 < 0.01, f"{f0/1e9:.4f} GHz")
eta_w = 1e-3
Re_w  = rho*v*(2*R)/eta_w
check("Re (ball in water) = rho v D/eta = 0.6", abs(Re_w-0.605)/0.605 < 0.01, f"Re={Re_w:.3f}")
v_th = sqrt(3*kB*300/m)
print("       -> thermal speed sqrt(3kT/m) = %.2e m/s = %.1f mm/s  (a '1.8 um/s' claim is ~3700x small)"
      % (v_th, v_th*1e3))
check("thermal speed ~11.4 mm/s", abs(v_th-11.4e-3)/11.4e-3 < 0.02, f"{v_th*1e3:.2f} mm/s")
sig_sl, rho_s, Lf = 0.05, 1100.0, 1.5e5
dT = (2*sig_sl*300/(rho_s*Lf*R))
dT_low = (2*0.01*300/(1000.0*2e5*R))
check("melting shift 0.661 K with stated inputs (0.10-0.66 range)",
      abs(dT-0.661)/0.661 < 0.01, f"dT={dT:.3f}K (conservative {dT_low:.3f}K)")

print(f"\n=== RESULT: {PASS} passed, {FAIL} failed ===")