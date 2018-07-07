Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: list1 = list(map(abs, [-1, -2 , 0, 1, 2]))

In [2]: list1
Out[2]: [1, 2, 0, 1, 2]

In [3]: L = [[1, 2, 3], 345, "string"]

In [4]: type(L[0])
Out[4]: list

In [5]: type(L[1])
Out[5]: int

In [6]: type(L[2])
Out[6]: str

In [7]: list1
Out[7]: [1, 2, 0, 1, 2]

In [8]: list1.sort()

In [9]: list1
Out[9]: [0, 1, 1, 2, 2]

In [10]: list1.sort(reverse = True)

In [11]: list1
Out[11]: [2, 2, 1, 1, 0]

In [12]: import random

In [13]: L = [random.randint(1, 10) for i in range(10)]

In [14]: L
Out[14]: [6, 9, 8, 9, 2, 4, 5, 1, 1, 8]

In [15]: del L[5:]

In [16]: L
Out[16]: [6, 9, 8, 9, 2]

In [17]: L.extend([random.randint(1, 10) for i in range(10)])

In [18]: L
Out[18]: [6, 9, 8, 9, 2, 9, 4, 1, 4, 5, 7, 10, 5, 7, 4]

In [19]: L.sort()

In [20]: L
Out[20]: [1, 2, 4, 4, 4, 5, 5, 6, 7, 7, 8, 9, 9, 9, 10]

In [21]: del L[L.index(5):]

In [22]: L
Out[22]: [1, 2, 4, 4, 4]

In [23]: L[0] = []

In [24]: L
Out[24]: [[], 2, 4, 4, 4]

In [25]: D = dict(name = "John", age = 24)

In [26]: D.pop(name)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-26-b1c9d775c5da> in <module>()
----> 1 D.pop(name)

NameError: name 'name' is not defined

In [27]: D
Out[27]: {'name': 'John', 'age': 24}

In [28]: D.pop("name")
Out[28]: 'John'

In [29]: D
Out[29]: {'age': 24}

In [30]: del D["age"]

In [31]: D
Out[31]: {}

In [32]: D = {x: x*2 for x in range(10)}

In [33]: D
Out[33]: {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}

In [34]: D.keys()
Out[34]: dict_keys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [35]: D.keys() & D.values()
Out[35]: {0, 2, 4, 6, 8}

In [36]: list(D.keys())
Out[36]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [37]: list(D.keys()).sort(reverse = True)

In [38]: D.keys() # return iterator
Out[38]: dict_keys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [39]: D.get(5)
Out[39]: 10

In [40]: D.get("key")

In [41]: print(D.get("key"))
None

In [42]: Matrix = {(2, 3, 4): 88, (7, 8, 9): 99}

In [43]: try:
    ...:     print(Matrix[(2, 3, 6)])
    ...: except KeyError:
    ...:     print(0)
    ...:
0

In [44]: try:
    ...:     print(Matrix[(2, 3, 4)])
    ...: except KeyError:
    ...:     print(0)
    ...:
88

In [45]: # same

In [46]: Matrix.get((2, 3, 6), 0)
Out[46]: 0

In [47]: K = ["a", "b", "c"]

In [48]: V = [1, 2, 3]

In [49]: L = list(zip(K, V))

In [50]: L
Out[50]: [('a', 1), ('b', 2), ('c', 3)]

In [51]: D = dict(zip(K, V))

In [52]: D
Out[52]: {'a': 1, 'b': 2, 'c': 3}

In [53]: D = {c.lower(): c + "!" for c in ["SPAM", "EGGS", "HAM"]}

In [54]: D
Out[54]: {'spam': 'SPAM!', 'eggs': 'EGGS!', 'ham': 'HAM!'}
