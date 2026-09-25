# RANKS AND DEGREES (the two-axis expansion, expanded all directions 2026-09-25)

Law-thread, informational. Formalizes the thread's ladder as a coordinate system:
every entry in the framework is a point (rank, degree). All numbers below are
verified readings from the canonical corpus (corrigendum 70; battery; script
expansion pass 2026-09-25); the vocabulary itself is machinery, not physics.
Supersedes the draft table of the same day (atom was r=1 there; renumbered to
a full Planck-to-Hubble ladder — see corrigendum 74).

## Definitions

- RANK r: the position of a scale rung on the ladder. r = 0 is the datum (the
  point); r = 1..16 are the rungs from the Planck floor to the Hubble sphere,
  in size order. Rank is the "how high" axis. The primes indexed these: the
  counting sense of the ladder is 0,1,primes (node B1).
- DEGREE d: the dimensionality of the embedding structure at that rung.
  d = 0 point (constant; size^0), d = 1 line (size^1), d = 2 plane (size^2),
  d = 3 solid (size^3). In the algebraic sense the doubling chain gives the
  degree sequence 1,2,4,8 (Frobenius/Hurwitz caps, node C2) — algebraic only.
- RUNG size: s(r) = u_0 * kappa^r would be uniform (geometric) growth. The real
  ladder is irregular: log10(s) at consecutive rungs has unequal gaps, exactly
  like prime gaps — uniform growth is the MEAN (PNT-style), not the law.
- READING: n(u) = s/u (self-gauge lemma; n ~ 1/u, unit-invariant). This is how
  rank and degree interact observationally.

## The (rank, degree) table — full ladder, Planck to Hubble, ball = 550 nm source

| r | rung | size s (m) | log10(s/m) | gap | ball n(u) = D/s | ball degree here |
|---|---|---|---|---|---|---|
| 0 | datum / point | - | -inf | - | 0 ticks (own gauge) | 0 |
| 1 | Planck | 1.616e-35 | -34.79 | - | 3.40e+28 | 3 (solid down here) |
| 2 | quark | 1e-19 | -19.00 | 15.79 | 5.5e+12 | 3 |
| 3 | proton | 8.4e-16 | -15.08 | 3.92 | 6.55e+08 | 3 |
| 4 | atom | 1e-10 | -10.00 | 5.08 | 5.5e+03 | 3 (colloid; Mie region) |
| 5 | molecule | 1e-9 | -9.00 | 1.00 | 5.5e+02 | 3 |
| 6 | virus | 1e-7 | -7.00 | 2.00 | 5.5 | 3 |
| 7 | ball | 5.5e-7 | -6.26 | 0.74 | 1.0 | 3 (own rung, n = 1) |
| 8 | cell | 1e-5 | -5.00 | 1.26 | 0.055 | DEGREE COLLAPSE (reads 0D) |
| 9 | human | 1.75 | +0.24 | 5.24 | 3.14e-07 | 0 |
| 10 | Earth | 6.378e6 | +6.80 | 6.56 | 8.62e-14 | 0 |
| 11 | Sun | 1.393e9 | +9.14 | 2.34 | 3.95e-16 | 0 |
| 12 | Solar system (Kuiper 50 AU) | 7.48e12 | +12.87 | 3.73 | 7.35e-20 | 0 |
| 13 | galaxy (30 kpc) | 9.257e20 | +20.97 | 8.09 | 5.94e-28 | 0 |
| 14 | Great Attractor (50 Mpc) | 1.543e24 | +24.19 | 3.22 | 3.56e-31 | 0 |
| 15 | Laniakea (160 Mpc) | 4.937e24 | +24.69 | 0.51 | 1.11e-31 | 0 |
| 16 | Hubble sphere | 4.4e26 | +26.64 | 1.95 | 1.25e-33 | 0 |

Gaps: 15.79, 3.92, 5.08, 1.00, 2.00, 0.74, 1.26, 5.24, 6.56, 2.34, 3.73,
8.09, 3.22, 0.51, 1.95 — none equal; rank positions are irregular everywhere,
uniform growth only the average law (PNT mean-gap result). All values recomputed
by script 2026-09-25 (log10, gap, n(u); D = 550 nm).

## Degree collapse (the main corollary)

An object at rank r_obj keeps its native degree d_obj only while u < s_obj
(n(u) >= 1). Above that rank, its reading is fractional (< 1 tick) and it is
OBSERVABLE only as a degree-0 point:

    ball r=7, d=3  ->  at r>=8 (cell) effective degree becomes 0.
    Verified: 1 um tick -> n = 0.55 (< 1); Earth n = 8.62e-14; GA 3.56e-31;
    Laniakea 1.11e-31; Hubble sphere 1.25e-33 (corrigendum 70 ladder).

This is the Law of Center Ascent's L2 (resolution bound) restated in degrees:
"as high as it can go" = the last rank where its degree survives. The datum
(rank 0, degree 0) collapses at every rank and still climbs — its degree never
changes, so nothing stops it (L1).

## Rank x degree product (the expansions)

For an object in dimension d at rank r:

    extent    ~ s(r)^1
    cross-sec ~ s(r)^2          (geometric only: Mie C = Q*pi*R^2, Q = 3.4822)
    volume    ~ s(r)^3          (mass: rho*s^3; ball 8.71e-20 m^3 verified)
    Mie x     ~ s(r)^1          (x = pi exactly at ball rung; Qe = Qs = 3.4822)
    CONTACT spot is NOT ~ s^2: JKR zero-load a = (6*pi*w*R^2/E*)^{1/3}
        -> a ~ s^(2/3), spot area ~ s^(4/3); Hertz loaded a ~ s^(1/3)
        [corrected in place, corrigendum 76: draft said "JKR spot ~ s^2"]

Degrees beyond 3 are algebraic only (1,2,4,8); spatial physics caps at 3+1
(entry-70 and Bott-periodicity discipline, node C2).

## Expansion in the four other directions (verified values only)

DOWN (rungs below the ball, all degree-3 readings with huge tick counts):
    Planck n = 3.4e28  ->  ball as a solid fills 3.4e28 Planck lengths.
    quark n = 5.5e12; proton n = 6.55e8 — the ball is a solid *everywhere below*
    its own rung; the "point" identity (corrigendum 70) only ever claims the
    regime ABOVE ~um, never below.

UP (rungs above, all degree-0 collapsed readings):
    human 3.14e-07; Earth 8.62e-14; Sun 3.95e-16; Solar-system 7.35e-20;
    galaxy 5.94e-28; GA 3.56e-31; Laniakea 1.11e-31; Hubble 1.25e-33.
    The reading keeps shrinking 33+ orders past the datum — this is the measured
    content of "as high as it can go" (L2).

ALGEBRA (the degree cap, theorem-proven): the doubling chain 1,2,4,8 stops at
Hurwitz; Cl(0,8) Bott period-8 repeats the table. i period 4 (i^2 = -1, i^4 = 1)
is the pi/2 turn. All gate-asserted (results_of_record checks 19-21); the
algebra is the C2 machinery, not physics (3(+1)D is empirical).

SPIRAL (the turn-walk, node C2; corrected in place 2026-09-25, corrigendum 74):
    The ladder walk 0,1,primes with pi/2 turns (E,N,W,S, period 4) is an OPEN
    SPIRAL, not nested squares. The draft claim "radius^2 = sum of squares of
    ladder terms" is FALSE (fails from step 3 on). Verified vertices:
        steps 0,1,2,3,5,7,11,13,17,19 -> endpoint (9,11), r^2 = 202;
        step 6 (through L=11) -> vertex (-8, 5), r^2 = 89   (sum L^2 = 209);
        the 6 steps 0,1,2,3,5,7 -> (3,5), r^2 = 34 (sum L^2 = 88);
        steps 0..7 (through L=13) -> (-8,-8), r^2 = 128.
    Exact identity (holds for any turn-walk with period-4 turns):
        r^2 = (sum of E-W contributions)^2 + (sum of N-S contributions)^2,
        x = L0 + L4 + ... - L2 - ...;  y = L1 + L5 + ... - L3 - ...

COUNTING SUBSTRATE (node B1, the ladder's spacing statistics):
    pi(1e7) = 664579 (sieve-verified, n/ln n 6.6% off); twins < 1e7 = 58980
    (Hardy-Littlewood 2*C2*x/ln^2 x ~ 50822, 14% as-yet asymptotic error -
    CONJECTURE, evidence only). Mean gap ~ ln p stays the only reliable law;
    the irregular gaps ARE the dense texture that the conjectures live in.
    External anchor (STATE_OF_THE_SCIENCE_2026 §1.4, 2026-09): across all known
    prime data, gaps never beat merit 41.94 (2017 Gapcoin) or CSG 0.9206 (known
    maxima); largest gap 16,045,848 (PRP ends) / 1,113,106 (proven ends). The
    ladder's irregular log10 spacing (gaps 0.51-14.16 decades, max/min ~28) sits
    well within those real bounds — a bounded resemblance, FRAMING only.

## Discipline

RANKS and DEGREES are the thread's coordinates, not new physics. Every number in
the table is a verified reading or a computed one from the battery (entry 70,
battery, expansion pass); the vocabulary is FRAMING machinery with a proven
skeleton (PNT mean-gap, the 1,2,4,8 theorem caps, the self-gauge invariance).
Nothing here asserts that the universe "is" rank-degree; it asserts the ladder
is irregular like primes, the 3+1 caps are real, and the degree collapse is
measured.