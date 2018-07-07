Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: (1, 2) + (3, 4)
Out[1]: (1, 2, 3, 4)

In [2]: (1, 2) * 4
Out[2]: (1, 2, 1, 2, 1, 2, 1, 2)

In [3]: T = (1, 2) + (3, 4)

In [4]: T[0], T[1:3]
Out[4]: (1, (2, 3))

In [6]: x = (40)

In [7]: x
Out[7]: 40

In [8]: type(x)
Out[8]: int

In [9]: y = (1,)

In [10]: y
Out[10]: (1,)

In [11]: type(y)
Out[11]: tuple

In [12]: L = [1, 3, 4, 7]

In [13]: L = tuple(L)

In [14]: L
Out[14]: (1, 3, 4, 7)

In [15]: L[2]
Out[15]: 4

In [16]: L[0] = 6


In [17]: L = list(L)

In [18]: L
Out[18]: [1, 3, 4, 7]

In [19]: L.index(3)
Out[19]: 1

In [20]: L.append(5)

In [21]: L
Out[21]: [1, 3, 4, 7, 5]

In [22]: L = tuple(L)

In [23]: L.index(5)
Out[23]: 4

In [24]: L.count(1)
Out[24]: 1

In [25]: L.append(5)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-25-29c01a55dfb2> in <module>()
----> 1 L.append(5)

AttributeError: 'tuple' object has no attribute 'append'

In [26]:
