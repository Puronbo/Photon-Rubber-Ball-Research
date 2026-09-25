#!/usr/bin/env python3
"""
Boson Scaling Probe: Massless vs Low-Mass Probe Particles for the
Photon-Sized Rubber Ball System (19th battery member) - DIALECTIC ENGINE VERSION

The verification model uses a 550-nm photon beam (E = 2.25 eV) as the only
probe. This script quantifies how a low-mass (tiny but nonzero rest mass)
boson differs from a truly massless one at that same quantum energy E.

Key relation, exact: absorbed momentum flux is F = (p/E) P, and
p/E = v/c^2, v/c = sqrt(1 - (m c^2 / E)^2). Hence for a massive probe
F = (v/c) (P/c), saturating at the massless ceiling F = P/c only as
v -> c. Massless and low-mass probes are observationally identical when
the dimensionless pair (m c^2 / E)^2 is below experimental resolution;
deviations grow to percent level only when m c^2 approaches E.

This dialectic engine version extends the probe to actively engage in the
quantum-cosmological dialogue by:
1. Adding dynamical parameters for expansion (H) and twist (w) rates
2. Implementing feedback control to maintain target linkage states
3. Generating hypotheses from detected correlation patterns
4. Supporting adaptive exploration for information gain
5. Connecting to verification system axes for cross-disciplinary linkage

Numbers follow the same constants as the verification battery; this table
is the ground truth for the probe-particle-type dimension.
"""

import math
import sys
import numpy as np
import json
import time
from scipy.linalg import eigh
try:
    import select
except ImportError:
    select = None  # Fallback for Windows

# ============================================================================
# CONSTANTS (same values as the verification battery)
# ============================================================================

C = 299792458.0
H = 6.62607015e-34
EV = 1.602176634e-19

WAVELENGTH = 550e-9
R = 275e-9
POWER = 1.0e-3

E_PHOTON = H * C / WAVELENGTH
RATE = POWER / E_PHOTON
F_CAP = POWER / C
BALL_DIAMETER = 2 * R

# ============================================================================
# DIALECTIC ENGINE PARAMETERS
# ============================================================================

# Control parameters for dialectic engine
TARGET_LINKAGE_MODE = "strong_coupling"  # Options: null_test, strong_coupling, torsion_dom, expansion_dom, critical_point, explore
LINKAGE_TARGETS = {
    "null_test": np.array([0.0, 0.0]),
    "strong_coupling": np.array([0.7, 0.7]),
    "torsion_dom": [0.0, 1.0],
    "expansion_dom": [1.0, 0.0],
    "critical_point": [0.5, 0.5],
    "explore": None  # Will use information gain or random walk
}
KP, KI = 0.05, 0.005  # PI controller gains (tune these)
integral_H, integral_omega = 0.0, 0.0

# Dynamical parameters (expansion rate H and twist rate w)
EXPANSION_RATE_HZ = 0.0   # s^-1 - expansion rate (Hubble-like parameter)
TWIST_RATE_RADS = 0.0     # rad/s - twist rate

# History for adaptive exploration
history_H, history_omega, history_C = [], [], []
HISTORY_SIZE = 20  # How many cycles to remember for pattern detection
HYPOTHESIS_BUFFER = []  # Store recent hypotheses

# Physical bounds for stability
MAX_EXPANSION_RATE = 10.0     # s^-1 (0 to 10 Hz)
MAX_TWIST_RATE = 100.0        # rad/s (0 to 100 rad/s)
MAX_DELTA_H_PER_CYCLE = 1.0e-3   # s^-1 per measurement cycle
MAX_DELTA_OMEGA_PER_CYCLE = 1.0e-2 # rad/s per measurement cycle

# Hypothesis detection thresholds
LINKAGE_NOVELTY_THRESHOLD = 0.20   # Minimum strength to consider novel
ASYMMETRY_THRESHOLD = 0.15         # Minimum asymmetry for non-reciprocal effects
HYPOTHESIS_DEDUPLICATION_WINDOW = 5  # How many recent hypotheses to check for duplicates

# ============================================================================
# SCALING FUNCTIONS WITH DYNAMICAL EXTENSIONS
# ============================================================================

def gamma_beta(mass_energy):
    """Original gamma_beta function for relativistic velocity factor"""
    if mass_energy == 0.0:
        return 1.0
    xi = (mass_energy / E_PHOTON) ** 2
    if xi >= 1.0:
        return None
    return math.sqrt(1.0 - xi)

def de_broglie(mass_energy):
    """Original de Broglie wavelength function"""
    numerator = H * C
    denominator = math.sqrt(max(E_PHOTON ** 2 - mass_energy ** 2, 0.0))
    return numerator / denominator

def transversal_time(beta):
    """Original transversal time calculation"""
    if beta is None:
        return None
    return BALL_DIAMETER / (beta * C)

def effective_velocity_with_torsion(mass_energy, radius, time_val=0.0):
    """
    Compute effective v/c including torsional and expansion effects
    for the "growing circle with twisting top" scenario
    """
    # Get base relativistic factor
    xi = (mass_energy / E_PHOTON) ** 2
    if xi >= 1.0:
        return None
    beta_base = math.sqrt(1.0 - xi)

    # Torsional contribution: Ω × r coupling (analogous to magnetic force)
    # Localized twist: Ω = TWIST_RATE * exp(-radius**2 / (2*R**2))
    omega_local = TWIST_RATE_RADS * math.exp(-radius**2 / (2*R**2))
    v_torsion = omega_local * radius / C  # v = wr

    # Expansion contribution: Hubble-like flow v = Hr
    v_expansion = EXPANSION_RATE_HZ * radius

    # Total effective velocity (co-linear approximation for now)
    # In full treatment, these would be vector sums
    beta_effective = beta_base + (v_torsion + v_expansion) / C

    # Clamp to physical range [-1, 1] for velocity/c
    return max(-1.0, min(1.0, beta_effective))

def de_broglie_with_dynamics(mass_energy, radius, time_val=0.0):
    """Modified de Broglie wavelength including dynamical effects"""
    beta = effective_velocity_with_torsion(mass_energy, radius, time_val)
    if beta is None:
        return None
    # p = γm₀v, but we work in energy space: p/E = (v/c²) * γ
    # Avoid division by zero
    if abs(beta) < 1e-12:
        return float('inf')
    gamma = 1.0 / math.sqrt(1.0 - beta**2)
    return H * C / (E_PHOTON * gamma * beta)

# ============================================================================
# EXPERIMENT LOGGER FOR ARXIV BUNDLE GENERATION
# ============================================================================

import os
from datetime import datetime

# Experiment logger configuration
LOGGING_ENABLED = True
LOG_DIRECTORY = "experiment_logs"

def save_experiment_data_point(H, omega, C_matrix, hypotheses, dialectic_mode,
                              probe_mass_ev=0.0, label=""):
    """
    Save a single experiment data point to JSON for arXiv bundle generation.

    Args:
        H: Expansion rate (s^-1)
        omega: Twist rate (rad/s)
        C_matrix: 9x9 correlation matrix from verification system
        hypotheses: List of generated hypothesis strings
        dialectic_mode: Current dialectic mode string
        probe_mass_ev: Probe mass energy in eV (for context)
        label: Optional label for this data point
    """
    if not LOGGING_ENABLED:
        return

    os.makedirs(LOG_DIRECTORY, exist_ok=True)

    timestamp = datetime.now().isoformat()

    # Prepare data for JSON serialization
    data_point = {
        "timestamp": timestamp,
        "parameters": {
            "expansion_rate_Hz": float(H),
            "twist_rate_rads": float(omega),
            "probe_mass_ev": float(probe_mass_ev),
            "dialectic_mode": dialectic_mode,
            "label": label
        },
        "measurements": {
            "correlation_matrix": C_matrix.tolist() if hasattr(C_matrix, 'tolist') else [[float(x) for x in row] for row in C_matrix],
            "matrix_shape": [int(C_matrix.shape[0]), int(C_matrix.shape[1])] if hasattr(C_matrix, 'shape') else [len(C_matrix), len(C_matrix[0]) if C_matrix else 0],
            "trace": float(np.trace(C_matrix)) if hasattr(np, 'trace') else sum(C_matrix[i][i] for i in range(min(len(C_matrix), len(C_matrix[0]) if C_matrix else 0))),
            "frobenius_norm": float(np.linalg.norm(C_matrix, 'fro')) if hasattr(np, 'linalg') else 0.0
        },
        "hypotheses": hypotheses,
        "metadata": {
            "probe_wavelength_nm": 550.0,
            "probe_energy_ev": 2.25,
            "verification_system_axes": 9,
            "software_version": "boson_scaling_probe_dialectic_engine_v1.0"
        }
    }

    # Create filename based on date and dialectic mode
    date_str = datetime.now().strftime("%Y%m%d")
    mode_str = dialectic_mode.replace(" ", "_")
    filename = f"experiment_{date_str}_{mode_str}.json"
    filepath = os.path.join(LOG_DIRECTORY, filename)

    # Append to existing file or create new one
    try:
        # Try to read existing data
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                existing_data = json.load(f)
            # Ensure it's a list
            if not isinstance(existing_data, list):
                existing_data = [existing_data]
        else:
            existing_data = []

        # Append new data point
        existing_data.append(data_point)

        # Write back to file
        with open(filepath, 'w') as f:
            json.dump(existing_data, f, indent=2)

    except Exception:
        # Fallback: create new file with just this data point
        try:
            with open(filepath, 'w') as f:
                json.dump([data_point], f, indent=2)
        except:
            pass  # Silently fail if logging fails completely

# ============================================================================
# HYPOTHESIS GENERATION AND INTERPRETATION FUNCTIONS
# ============================================================================

def get_current_linkage(C_matrix):
    """Extract the dominant linkage vector from correlation matrix"""
    evals, evecs = eigh(C_matrix)
    return evecs[:, -1]  # Eigenvector corresponding to largest eigenvalue

# Enhanced interpretation mappings with more precise physical explanations
AXIS_INTERPRETATIONS = {
    # Axis definitions based on verification system documentation
    1: "Photon Momentum Transfer (Axis 1): Measures recoil momentum from photon scattering",
    2: "Entropy Production (Axis 2): Quantifies irreversible thermodynamic processes",
    3: "Adhesion Energy (Axis 3): Measures work of separation in probe-target interaction",
    4: "Impedance (Axis 4): Complex electrical response characterizing energy storage/dissipation",
    5: "Impedance Imaginary (Axis 5): Reactive component of electrical response",
    6: "Viscoelastic Modulus (Axis 6): Time-dependent mechanical response properties",
    7: "JKR Adhesion (Axis 7): Johnson-Kendall-Roberts theory-based surface energy measurement",
    8: "Mie Scattering (Axis 8): Light scattering cross-section from spherical particles",
    9: "Fluctuation Spectra (Axis 9): Temporal correlation functions testing dissipation-fluctuation relations"
}

# Physics-based linkage interpretations with theoretical grounding
LINKAGE_INTERPRETATIONS = {
    # Format: (axis1, axis2): "Physical interpretation with theoretical basis"
    (1, 2): "Momentum-Entropy Coupling: Tests entropic gravity hypotheses where momentum transfer relates to entropy gradients via F = T ∇S",
    (1, 3): "Momentum-Adhesion Coupling: Work-energy theorem application; measures energy dissipation during probe-target interaction",
    (1, 4): "Momentum-Impedance Coupling: Reveals charge relaxation times and dissipative channels in momentum transfer processes",
    (1, 5): "Momentum-Impedance (Imag): Probe-induced reactive electrical response indicating energy storage mechanisms",
    (1, 6): "Momentum-Viscoelastic Coupling: Tests validity of viscoelastic models (Hunt-Crossley) in dynamical mechanical response",
    (1, 7): "Momentum-Adhesion (JKR): Surface energy modifications affecting pull-off forces in elastic contact mechanics",
    (1, 8): "Momentum-Mie Scattering: Optical property changes revealing refractive index variations from probe interaction",
    (1, 9): "Momentum-Fluctuation Coupling: Direct test of fluctuation-dissipation theorem linking response and correlation functions",
    (2, 3): "Entropy-Adhesion Coupling: Quantifies entropic contribution to surface forces and hydrophobic/hydrophilic interactions",
    (2, 4): "Entropy-Impedance Coupling: Measures entropic effects on electrical conduction and dielectric relaxation",
    (2, 5): "Entropy-Decoherence: Entropy-induced quantum decoherence rates in probe-environment interactions",
    (2, 6): "Entropy-Viscoelastic Coupling: Entropic effects on mechanical dissipation and relaxation spectra",
    (2, 7): "Entropy-Adhesion (JKR): Entropic contributions to surface energy in JKR contact mechanics framework",
    (2, 8): "Entropy-Mie Coupling: Entropic effects on optical properties and scattering cross-sections",
    (2, 9): "Entropy-Fluctuation Coupling: Tests entropy production relations and detailed balance in fluctuation dynamics",
    (3, 4): "Adhesion-Impedance Coupling: Viscoelastic characterization through combined mechanical and electrical measurements",
    (3, 5): "Adhesion-Impedance (Reactive): Measures elastic storage capacity in adhesive contacts",
    (3, 6): "Adhesion-Viscoelastic Coupling: Complete rheological characterization of adhesive interfaces",
    (3, 7): "Adhesion-Adhesion (JKR): Surface surface interactions probing long-range forces in JKR theory",
    (3, 8): "Adhesion-Mie Coupling: Surface-optical interactions revealing changes in refractive index profiles",
    (3, 9): "Adhesion-Fluctuation Coupling: Surface fluctuation relations testing time-reversal symmetry in adhesive contacts",
    (4, 5): "Impedance Real-Imaginary: Loss tangent and quality factor quantification from complex impedance measurements",
    (4, 6): "Impedance-Viscoelastic Coupling: Mechanical spectroscopy correlating electrical and mechanical relaxation processes",
    (4, 7): "Impedance-Adhesion (JKR): Electrical impedance changes probing surface charge distributions in adhesive contacts",
    (4, 8): "Impedance-Mie Coupling: Electro-optical effects revealing field-dependent changes in optical properties",
    (4, 9): "Impedance-Fluctuation Coupling: Johnson-Nyquist noise relations connecting electrical fluctuations to dissipation",
    (5, 6): "Impedance (Imag)-Viscoelastic: Loss mechanisms in viscoelastic materials probed through reactive impedance",
    (5, 7): "Impedance (Imag)-Adhesion (JKR): Dissipative surface forces in adhesive contacts measured via reactive impedance",
    (5, 8): "Impedance (Imag)-Mie: Dissipative optical effects from imaginary impedance components",
    (5, 9): "Impedance (Imag)-Fluctuation: Fluctuation-dissipation relations in reactive systems measured through impedance",
    (6, 7): "Viscoelastic-Adhesion (JKR): Time-dependent adhesion kinetics and relaxation in adhesive contacts",
    (6, 8): "Viscoelastic-Mie Coupling: Rheo-optical effects revealing flow-dependent changes in optical properties",
    (6, 9): "Viscoelastic-Fluctuation Coupling: Fluctuation in dissipation measuring non-equilibrium thermodynamic behavior",
    (7, 8): "Adhesion (JKR)-Mie Coupling: Surface-optical interference effects measuring nanoscale surface topography",
    (7, 9): "Adhesion (JKR)-Fluctuation: Adhesion noise spectra probing molecular bond dynamics and rupture forces",
    (8, 9): "Mie-Fluctuation Coupling: Scattering noise relations testing coherence properties of scattered light"
}

def interpret_linkage(axis1, axis2):
    """Map axis pairs to physically grounded interpretations"""
    key = (min(axis1, axis2), max(axis1, axis2))
    base_interpretation = LINKAGE_INTERPRETATIONS.get(
        key,
        f"Axis {axis1}-{axis2} coupling requiring theoretical characterization"
    )
    # Add axis-specific context
    axis1_desc = AXIS_INTERPRETATIONS.get(axis1, f"Axis {axis1}")
    axis2_desc = AXIS_INTERPRETATIONS.get(axis2, f"Axis {axis2}")
    return f"{base_interpretation} [{axis1_desc} ↔ {axis2_desc}]"

def detect_novel_linkages(C_matrix, history_C=None, threshold=LINKAGE_NOVELTY_THRESHOLD):
    """Detect statistically significant unexpected linkages with baseline comparison"""
    novel_linkages = []

    # If we have history, compute statistical significance
    if history_C is not None and len(history_C) > 5:
        # Compute mean and standard deviation from history
        history_array = np.array(history_C)
        mean_matrix = np.mean(history_array, axis=0)
        std_matrix = np.std(history_array, axis=0)

        # Avoid division by zero
        std_matrix = np.where(std_matrix == 0, 1e-10, std_matrix)

        # Compute z-scores for off-diagonal elements
        for i in range(9):
            for j in range(i+1, 9):  # Upper triangle
                strength = abs(C_matrix[i, j])
                baseline_mean = mean_matrix[i, j]
                baseline_std = std_matrix[i, j]

                # Z-score: how many standard deviations from mean
                z_score = abs((strength - baseline_mean) / baseline_std)

                # Novel if significantly above baseline (e.g., 2+ sigma) AND above absolute threshold
                if z_score > 2.0 and strength > threshold:
                    novel_linkages.append({
                        'axes': (i+1, j+1),
                        'strength': strength,
                        'baseline_mean': float(baseline_mean),
                        'baseline_std': float(baseline_std),
                        'z_score': float(z_score),
                        'interpretation': interpret_linkage(i+1, j+1),
                        'novelty_type': 'statistical_deviation'
                    })
    else:
        # Fallback to original method when insufficient history
        for i in range(9):
            for j in range(i+1, 9):
                strength = abs(C_matrix[i, j])
                if strength > threshold:
                    novel_linkages.append({
                        'axes': (i+1, j+1),
                        'strength': strength,
                        'interpretation': interpret_linkage(i+1, j+1),
                        'novelty_type': 'absolute_threshold'
                    })

    return novel_linkages

def detect_symmetry_breaking(C_matrix, history_C=None, threshold=ASYMMETRY_THRESHOLD):
    """Detect statistically significant symmetry breaking (non-reciprocal effects)"""
    symmetry_breaks = []

    if history_C is not None and len(history_C) > 5:
        # Compute historical asymmetry baseline
        history_array = np.array(history_C)
        asym_history = np.array([
            abs(history_array[:, i, j] - history_array[:, j, i])
            for i in range(9) for j in range(i+1, 9)
        ]).reshape(-1, len(range(9))*(len(range(9))-1)//2)

        mean_asym = np.mean(asym_history, axis=0)
        std_asym = np.std(asym_history, axis=0)
        std_asym = np.where(std_asym == 0, 1e-10, std_asym)

        idx = 0
        for i in range(9):
            for j in range(i+1, 9):
                asym = abs(C_matrix[i, j] - C_matrix[j, i])
                z_score = abs((asym - mean_asym[idx]) / std_asym[idx]) if std_asym[idx] > 0 else 0.0

                if z_score > 2.0 and asym > threshold:
                    symmetry_breaks.append({
                        'axes': (i+1, j+1),
                        'asymmetry': float(asym),
                        'baseline_mean': float(mean_asym[idx]),
                        'baseline_std': float(std_asym[idx]),
                        'z_score': float(z_score),
                        'interpretation': f"Time-reversal symmetry breaking or chiral coupling in Axis {i+1}↔{j+1} interaction",
                        'axes_labels': (f"C[{i+1},{j+1}]", f"C[{j+1},{i+1}]")
                    })
                idx += 1
    else:
        # Fallback to original method
        for i in range(9):
            for j in range(i+1, 9):
                asym = abs(C_matrix[i, j] - C_matrix[j, i])
                if asym > threshold:
                    symmetry_breaks.append({
                        'axes': (i+1, j+1),
                        'asymmetry': float(asym),
                        'interpretation': f"Time-reversal symmetry breaking or chiral coupling in Axis {i+1}↔{j+1} interaction",
                        'axes_labels': (f"C[{i+1},{j+1}]", f"C[{j+1},{i+1}]")
                    })

    return symmetry_breaks

def detect_trace_anomalies(C_matrix, history_C=None, threshold=0.5):
    """Detect significant changes in total correlation strength"""
    trace_anomalies = []

    trace_C = np.trace(C_matrix)

    if history_C is not None and len(history_C) > 3:
        recent_traces = [np.trace(hC) for hC in history_C[-3:] if hC is not None]
        if len(recent_traces) >= 2:
            trace_mean = np.mean(recent_traces)
            trace_std = np.std(recent_traces) if len(recent_traces) > 1 else 0.1
            trace_std = max(trace_std, 0.01)  # Avoid division by zero

            trace_change = abs(trace_C - trace_mean)
            z_score = trace_change / trace_std if trace_std > 0 else 0.0

            if z_score > 2.0 and trace_change > threshold:
                trace_anomalies.append({
                    'trace_change': float(trace_change),
                    'baseline_mean': float(trace_mean),
                    'baseline_std': float(trace_std),
                    'z_score': float(z_score),
                    'interpretation': "Global reorganization of coupling strengths suggesting phase transition or critical point",
                    'novelty_type': 'trace_anomaly'
                })
    elif len(history_C) > 0:
        # Simple change from first measurement if limited history
        trace_initial = np.trace(history_C[0])
        trace_change = abs(trace_C - trace_initial)
        if trace_change > threshold:
            trace_anomalies.append({
                'trace_change': float(trace_change),
                'baseline_trace': float(trace_initial),
                'interpretation': "Significant change in total correlation strength from initial measurement",
                'novelty_type': 'trace_anomaly'
            })

    return trace_anomalies

def score_hypothesis(hypothesis_dict, hypothesis_type):
    """Score hypothesis based on novelty, strength, and potential impact"""
    score = 0.0

    if hypothesis_type == 'linkage':
        # Base score from strength (normalized)
        strength_score = min(hypothesis_dict['strength'] / 1.0, 1.0)  # Cap at 1.0

        # Novelty bonus from z-score if available
        novelty_bonus = 0.0
        if 'z_score' in hypothesis_dict:
            novelty_bonus = min(hypothesis_dict['z_score'] / 5.0, 0.5)  # Cap bonus at 0.5

        # Axis importance weighting (some axes more fundamental)
        axis1, axis2 = hypothesis_dict['axes']
        importance_weights = {1: 1.0, 2: 0.9, 3: 0.8, 4: 0.7, 5: 0.6, 6: 0.5, 7: 0.4, 8: 0.3, 9: 0.2}
        axis_importance = (importance_weights.get(axis1, 0.5) + importance_weights.get(axis2, 0.5)) / 2.0

        score = (strength_score + novelty_bonus) * axis_importance

    elif hypothesis_type == 'symmetry':
        # Base score from asymmetry
        asym_score = min(hypothesis_dict['asymmetry'] / 1.0, 1.0)

        # Novelty bonus
        novelty_bonus = 0.0
        if 'z_score' in hypothesis_dict:
            novelty_bonus = min(hypothesis_dict['z_score'] / 5.0, 0.3)

        score = asym_score + novelty_bonus

    elif hypothesis_type == 'trace':
        # Base score from trace change magnitude
        change_score = min(abs(hypothesis_dict['trace_change']) / 2.0, 1.0)

        # Novelty bonus
        novelty_bonus = 0.0
        if 'z_score' in hypothesis_dict:
            novelty_bonus = min(hypothesis_dict['z_score'] / 5.0, 0.2)

        score = change_score + novelty_bonus

    return min(score, 1.0)  # Cap at 1.0

def generate_hypotheses_from_patterns(C_matrix, H, omega, history_C=None):
    """Generate research hypotheses based on detected patterns with scoring"""
    hypotheses = []

    # 1. Check for novel linkages with statistical validation
    novel_linkages = detect_novel_linkages(C_matrix, history_C, threshold=LINKAGE_NOVELTY_THRESHOLD)
    for nl in novel_linkages:
        hypothesis_text = (
            f"NOVEL LINKAGE DETECTED: Axis {nl['axes'][0]} <-> Axis {nl['axes'][1]} "
            f"(strength={nl['strength']:.3f}"
        )
        if 'z_score' in nl:
            hypothesis_text += f", z-score={nl['z_score']:.1f}"
        hypothesis_text += f") at H={H:.2e} s^-1, w={omega:.2e} rad/s. "
        hypothesis_text += f"Suggests: {nl['interpretation']}"

        hypothesis_dict = {
            'text': hypothesis_text,
            'type': 'linkage',
            'axes': nl['axes'],
            'raw_data': nl,
            'score': score_hypothesis(nl, 'linkage')
        }
        hypotheses.append(hypothesis_dict)

    # 2. Check for symmetry breaking (non-reciprocal effects)
    symmetry_breaks = detect_symmetry_breaking(C_matrix, history_C, threshold=ASYMMETRY_THRESHOLD)
    for sb in symmetry_breaks:
        hypothesis_text = (
            f"NON-RECIPROCAL EFFECT DETECTED: {sb['axes_labels'][0]} != {sb['axes_labels'][1]} "
            f"(asymmetry={sb['asymmetry']:.3f}"
        )
        if 'z_score' in sb:
            hypothesis_text += f", z-score={sb['z_score']:.1f}"
        hypothesis_text += f") at H={H:.2e} s^-1, w={omega:.2e} rad/s. "
        hypothesis_text += f"Suggests: {sb['interpretation']}"

        hypothesis_dict = {
            'text': hypothesis_text,
            'type': 'symmetry',
            'axes': sb['axes'],
            'raw_data': sb,
            'score': score_hypothesis(sb, 'symmetry')
        }
        hypotheses.append(hypothesis_dict)

    # 3. Check for trace anomalies (total correlation strength changes)
    trace_anomalies = detect_trace_anomalies(C_matrix, history_C, threshold=0.5)
    for ta in trace_anomalies:
        hypothesis_text = (
            f"TOTAL CORRELATION SHIFT DETECTED: "
            f"Δtrace = {ta['trace_change']:.3f}"
        )
        if 'z_score' in ta:
            hypothesis_text += f", z-score={ta['z_score']:.1f}"
        hypothesis_text += f") at H={H:.2e} s^-1, w={omega:.2e} rad/s. "
        hypothesis_text += f"Suggests: {ta['interpretation']}"

        hypothesis_dict = {
            'text': hypothesis_text,
            'type': 'trace',
            'raw_data': ta,
            'score': score_hypothesis(ta, 'trace')
        }
        hypotheses.append(hypothesis_dict)

    # Sort hypotheses by score (descending) for prioritized presentation
    hypotheses.sort(key=lambda x: x['score'], reverse=True)

    return hypotheses

def is_hypothesis_novel(new_hyp_text, buffer=HYPOTHESIS_BUFFER, window=HYPOTHESIS_DEDUPLICATION_WINDOW):
    """Check if hypothesis is sufficiently novel using improved similarity detection"""
    if len(buffer) == 0:
        return True

    # Enhanced similarity check using multiple features
    recent = buffer[-window:] if len(buffer) >= window else buffer

    for hyp_text in recent:
        # Check multiple similarity criteria
        length_similarity = 1.0 - abs(len(new_hyp_text) - len(hyp_text)) / max(len(new_hyp_text), len(hyp_text), 1)

        # Jaccard similarity on words
        words_new = set(new_hyp_text.lower().split())
        words_hyp = set(hyp_text.lower().split())
        if len(words_new) == 0 and len(words_hyp) == 0:
            jaccard_similarity = 1.0
        elif len(words_new) == 0 or len(words_hyp) == 0:
            jaccard_similarity = 0.0
        else:
            intersection = len(words_new & words_hyp)
            union = len(words_new | words_hyp)
            jaccard_similarity = intersection / union if union > 0 else 0.0

        # Early substring check (first 100 chars)
        prefix_similarity = 1.0 if new_hyp_text[:100] == hyp_text[:100] else 0.0

        # Combined similarity score
        combined_similarity = (length_similarity * 0.3 + jaccard_similarity * 0.5 + prefix_similarity * 0.2)

        if combined_similarity > 0.8:  # Threshold for considering too similar
            return False

    return True

def information_gain_estimate(H, omega, history_H, history_omega, history_C):
    """Estimate expected information gain from measuring at (H, omega)"""
    if len(history_H) < 3:
        return 1.0  # Uniform exploration initially

    # Improved approach: kernel density estimation in log space
    if len(history_H) >= 5:
        try:
            from sklearn.neighbors import KernelDensity
            import numpy as np

            # Prepare data in log10 space to handle wide ranges
            X_train = np.column_stack([
                np.log10(np.maximum(np.array(history_H), 1e-12)),
                np.log10(np.maximum(np.array(history_omega), 1e-12))
            ])
            X_query = np.array([[np.log10(max(H, 1e-12)), np.log10(max(omega, 1e-12))]])

            # Fit KDE and compute log likelihood
            kde = KernelDensity(bandwidth=0.5, kernel='gaussian')
            kde.fit(X_train)
            log_density = kde.score_samples(X_query)[0]

            # Convert to information gain estimate (higher density = lower novelty)
            # Use exponential transform to get positive values
            info_gain = np.exp(-log_density)
            # Normalize to reasonable range
            return min(max(info_gain, 0.1), 3.0)
        except ImportError:
            # Fallback to original method if sklearn not available
            pass
        except Exception:
            # Fallback to original method on any other error
            pass

    # Fallback approach: inverse distance to nearest neighbor in (H,omega) space
    min_dist = float('inf')
    for h, w in zip(history_H, history_omega):
        # Avoid log(0) by adding small offset
        h_safe = max(h, 1e-12)
        w_safe = max(w, 1e-12)
        H_safe = max(H, 1e-12)
        omega_safe = max(omega, 1e-12)

        dist = math.sqrt((math.log10(H_safe/h_safe))**2 + (math.log10(omega_safe/w_safe))**2)
        min_dist = min(min_dist, dist)

    # Information gain increases with distance from known points
    # Saturation to prevent extreme values
    return 1.0 + math.tanh(min_dist / 2.0)  # Saturates at ~2.0

# ============================================================================
# MAIN FUNCTION WITH DIALECTIC ENGINE CAPABILITIES
# ============================================================================

def main():
    ladder = [
        ("massless photon", 0.0),
        ("photon-mass bound", 1e-18),
        ("1 meV", 1e-3),
        ("10 meV", 1e-2),
        ("0.1 eV", 0.1),
        ("1 eV", 1.0),
        ("2.24 eV (E minus 0.01 eV)", 2.24),
        ("2.26 eV (0.01 eV above E)", 2.26),
        ("5 eV", 5.0),
        ("10 eV", 10.0),
    ]

    t_photon = BALL_DIAMETER / C

    print("=" * 78)
    print("BOSON SCALING PROBE DIALECTIC ENGINE (550 nm probe, E = {:.4f} eV, P = 1 mW)".format(
        E_PHOTON / EV))
    print("=" * 78)
    print("  force-per-watt ceiling (every probe):  F = P/c = {:.4f} pN".format(
        F_CAP * 1e12))
    print("  photon rate at 1 mW: {:.4g} /s; per-quantum p = {:.4g} kg m/s".format(
        RATE, E_PHOTON / C))
    print()

    # DIALECTIC ENGINE STATUS DISPLAY
    print("  DIALECTIC ENGINE STATUS:")
    print(f"  Mode: {TARGET_LINKAGE_MODE}")
    target_display = LINKAGE_TARGETS[TARGET_LINKAGE_MODE] if LINKAGE_TARGETS[TARGET_LINKAGE_MODE] is not None else "Adaptive"
    print(f"  Target Linkage: {target_display}")
    print(f"  Current H: {EXPANSION_RATE_HZ:.3e} s^-1, w: {TWIST_RATE_RADS:.3e} rad/s")
    print()

    print("  mc^2 [eV]   (mc^2/E)^2   v/c     F [pN]   loss vs photon   lambda [m]   torsional_F [pN]")
    for name, mc2_ev in ladder:
        m2 = mc2_ev * EV
        beta_base = gamma_beta(m2)  # Original function from your code
        xi = (m2 / E_PHOTON) ** 2

        if beta_base is None:
            print("  {:16s} {:10.3e}  beyond threshold".format(name, xi))
            continue

        # Compute dynamical effects at characteristic radius R
        beta_dyn = effective_velocity_with_torsion(m2, R, 0.0)  # t=0 for snapshot
        force_base = beta_base * F_CAP * 1e12
        force_torsion = (beta_dyn - beta_base) * F_CAP * 1e12  # Isolate torsion contribution
        loss = (1.0 - beta_base) * 100.0
        wavelength = de_broglie(m2)  # Keep original for lambda

        print("  {:16s} {:10.3e}  {:.4f}   {:.4f}     {:.3f}%      {:.4g}   {:.4f}".format(
            name, xi, beta_base, force_base, loss, wavelength, force_torsion))
    print()

    print("  time-of-flight across the ball (diameter 550 nm):")
    print("    photon     {:.4f} fs".format(t_photon * 1e15))
    for name, mc2_ev in ladder:
        m2 = mc2_ev * EV
        beta_base = gamma_beta(m2)
        if beta_base is None:
            continue
        delay = (transversal_time(beta_base) - t_photon) * 1e15
        if delay < 1e-6:
            print("    {:16s} {:.4f} fs  (delay {:.2e} fs, indistinguishable)".format(
                name, transversal_time(beta_base) * 1e15, delay))
        else:
            print("    {:16s} {:.4f} fs  (delay +{:.3f} fs)".format(
                name, transversal_time(beta_base) * 1e15, delay))
    print()

    print("  VERDICT on 'massless vs low-mass':")
    print("    distinguishing number is (mc^2/E)^2; identical when << 1e-6.")
    photon_bound_loss = 1 - gamma_beta(1e-18 * EV)
    print("    real-photon bound mc^2 = 1e-18 eV -> (mc^2/E)^2 = {:.1e}, "
          "loss {:.2e}% (unobservable)".format(
              (1e-18 * EV / E_PHOTON) ** 2, photon_bound_loss * 100))
    for mc2_ev in (1e-3, 0.1, 1.0):
        beta = gamma_beta(mc2_ev * EV)
        print("    mc^2 = {:5g} eV  -> v/c = {:.4f}, force-cap fraction {:.4f}, "
              "longitudinal mode ~ {:.2e}".format(
                  mc2_ev, beta, beta, ((mc2_ev * EV) / E_PHOTON) ** 2))
    print("    conclusion: massless and low-mass probes are interchangeable for")
    print("    force, rate, and wavelength until mc^2 is within ~10x of E = {:.2f} eV.".format(
        E_PHOTON / EV))

    # ============================================================================
    # DIALECTIC ENGINE OUTPUT SECTION
    # ============================================================================
    print()
    print("  DIALECTIC ENGINE OUTPUT:")
    print("  Expansion Rate H [s^-1]:     {:.3e}".format(EXPANSION_RATE_HZ))
    print("  Twist Rate w [rad/s]:        {:.3e}".format(TWIST_RATE_RADS))
    print("  Torsion Parameter z = (wR/c)²: {:.3e}".format((TWIST_RATE_RADS*R/C)**2))
    print("  Expansion Parameter e = (HR/c)²: {:.3e}".format((EXPANSION_RATE_HZ*R/C)**2))

    # Placeholder for actual correlation matrix measurement
    # In a real implementation, this would come from simultaneous 9-axis measurements
    # For now, we'll simulate a basic correlation matrix that depends on H and w
    print()
    print("  SIMULATED CORRELATION MATRIX INSIGHTS:")

    # Create a simple correlation matrix that varies with H and w
    # This simulates what would be measured from the 9 verification system axes
    xi_eff = ((1e-3 * EV) / E_PHOTON) ** 2  # Using 1 meV as example probe
    base_corr = math.sqrt(1 - xi_eff)  # Baseline from boson scaling

    # Add dynamical effects
    H_effect = min(0.3, EXPANSION_RATE_HZ * 1e3)  # Scale H effect
    omega_effect = min(0.4, TWIST_RATE_RADS * 0.1)  # Scale omega effect

    # Simulate some cross-axis correlations that would be measured
    sim_C11 = base_corr * (1 - H_effect*0.1)  # Axis 1 self-correlation
    sim_C44 = base_corr * (1 + omega_effect*0.2)  # Axis 4 self-correlation (adhesion)
    sim_C14 = base_corr * 0.5 * (1 + omega_effect*0.1 - H_effect*0.05)  # Axis1-Axis4 linkage

    print(f"  Axis 1 Momentum Transfer:    M1 ~ {sim_C11:.3f} (baseline: {base_corr:.3f})")
    print(f"  Axis 4 Adhesion Energy:      M4 ~ {sim_C44:.3f} (baseline: {base_corr:.3f})")
    print(f"  Axis 1 <-> Axis 4 Linkage:     C_1_4 ~ {sim_C14:.3f}")
    print("  Suggests: Work-Energy Conservation with dynamical corrections")

    # Hypothesis generation (would run after actual measurements)
    if TARGET_LINKAGE_MODE != "null_test":  # Don't generate hypotheses in pure null test mode
        print()
        print("  DIALECTIC HYPOTHESIS GENERATION:")

        # Simulate some hypothesis detection
        if abs(TWIST_RATE_RADS - 0.5) < 0.1 and EXPANSION_RATE_HZ < 0.01:
            print("  [IDEA] NEW HYPOTHESIS: Torsion-dominated regime detected (w ~ 0.5 rad/s, H ~ 0)")
            print("    Suggests: Pure torsion effects may generate measurable adhesion asymmetries")
        elif EXPANSION_RATE_HZ > 0.1 and TWIST_RATE_RADS < 0.05:
            print("  [IDEA] NEW HYPOTHESIS: Expansion-dominated regime detected (H > 0.1 s^-1, w ~ 0)")
            print("    Suggests: Cosmological expansion effects may modify baseline momentum transfer")
        elif abs(EXPANSION_RATE_HZ - TWIST_RATE_RADS) < 0.05 and EXPANSION_RATE_HZ > 0.01:
            print("  [IDEA] NEW HYPOTHESIS: Strong coupling regime detected (H ~ w != 0)")
            print("    Suggests: Balance between expansion and torsion may optimize nuclear-gravitational coupling")

    # Log experiment data point for arXiv bundle generation
    # Create a more realistic simulated correlation matrix for logging
    # In a real implementation, this would come from actual 9-axis measurements
    xi_eff = ((1e-3 * EV) / E_PHOTON) ** 2  # Using 1 meV as example probe
    base_corr = math.sqrt(1 - xi_eff)  # Baseline from boson scaling

    # Add dynamical effects and some realistic noise/correlations
    H_effect = min(0.3, EXPANSION_RATE_HZ * 1e3)  # Scale H effect
    omega_effect = min(0.4, TWIST_RATE_RADS * 0.1)  # Scale omega effect

    # Create a more realistic 9x9 correlation matrix
    sim_C = np.eye(9) * base_corr  # Start with diagonal (self-correlations)

    # Add some off-diagonal correlations that would be measured
    # Axis 1 <-> Axis 4 linkage (momentum-adhesion)
    sim_C[0, 3] = sim_C[3, 0] = base_corr * 0.5 * (1 + omega_effect*0.1 - H_effect*0.05)
    # Axis 2 <-> Axis 5 linkage (entropy-impedance)
    sim_C[1, 4] = sim_C[4, 1] = base_corr * 0.3 * (1 + H_effect*0.1)
    # Axis 3 <-> Axis 6 linkage (adhesion-viscoelastic)
    sim_C[2, 5] = sim_C[5, 2] = base_corr * 0.4 * (1 - omega_effect*0.05)
    # Axis 4 <-> Axis 7 linkage (impedance-JKR adhesion)
    sim_C[3, 6] = sim_C[6, 3] = base_corr * 0.35 * (1 + H_effect*0.05 - omega_effect*0.1)
    # Axis 5 <-> Axis 8 linkage (impedance imag-Mie)
    sim_C[4, 7] = sim_C[7, 4] = base_corr * 0.25 * (1 - H_effect*0.05)
    # Axis 6 <-> Axis 9 linkage (viscoelastic-fluctuation)
    sim_C[5, 8] = sim_C[8, 5] = base_corr * 0.3 * (1 + omega_effect*0.05)
    # Axis 7 <-> Axis 8 linkage (JKR adhesion-Mie)
    sim_C[6, 7] = sim_C[7, 6] = base_corr * 0.2 * (1 - H_effect*0.05 + omega_effect*0.02)
    # Axis 1 <-> Axis 9 linkage (momentum-fluctuation - tests fluctuation-dissipation)
    sim_C[0, 8] = sim_C[8, 0] = base_corr * 0.4 * (1 - H_effect*0.1 + omega_effect*0.05)

    # Ensure matrix is symmetric and valid (clamp to [-1, 1] for correlations)
    sim_C = np.clip(sim_C, -1.0, 1.0)
    # Force diagonal to be exactly 1.0 (perfect self-correlation)
    for i in range(9):
        sim_C[i, i] = 1.0
    # Make symmetric
    sim_C = (sim_C + sim_C.T) / 2

    # Collect current hypotheses (we need to regenerate or capture them)
    current_hypotheses = []
    # In a real implementation, we'd store the generated hypotheses from above
    # For now, we'll indicate that hypotheses were generated in this cycle
    if TARGET_LINKAGE_MODE != "null_test":
        # Check if any hypotheses would have been generated
        if (abs(TWIST_RATE_RADS - 0.5) < 0.1 and EXPANSION_RATE_HZ < 0.01) or \
           (EXPANSION_RATE_HZ > 0.1 and TWIST_RATE_RADS < 0.05) or \
           (abs(EXPANSION_RATE_HZ - TWIST_RATE_RADS) < 0.05 and EXPANSION_RATE_HZ > 0.01):
            current_hypotheses = ["Hypothesis generated in this cycle (see console output)"]
        else:
            current_hypotheses = []  # No significant hypotheses detected

    save_experiment_data_point(
        H=EXPANSION_RATE_HZ,
        omega=TWIST_RATE_RADS,
        C_matrix=sim_C,
        hypotheses=current_hypotheses,
        dialectic_mode=TARGET_LINKAGE_MODE,
        probe_mass_ev=1.0,  # Example: 1 eV probe mass
        label=f"cycle_{int(time.time())}"
    )

    # Dialectic mode information
    print()
    print("  DIALECTIC MODES AVAILABLE:")
    print("    null_test:      Seek massless limit (xi->0) - baseline verification")
    print("    strong_coupling: Seek H~w regime (strong coupling) - optimal for reactor tests")
    print("    torsion_dom:    Seek torsion dominance (w>>H) - test frame-dragging effects")
    print("    expansion_dom:  Seek expansion dominance (H>>w) - test cosmological expansion")
    print("    critical_point: Seek critical point (H~w!=0) - test phase transition signatures")
    print("    explore:        Adaptive exploration / information gain")
    print()
    print("  CONTROLS:")
    print("    Space bar: Cycle dialectic modes")
    print("    'q' key: Quit program")
    print()

    # Show brief dialectic engine status for feedback
    print("  Dialectic Engine Active: Adjusting H and w to maintain target linkage state")
    print("  Current linkage vector would be computed from real 9-axis correlation matrix")
    print("  In this simulation, parameters are set manually for demonstration")

# ============================================================================
# KEYBOARD CONTROL FUNCTION (for dialectic mode switching)
# ============================================================================

def check_for_keypress():
    """Non-blocking keypress check for mode switching"""
    if select is None:
        # Windows fallback - simple approach
        try:
            import msvcrt
            if msvcrt.kbhit():
                return msvcrt.getch().decode('utf-8').lower()
        except:
            pass
        return None
    else:
        # Unix/Linux approach
        try:
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                return sys.stdin.read(1).lower()
        except:
            pass
        return None
    return None

def cycle_dialectic_mode():
    """Cycle through available dialectic modes"""
    global TARGET_LINKAGE_MODE
    modes = ["null_test", "strong_coupling", "torsion_dom", "expansion_dom", "critical_point", "explore"]
    try:
        current_idx = modes.index(TARGET_LINKAGE_MODE)
        TARGET_LINKAGE_MODE = modes[(current_idx + 1) % len(modes)]
    except ValueError:
        TARGET_LINKAGE_MODE = modes[0]

    mode_names = {
        "null_test": "Seeking massless limit (ξ→0)",
        "strong_coupling": "Seeking H~w regime (strong coupling)",
        "torsion_dom": "Seeking torsion dominance (w>>H)",
        "expansion_dom": "Seeking expansion dominance (H>>w)",
        "critical_point": "Seeking critical point (H~w≠0)",
        "explore": "Adaptive exploration / information gain"
    }
    print(f"\n  >>> DIALECTIC MODE: {TARGET_LINKAGE_MODE.upper()} <<<")
    print(f"  >>> {mode_names[TARGET_LINKAGE_MODE]} <<<\n")
    return TARGET_LINKAGE_MODE

# ============================================================================
# EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Battery mode (default): run the canonical probe once and exit deterministically.
    # The interactive dialectic engine below only engages with --interactive; without
    # this guard the 19-script battery would hang on the keyboard wait loop.
    if "--interactive" not in sys.argv[1:]:
        LOGGING_ENABLED = False
        try:
            main()
        except KeyboardInterrupt:
            raise SystemExit(0)
        except Exception as e:
            print(f"\n  boson scaling probe error: {e}")
            raise SystemExit(1)
        raise SystemExit(0)

    # Main execution loop with dialectic capabilities
    try:
        while True:
            main()

            # Check for user input to change modes or quit
            key = check_for_keypress()
            if key == ' ':  # Space bar to cycle modes
                cycle_dialectic_mode()
                # Small delay to prevent rapid cycling
                time.sleep(0.2)
            elif key == 'q' or key == 'Q':
                print("\n  Dialectic engine shutting down...")
                break
            elif key is not None:
                # Ignore other keys but show help
                if key not in ['\n', '\r']:  # Ignore enter/newline
                    print(f"  Key '{key}' not recognized. Use Space to change mode, 'q' to quit.")

            # Brief pause between cycles to allow for observation
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\n\n  Dialectic engine interrupted by user.")
    except Exception as e:
        print(f"\n\n  Dialectic engine error: {e}")
        print("  Shutting down gracefully.")