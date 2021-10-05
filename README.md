# rearrangement_theorem
A classroom demonstration of Riemann series theorem (Riemann rearrangement theorem)

Riemann series theorem (or Riemann rearrangement theorem) says that if an infinite series of real numbers is conditionally convergent, then its terms can be arranged in a permutation so that the new series converges to an arbitrary real number, or diverges. More about the theorem can be found in the wikipedia[1] or any introductory real analysis textbook.

One proof of Riemann series theorem is algorithmic: given a conditionally convergent series and a target limit (which could either be a real number, +\infty, or -\infty), the proof gives a recipe to rearrange the terms of the series so that the new series converge to an arbitrary real number. 

Functions:

1. binarySequence(power)
Given an integer power >= 1, return the list 1, 1/2, 1/2, 1/4, 1/4, 1/4, 1/4, ..., with the last 2^power-many terms being 1/2^power.

2. printSeries(L, l)
Given the first n terms L of a conditionally convergent series in form of a list, print the first l partial sums of the series, with l <= n. The i-th partial sum of the series is defined to be the sum of first i terms of the list L.

3. defaultSequence(p,n)
Given a list p of positive numbers and a list n of negative numbers, return a list r consisting of terms in p and n appearing alternately, until every term in one of p and n is used up. The unused terms of p or n are appended at the end of r.

4. targetSequence(p,n, target, l)
Given a list p of positive numbers, a list n of negative numbers, a target limit target, and positive integer l, the first l partial sums of the rearranged series.

Reference: 
[1] https://en.wikipedia.org/wiki/Riemann_series_theorem
