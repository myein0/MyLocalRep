
In [2]: %automagic

Automagic is OFF, % prefix IS needed for line magics.

In [3]: pwd
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-3-86938b1e80ee> in <module>()
----> 1 pwd

NameError: name 'pwd' is not defined

In [4]: %pwd
Out[4]: '/Users/yuichiyamamoto'

In [5]: %automagic

Automagic is ON, % prefix IS NOT needed for line magics.

In [6]: pwd
Out[6]: '/Users/yuichiyamamoto'

In [7]: run ipython_script_test.py

In [8]: result
Out[8]: 1.4666666666666666

In [9]: c = 8

In [10]: result
Out[10]: 1.4666666666666666

In [11]: c = 10

In [12]: result
Out[12]: 1.4666666666666666

In [13]: f(1, 4, 1000)
Out[13]: 0.005

In [14]: matplotlib
/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/matplotlib/font_manager.py:278: UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.
  'Matplotlib is building the font cache using fc-list. '





Fontconfig warning: ignoring UTF-8: not a valid region tag
Using matplotlib backend: MacOSX

In [15]:

In [15]: matplotlib online
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-15-1fa4abac7a75> in <module>()
----> 1 get_ipython().run_line_magic('matplotlib', 'online')

/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/IPython/core/interactiveshell.py in run_line_magic(self, magic_name, line, _stack_depth)
   2129                 kwargs['local_ns'] = sys._getframe(stack_depth).f_locals
   2130             with self.builtin_trap:
-> 2131                 result = fn(*args,**kwargs)
   2132             return result
   2133

<decorator-gen-107> in matplotlib(self, line)

/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/IPython/core/magic.py in <lambda>(f, *a, **k)
    185     # but it's overkill for just that one bit of state.
    186     def magic_deco(arg):
--> 187         call = lambda f, *a, **k: f(*a, **k)
    188
    189         if callable(arg):

/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/IPython/core/magics/pylab.py in matplotlib(self, line)
     97             print("Available matplotlib backends: %s" % backends_list)
     98         else:
---> 99             gui, backend = self.shell.enable_matplotlib(args.gui)
    100             self._show_matplotlib_backend(args.gui, backend)
    101

/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/IPython/core/interactiveshell.py in enable_matplotlib(self, gui)
   3037
   3038         from IPython.core import pylabtools as pt
-> 3039         gui, backend = pt.find_gui_and_backend(gui, self.pylab_gui_select)
   3040
   3041         if gui != 'inline':

/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/IPython/core/pylabtools.py in find_gui_and_backend(gui, gui_select)
    275     if gui and gui != 'auto':
    276         # select backend based on requested gui
--> 277         backend = backends[gui]
    278         if gui == 'agg':
    279             gui = None

KeyError: 'online'

In [16]: import matplotlib.pyplot as plt

In [17]: plt.plot(np.random.randn(50).cumsum())
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-17-e17605d4ab5b> in <module>()
----> 1 plt.plot(np.random.randn(50).cumsum())

NameError: name 'np' is not defined

In [18]: import numpy as np

In [19]: plt.plot(np.random.randn(50).cumsum())
Out[19]: [<matplotlib.lines.Line2D at 0x10a74f128>]

In [20]: plt.plot(np.random.randn(50).cumsum())
Out[20]: [<matplotlib.lines.Line2D at 0x10a784be0>]

In [21]: plt.plot(np.random.randn(50).cumsum())
Out[21]: [<matplotlib.lines.Line2D at 0x10a7a1400>]

In [22]: plt.plot(np.random.randn(50).cumsum())
Out[22]: [<matplotlib.lines.Line2D at 0x10a7a1da0>]

In [23]: plt.plot(np.random.randn(50).cumsum())
Out[23]: [<matplotlib.lines.Line2D at 0x10a7a94a8>]

In [24]: plt.plot(np.random.randn(50).cumsum())
Out[24]: [<matplotlib.lines.Line2D at 0x10a7a9908>]

In [25]: plt.plot(np.random.randn(50).cumsum())
Out[25]: [<matplotlib.lines.Line2D at 0x10a78d6a0>]

In [26]: plt.plot(np.random.randn(50).cumsum())
Out[26]: [<matplotlib.lines.Line2D at 0x10a7b3518>]

In [27]: plt.plot(np.random.randn(50).cumsum())
Out[27]: [<matplotlib.lines.Line2D at 0x10a7b3668>]

In [28]: plt.plot(np.random.randn(50).cumsum())
Out[28]: [<matplotlib.lines.Line2D at 0x10a7bc908>]

In [29]: plt.plot(np.random.randn(50).cumsum())
Out[29]: [<matplotlib.lines.Line2D at 0x10985dcf8>]

In [30]: plt.plot(np.random.randn(50).cumsum())
Out[30]: [<matplotlib.lines.Line2D at 0x10a7bcc18>]

In [31]: plt.plot(np.random.randn(50).cumsum())
Out[31]: [<matplotlib.lines.Line2D at 0x10b0359b0>]

In [32]: plt.plot(np.random.randn(50).cumsum())
Out[32]: [<matplotlib.lines.Line2D at 0x10b03d7b8>]

In [33]: plt.plot(np.random.randn(50).cumsum())
Out[33]: [<matplotlib.lines.Line2D at 0x10b03d438>]

In [34]: plt.plot(np.random.randn(50).cumsum())
Out[34]: [<matplotlib.lines.Line2D at 0x10b03d4e0>]

In [35]: plt.plot(np.random.randn(50).cumsum())
Out[35]: [<matplotlib.lines.Line2D at 0x10b04de10>]

In [36]: plt.plot(np.random.randn(50).cumsum())
Out[36]: [<matplotlib.lines.Line2D at 0x10b04d6d8>]

In [37]: plt.plot(np.random.randn(50).cumsum())
Out[37]: [<matplotlib.lines.Line2D at 0x10b0507f0>]

In [38]: plt.plot(np.random.randn(50).cumsum())
Out[38]: [<matplotlib.lines.Line2D at 0x10b056748>]

In [39]: plt.plot(np.random.randn(50).cumsum())
Out[39]: [<matplotlib.lines.Line2D at 0x10b056390>]

In [40]: plt.plot(np.random.randn(50).cumsum())
Out[40]: [<matplotlib.lines.Line2D at 0x10b056588>]

In [41]: plt.plot(np.random.randn(50).cumsum())
Out[41]: [<matplotlib.lines.Line2D at 0x10b05eeb8>]

In [42]: plt.plot(np.random.randn(50).cumsum())
Out[42]: [<matplotlib.lines.Line2D at 0x10b05e860>]

In [43]: plt.plot(np.random.randn(50).cumsum())
Out[43]: [<matplotlib.lines.Line2D at 0x10be84828>]

In [44]: plt.plot(np.random.randn(50).cumsum())
Out[44]: [<matplotlib.lines.Line2D at 0x10be8e828>]

In [45]: plt.plot(np.random.randn(50).cumsum())
Out[45]: [<matplotlib.lines.Line2D at 0x10be8e6a0>]

In [46]: plt.plot(np.random.randn(50).cumsum())
Out[46]: [<matplotlib.lines.Line2D at 0x10be903c8>]

In [47]: plt.plot(np.random.randn(50).cumsum())
Out[47]: [<matplotlib.lines.Line2D at 0x10be90f28>]

In [48]: plt.plot(np.random.randn(50).cumsum())
Out[48]: [<matplotlib.lines.Line2D at 0x10be90978>]

In [49]: plt.plot(np.random.randn(50).cumsum())
Out[49]: [<matplotlib.lines.Line2D at 0x10a7b3630>]

In [50]: plt.plot(np.random.randn(50).cumsum())
Out[50]: [<matplotlib.lines.Line2D at 0x10be9d400>]

In [51]: plt.plot(np.random.randn(50).cumsum())
Out[51]: [<matplotlib.lines.Line2D at 0x10be9d358>]

In [52]: plt.plot(np.random.randn(50).cumsum())
Out[52]: [<matplotlib.lines.Line2D at 0x10bea7ba8>]

In [53]: plt.plot(np.random.randn(50).cumsum())
Out[53]: [<matplotlib.lines.Line2D at 0x10beb1978>]

In [54]: plt.plot(np.random.randn(50).cumsum())
Out[54]: [<matplotlib.lines.Line2D at 0x10beb1198>]

In [55]: plt.plot(np.random.randn(50).cumsum())
Out[55]: [<matplotlib.lines.Line2D at 0x10beb4128>]

In [56]: plt.plot(np.random.randn(50).cumsum())
Out[56]: [<matplotlib.lines.Line2D at 0x10c246208>]

In [57]: plt.plot(np.random.randn(50).cumsum())
Out[57]: [<matplotlib.lines.Line2D at 0x10c246588>]

In [58]: plt.plot(np.random.randn(50).cumsum())
Out[58]: [<matplotlib.lines.Line2D at 0x10c2465f8>]

In [59]: plt.plot(np.random.randn(50).cumsum())
Out[59]: [<matplotlib.lines.Line2D at 0x10c24cd30>]

In [60]: plt.plot(np.random.randn(50).cumsum())
Out[60]: [<matplotlib.lines.Line2D at 0x10c24c208>]

In [61]: plt.plot(np.random.randn(50).cumsum())
Out[61]: [<matplotlib.lines.Line2D at 0x10c283f60>]

In [62]:

In [62]:

In [62]:

In [62]:

In [62]:

In [62]: plt.plot(np.random.randn(50).cumsum())
Out[62]: [<matplotlib.lines.Line2D at 0x10a36aa58>]

In [63]: exit()
mba:~ yuichiyamamoto$
  [Restored Jun 11, 2018 1:01:31]
Last login: Sun Jun 10 20:59:40 on ttys000
mba:~ yuichiyamamoto$ IPYTHON
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: a = [1, 2, 3]

In [2]: a
Out[2]: [1, 2, 3]

In [3]: b = a

In [4]: b
Out[4]: [1, 2, 3]

In [5]: a = 1

In [6]: b
Out[6]: [1, 2, 3]

In [7]: b
Out[7]: [1, 2, 3]

In [8]: a
Out[8]: 1


In [9]: a
Out[9]: 1

In [10]: a = [1, 2, 3]

In [11]: a
Out[11]: [1, 2, 3]

In [12]: b = a

In [13]: b
Out[13]: [1, 2, 3]

In [14]: a.append(4)

In [15]: b
Out[15]: [1, 2, 3, 4]

In [16]: def append_element(some_list, element):
    ...:     some_list.append(element)
    ...:

In [17]: data = [1,2,3]

In [18]: append_element(data, [4, 5, 6])

In [19]: data
Out[19]: [1, 2, 3, [4, 5, 6]]

In [20]: isinstance(data, list)
Out[20]: True

In [21]: isinstance(data, int)
Out[21]: False

In [22]: isinstance(data, (list, str))
Out[22]: True

In [23]: isinstance(data, (int, str))
Out[23]: False

In [24]: data.sort
Out[24]: <function list.sort>

In [25]: data
Out[25]: [1, 2, 3, [4, 5, 6]]

In [26]: sorted(data)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-26-33bae22008f5> in <module>()
----> 1 sorted(data)

TypeError: '<' not supported between instances of 'list' and 'int'

In [27]: data.pop(3)
Out[27]: [4, 5, 6]

In [28]: data
Out[28]: [1, 2, 3]

In [29]: data.erase()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-29-df5574c74248> in <module>()
----> 1 data.erase()

AttributeError: 'list' object has no attribute 'erase'

In [30]: data.remove(2)

In [31]: data
Out[31]: [1, 3]

In [32]: data.pop(1)
Out[32]: 3

In [33]: data
Out[33]: [1]

In [34]: data.append(4)

In [35]: for i  in range(5):
    ...:     data.append(i + 2)
    ...:

In [36]: data
Out[36]: [1, 4, 2, 3, 4, 5, 6]

In [37]: data.remove(1)

In [38]: data
Out[38]: [4, 2, 3, 4, 5, 6]

In [39]: data.remove(4)

In [40]: data
Out[40]: [2, 3, 4, 5, 6]

In [41]: data.append(4)

In [42]: data
Out[42]: [2, 3, 4, 5, 6, 4]

In [43]: data.remove(4)

In [44]: data
Out[44]: [2, 3, 5, 6, 4]

In [45]: data.remove(4)

In [46]: data
Out[46]: [2, 3, 5, 6]

In [47]: data.pop(1)
Out[47]: 3

In [48]: data
Out[48]: [2, 5, 6]

In [49]: data.insert(2, 1)

In [50]: data
Out[50]: [2, 5, 1, 6]

In [51]: while i <= 10:
    ...:     data.insert(0, i)
    ...:     i += 1
    ...:

In [52]: data
Out[52]: [10, 9, 8, 7, 6, 5, 4, 2, 5, 1, 6]

In [53]: a = 5

In [54]: a.numerator
Out[54]: 5

In [55]: a = "str"

In [56]: a
Out[56]: 'str'

In [57]: a.capitarize
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-57-ed555a6fe55a> in <module>()
----> 1 a.capitarize

AttributeError: 'str' object has no attribute 'capitarize'

In [58]: a.capitalize
Out[58]: <function str.capitalize>

In [59]: a
Out[59]: 'str'

In [60]: a
Out[60]: 'str'

In [61]: a.capitalize()
Out[61]: 'Str'

In [62]: a
Out[62]: 'str'

In [63]: a
Out[63]: 'str'

In [64]: a
Out[64]: 'str'

In [65]: a
Out[65]: 'str'

In [66]: a
Out[66]: 'str'

In [67]: a
Out[67]: 'str'

In [68]: a
Out[68]: 'str'

In [69]: a
Out[69]: 'str'

In [70]: a.swapcase()
Out[70]: 'STR'

In [71]: a
Out[71]: 'str'

In [72]: a = a.swapcase()

In [73]: a
Out[73]: 'STR'

In [74]: a = a.lower

In [75]: a
Out[75]: <function str.lower>

In [76]: a = a.lower()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-76-209700645a47> in <module>()
----> 1 a = a.lower()

AttributeError: 'builtin_function_or_method' object has no attribute 'lower'

In [77]: a
Out[77]: <function str.lower>

In [78]: a.lower()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-78-29999c50fa8b> in <module>()
----> 1 a.lower()

AttributeError: 'builtin_function_or_method' object has no attribute 'lower'

In [79]: isinstance(a, str)
Out[79]: False

In [80]: a
Out[80]: <function str.lower>

In [81]: b = "a became function!"

In [82]: b.a()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-82-bd1c50f0f5b8> in <module>()
----> 1 b.a()

AttributeError: 'str' object has no attribute 'a'

In [83]: b.a()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-83-bd1c50f0f5b8> in <module>()
----> 1 b.a()

AttributeError: 'str' object has no attribute 'a'

In [84]: b.a
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-84-98be602909d9> in <module>()
----> 1 b.a

AttributeError: 'str' object has no attribute 'a'

In [85]: getattr(b)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-85-2055cb58c78e> in <module>()
----> 1 getattr(b)

TypeError: getattr expected at least 2 arguments, got 1

In [86]: getattr(5, int)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-86-543fec8acde8> in <module>()
----> 1 getattr(5, int)

TypeError: getattr(): attribute name must be string

In [87]: a= 5

In [88]: getattr(a, int)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-88-57cb11a3e99a> in <module>()
----> 1 getattr(a, int)

TypeError: getattr(): attribute name must be string

In [89]: 10 // 2
Out[89]: 5

In [90]: 10 // 234
Out[90]: 0

In [91]: 11 // 2
Out[91]: 5

In [92]: 23 // 11
Out[92]: 2

In [93]: 23 / 11
Out[93]: 2.090909090909091

In [94]: 5 >= 3 & 2 + 1 == 3
Out[94]: True

In [95]: a = 3

In [96]: b = 5

In [97]: a^b
Out[97]: 6

In [98]: a ** b
Out[98]: 243

In [99]: c = """
    ...: this is a longer string that
    ...: spans multiple lines"""

In [100]:

In [100]: c
Out[100]: '\nthis is a longer string that\nspans multiple lines'

In [101]: a = amazing
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-101-4707a9013582> in <module>()
----> 1 a = amazing

NameError: name 'amazing' is not defined

In [102]: a = "amazing"

In [103]: a += c

In [104]: a
Out[104]: 'amazing\nthis is a longer string that\nspans multiple lines'

In [105]: s = "python"

In [106]: s
Out[106]: 'python'

In [107]: list(s)
Out[107]: ['p', 'y', 't', 'h', 'o', 'n']

In [108]: s[:4]
Out[108]: 'pyth'

In [109]: s[4:]
Out[109]: 'on'

In [110]: s[6:]
Out[110]: ''

In [111]: template = "{0:.2f} is now used for caliculate in {1:s}."

In [112]: template.format(3.1415926535, "1234")
Out[112]: '3.14 is now used for caliculate in 1234.'

In [113]: from datetime import datetime, date, time

In [114]: dt ] datetime(2011, 10 ,29, 20, 30, 21)
  File "<ipython-input-114-fbb075259c85>", line 1
    dt ] datetime(2011, 10 ,29, 20, 30, 21)
       ^
SyntaxError: invalid syntax


In [115]: dt.date
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-115-38e642a81e31> in <module>()
----> 1 dt.date

NameError: name 'dt' is not defined

In [116]: dt = datetime(2011, 10 ,29, 20, 30, 21)

In [117]: dt.date
Out[117]: <function datetime.date>

In [118]: dt.date()
Out[118]: datetime.date(2011, 10, 29)

In [119]: dy
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-119-466bf8f41b9a> in <module>()
----> 1 dy

NameError: name 'dy' is not defined

In [120]: dt
Out[120]: datetime.datetime(2011, 10, 29, 20, 30, 21)

In [121]: DT = datetime(2011, 10, 29, 20, 30, 21)

In [122]: DT
Out[122]: datetime.datetime(2011, 10, 29, 20, 30, 21)

In [123]: DT.day
Out[123]: 29

In [124]: DT.second
Out[124]: 21

In [125]: DT.year
Out[125]: 2011

In [126]: DT.month
Out[126]: 10

In [127]: DT.hour
Out[127]: 20

In [128]: DT.minute
Out[128]: 30

In [129]: DT.date()
Out[129]: datetime.date(2011, 10, 29)

In [130]: DT.time()
Out[130]: datetime.time(20, 30, 21)

In [131]: DT.strftime('%Y/%m/%d %H:%M:%S')
Out[131]: '2011/10/29 20:30:21'

In [132]:  5 > 3 > 2  > -1 > -2
Out[132]: True

In [133]: 4> 3> 2 >7 >0
Out[133]: False

In [134]: x = 12

In [135]: x & 3==0 and x * 6 == 72 and x + 12 == 24
Out[135]: True

In [136]: sequence = [1,2,0,4,6,5,2,1]

In [137]: total_unit_5 = 0

In [138]: for value in sequence:
     ...:     if value == 5:
     ...:         break
     ...:     total_unit_5 += value
     ...:

In [139]: total_unit_5
Out[139]: 13

In [140]: for i in range(4):
     ...:     for j in range(4):
     ...:         if j > i:
     ...:             break
     ...:         print((i, j))
     ...:
(0, 0)
(1, 0)
(1, 1)
(2, 0)
(2, 1)
(2, 2)
(3, 0)
(3, 1)
(3, 2)
(3, 3)

In [141]: # i はつねに0から始まる

In [142]: x = 256

In [143]: total = 0

In [144]: while x > 500:
     ...:     if total > 500:
     ...:         break
     ...:     total += x
     ...:     x = x // 2
     ...:     print(x)
     ...:

In [145]:

In [145]: while x > 0:
     ...:      ...:     if total > 500:
     ...:      ...:         break
     ...:      ...:     total += x
     ...:      ...:     x = x // 2
     ...:      ...:     print(x)
     ...:
128
64
32
16
8
4

In [146]: def f(x):
     ...:     if x < 0:
     ...:         print('negative!')
     ...:     elif x ==0:
     ...:         pass
     ...:     else:
     ...:         print('positive!')
     ...:

In [147]: f(31)
positive!

In [148]: f(-777)
negative!

In [149]: f(0)

In [150]: range(10)
Out[150]: range(0, 10)

In [151]: print(range(10))
range(0, 10)

In [152]: list(range(10))
Out[152]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [153]: x = list(range(10))

In [154]: x
Out[154]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [155]: y = list(range(0, 20, 2))

In [156]: y
Out[156]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

In [157]: x + y
Out[157]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

In [158]: x * y
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-158-e32109319f52> in <module>()
----> 1 x * y

TypeError: can't multiply sequence by non-int of type 'list'

In [159]: x - 2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-159-829c88ab0899> in <module>()
----> 1 x - 2

TypeError: unsupported operand type(s) for -: 'list' and 'int'

In [160]: x
Out[160]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [161]: sum = 0;

In [162]: for i in range(100000):
     ...:     if i % 3 == 0 or i % 5 == 0:
     ...:         sum += i
     ...:         print(sum)
     ...:





In [163]: x = 5

In [164]: "non-negative" if x >= 0 else "Negative"
Out[164]: 'non-negative'

In [165]: tup = tuple("string)
  File "<ipython-input-165-ea4e6e268aac>", line 1
    tup = tuple("string)
                        ^
SyntaxError: EOL while scanning string literal


In [166]: tup = tuple("string")
     ...:
     ...:

In [167]: tup
Out[167]: ('s', 't', 'r', 'i', 'n', 'g')

In [168]: tup(1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-168-627d61b0936a> in <module>()
----> 1 tup(1)

TypeError: 'tuple' object is not callable

In [169]: tup[0]
Out[169]: 's'

In [170]: tup.count
Out[170]: <function tuple.count>

In [171]: tup.count()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-171-fe9cf99f889d> in <module>()
----> 1 tup.count()

TypeError: count() takes exactly one argument (0 given)

In [172]: tup.count(1)
Out[172]: 0

In [173]: tup.count("s")
Out[173]: 1

In [174]: msg = list("this is amazing programming language!")

In [175]: msg
Out[175]:
['t',
 'h',
 'i',
 's',
 ' ',
 'i',
 's',
 ' ',
 'a',
 'm',
 'a',
 'z',
 'i',
 'n',
 'g',
 ' ',
 'p',
 'r',
 'o',
 'g',
 'r',
 'a',
 'm',
 'm',
 'i',
 'n',
 'g',
 ' ',
 'l',
 'a',
 'n',
 'g',
 'u',
 'a',
 'g',
 'e',
 '!']

In [176]: for i in range(len(msg)):
     ...:     print(msg[i])
     ...:
t
h
i
s

i
s

a
m
a
z
i
n
g

p
r
o
g
r
a
m
m
i
n
g

l
a
n
g
u
a
g
e
!

In [177]: for i in range(len(msg)):
     ...:     print(msg[i], end="")
     ...:
     ...:
this is amazing programming language!
In [178]: a = 4; b = 5

In [179]: a
Out[179]: 4

In [180]: b
Out[180]: 5

In [181]: a, b = b, a

In [182]: a
Out[182]: 5

In [183]: b
Out[183]: 4

In [184]: values = 1,2,3,4,5,6,7

In [185]: a,b,*_ = values

In [186]: *_
  File "<ipython-input-186-2de828294d4c>", line 1
    *_
      ^
SyntaxError: can't use starred expression here


In [187]: a
Out[187]: 1

In [188]: b
Out[188]: 2

In [189]: a_list = [2,3,7,None]

In [190]: tup = ("foo", "bar", "baz")

In [191]: b_list = list(tup)

In [192]: b_list
Out[192]: ['foo', 'bar', 'baz']

In [193]:

In [193]: b_list[1] = "peekaboo"

In [194]: b_list
Out[194]: ['foo', 'peekaboo', 'baz']

In [195]: b_list.append("dwarf)
  File "<ipython-input-195-9f54bf6ad89e>", line 1
    b_list.append("dwarf)
                         ^
SyntaxError: EOL while scanning string literal


In [196]: b_list.append("dwarf")

In [197]: b_list
Out[197]: ['foo', 'peekaboo', 'baz', 'dwarf']

In [198]: 'dwarf" in b_list
  File "<ipython-input-198-7eb0faf454a7>", line 1
    'dwarf" in b_list
                     ^
SyntaxError: EOL while scanning string literal


In [199]: "dwarf" in b_list
Out[199]: True

In [200]: x= [4, None, "foo"]

In [201]: x.extend([7, 8, (2, 3)])

In [202]: x
Out[202]: [4, None, 'foo', 7, 8, (2, 3)]

In [203]: a = [1,2,3,7, 3, 1]

In [204]: a.sort()

In [205]: a
Out[205]: [1, 1, 2, 3, 3, 7]

In [206]: sorted(a, reverse = True)
Out[206]: [7, 3, 3, 2, 1, 1]

In [207]: a
Out[207]: [1, 1, 2, 3, 3, 7]

In [208]: b = ["saw", "samml", "he", "foxes", "six"]

In [209]: b.sort(key=len)

In [210]: b
Out[210]: ['he', 'saw', 'six', 'samml', 'foxes']

In [211]: b.sort()

In [212]: b
Out[212]: ['foxes', 'he', 'samml', 'saw', 'six']

In [213]: import bisect

In [214]: c = [1,2,2,2,3,4,7]

In [215]: bisect.bisect(c, 2)
Out[215]: 4

In [216]: bisect.insort(c, 6)

In [217]: c
Out[217]: [1, 2, 2, 2, 3, 4, 6, 7]

In [218]: bisect.insort(b, "asdf")

In [219]: b
Out[219]: ['asdf', 'foxes', 'he', 'samml', 'saw', 'six']

In [220]: b.sort(key=len)

In [221]: b
Out[221]: ['he', 'saw', 'six', 'asdf', 'foxes', 'samml']

In [222]: bisect.insort(b, 5)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-222-4d8b6b468ee9> in <module>()
----> 1 bisect.insort(b, 5)

TypeError: '<' not supported between instances of 'int' and 'str'

In [223]: bisect.insort(b, "ghh")

In [224]: b
Out[224]: ['he', 'saw', 'six', 'asdf', 'foxes', 'ghh', 'samml']

In [225]: seq = [7, 2, 3, 7, 6, 6, 0, 1]

In [226]: seq[1:5]
Out[226]: [2, 3, 7, 6]

In [227]: seq[1:4]
Out[227]: [2, 3, 7]

In [228]: seq[1:3]
Out[228]: [2, 3]

In [229]: seq[1:2]
Out[229]: [2]

In [230]: seq[1:1]
Out[230]: []

In [231]: seq[3:4]
Out[231]: [7]

In [232]: seq2 = [1:6]
  File "<ipython-input-232-3c36b52cf5c5>", line 1
    seq2 = [1:6]
             ^
SyntaxError: invalid syntax


In [233]: a = seq(1:5)
  File "<ipython-input-233-073c0f074a2b>", line 1
    a = seq(1:5)
             ^
SyntaxError: invalid syntax


In [234]: a
Out[234]: [1, 1, 2, 3, 3, 7]

In [235]: seq
Out[235]: [7, 2, 3, 7, 6, 6, 0, 1]

In [236]: seq(::2)
  File "<ipython-input-236-d54bc2d9730a>", line 1
    seq(::2)
        ^
SyntaxError: invalid syntax


In [237]: seq[::2]
Out[237]: [7, 3, 6, 0]

In [238]: seq[::3]
Out[238]: [7, 7, 0]

In [239]: seq[::4]
Out[239]: [7, 6]

In [240]: mapping = {}

In [241]: some_list =['bar', 'baz', 'foo']

In [242]: for i, v in enumerate(some_list):
     ...:     mapping[v] = i
     ...:

In [243]: mapping
Out[243]: {'bar': 0, 'baz': 1, 'foo': 2}

In [244]: seq1 = ["apple", "banana", "orange"]

In [245]: seq2 = [1, 2, 3]

In [246]: zipped = zip(seq1, seq2)

In [247]: zipped
Out[247]: <zip at 0x10fc22a88>

In [248]: list(zipped)
Out[248]: [('apple', 1), ('banana', 2), ('orange', 3)]

In [249]: seq3 = [True, False]

In [250]: zipped = zip(seq1, seq2, seq3)

In [251]: list(zipped)
Out[251]: [('apple', 1, True), ('banana', 2, False)]

In [252]: zipped = zip(seq3, seq2)

In [253]: list(zipped)
Out[253]: [(True, 1), (False, 2)]

In [254]: list(range(4))
Out[254]: [0, 1, 2, 3]

In [255]: list(range(1, 100, 5))
Out[255]: [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96]

In [256]: d1 = {"dummy": "another value"}

In [257]: ret = d1.pop("dummy")

In [258]: ret
Out[258]: 'another value'

In [259]: ret
Out[259]: 'another value'

In [260]: ret
Out[260]: 'another value'

In [261]: ret
Out[261]: 'another value'

In [262]: ret
Out[262]: 'another value'

In [263]: ret
Out[263]: 'another value'

In [264]: ret
Out[264]: 'another value'

In [265]: ret
Out[265]: 'another value'

In [266]: d1
Out[266]: {}

In [267]:
