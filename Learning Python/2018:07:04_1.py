Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from fractions import Fraction

In [2]: x = Fraction(1, 3); y = Fraction(4, 6)

In [3]: x
Out[3]: Fraction(1, 3)

In [4]: x + y
Out[4]: Fraction(1, 1)

In [5]: x * y
Out[5]: Fraction(2, 9)

In [6]: x / y
Out[6]: Fraction(1, 2)

In [7]: x // y
Out[7]: 0

In [8]: - x
Out[8]: Fraction(-1, 3)

In [9]: x ** 2
Out[9]: Fraction(1, 9)

In [10]: import math

In [11]: math.sin(x)
Out[11]: 0.3271946967961522

In [12]: math.sin(Fraction(math.pi, 6))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-12-bd758c70fb9c> in <module>()
----> 1 math.sin(Fraction(math.pi, 6))

/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/fractions.py in __new__(cls, numerator, denominator, _normalize)
    172                 )
    173         else:
--> 174             raise TypeError("both arguments should be "
    175                             "Rational instances")
    176

TypeError: both arguments should be Rational instances

In [13]: print(x)
1/3

In [14]: Fraction(math.pi)
Out[14]: Fraction(884279719003555, 281474976710656)

In [15]: 1/3
Out[15]: 0.3333333333333333

In [16]: 2 / 6
Out[16]: 0.3333333333333333

In [17]: 12 / 36
Out[17]: 0.3333333333333333

In [18]: (2.5).as_integer_ratio()
Out[18]: (5, 2)

In [19]: f = 2.5

In [20]: z = Fraction(*f.as_integer_ratio())

In [21]: z
Out[21]: Fraction(5, 2)

In [22]: float(z)
Out[22]: 2.5

In [23]: float(Fraction(1/7))
Out[23]: 0.14285714285714285

In [24]: (4/3).as_integer_ratio()
Out[24]: (6004799503160661, 4503599627370496)

In [25]: set1 = {1, 2, 3, 4}

In [26]: set1.add(5)

In [27]: set1
Out[27]: {1, 2, 3, 4, 5}

In [28]: set2 ={i for i in range(2, 9)}

In [29]: set1 & set2
Out[29]: {2, 3, 4, 5}

In [30]: set1 | set2
Out[30]: {1, 2, 3, 4, 5, 6, 7, 8}

In [31]: set1 > set2
Out[31]: False

In [32]: set1 < set2
Out[32]: False

In [33]: S = set{[]}
  File "<ipython-input-33-ff4979aeb93c>", line 1
    S = set{[]}
           ^
SyntaxError: invalid syntax


In [34]: S = set([])

In [35]: type(S)
Out[35]: set

In [36]: T = {}

In [37]: type(T)
Out[37]: dict

In [38]: # {} is empty dict

In [39]: set1
Out[39]: {1, 2, 3, 4, 5}

In [40]: (1, 2) in set1
Out[40]: False

In [41]: 1 in set1
Out[41]: True

In [42]: [1, 2] in set1
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-42-fbed9be8b7a6> in <module>()
----> 1 [1, 2] in set1

TypeError: unhashable type: 'list'

In [43]: {1, 2} in set1
Out[43]: False

In [44]: {x for x in "some string"}
Out[44]: {' ', 'e', 'g', 'i', 'm', 'n', 'o', 'r', 's', 't'}

In [45]: {x * 4 for x in "spam"}
Out[45]: {'aaaa', 'mmmm', 'pppp', 'ssss'}

In [46]: True + 1
Out[46]: 2

In [47]: False + 2
Out[47]: 2

In [48]: True * 5
Out[48]: 5

In [49]: True == 1
Out[49]: True

In [50]: math.pi
Out[50]: 3.141592653589793

In [51]: math.sqrt(2)
Out[51]: 1.4142135623730951

In [52]: pow(2, 0.5)
Out[52]: 1.4142135623730951

In [53]: 2 ** .5
Out[53]: 1.4142135623730951

In [54]: root_2 = 2 ** .5

In [55]: round(root_2, 3)
Out[55]: 1.414

In [56]: round(root_2, 0)
Out[56]: 1.0

In [57]: L1 = [1, 2, 3]

In [58]: L2 = L1

In [59]: L1[0] = 123

In [60]: L2
Out[60]: [123, 2, 3]

In [61]: L1
Out[61]: [123, 2, 3]

In [62]: # solution

In [63]: L1 = [1, 2, 3]

In [64]: L2 = L1[:]

In [65]: L1[0] = 123

In [66]: L1
Out[66]: [123, 2, 3]

In [67]: L2
Out[67]: [1, 2, 3]

In [68]: # but this method is only valid for list(sequence)

In [69]: # set, dict can use .copy()

In [70]: import copy

In [71]: S = {1, 2, 3}

In [72]: T = copy.copy(S)

In [73]: T
Out[73]: {1, 2, 3}

In [74]: S.add(4)

In [75]: S
Out[75]: {1, 2, 3, 4}

In [76]: T
Out[76]: {1, 2, 3}

In [77]:
