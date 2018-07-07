Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: L = [1, 2, 3]

In [2]: M = L

In [3]: L == M # same value
Out[3]: True

In [4]: L is M # same object
Out[4]: True

In [5]: P = [1, 2, 3]

In [6]: Q = [1, 2, 3]

In [7]: P == Q
Out[7]: True

In [8]: P is Q
Out[8]: False

In [9]: #but small integers and strings are chached and reused

In [10]: x = 42

In [11]: y = 42

In [12]: x == y
Out[12]: True

In [13]: x is y
Out[13]: True

In [14]: x is not y
Out[14]: False

In [15]: import sys

In [16]: sys.getrefcount(1)
Out[16]: 2589

In [17]: sys.getrefcount(42)
Out[17]: 23
