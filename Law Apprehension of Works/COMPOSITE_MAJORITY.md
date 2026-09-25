# COMPOSITE MAJORITY (the common-sense counting theorem, made exact)

Status: **INFORMATIONAL** — internal number-theory substrate, gated by battery
check 24 of `results_of_record.py`. Researched and verified 2026-09-25. No
physics claim; this is arithmetic about the counting substrate the thread's
prime-ladder framing leans on (RANKS_AND_DEGREES.md COUNTING direction).

> The common-sense idea under examination: *"there are more composite numbers
> than primes, because composites themselves consist of primes, while primes are
> bounded by nothing composite — only by themselves."*
>
> Verdict: the conclusion is TRUE and provable; the "because" is half-right.
> Composite abundance comes from the *sieve*, not from the fundamental theorem
> (the FTA fixes the FORM of composites, not their abundance). The "self-bounded"
> kernel is where the idea is genuinely correct.

## 1. Definitions

- `pi(n)` — number of primes ≤ n.
- `C(n)` = n − 1 − pi(n) — number of composites in {2, …, n} (1 is neither).
- `S(n)` = C(n) − pi(n) = n − 1 − 2·pi(n) — the composite-majority **margin**
  (positive = strictly more composites than primes).

## 2. Small-n landscape (exact, sieve-confirmed)

| n | pi(n) | C(n) | S(n) | reading |
|---|---|---|---|---|
| 1 | 0 | 0 | 0 | degenerate tie (neither) |
| 2 | 1 | 0 | −1 | primes lead |
| 3 | 2 | 0 | −2 | primes lead |
| 4 | 2 | 1 | −1 | primes lead |
| 5 | 3 | 1 | −2 | primes lead |
| 6 | 3 | 2 | −1 | primes lead |
| 7 | 4 | 2 | −2 | primes lead |
| 8 | 4 | 3 | −1 | primes lead |
| 9 | 4 | 4 | 0 | tie |
| 10 | 4 | 5 | **+1** | **composites win — for good** |
| 11 | 5 | 5 | 0 | tie |
| 12 | 5 | 6 | +1 | composites |
| 13 | 6 | 6 | 0 | tie |
| 14 | 6 | 7 | +1 | composites |

First strict composite majority: **n = 10** (C(10) = 5 > pi(10) = 4).

## 3. Permanence theorem (elementary proof)

**Theorem.** S(n) ≥ 0 for every n ≥ 9. Equivalently, once composites open their
lead at n = 10, they never lose it.

*Proof.* S changes by steps of one: S(n+1) − S(n) = 1 when n+1 is composite
(C gains one, pi does not) and −1 when n+1 is prime (pi gains one, C does not).

Suppose, toward a contradiction, that some n ≥ 9 has S(n) < 0. Take the least
such n. Then n is prime (a composite step raises S) and S(n−1) = 0. Since n is
prime with n ≥ 9, n is odd. But S(n−1) = 0 means (n−1) − 1 = 2·pi(n−1), i.e.
n = 2·pi(n−1) + 2, which is even. Contradiction. ∎

**Corollary (ties).** S(n) = 0 ⇔ n = 2·pi(n) + 1, so every tie is *odd*; at a
tie the next integer is even, hence composite, so the margin returns to +1. The
exact tie set up to 10⁷ (battery sieve): **{1, 9, 11, 13}** — no tie beyond 13.

**Exhaustion of ties (unconditional).** The PNT gives S(n) = n − 1 − 2·pi(n) ~
n · (1 − 2/ln n) → +∞, so there are only finitely many ties in total; the sieve
certifies that up to 10⁷ they are exactly {1, 9, 11, 13}. (Ties at 11 and 13
occur at *primes* brushing the balance from above; the tie at 9 is a composite
lifting the margin from −1 to 0.)

## 4. Asymptotics (PNT)

- pi(n) = n/ln n · (1 + o(1)); C(n) = n − 1 − pi(n) ~ n · (1 − 1/ln n).
- Composite fraction C(n)/n → 1; ratio C(n)/pi(n) ~ ln n − 1 → +∞.
- Margin S(n) ~ n − 2n/ln n → +∞ (linear in n, minus a thinning correction).

Exact margins at powers of ten (battery check 24):

| n | pi(n) | C(n) | S(n) |
|---|---|---|---|
| 10¹ | 4 | 5 | 1 |
| 10² | 25 | 74 | 49 |
| 10³ | 168 | 831 | 663 |
| 10⁴ | 1229 | 8770 | 7541 |
| 10⁵ | 9592 | 90407 | 80815 |
| 10⁶ | 78498 | 921501 | 843003 |
| 10⁷ | 664579 | 9335420 | 8670841 |

At 10⁷ the margin has grown to ≈13× pi(10⁷): primes are ≈6.65% of the numbers
(and 1/ln(10⁷) ≈ 6.2% — the PNT correction is the *phrasing* of the thinning).

## 5. Why "composites consist of primes" gives FORM, not abundance

- **True half (form).** Fundamental theorem of arithmetic: every composite m is
  an ordered product of primes, and has a prime "witness" p ≤ √m. Composites are
  *downward-referenced*: their primality-status depends entirely on primes.
  Primes are *self-bounded*: the divisor set of a prime p is exactly {1, p} —
  nothing below p certifies it. This is the kernel of "bounded only by
  themselves" and it is exactly right.
- **Incomplete half (abundance).** The FTA does not *count* composites. Composite
  density follows from the **sieve**: each newly discovered prime p permanently
  removes all multiples kp > p from the candidate set, and nothing is ever added
  back. Sieving extracts composites faster than new primes appear — that, not
  factorization, is the mechanism behind C/pi → +∞.
- **Common misconception avoided.** Fewer primes because "composites consume
  them" is false; fewer primes because every additional divisor rule removes more
  candidates is true.

## 6. Not claimed (honesty boundary)

- This theorem does NOT license any Law-thread claim such as "the self-gauged
  center is rare because it is self-bounded" (the mirror-resemblance is the
  wrong direction — self-bounded primes are the *dense*-opposite: primes are the
  *rare* self-bounded objects). Any such use would be [FRAMING] at most and is
  flagged here against it.
- No new physics; no new prime-distribution theorem. The permanence proof is
  elementary; the tie-exhaustion up to 10⁷ is a hard sieve fact in the same
  family as `pi(1e7) = 664579` and `twins < 1e7 = 58980`.

## 7. Gate

`results_of_record.py` check 24 asserts, verbatim: S(n) < 0 only for the seven
values n = 2..8; ties == [1, 9, 11, 13]; first strict composite majority n = 10;
min(S(n) for n in [9, 10⁷]) == 0; S(10⁷) == 8670841.