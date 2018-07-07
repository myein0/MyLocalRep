Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import sys

In [2]: "My {1[spam]} runs {0.platform}".format(sys, {"spam": "laptop"})
Out[2]: 'My laptop runs darwin'

In [3]: "My {config[spam]} runs {sys.platform}".format(sys = sys, config = {"spa
   ...: m": "laptop"})
Out[3]: 'My laptop runs darwin'

In [4]: somelist = list("spam")

In [5]: somelist
Out[5]: ['s', 'p', 'a', 'm']

In [6]: "first={0[0]}, third={0[2]}".format(somelist)
Out[6]: 'first=s, third=a'

In [7]: parts = somelist[0], somelist[-1], somelist[1:3]

In [8]: parts
Out[8]: ('s', 'm', ['p', 'a'])

In [9]: "first={0}, last={1}, middle={2}",format(*parts)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-9-568b8d345364> in <module>()
----> 1 "first={0}, last={1}, middle={2}",format(*parts)

TypeError: format() takes at most 2 arguments (3 given)

In [10]: "first={0}, last={1}, middle={2}".format(*parts)
Out[10]: "first=s, last=m, middle=['p', 'a']"

In [11]: *parts
  File "<ipython-input-11-1cd95d35c398>", line 1
    *parts
          ^
SyntaxError: can't use starred expression here


In [12]: for i in range(10):
    ...:     print("{0:5} ^ 2 = {1:5}".format(i, i ** 2))
    ...:
    0 ^ 2 =     0
    1 ^ 2 =     1
    2 ^ 2 =     4
    3 ^ 2 =     9
    4 ^ 2 =    16
    5 ^ 2 =    25
    6 ^ 2 =    36
    7 ^ 2 =    49
    8 ^ 2 =    64
    9 ^ 2 =    81

In [13]: for i in range(10):
    ...:     print("{0:5} ^ 2 = {1:<5}".format(i, i ** 2))
    ...:
    ...:
    0 ^ 2 = 0
    1 ^ 2 = 1
    2 ^ 2 = 4
    3 ^ 2 = 9
    4 ^ 2 = 16
    5 ^ 2 = 25
    6 ^ 2 = 36
    7 ^ 2 = 49
    8 ^ 2 = 64
    9 ^ 2 = 81

In [14]: ''' align
    ...: left: <
    ...: center: ^
    ...: right: >
    ...: padding after a sign character: =
    ...: '''
Out[14]: ' align\nleft: <\ncenter: ^\nright: >\npadding after a sign character: =\n'

In [15]: for i in range(10):
    ...:     print("{0:^5} ^ 2 = {1:=5}".format(i, i ** 2))
    ...:
    ...:
    ...:
  0   ^ 2 =     0
  1   ^ 2 =     1
  2   ^ 2 =     4
  3   ^ 2 =     9
  4   ^ 2 =    16
  5   ^ 2 =    25
  6   ^ 2 =    36
  7   ^ 2 =    49
  8   ^ 2 =    64
  9   ^ 2 =    81

In [16]: ""{} is nested"".format("this")
  File "<ipython-input-16-8563782c1bcf>", line 1
    ""{} is nested"".format("this")
      ^
SyntaxError: invalid syntax


In [17]: "\"{} is nested\"".format("this")
Out[17]: '"this is nested"'

In [18]: print("\"{} is nested\"".format("this"))
"this is nested"

In [19]: import math

In [20]: "{0:#10.10f}".format(math.pi)
Out[20]: '3.1415926536'

In [21]: "{0:08.10f}".format(math.pi)
Out[21]: '3.1415926536'

In [22]: "{0:020.10f}".format(math.pi)
Out[22]: '000000003.1415926536'

In [23]: "{0:#20.10f}".format(math.pi)
Out[23]: '        3.1415926536'

In [24]: data = {"platform": sys.platform, "spam": "laptop"}

In [25]: "My {spam:<8} runs {platform:>8}".format(**data)
Out[25]: 'My laptop   runs   darwin'

In [26]: "{0:,d}".format(999999999999999)
Out[26]: '999,999,999,999,999'

In [27]: S = "s,pa,m"

In [28]: S.split(",")[1]
Out[28]: 'pa'

In [29]: S[2:4]
Out[29]: 'pa'





Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: formatter = "".join(["{}" for i in range(10)])

In [2]: formatter
Out[2]: '{}{}{}{}{}{}{}{}{}{}'

In [3]: row_i = ["#", ".", "#", "#", ".", "#", "#", "#", ".", "."]

In [4]: formatter.format(*row_i)
Out[4]: '#.##.###..'

In [5]: list = [1, 2, 3, 4, 5]

In [6]: del list[2]

In [7]: list
Out[7]: [1, 2, 4, 5]

In [8]: list.remove(4)

In [9]: list
Out[9]: [1, 2, 5]

In [10]: help(list.pop)




In [12]: list = [i for i in range(10)]

In [13]: list
Out[13]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [18]: list = [] * 10

In [19]: list
Out[19]: []

In [20]: list = [0] * 10

In [21]: list
Out[21]: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

In [22]: list = [0 for i in range(10)] # same

In [23]: list
Out[23]: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


In [26]: list1 = list(map(abs, [-1, -2 , 0, 1, 2]))
