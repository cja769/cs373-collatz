#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % coverage3 run --branch TestCollatz.py

To obtain coverage of the test:
    % coverage3 report -m
"""

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_recursive

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r    = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_1 (self) :
        r    = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        i, j = collatz_read(r)
        i, j = collatz_read(r)
        self.assertEqual(i,  100)
        self.assertEqual(j, 200)

    # ---------
    # Recursive
    # ---------

    def test_recursive_1 (self):
        v = collatz_recursive(5)
        self.assertEqual(v, 6)

    def test_recursive_2 (self):
        v = collatz_recursive(1000000)
        self.assertEqual(v, 153)

    def test_recursive_3 (self):
        v = collatz_recursive(9)
        self.assertEqual(v, 20)
    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 74, 75, 23)
        self.assertEqual(w.getvalue(), "74 75 23\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, -11, 1000000, -9999999)
        self.assertEqual(w.getvalue(), "-11 1000000 -9999999\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1 (self) :
        r = StringIO("74 75\n1000 100\n1 1\n10000 15000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "74 75 23\n1000 100 179\n1 1 1\n10000 15000 276\n")

    def test_solve_2 (self) :
        r = StringIO("1 2\n1000000 1\n999999 999999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 2 2\n1000000 1 525\n999999 999999 259\n")
# ----
# main
# ----

main()

"""
coverage3 run --branch TestCollatz.py
...............
----------------------------------------------------------------------
Ran 15 tests in 23.271s

OK

----------------------------------------------------------------------

coverage3 report -m
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          63      0     24      0   100%   
TestCollatz      66      1      0      0    98%   129
---------------------------------------------------------
TOTAL           129      1     24      0    99%  
"""
