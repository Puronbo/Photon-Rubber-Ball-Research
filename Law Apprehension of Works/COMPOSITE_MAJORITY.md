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

`results_of_record.py` checks 24-26 assert, verbatim:

- check 24 (composite-majority): S(n) < 0 only for n = 2..8; ties == [1, 9,
  11, 13]; first strict composite majority n = 10; min(S(n) for n in
  [9, 10⁷]) == 0; S(10⁷) == 8670841.
- check 25 (runs): 201!+2..201!+201 is a run of 200 consecutive composites,
  divisibility j | (201!+j) exact — witness the unboundedness of prime-free
  runs (any length n from (n+1)!+2, classical construction).
- check 26 (small-factor dominance): among the integers ≤ 10⁷, exactly
  7,714,287 are divisible by one of 2,3,5,7 (2,285,713 are coprime to 210).

## 8. The claim tree — every claim this idea can carry, verdict-coded

All verdicts as of 2026-09-25. PROVEN(gate) = asserted by `results_of_record.py`
(53 checks). PROVEN(cls) = elementary/classical theorem, quoted. CONJECTURE =
open or empirically-suggested only. FALSE = tested and rejected. FRAMING =
coherent in the Law thread's vocabulary, but not a science claim.

### A. Counting claims (the core)
| # | claim | verdict | witness |
|---|---|---|---|
| C1 | There are more composites than primes (in prefix [1, n]) for every n ≥ 10 | PROVEN(gate) | C(10)=5 > π(10)=4; permanence S(n) ≥ 0 for n ≥ 9 |
| C2 | The margin S(n)=C−π is never negative from n = 9 on | PROVEN(cls) | elementary parity/odd-prime proof |
| C3 | n = 10 is the first n with strict composite majority; n = 8 the last with prime majority | PROVEN(gate) | exact table 1..14 |
| C4 | Ties (C=π) in [1, 10⁷] are exactly {1, 9, 11, 13} | PROVEN(gate,finite) | battery sieve; unconditional: p_k ≥ 2k+1 ⇒ none for n ≥ 15 |
| C5 | Ties are finite in total | PROVEN(cls) | PNT: S(n) ~ n → +∞ |
| C6 | Composite fraction C(n)/n → 1 | PROVEN(cls) | PNT |
| C7 | Ratio C(n)/π(n) ~ ln n − 1 → +∞ | PROVEN(cls) | PNT |
| C8 | Margin S(n) ~ n − 2n/ln n → +∞ | PROVEN(cls) | PNT |
| C9 | At 10⁷ the margin is 8,670,841 (≈13× the prime count) | PROVEN(gate) | check 24 |
| C10 | Most numbers carry a small prime factor: exactly 77.14287% of n ≤ 10⁷ divide by one of 2,3,5,7 | PROVEN(gate) | check 26 |

### B. Structural claims
| # | claim | verdict | witness |
|---|---|---|---|
| C11 | Every composite m has a prime witness p ≤ √m | PROVEN(cls) | least prime divisor bound |
| C12 | Every composite is a product of primes (FTA) | PROVEN(cls) | FTA |
| C13 | Primes are self-bounded: divisor set exactly {1, p} | PROVEN(cls) | definition |
| C14 | C composites are prime-bounded: their divisor set contains a prime | PROVEN(cls) | C11 |
| C15 | "Composites are more numerous BECAUSE they are prime products" | FALSE-as-mechanism | FTA fixes form; the sieve produces abundance; the causal deduction is invalid though the conclusion survives |
| C16 | Unbounded prime-free runs exist (gaps are arbitrarily long) | PROVEN(gate) | check 25: 201!+2..+201; classical (n+1)! construction |
| C17 | The sieve "wins" the counting race (removals beat additions) | PROVEN(framed) | lifetime removals per new prime; PNT restates it as π/n → 0 |
| C18 | Almost all numbers have exactly ~ln ln n prime factors (Erdős–Kac) | PROVEN(cls) | Erdős–Kac |
| C19 | ∫ Mertens: ∏_{p≤z}(1−1/p) ~ e^−γ/ln z → 0 (fresh candidates are fewer) | PROVEN(cls) | Mertens |

### C. Window claims (traps)
| # | claim | verdict | witness |
|---|---|---|---|
| C20 | "Any interval of the integers has more composites than primes" | FALSE | window [2,3]: 1 prime, 0 composites |
| C21 | "The composite majority proves the twin-prime or k-tuple conjectures" | FALSE/conflation | twins=58980 < 10⁷ is exact but finite; 2·C₂·x/ln²x = 50822 is 14% off — CONJECTURE (gate note, check 23) |

### D. Ladder / Law-thread mirror claims (honesty boundary)
| # | claim | verdict | witness |
|---|---|---|---|
| C22 | "Prime-gap-like irregular ladder spacing is EXPLAINED by composite majority" | FALSE-as-derivation | ladder spacing is check-18-verified and independent; correlation ≠ mechanism |
| C23 | "Self-bounded things are rare ⇒ the self-gauged center is rare" | FALSE | no mapping integers→objects; and self-bounded primes are the RARE object, the exact mirror of any 'abundance' claim |
| C24 | "Composites' abundance confirms the center is common/naturally supported" | FRAMING | vocabulary-level only; no science content |
| C25 | "The sieve validates the law of thinning/multiplication as physics" | FRAMING | sieve is arithmetic; do not cite as experiment |

### E. Meta-claims
| # | claim | verdict | witness |
|---|---|---|---|
| C26 | Every numeric claim above is reproducible by the 26-check gate | PROVEN | `python results_of_record.py` exit 0 |
| C27 | The catalog above is exhaustive within this idea-family | PROVEN(modest) | pruning rule: any further claim is a restatement, an instance of C1-C26, or a window-trap of class C20 |

Not claimed, ever (explicit): any physics, any experimental citation, any
"center" consequence — those all die at C22-C25.

## Appendix A. The tie-exhaustion lemma, proved unconditionally (checks 24 + C2)

The gate asserts the composite-majority pattern only to 10⁷. In fact it is a
theorem for every positive integer. Let S(n) = (n-1) - 2·π(n). Then:

- (i)   S(n) < 0  if and only if  n ∈ {2,...,8};
- (ii)  S(n) = 0  if and only if  n ∈ {1, 9, 11, 13};
- (iii) n = 10 is the first strict composite majority (S(10) = 1);
- (iv)  S(n) ≥ 0 for every n ≥ 9.

Proof. Finite check: for n ≤ 16 the values of π(n) (4,4,5,5,6,6,6,6 on
9..16) give S(9..16) = 0,1,0,1,0,1,2,3 and S(2..8) = -1,-2,-1,-2,-1,-2,-1,
so (i)-(iii) and (iv) on [9,16] hold, and S(1) = 0 is the initial tie.
For n ≥ 17 use the classical Rosser–Schoenfeld bound π(n) < 1.25506·n/ln n:
2·π(n) < 2.51012·n/ln n ≤ n - 1  because  2.51012/ln n ≤ 1 - 1/n  for
n ≥ 17 (checked at n = 17: 2.51012/2.8332 = 0.886 ≤ 0.941; the left side
decreases). Hence S(n) ≥ 0 for all n ≥ 17, completing (iv). QED.

Corollary: the counting window (C2) is unconditional arithmetic — the gate
reproduces it exhaustively to 10⁷, the proof covers all n. Scope note: this
proves an ARITHMETIC lemma about π(n); it is silent on primes at large scales
beyond the cited bound and says nothing about any physical object (C22-C25).