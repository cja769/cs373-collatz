#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------
cache = [0] * 100000
cache_len = 100000
def collatz_read (r) :
    assert(r is not None)
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
    assert (n is not None)
    assert (n > 0)
    temp = 0
    odd = False # if n is odd then we have to fill the cache for index 3n+1 and for n
    if n == 1:
        return 1
    else:
        if n < cache_len and cache[n] != 0:
            return cache[n]
        if n%2 == 0:
            temp = collatz_recursive(n//2) + 1
        else:
            odd = True
            temp = collatz_recursive((3*n + 1)//2) + 2 # optimized since 3n+1 for odd n will be even
        assert (temp is not None)
        if n < cache_len:
            cache[n] = temp
        odd_case = 3*n +1
        if odd and odd_case < cache_len:
            cache[odd_case] = temp-1 # fill in for the case we skipped
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
    assert (i is not None and j is not None)
    assert (i > 0 and j > 0)
    if i > j:          # we want to make sure that we start at i and end at j
        temp = i
        i = j
        j = temp
    base = i
    half = j//2
    if half+1 >= i:     # *from quiz* if for an n there exist 2n in the range from i->j
        base = half+1   #  then we know that 2n will have a larger cycle therefore we
    largest = 0         #  we don't need to bother calculating n
    cycle = 0
    while base <= j:
        cycle = collatz_recursive(base)
        assert (cycle is not None and cycle >= 0)
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
    assert(w is not None)
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
    assert (r is not None and w is not None)
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        assert (i is not None and j is not None)
        v = collatz_eval(i, j)
        assert (v is not None and v >= 0)
        collatz_print(w, i, j, v)


