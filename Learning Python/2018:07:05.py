Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.


In [1]: S = "string"

In [2]: S.endswith("g")
Out[2]: True

In [3]: S.startswith("d")
Out[3]: False

In [4]: for x in S:
   ...:     print(x)
   ...:
s
t
r
i
n
g

In [5]: S = r"\\\"
  File "<ipython-input-5-88d267e8ff7b>", line 1
    S = r"\\\"
              ^
SyntaxError: EOL while scanning string literal


In [6]: path = r'C:\new\text.dat'

In [7]: path
Out[7]: 'C:\\new\\text.dat'

In [8]: print(path)
C:\new\text.dat

In [9]: path = r"\new\text.dat"

In [10]: path
Out[10]: '\\new\\text.dat'

In [11]: str(path)
Out[11]: '\\new\\text.dat'

In [12]: repr(path)
Out[12]: "'\\\\new\\\\text.dat'"

In [13]: len(path)
Out[13]: 13

In [14]: print("-" * 100)
----------------------------------------------------------------------------------------------------

In [15]: []
Out[15]: []

In [16]: list = [i for i in range(10)] for j in range(10)]
  File "<ipython-input-16-49dedd738e8b>", line 1
    list = [i for i in range(10)] for j in range(10)]
                                    ^
SyntaxError: invalid syntax


In [17]: list = [[i for i in range(10)] for j in range(10)]

In [18]: for row in list:
    ...:     nums = ""
    ...:     for num in row:
    ...:         nums += str(num)
    ...:     print(nums)
    ...:
0123456789
0123456789
0123456789
0123456789
0123456789
0123456789
0123456789
0123456789
0123456789
0123456789

In [19]: S = "1234567890"

In [20]: S[0:9:3]
Out[20]: '147'

In [21]: S[::2]
Out[21]: '13579'

In [22]: S[::3]
Out[22]: '1470'

In [23]: S[::-1]
Out[23]: '0987654321'

In [24]: S[]
  File "<ipython-input-24-371763e58c5d>", line 1
    S[]
      ^
SyntaxError: invalid syntax


In [25]:

In [25]:

In [25]: S.reverse()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-25-73509bd5565d> in <module>()
----> 1 S.reverse()

AttributeError: 'str' object has no attribute 'reverse'

In [26]: S.sort(reverse=True)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-26-4e6bf98beb03> in <module>()
----> 1 S.sort(reverse=True)

AttributeError: 'str' object has no attribute 'sort'

In [27]: S.sorted(reverse = True)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-27-931a3fb05429> in <module>()
----> 1 S.sorted(reverse = True)

AttributeError: 'str' object has no attribute 'sorted'

In [28]: S[::-1]
Out[28]: '0987654321'

In [29]: list1 = [1, 2, 3, 4, 5]

In [30]: list1[::-1]
Out[30]: [5, 4, 3, 2, 1]

In [31]: list1[::-2]
Out[31]: [5, 3, 1]

In [32]: S[-1:-10:2]
Out[32]: ''

In [33]: S[-1:-5:2]
Out[33]: ''

In [34]: S[-5:-1:2]
Out[34]: '68'

In [35]: S[-1:-10:-2]
Out[35]: '08642'

In [36]: import sys

In [37]: print(sys.argv)
['/Library/Frameworks/Python.framework/Versions/3.6/bin/ipython']

In [38]: S = str()

In [39]: dir(S)
Out[39]:
['__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getnewargs__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rmod__',
 '__rmul__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'capitalize',
 'casefold',
 'center',
 'count',
 'encode',
 'endswith',
 'expandtabs',
 'find',
 'format',
 'format_map',
 'index',
 'isalnum',
 'isalpha',
 'isdecimal',
 'isdigit',
 'isidentifier',
 'islower',
 'isnumeric',
 'isprintable',
 'isspace',
 'istitle',
 'isupper',
 'join',
 'ljust',
 'lower',
 'lstrip',
 'maketrans',
 'partition',
 'replace',
 'rfind',
 'rindex',
 'rjust',
 'rpartition',
 'rsplit',
 'rstrip',
 'split',
 'splitlines',
 'startswith',
 'strip',
 'swapcase',
 'title',
 'translate',
 'upper',
 'zfill']

In [40]: S.capitalize()
Out[40]: ''

In [41]: S = "some string"

In [42]: S.capitalize()
Out[42]: 'Some string'

In [43]: S.isdigit()
Out[43]: False

In [44]: T = "100100100"

In [45]: T.isdigit()
Out[45]: True

In [46]: U = "10080"

In [47]: U.isdigit()
Out[47]: True

In [48]: U.rindex(8)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-48-e5c441e664c3> in <module>()
----> 1 U.rindex(8)

TypeError: must be str, not int

In [49]: U.rindex("8")
Out[49]: 3

In [50]: S.uppercase()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-50-a0744e434661> in <module>()
----> 1 S.uppercase()

AttributeError: 'str' object has no attribute 'uppercase'

In [51]: S
Out[51]: 'some string'

In [52]: S.upper()
Out[52]: 'SOME STRING'

In [53]: S.lower()
Out[53]: 'some string'

In [54]: S.islower()
Out[54]: True

In [55]: helo(S.title())
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-55-a35ec853e2e7> in <module>()
----> 1 helo(S.title())

NameError: name 'helo' is not defined

In [56]: help(S.title())
No Python documentation found for 'Some String'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.


In [57]: help(title())
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-57-f4ea42ffd611> in <module>()
----> 1 help(title())

NameError: name 'title' is not defined

In [58]: help(title)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-58-310df90c236b> in <module>()
----> 1 help(title)

NameError: name 'title' is not defined

In [59]: help(str.title)


In [60]: S.title()
Out[60]: 'Some String'

In [61]: S = "bringing back yourself is signifiicance of something"

In [62]: S.title()
Out[62]: 'Bringing Back Yourself Is Signifiicance Of Something'

In [63]: T = "23487"

In [64]: T.zfill(10)
Out[64]: '0000023487'

In [65]: T.replace("23", "55")
Out[65]: '55487'

In [66]: T
Out[66]: '23487'

In [67]: U = "0000000001100000000"

In [68]: U.replace("0", "#") # change all "0"s
Out[68]: '#########11########'

In [69]: U = "00010010100001"

In [70]: U.replace("00", "#")
Out[70]: '#01#101##1'

In [71]: U = "00000000011100011"

In [72]: U.replace("0", "#", 5) # replace five
Out[72]: '#####000011100011'

In [73]: L = "some string"

In [74]: L = list(L)
