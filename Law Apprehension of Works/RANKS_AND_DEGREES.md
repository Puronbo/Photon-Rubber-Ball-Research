# RANKS AND DEGREES (the two-axis expansion)

Law-thread, informational. Formalizes the thread's ladder as a coordinate system:
every entry in the framework is a point (rank, degree). All numbers below are
verified readings from the canonical corpus (entry scales, corrigendum 70;
battery); the vocabulary itself is machinery, not physics.

## Definitions

- RANK r: the position of a scale rung on the ladder. r = 0 is the datum (the
  point); r = 1,2,3,... index the rungs above it. Rank is the "how high" axis.
  The primes indexed these: the ladder is 0,1,primes in the counting sense
  (node B1) and each appended prime adds one rank.
- DEGREE d: the dimensionality of the embedding structure at that rung.
  d = 0 point (constant; size^0), d = 1 line (size^1), d = 2 plane (size^2),
  d = 3 solid (size^3). In the algebraic sense the doubling chain gives the
  degree sequence 1,2,4,8 (Frobenius/Hurwitz caps, node C2).
- RUNG size: s(r) = u_0 * kappa^r would be uniform (geometric) growth. The real
  ladder is irregular: log10(s) at consecutive rungs has unequal gaps, exactly
  like prime gaps - uniform growth is the MEAN (PNT-style), not the law.
- READING: n(u) = s/u (self-gauge lemma; n ~ 1/u, unit-invariant). This is how
  rank and degree interact observationally.

## The (rank, degree) table — canonical rungs, ball = 550 nm source

| r | rung | log10(s/m) | gap | ball reading n(u) | effective degree of the ball here |
|---|---|---|---|---|---|
| 0 | datum / point | -inf | - | 0 ticks (own gauge) | 0 |
| 1 | atom | -10.0 | - | 5.5e+03 | 3 (colloid ranking device) |
| 2 | molecule | -9.0 | 1.0 | 5.5e+02 | 3 |
| 3 | virus | -7.0 | 2.0 | 5.5 | 3 |
| 4 | ball | -6.26 | 0.74 | 1.0  | 3 (its own rung, n = 1) |
| 5 | cell | -5.0 | 1.26 | 0.055 | DEGREE COLLAPSE: reads 0D point |
| 6 | ... | ... | irregular (prime-gap-like) | <1 | 0 |
| 17 | Earth | +6.80 | ~12 | 8.62e-14 | 0 |
| 31 | galaxy | +20.97 | ~14 | 5.94e-28 | 0 |
| 33 | Great Attractor | +24.19 | ~3 | 3.56e-31 | 0 |
| 34 | Laniakea | +24.69 | ~0.5 | 1.11e-31 | 0 |

Gap column: consecutive log10 steps are NOT equal (1.0, 2.0, 0.74, 1.26, ~12,
~14, ~3, ~0.5) - rank positions follow the irregular (prime-like) spacing;
uniform growth is only the average law (PNT mean-gap result). All values
recomputed by script 2026-09-25 (log10 and n(u) column, D = 550 nm source;
Laniakea log10 = +24.69 corrected in place before first commit).

## Degree collapse (the main corollary)

An object at rank r_obj keeps its native degree d_obj only while u < s_obj
(n(u) >= 1). Above that rank, its reading is fractional (< 1 tick) and it is
OBSERVABLE only as a degree-0 point:

    ball r=4, d=3  ->  at r>=5 (cell) effective degree becomes 0.
    Verified: 1 um tick -> n = 0.55 (< 1); Earth n = 8.62e-14; GA n = 3.56e-31
    (corrigendum 70, entry-70 ladder).

This is the Law of Center Ascent's L2 (resolution bound) restated in degrees:
"as high as it can go" = the last rank where its degree survives. The datum
(rank 0, degree 0) collapses at every rank and still climbs - its degree never
changes, so nothing stops it (L1).

## Rank x degree product (the expansions)

For an object in dimension d at rank r:

    extent    ~ s(r)^1
    area      ~ s(r)^2          (surface physics: JKR spot ~ s^2, Mie cross-section)
    volume    ~ s(r)^3          (mass: rho*s^3; ball 8.71e-20 m^3 verified)
    Mie x     ~ s(r)^1          (x = pi exactly at ball rung; Qe = Qs = 3.4822)

Degrees beyond 3 are algebraic only (1,2,4,8); spatial physics caps at 3+1
(entry-70 and Bott-periodicity discipline, node C2).

## Discipline

RANKS and DEGREES are the thread's coordinates, not new physics. Every number in
the table is a verified reading or a computed one from the battery (entry 70);
the vocabulary is FRAMING machinery with a proven skeleton (PNT mean-gap, the
1,2,4,8 theorem caps, the self-gauge invariance). Nothing here asserts that the
universe "is" rank-degree; it asserts the ladder is irregular like primes, the
3+1 caps are real, and the degree collapse is measured.