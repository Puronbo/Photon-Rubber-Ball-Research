#!/usr/bin/env python3
"""
Simulation of heating by a magnifying glass (convex lens) focusing sunlight.
Calculates the power concentration and estimates temperature at the focal point.
"""

import math

def main():
    # Parameters (reasonable defaults)
    # Lens diameter (m)
    D_lens = 0.10  # 10 cm
    # Focal length (m)
    f = 0.20       # 20 cm
    # Solar irradiance at Earth's surface (W/m^2)
    I_solar = 1000.0  # clear day
    # Wavelength for diffraction estimate (m)
    lambda_light = 550e-9  # green light ~550 nm
    # Sun's angular diameter (radians)
    theta_sun = 0.53 * math.pi / 180.0  # convert degrees to radians
    # Material absorption efficiency (fraction of incident light absorbed)
    absorption = 0.9
    # Emissivity for radiative cooling (assume blackbody)
    emissivity = 1.0
    # Stefan-Boltzmann constant (W/m^2/K^4)
    sigma = 5.670374419e-8
    # Ambient temperature (K)
    T_ambient = 300.0

    # 1. Power collected by the lens
    A_lens = math.pi * (D_lens/2)**2
    P_collected = I_solar * A_lens * absorption
    print(f"Lens diameter: {D_lens*1000:.1f} mm")
    print(f"Focal length: {f*1000:.1f} mm")
    print(f"Collected solar power: {P_collected:.2f} W")

    # 2. Estimate spot size
    # Geometric spot size due to sun's finite angular size
    spot_diameter_geom = f * theta_sun
    spot_radius_geom = spot_diameter_geom / 2
    # Diffraction-limited spot size (Airy disk radius)
    spot_radius_diff = 1.22 * lambda_light * f / D_lens
    # Take the larger of the two (real spot size is dominated by whichever is larger)
    spot_radius = max(spot_radius_geom, spot_radius_diff)
    spot_area = math.pi * spot_radius**2
    print("\nSpot size estimation:")
    print(f"  Geometric spot radius (from sun's angle): {spot_radius_geom*1000:.3f} mm")
    print(f"  Diffraction-limited radius: {spot_radius_diff*1000:.3f} mm")
    print(f"  Effective spot radius: {spot_radius*1000:.3f} mm")
    print(f"  Spot area: {spot_area*1e6:.2f} mm^2")

    # 3. Power density (flux) at the spot
    if spot_area > 0:
        flux = P_collected / spot_area
        concentration_ratio = flux / I_solar
        print(f"\nPower density at spot: {flux/1e6:.2f} MW/m^2")
        print(f"Concentration ratio: {concentration_ratio:.0f}x")
    else:
        print("Spot area zero!")

    # 4. Temperature estimate via radiative equilibrium
    # Assume the spot loses heat only by radiation from its top surface (area = spot_area)
    # Power in = Power out (radiated)
    # P_collected = emissivity * sigma * spot_area * (T^4 - T_ambient^4)
    # Solve for T
    if spot_area > 0 and emissivity * sigma * spot_area > 0:
        T4 = T_ambient**4 + P_collected / (emissivity * sigma * spot_area)
        T_center = T4 ** 0.25
        print("\nTemperature estimate (radiative equilibrium):")
        print(f"  Center temperature: {T_center:.1f} K = {T_center - 273.15:.1f} °C")
        print(f"  Ambient temperature: {T_ambient:.1f} K = {T_ambient - 273.15:.1f} °C")
        print(f"  Temperature rise: {T_center - T_ambient:.1f} K")
    else:
        print("Cannot compute temperature (zero area or zero emissivity).")

    # 5. Simple radial temperature distribution (assuming flux follows Gaussian and radiative cooling dominates)
    # For simplicity, assume intensity I(r) = I0 * exp(-2*r^2 / w^2) where w = spot_radius (1/e^2 radius)
    # Then local power absorbed per unit area proportional to I(r)
    # Local radiative equilibrium: I(r) * absorption = emissivity * sigma * (T(r)^4 - T_ambient^4)
    # So T(r) = [ (I(r)*absorption)/(emissivity*sigma) + T_ambient^4 ]^0.25
    # We'll compute a few points.
    print("\nRadial temperature distribution (assuming Gaussian beam):")
    w = spot_radius  # beam radius (1/e^2)
    I0 = P_collected / (math.pi * w**2)  # peak intensity for Gaussian beam with power P_collected
    print(f"  Peak intensity I0: {I0/1e6:.2f} MW/m^2")
    for r in [0, w/2, w, 2*w]:
        if r == 0:
            factor = 1.0
        else:
            factor = math.exp(-2*r**2 / w**2)
        I_local = I0 * factor
        if I_local > 0:
            T4_local = T_ambient**4 + (I_local * absorption) / (emissivity * sigma)
            T_local = T4_local ** 0.25
            print(f"  r = {r*1000:.2f} mm: T = {T_local:.1f} K = {T_local - 273.15:.1f} °C")
        else:
            print(f"  r = {r*1000:.2f} mm: T ≈ ambient")

if __name__ == "__main__":
    main()