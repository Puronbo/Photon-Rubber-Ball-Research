#!/usr/bin/env python3
"""
Parameter sweep for magnifying glass heating simulation.
"""

import math

def compute_temperature(D_lens_mm, f_mm, absorption=0.9):
    # Convert to meters
    D_lens = D_lens_mm / 1000.0
    f = f_mm / 1000.0
    I_solar = 1000.0  # W/m^2
    lambda_light = 550e-9
    theta_sun = 0.53 * math.pi / 180.0
    emissivity = 1.0
    sigma = 5.670374419e-8
    T_ambient = 300.0

    # Collected power
    A_lens = math.pi * (D_lens/2)**2
    P_collected = I_solar * A_lens * absorption

    # Spot size (geometric dominates for these sizes)
    spot_radius_geom = f * theta_sun / 2.0  # radius
    spot_radius_diff = 1.22 * lambda_light * f / D_lens
    spot_radius = max(spot_radius_geom, spot_radius_diff)
    spot_area = math.pi * spot_radius**2

    if spot_area == 0:
        return None

    # Radiative equilibrium temperature
    T4 = T_ambient**4 + P_collected / (emissivity * sigma * spot_area)
    T_center = T4 ** 0.25
    return T_center - 273.15  # return in Celsius

def main():
    print("Magnifying Glass Temperature Sweep (°C)")
    print("Assumptions: 1000 W/m^2 solar irradiance, 90% absorption, radiative equilibrium only")
    print()

    # Sweep lens diameter (keep f=200mm)
    print("Varying lens diameter (focal length = 200 mm):")
    print("Diameter (mm) | Temperature (°C)")
    print("--------------|------------------")
    for D in [30, 50, 70, 100, 150, 200]:
        Tc = compute_temperature(D, 200)
        if Tc is not None:
            print(f"{D:12} | {Tc:16.1f}")
    print()

    # Sweep focal length (keep D=100mm)
    print("Varying focal length (lens diameter = 100 mm):")
    print("Focal length (mm) | Temperature (°C)")
    print("------------------|------------------")
    for f in [50, 100, 150, 200, 250, 300]:
        Tc = compute_temperature(100, f)
        if Tc is not None:
            print(f"{f:17} | {Tc:16.1f}")
    print()

    # Example: extreme values
    print("Extreme examples:")
    print("1. Small lens (30mm dia, 50mm f):", f"{compute_temperature(30, 50):.1f}°C")
    print("2. Large lens (200mm dia, 200mm f):", f"{compute_temperature(200, 200):.1f}°C")
    print("3. Short focus (100mm dia, 50mm f):", f"{compute_temperature(100, 50):.1f}°C")
    print("4. Long focus (100mm dia, 500mm f):", f"{compute_temperature(100, 500):.1f}°C")

if __name__ == "__main__":
    main()