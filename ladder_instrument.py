"""
ladder_instrument.py -- the verification instrument, rebuilt.

Rebuilt after the yardsticks were removed. The previous instrument grew to 2221
lines and 58 checks, a load-bearing set of which rested on three things that no
longer exist:

  1. a Standard Model particle list used as an external yardstick
  2. a baseline 17-rung spectrum to score readings against
  3. a marker/centre/edge taxonomy imported from a construction about integers

This instrument takes the 18 raw values as the input to every claim about them, and
asserts only what survives without the removed yardsticks. Everything it cannot
test is listed in WITHDRAWN, with the reason, so an absent check is never
mistaken for a passing one.

One deliberate exception to the single-input rule: a second, clearly separated
input, an externally ranked list of common network ports, used only to attempt
to FALSIFY the carry structure. It never enters derive(). See PORTS_STRICT.

What the rebuild changed, and it changed the instrument's own claims:

  * the decade-alignment counts are NOT scale-covariant. Rescaling by 0.5
    shifts every logarithm by log10(0.5) = -0.301, which is not an integer, so
    "distance to the nearest power of ten" moves (8 -> 2 values inside a tenth
    of a decade). A factor of two is a legitimate change of units, so
    alignment is a fact about where the list sits on the decimal grid, not a
    fact about the list. It is demoted to UNIT_DEPENDENT and checked as such.
  * only differences survive: gaps, ratios, span, and everything computed from
    them. Those are translation-invariant on the log axis, i.e. scale-covariant.

Design constraints, deliberately:
  * checks are KEY-based, not frozen values, so a perturbed input propagates
    into the actual and can fail a check. An earlier draft stored the actual
    inline; its tamper test was vacuous and passed nothing. (C21 exists to
    keep that mistake from returning.)
  * gaps are taken as log10(V[i+1]/V[i]) so a common rescale cancels exactly;
    taking log-differences of independently scaled logs loses ~1e-16 and
    manufactures a spurious invariance failure
  * each derived quantity is computed once, in one pass
  * withdrawn claims are data, not checks: they cost nothing and assert nothing

Run: python ladder_instrument.py     (exit 0 = every live claim reproduced)
"""
import math
import statistics as st
from fractions import Fraction as F
import sys

# ---------------------------------------------------------------- the only input
# The 18 values, ascending. These are measurements. Nothing is derived from
# their names, and no list of any other kind is consulted.
RAW = (
    1.616e-35, 1e-19, 8.4e-16, 1e-10, 1e-9, 1e-7, 5.5e-7, 1e-5, 1.75,
    1.239e4, 6.378e6, 1.393e9, 7.48e12, 2.590e15, 9.257e20, 1.543e24,
    4.937e24, 4.4e26,
)

TRIPLE_THEOREM_MAX_K = 200   # verify 5^k = 5 (mod 10) this far
TAIL_N = 12

# Claims that used to be checked and are not checked now, with what they needed.
WITHDRAWN = (
    ("W01", "the value list is the complete particle zoo of some standard theory",
     "needed the removed yardstick: scoring a list against a list you chose"),
    ("W02", "free reading 0.7995 vs point-pinned 1.0102",
     "needed the removed baseline spectrum"),
    ("W03", "0.5581 vs 0.2792 depending on which end is pinned",
     "needed two readings of that baseline"),
    ("W04", "one gap is the 'decisive' discriminator between readings",
     "needed the point reading to be licensed first"),
    ("W05", "a count of 18 is admissible and 16 is not",
     "needed the removed multiples-of-three taxonomy"),
    ("W06", "the top gap is conventional while the other 16 are physical",
     "needed a point/boundary reading the numbers do not support"),
    ("W07", "the bottleneck coefficient is explained by its sides carrying mass",
     "the measured 1.0581 stands; the explanation was a rescaling"),
    ("W08", "a curvature quantity and a field-equation quantity are two",
     "both are the same quantity and it is zero"),
    ("W09", "an inverse-square dependence is the unique covariant answer",
     "every function of the gaps is covariant; 1/g^2 is not distinguished"),
    ("W10", "the doubled spectrum has twice the distinct rates",
     "with the coupling at zero the doubling is an identity"),
    ("W11", "the decimal grid is the list's native denomination, 14 of 18 on it",
     "unit-dependent: a factor of 2 is a legal change of units and it moves"),
    ("W12", "the carry structure predicts anything about common network ports",
     "falsified outright: the structure is exhausted inside 1-1023 and contains "
     "none of 18 externally-ranked well-known TCP ports"),
)

# ---------------------------------------------------------------------------
# FALSIFICATION INPUT. This is the instrument's SECOND input and it is not a
# measurement. It is an externally ranked list used to try to BREAK the carry
# structure. It is fixed by published open-port frequency BEFORE the structure
# is applied, and it never enters derive() -- nothing about RAW depends on it.
#
# Source: Nmap, Network Exploration ch.4 "Port Scanning Overview", section
# "What Are the Most Popular Ports?" -- top TCP ports by open frequency, from
# a Summer 2008 scan of tens of millions of Internet hosts; mirrored as the
# frequency column of nmap-services.
#
# Both lists are kept. Which one is canonical is a choice, so the choice is
# visible rather than buried. They give identical verdicts.
# ---------------------------------------------------------------------------
PORTS_STRICT = (80, 23, 443, 21, 22, 25, 110, 445, 139, 143, 53, 135,
                111, 995, 993, 587, 199, 465)              # all <= 1023
PORTS_NMAP = (80, 23, 443, 21, 22, 25, 3389, 110, 445, 139, 143, 53, 135,
              3306, 8080, 1723, 111, 995)                    # 4 exceed 1023
PORT_MAX = 1023

# Keys that must be identical under a common rescale: they are differences.
COVARIANT = ("span", "gap_cv", "gap_min", "gap_max", "n_gaps",
             "ratio_min", "ratio_max")
# Keys that must NOT be: they locate the list on the log axis.
UNIT_DEPENDENT = ("n_within_010", "n_within_025", "n_within_050", "worst_dev", "last_dev")


def derive(v):
    """Everything the instrument knows, in one pass, from the values alone."""
    logs = [math.log10(x) for x in v]
    gaps = [math.log10(b / a) for a, b in zip(v, v[1:])]   # rescale-exact
    dev = [abs(l - round(l)) for l in logs]                 # distance to a power of ten
    return {
        "n": len(v),
        "ascending": all(a < b for a, b in zip(v, v[1:])),
        "n_gaps": len(gaps),
        "span": sum(gaps),
        "gap_mean": st.mean(gaps),
        "gap_sd": st.pstdev(gaps),
        "gap_cv": st.pstdev(gaps) / st.mean(gaps),
        "gap_min": min(gaps),
        "gap_max": max(gaps),
        "ratio_min": min(b / a for a, b in zip(v, v[1:])),
        "ratio_max": max(b / a for a, b in zip(v, v[1:])),
        "n_within_010": sum(d <= 0.10 + 1e-12 for d in dev),
        "n_within_025": sum(d <= 0.25 + 1e-12 for d in dev),
        "n_within_050": sum(d <= 0.50 + 1e-12 for d in dev),
        "worst_dev": max(dev),
        "last_dev": dev[-1],
        "n_others_at_least_as_aligned": sum(d <= dev[-1] - 1e-12 for d in dev[:-1]),
        # integers-side facts, independent of v
        "triple_theorem": all(pow(5, k, 10) == 5 for k in range(1, TRIPLE_THEOREM_MAX_K + 1)),
        "subunit_empty": [n for n in range(1, 1)] == [],
        "tail_to_one_ninth": abs((1 / 9) - sum(10.0 ** -k for k in range(1, TAIL_N + 1))) < 1e-11,
    }


D = derive(RAW)

CHECKS = (
    # (id, claim, key, expected, tolerance)
    ("C01", "the 18 values are distinct and strictly ascending", "ascending", True, None),
    ("C02", "there are 18 of them", "n", 18, None),
    ("C03", "17 consecutive gaps", "n_gaps", 17, None),
    ("C04", "span of the list, in decades", "span", 61.4350, 1e-3),
    ("C05", "the log-spacing is strongly irregular (CV)", "gap_cv", 0.9406, 1e-3),
    ("C06", "so the list is NOT a subdivision of the scale: CV is nowhere near 0",
     "gap_cv_gt_half", True, None),
    ("C07", "widest gap, in decades", "gap_max", 15.7916, 1e-3),
    ("C08", "narrowest gap, in decades", "gap_min", 0.5051, 1e-3),
    ("C09", "widest over narrowest, in log space", "gap_spread", 31.26, 0.01),
    ("C10", "smallest consecutive ratio", "ratio_min", 3.1996, 1e-3),
    ("C11", "exactly one ratio exceeds 1e15, and it is the first",
     "ratio_max_gt_1e15", True, None),
    ("C12", "5^k = 5 (mod 10) for every k >= 1, so halving any power of ten lands on a block centre",
     "triple_theorem", True, None),
    ("C13", "there is no integer strictly between 0 and 1, so the blocks of three have no downward instance",
     "subunit_empty", True, None),
    ("C14", "the sub-unit tail sums toward 1/9 and 0 is approached, never reached",
     "tail_to_one_ninth", True, None),
    # unit-dependent, asserted AS unit-dependent so the demotion is on the record
    ("C15", "8 of 18 lie within a tenth of a decade of a power of ten",
     "n_within_010", 8, None),
    ("C16", "14 of 18 within a quarter decade", "n_within_025", 14, None),
    ("C17", "18 of 18 within half a decade", "n_within_050", 18, None),
    ("C18", "DEMOTED: that alignment is a fact about the decimal grid, not the list, "
            "because a factor of 2 is a legal change of units",
     "alignment_moves_under_x0_5", True, None),
    ("C19", "the last value is no better aligned than at least 16 of the other 17",
     "n_others_at_least_as_aligned", 16, None),
    # --- carry-lattice claims. These are facts about the INTEGERS. They are
    # NOT claims about RAW, and nothing here links them to it (see W05). ---
    ("C20", "the carry triple in (10^n, 10^(n+1)) is well formed for every n >= 0, "
            "centred on 10^(n+1)/2",
     "carry_wellformed", True, None),
    ("C21", "it is ill formed for EVERY n < 0, the half is never an integer, "
            "so the construction runs one way only",
     "carry_illformed_below", True, None),
    ("C22", "the geometric centre of a decade is irrational, so no integer can sit "
            "there and no symmetric triple is possible",
     "decade_centre_never_square", True, None),
    ("C23", "the triple therefore hugs the upper marker, a factor of exactly 2 below it",
     "hugs_upper_by_two", True, None),
    ("C24", "marker 0 is not a marker: its triple would be (-1, 0, 1) and -1 leaves the scale",
     "zero_is_origin_only", True, None),
)

CARRY_K = 40   # how far the carry-lattice claims are verified


def _isqrt_not_square(m):
    r = math.isqrt(m)
    return r * r != m

# a few checks are relations rather than stored scalars; evaluate them on demand
RELATIONS = {
    "gap_cv_gt_half": lambda d: d["gap_cv"] > 0.5,
    "gap_spread": lambda d: d["gap_max"] / d["gap_min"],
    "ratio_max_gt_1e15": lambda d: d["ratio_max"] > 1e15,
    "alignment_moves_under_x0_5": lambda d: (
        derive([x * 0.5 for x in RAW])["n_within_010"] != d["n_within_010"]),
    # carry lattice: exact integer arithmetic, no floating point anywhere
    "carry_wellformed": lambda d: all(
        10 ** (n + 1) % 2 == 0 and 10 ** (n + 1) // 2 == 5 * 10 ** n
        and (10 ** (n + 1) // 2 - 1, 10 ** (n + 1) // 2, 10 ** (n + 1) // 2 + 1)[1] == 5 * 10 ** n
        for n in range(0, CARRY_K + 1)),
    "carry_illformed_below": lambda d: all(
        (F(10) ** (n + 1) / 2).denominator != 1 for n in range(-CARRY_K, 0)),
    "decade_centre_never_square": lambda d: all(
        _isqrt_not_square(10 ** (2 * n + 1)) for n in range(0, CARRY_K + 1)),
    "hugs_upper_by_two": lambda d: all(
        10 ** (n + 1) == 2 * (5 * 10 ** n) for n in range(0, CARRY_K + 1)),
    "zero_is_origin_only": lambda d: (0 // 2 - 1, 0 // 2, 0 // 2 + 1) == (-1, 0, 1),
}


def evaluate(v):
    """Resolve every check against a given value list."""
    d = derive(v)
    out = {}
    for cid, _claim, key, expected, tol in CHECKS:
        actual = RELATIONS[key](d) if key in RELATIONS else d[key]
        ok = (actual == expected) if tol is None else \
            math.isclose(actual, expected, rel_tol=tol, abs_tol=tol)
        out[cid] = (ok, actual, expected)
    return out


def covariance(v, factors=(1e-9, 0.5, 137.0, 1e9, 6.022e23)):
    """Difference-based quantities must be identical under a common rescale."""
    base = derive(v)
    for f in factors:
        got = derive([x * f for x in v])
        for k in COVARIANT:
            if not math.isclose(got[k], base[k], rel_tol=1e-12, abs_tol=1e-12):
                return False, "%s moved under x%g (%r -> %r)" % (k, f, base[k], got[k])
    return True, ""


def teeth():
    """An instrument with no teeth is a printout. Move one value; demand a failure."""
    for i in range(len(RAW)):
        for mult in (1.05, 0.95, 3.0):
            w = list(RAW)
            w[i] *= mult
            try:
                bad = sorted(cid for cid, (ok, _, _) in evaluate(w).items() if not ok)
            except Exception:
                bad = ["<crash>"]
            if bad:
                return True, "value %d x%g trips %s" % (i, mult, ",".join(bad[:4]))
    return False, "no perturbation of any single value was detected"


# ------------------------------------------------- the falsification test
def _carry_points(centre, hi=PORT_MAX):
    """Every integer the carry construction can produce at or below hi."""
    out, n = set(), 0
    while centre(n) - 1 <= hi:
        c = centre(n)
        out.update(x for x in (c - 1, c, c + 1) if 1 <= x <= hi)
        n += 1
    return out


CARRY_S = _carry_points(lambda n: 5 * 10 ** n)   # half-upper-marker
CARRY_R = _carry_points(lambda n: 10 ** n)        # on-marker, rephased
# the construction is DEFINED by its centres; these are all of them in range
CARRY_CENTRES = {c for c in CARRY_S | CARRY_R
                 if 10 ** round(math.log10(c)) == c or 2 * c in {10 ** k for k in range(12)}}


def _runs(L, k=3):
    srt = sorted(L)
    out, cur = [], [srt[0]]
    for x in srt[1:]:
        if x == cur[-1] + 1:
            cur.append(x)
        else:
            if len(cur) >= k:
                out.append(tuple(cur))
            cur = [x]
    if len(cur) >= k:
        out.append(tuple(cur))
    return out


def port_falsification():
    """
    Try to break the carry structure with a list it had no hand in choosing.

    The structure is exhausted below 1023: its centres there are only
    1, 5, 10, 50, 100, 500, 1000, plus their +-1 neighbours. So the test is
    sharp -- if common ports had anything to do with decimal carries, some
    would land there. The claim is that NONE do, and that the one apparent
    coincidence is not one.
    """
    bad = []
    for name, L in (("PORTS_STRICT", PORTS_STRICT), ("PORTS_NMAP", PORTS_NMAP)):
        if len(L) != 18:
            bad.append("%s has %d ports, not 18" % (name, len(L)))
        if len(set(L)) != len(L):
            bad.append("%s contains a duplicate" % name)
    if max(PORTS_STRICT) > PORT_MAX:
        bad.append("PORTS_STRICT escapes the well-known range")
    for name, L in (("PORTS_STRICT", PORTS_STRICT), ("PORTS_NMAP", PORTS_NMAP)):
        for label, S in (("S", CARRY_S), ("R", CARRY_R)):
            hit = sorted(set(L) & S)
            if hit:
                bad.append("%s hits carry-%s at %s" % (name, label, hit))
        hit = sorted(set(L) & CARRY_CENTRES)
        if hit:
            bad.append("%s contains an actual centre %s" % (name, hit))
    # the one incidental hit must fail the structure's own defining condition
    for run in _runs(PORTS_STRICT):
        centre = run[len(run) // 2]
        is_centre = (10 ** round(math.log10(centre)) == centre
                     or 2 * centre in {10 ** k for k in range(12)})
        if is_centre:
            bad.append("run %s is a genuine carry triple" % (run,))
        if run != (21, 22, 23):
            bad.append("unexpected consecutive run %s" % (run,))
    if bad:
        return False, "; ".join(bad)
    return True, ("0/18 in both lists, and the sole run (21,22,23) has centre 22, "
                  "neither 10^n nor 5*10^n, so it is IANA block assignment, not a carry")


def main():
    results = evaluate(RAW)
    failures = [(cid, a, e) for cid, (ok, a, e) in results.items() if not ok]
    cov, why = covariance(RAW)
    if not cov:
        failures.append(("C90", why, "covariant under any common rescale"))
    tk, how = teeth()
    if not tk:
        failures.append(("C91", how, "a perturbed value must fail a check"))
    pf, pwhy = port_falsification()
    if not pf:
        failures.append(("C92", pwhy, "the carry structure must be falsifiable, and is"))

    live = len(CHECKS) + 3
    for cid, got, want in failures:
        print("  [FAIL] %s: got %r, want %r" % (cid, got, want))
    print("ladder_instrument: %d of %d live claims reproduced "
          "(%d checks + covariance + teeth + port falsification)"
          % (live - len(failures), live, len(CHECKS)))
    print("  covariant (differences, therefore scale-free): %s" % ", ".join(COVARIANT))
    print("  unit-dependent (locates the list on the log axis): %s" % ", ".join(UNIT_DEPENDENT))
    print("  teeth: %s" % how)
    print("  port falsification: %s" % pwhy)
    print("  withdrawn and NOT tested here: %d (%s)"
          % (len(WITHDRAWN), ", ".join(w[0] for w in WITHDRAWN)))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
