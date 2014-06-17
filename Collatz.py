#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------
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

def recursive_execute(n):

    temp = 0
    odd = 0
    if n == 1:
        return 1
    else:
        if n < cache_len and cache[n] != 0:
            return cache[n]
        if n%2 == 0:
            temp = recursive_execute(n//2) + 1
        else:
            odd = 1
            temp = recursive_execute((3*n + 1)//2) + 2
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
    if i > j:
        temp = i
        i = j
        j = temp
    base = i
    if base%2 == 0 and base != j:
        base += 1
    largest = 0
    cycle = 0
    while base <= j:
        cycle = recursive_execute(base)
        if cycle > largest:
            largest = cycle
        base += 2
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


