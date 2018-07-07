Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: S = "string"

In [2]: list(S)
Out[2]: ['s', 't', 'r', 'i', 'n', 'g']

In [3]: L = list(S)

In [4]: T = "".join(L)

In [5]: T
Out[5]: 'string'

In [6]: L = list(T)

In [7]: L[1:3] = ["x', "x"]
  File "<ipython-input-7-a153020fa4fc>", line 1
    L[1:3] = ["x', "x"]
                    ^
SyntaxError: invalid syntax


In [8]: L[1:3] = ["x", "x"]

In [9]: L
Out[9]: ['s', 'x', 'x', 'i', 'n', 'g']

In [10]: "".join(L)
Out[10]: 'sxxing'

In [11]: help(str.isalpha)


In [12]: "asdflkjl".isalpha()
Out[12]: True

In [13]: "adf56kjg".isalpha()
Out[13]: False

In [14]: template = "{0}, {1} and {2}"

In [15]: template.format("eggs", "spam", "ham")
Out[15]: 'eggs, spam and ham'

In [16]: template.format("one", "two", "three")
Out[16]: 'one, two and three'
