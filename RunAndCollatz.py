#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------
import sys
cache = [0] * 1000000
cache_len = 1000000
def collatz_read (r) :
    """
    read two ints
    r is a reader
    return a list of the two ints, otherwise a list of zeros
    """
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]

# -----------------
# collatz_recursive
# -----------------

def collatz_recursive(n):
    """
    recursively finds the cycle of n and then stores it in the
    cache by taking advantage of recursive backtracking
    n is the current number we're finding the cycle for
    return an int that represents the cycle of n
    """

    temp = 0
    odd = 0 # if n is odd then we have to fill the cache for index 3n+1 and for n
    if n == 1:
        return 1
    else:
        if n < cache_len and cache[n] != 0:
            return cache[n]
        if n%2 == 0:
            temp = collatz_recursive(n//2) + 1
        else:
            odd = 1
            temp = collatz_recursive((3*n + 1)//2) + 2
        if n < cache_len:
            cache[n] = temp
        odd_case = 3*n +1
        if odd and odd_case < cache_len:
            cache[odd_case] = temp-1
    return temp

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    if i > j: # we want to make sure that we start at i and end at j
        temp = i
        i = j
        j = temp
    base = i
    half = j//2
    if half+1 >= i:
        base = half+1
    largest = 0
    cycle = 0
    while base <= j:
        cycle = collatz_recursive(base)
        if cycle > largest:
            largest = cycle
        base += 1
    return largest

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)


collatz_solve(sys.stdin, sys.stdout)
