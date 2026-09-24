# The Photon-Sized Rubber Ball: A Corrected Multi-Scale Analysis

A corrected and verified treatment of the "photon-sized rubber ball" thought
experiment. This document replaces the physical claims in
`infosheet.html`, `infosheet_expanded.html`, and `infosett_book.html`, and it
does not rely on any of the fabricated "expert" content found in
`expert_comments_*.txt`, `research_team_collaboration.txt`,
`synthesis_of_expert_perspectives.txt`, or `photon_in_a_net.txt`.

## 1. Setup

A rubber ball with rest diameter matching the wavelength of green light:

- D0 = 550 nm, R = 275 nm
- Rubber: Young modulus E = 0.05 GPa (50 MPa), Poisson ratio nu = 0.5,
  density rho = 1100 kg/m3
- Ball mass: m = 9.58 x 10^-17 kg

## 2. Length contraction

Longitudinal rest length L0 contracts to L = L0/gamma when observed in a frame
moving at speed beta c relative to the ball, with
gamma = 1/sqrt(1 - beta^2). The transverse dimensions are unchanged, so the
ball appears as an oblate spheroid (Terrell-Penrose visual corrections apply
to what a camera would record, but the lab-frame geometry is the contracted
ellipsoid).

| beta | gamma  | L (nm) | contraction % |
|------|--------|--------|---------------|
| 0.50 | 1.155  | 476    | 13.4 %        |
| 0.80 | 1.667  | 330    | 40.0 %        |
| 0.90 | 2.294  | 240    | 56.4 %        |
| 0.95 | 3.203  | 172    | 68.8 %        |
| 0.99 | 7.089  | 78     | 85.9 %        |

Volume obeys V = V0/gamma, i.e. the volume is divided by gamma.

Small-beta expansion: contraction fraction = 1 - 1/gamma = beta^2/2 + O(beta^4).
The approximation (beta^2/2) is within 1% of the exact value for beta < 0.12.

## 3. Impact of the ball on a rigid plane (corrected)

Energy balance for an elastic, frictionless normal impact at speed v. For
Hertzian sphere-on-plane contact the load-displacement relation is

    P = K delta^(3/2),   K = (4/3) E* sqrt(R),   E* = E/(1 - nu^2)

Equating the kinetic energy to the integrated contact work gives the maximum
approach:

    delta_max = [ (15/16) m v^2 / (E* sqrt(R)) ]^(2/5)
    P_max     = K delta_max^(3/2)

For v = 1 m/s:

- E* = 66.7 MPa
- delta_max = 5.8 nm
- P_max = 21 nN

The previous documents contained the expression F = sqrt(2mEv^2/R). It is
dimensionally wrong: it evaluates to kg/s^2 (a force-per-length), not a force,
and would produce ~0.19 N for this ball at 1 m/s, about seven orders of
magnitude larger than the correct P_max. It is discarded here.

## 4. Elastic versus surface and thermal effects

Comparing the elastic indentation with other relevant effects:

1. Hertzian elastic indentation: delta ~ 5.8 nm (computed above).
2. Thermal vibration amplitude at T = 300 K against the contact stiffness
   k = 5.3 N/m:

       x_rms = sqrt(k_B T / k) = 0.028 nm

   This is negligible against the elastic indentation. The statement in the
   expanded sheets that thermal deformation is "1-10 nm" is not supported.
   The correct large thermal effect is translational Brownian drift, not
   deformation: in water at 300 K the RMS displacement in one second is
   1.26 um (about 2.3 ball diameters), from Stokes-Einstein.

3. Surface force scales: van der Waals/capillary adhesion on a 275 nm radius
   sphere can produce effective forces in the tens of nN range for a
   water capillary bridge of radius ~5 nm, comparable to or larger than the
   1 m/s impact force. Surface effects genuinely become competitive at this
   scale; this qualitative claim is retained.

Conclusion: the dominant deviation from ideal elastic contact at 1 m/s is
adhesion/capillary (order 10 nN), while thermal vibration is negligible
(0.03 nm).

## 5. Melting point depression

For a spherical particle, the Gibbs-Thomson melting-point shift is

    dT = 2 sigma_sl T_m / (rho_s L_f r)

With sigma_sl = 0.05 J/m2, T_m = 300 K, L_f = 1.5 x 10^5 J/kg, r = 275 nm:
dT = 0.66 K. These are assumed parameters: with conservative rubber values
(sigma_sl ~ 0.01 J/m2, rho_s ~ 1000 kg/m3, L_f ~ 2 x 10^5 J/kg) the depression
is ~0.1 K, so the honest range is ~0.1-0.7 K. The "several degrees" claim in
the earlier sheets is an overstatement in all cases. (Conventions that use
4 sigma_sl with a diameter, or that include crystal shape factors, shift the
constant by a factor ~2.)

## 6. Quantum effects are negligible at 550 nm (corrected)

The earlier sheets stated that "the de Broglie wavelength of constituent atoms
becomes comparable to the object size" and that zero-point energy "becomes
comparable to chemical bond energies." Both are wrong:

- Thermal (300 K) de Broglie wavelengths:
  - electron: 6.1 nm
  - carbon atom (12 u): 0.042 nm
  - the ball itself: 6 x 10^-16 m
  None is remotely comparable to 550 nm.
- Particle-in-a-box ground-state energy for an electron localized across the
  whole ball: E1 = h^2/(8 m_e L^2) = 1.24 x 10^-6 eV. Chemical bond energies
  are ~1-4 eV. The zero-point contribution at this size scale is negligible.
- Quantum confinement of electrons in the polymer would only matter if the
  confining domains were ~1-10 nm (e.g., conjugated chain segments or quantum
  dots), not the 550 nm ball.

The relevant quantum statement, stated correctly: a 550 nm ball is deep in the
semiclassical regime; quantum corrections enter only through the molecular
constituents that are already nanoscale.

## 7. Spectral-regime table (retained, minor fix)

The wavelength-to-physics mapping in the original sheets is sound:

| Band                | Wavelength   | Dominant physics                    |
|---------------------|--------------|-------------------------------------|
| Radio/microwave     | 1 mm - 100 km| Classical EM                         |
| Infrared            | 700 nm - 1 mm| Thermal/vibrational                 |
| Visible (green)     | 400-700 nm   | Electronic transitions              |
| Ultraviolet         | 10-400 nm    | Quantum excitations, ionization     |
| X-rays              | 0.01-10 nm   | Core-level transitions, diffraction |
| Gamma rays          | < 0.01 nm    | Nuclear transitions, particle phys  |

Note that a 550 nm ball is the same size as the wavelength of green light, so
Mie scattering (not geometric optics) applies to its optical response.

## 8. Multi-scale framing (retained)

- Macroscopic (>1 mm): continuum, Hertz contact applies.
- Microscopic (1 um - 1 mm): droplets, particles; adhesion starts to matter.
- Mesoscopic (100 nm - 1 um): the ball's regime. Surface forces and Brownian
  motion compete with elasticity; Mie optics; quantum negligible.
- Nanoscopic (<100 nm): quantum confinement and surface thermodynamics
  dominate.

## 9. Summary of corrections

1. Removed F = sqrt(2mEv^2/R) (dimensionally invalid).
2. Replaced it with the Hertz-dynamic impact solution: delta_max = 5.8 nm,
   P_max = 21 nN at 1 m/s.
3. Removed the "thermal deformation ~1-10 nm" claim; correct value is
   x_rms = 0.03 nm; the large effect is Brownian drift (1.26 um rms
   displacement after 1 s in water).
4. Corrected melting-point depression to ~0.7 K (was "several degrees").
5. Removed the "de Broglie comparable to object size" and "ZPE comparable to
   bond energies" claims; quantum effects are negligible at 550 nm.
6. Kept the correct Lorentz table, V = V0/gamma, the spectral table, and the
   multi-scale framing.
7. Excluded all "expert" material (fabricated n = 10 beta parametrization,
   the "(n^2*5)/2" identity, the "fixed point" n = 0.4, and the "0.08 eV"
   claims), which is not present in the original research documents and is
   numerically incorrect.