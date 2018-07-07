Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: s = "hello world"

In [2]: s
Out[2]: 'hello world'

In [3]: print(s)
hello world

In [4]: repr(s)
Out[4]: "'hello world'"

In [5]: str(1/7)
Out[5]: '0.14285714285714285'

In [6]: repr(1/7)
Out[6]: '0.14285714285714285'

In [7]: hello = "hello world\n"

In [8]: hello
Out[8]: 'hello world\n'

In [9]: print(hello)
hello world


In [10]: # \n is valid.

In [11]: repr(hello)
Out[11]: "'hello world\\n'"

In [12]: for x in range(1, 11):
    ...:     print("{0:2d} {1:3d} {2:4d}".format(x, x*x, x*x*x))
    ...:
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000

In [13]: for x in range(1, 11):
    ...:     print("{0}{1}{2}".format(x, x * x, x * x * x))
    ...:
111
248
3927
41664
525125
636216
749343
864512
981729
101001000

In [14]: # zfill()

In [15]: "12345".zfill(10)
Out[15]: '0000012345'

In [16]: "12.34".zfill(6)
Out[16]: '012.34'

In [18]: # "." is also counted

In [19]: table = {}

In [20]: table = {"Bob": 2364, "john": 3265, "Mike": 2653}

In [21]: for name, score in table.items():
    ...:     print("{0:10} ==> {1:6d}".format(name, score))
    ...:
Bob        ==>   2364
john       ==>   3265
Mike       ==>   2653
