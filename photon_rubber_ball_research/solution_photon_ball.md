# The Photon-Sized Rubber Ball: Complete Analytical Solution

Closed-form solution of every mechanics/thermal/quantum question posed by the
"photon-sized rubber ball" thought experiment. All results verified
computationally. This is the derivation companion to `infosheet_corrected.md`.

Constants: D0 = 550 nm (R = 275 nm), rubber E = 50 MPa, nu = 0.5,
rho = 1100 kg/m3, so mass m = 9.58 x 10^-17 kg. Room temperature T = 300 K.

## A. Elastic impact of the ball on a rigid plane

Contact mechanics. For a sphere pressing on a half-space, Hertz theory gives a
power-law load-displacement relation. With E* = E/(1 - nu^2):

    P = K delta^(3/2),   K = (4/3) E* sqrt(R)

For a free impact the sphere does work against this nonlinear spring. Calling
delta_max the maximum indentation, energy conservation gives a closed form
(no approximation):

    (1/2) m v^2 = integral_0^delta_max K delta'^(3/2) d(delta')
                = (2/5) K delta_max^(5/2)

which inverts to

    delta_max = [ (15/16) m v^2 / (E* sqrt(R)) ]^(2/5)
    P_max     = (4/3) E* sqrt(R) delta_max^(3/2)

At v = 1 m/s:

    E* = 66.7 MPa
    delta_max = 5.81 nm
    P_max     = 20.6 nN
    contact radius a = sqrt(R delta_max) = 40.0 nm
    mean pressure  P_max / (pi a^2) = 4.1 MPa;  Hertz peak p0 = 3 P_max/(2 pi a^2) = 6.2 MPa

Contact duration. During approach, dt = -d(delta)/sqrt(v^2 - (2/m)(2/5)K delta^(5/2)).
Substituting u = delta/delta_max turns the compression time into a beta
function:

    t_c = (2/5)(delta_max/v) B(2/5, 1/2) = (2/5)(delta_max/v) (Gamma(2/5) Gamma(1/2))/Gamma(9/10)

The rebound is symmetric, so the total contact time is twice this:

    t_contact = (4/5)(delta_max/v) B(2/5, 1/2)

Numerically B(2/5, 1/2) = 3.68, giving t_c = 8.55 ns and t_contact = 17.1 ns.
Average force over the contact: m v / t_contact = 5.6 nN.

The old formula F = sqrt(2mEv^2/R) is dimensionally force-per-length (kg/s^2),
gives 0.19 N here, and is discarded.

## B. Contact stiffness and resonance

The differential stiffness at maximum approach is

    k = dP/d(delta) at delta_max = (3/2) K delta_max^(1/2) = 2 E* sqrt(R delta_max)

giving k = 5.33 N/m. The ball-on-plane oscillator rings at

    f0 = (1/2 pi) sqrt(k/m)

f0 = 0.0375 GHz (~37 MHz; the harmonic half-period 13.3 ns and the nonlinear
contact time 17.1 ns bracket the chattering timescale while in contact).

## C. Thermal effects

Vibrational amplitude against the contact spring (equipartition):

    x_rms = sqrt(k_B T / k) = 0.028 nm

This is negligible against the 5.8 nm elastic indentation, so the earlier
"1-10 nm thermal deformation" claim is retracted.

Brownian drift (translation, not deformation). Stokes-Einstein diffusion in
water (eta = 1e-3 Pa s):

    D = k_B T / (6 pi eta R) = 0.80 um^2/s
    sqrt(2 D t) = 1.26 um after 1 s

That is ~2.3 ball diameters of wandering per second, which dominates any
directed millimetric motion of a free 550 nm particle in water.

Momentum relaxation in the fluid: tau = m / (6 pi eta R) = 18.5 ns, far below
1 s, so the ball is overdamped: thermal motion is diffusive, not ballistic.

## D. Quantum corrections are negligible

Particle-in-a-box ground state for an electron localized across the whole
diameter:

    E_1 = h^2 / (8 m_e L^2) = 1.24 x 10^-6 eV,   L = 550 nm

Chemical bond energies are ~1-4 eV; this is seven orders of magnitude smaller.
Thermal de Broglie wavelengths at 300 K:

    electron:  6.1 nm
    carbon:    0.042 nm
    ball itself: h/sqrt(3 m k_B T) = 6 x 10^-16 m

None is comparable to 550 nm. Quantum confinement matters only for the ~1-10 nm
molecular domains (conjugated segments, quantum dots) inside the material, not
for the ball as a whole. The ball is deep in the semiclassical regime.

## E. Adhesion competes with impact

JKR pull-off force for a sphere (work of adhesion W ~ 0.1 J/m2 for rubber, a
bare contact):

    F_pull = (3/2) pi R W = 130 nN

Even at 1/10 that adhesion energy the pull-off (~13 nN) is comparable to the
20.6 nN impact force, and a water capillary bridge is often stronger still.
So a 550 nm rubber ball's contact behavior is dominated by surface forces as
much as by bulk elasticity - this is the one qualitative claim that survives
to nanoscale.

## F. Optical regime

The ball's size parameter at 550 nm:

    x = 2 pi R / lambda = 3.14

x ~ 3 places it in the full Mie regime (not Rayleigh, not geometric optics).
Its optical response must be computed via Mie theory; simple cross-section
formulas do not apply.

## G. Melting point depression (Gibbs-Thomson)

For a spherical particle the melting shift is

    Delta T = 2 sigma_sl T_m / (rho_s L_f r)

With sigma_sl = 0.05 J/m2, T_m = 300 K, L_f = 1.5 x 10^5 J/kg:
Delta T = 0.66 K. These are assumed parameters; with conservative rubber
values (sigma_sl ~ 0.01 J/m2) the shift drops to ~0.1 K, so the honest range
is ~0.1-0.7 K: real but small, and parameter-sensitive.

## H. Summary of the solved numbers

| Quantity                                    | Value              |
|---------------------------------------------|--------------------|
| mass                                        | 9.58 x 10^-17 kg   |
| E* (E = 50 MPa, nu = 0.5)                  | 66.7 MPa           |
| delta_max (1 m/s)                           | 5.81 nm            |
| P_max (1 m/s)                               | 20.6 nN            |
| contact radius a                            | 40.0 nm            |
| mean / Hertz-peak contact pressure           | 4.1 / 6.2 MPa      |
| contact time                                | 17.1 ns            |
| contact stiffness k                         | 5.33 N/m           |
| resonance f0                                | 0.0375 GHz         |
| x_rms (thermal, at contact)                 | 0.028 nm           |
| D (water), sqrt(2Dt) at 1 s                 | 0.80 um^2/s, 1.26 um |
| momentum relaxation tau                     | 18.5 ns            |
| E1 (550 nm electron box)                    | 1.2 x 10^-6 eV     |
| JKR pull-off (W = 0.1 J/m2)                 | 130 nN             |
| Mie size parameter at 550 nm                | 3.14               |
| melting-point depression                    | 0.1-0.7 K          |