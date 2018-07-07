
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

In [267]: quit()
mba:~ yuichiyamamoto$
mba:~ yuichiyamamoto$ ipython
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: print("hello world")
hello world

In [2]: d = {"a":"some value"}

In [3]: d.update({"b": "foo", "c": "an integer"})

In [4]: d
Out[4]: {'a': 'some value', 'b': 'foo', 'c': 'an integer'}

In [5]: d.keys()
Out[5]: dict_keys(['a', 'b', 'c'])

In [6]: print(d.keys())
dict_keys(['a', 'b', 'c'])

In [7]: list1 = list(d.keys())

In [8]: list1
Out[8]: ['a', 'b', 'c']

In [9]: list2 = list(d.values())

In [10]: list2
Out[10]: ['some value', 'foo', 'an integer']

In [11]: zip(list1, list2)
Out[11]: <zip at 0x107b98d88>

In [12]: zipped = zip(list1, list2)

In [13]: zipped
Out[13]: <zip at 0x107b82b48>

In [14]: zipped = list(zip(list1, list2))

In [15]: zipped
Out[15]: [('a', 'some value'), ('b', 'foo'), ('c', 'an integer')]

In [16]: for key, value in zip(list1, list2)
  File "<ipython-input-16-ad28257299ef>", line 1
    for key, value in zip(list1, list2)
                                       ^
SyntaxError: invalid syntax


In [17]: for key, value in zip(list1, list2):
    ...:     break
    ...:
    ...:

In [18]: dict = {}

In [19]: for key, value in zip(list1, list2):
    ...:     dict[key] = value
    ...:

In [20]: dict
Out[20]: {'a': 'some value', 'b': 'foo', 'c': 'an integer'}

In [21]: words = ["apple", "bat", "bar", "atom", "book"]

In [22]: by_letter = {}

In [23]: for word in words:
    ...:     letter = word[0]
    ...:     if letter not in by_letter:
    ...:         by_letter{letter] = [word]
  File "<ipython-input-23-ebb6492b1df4>", line 4
    by_letter{letter] = [word]
             ^
SyntaxError: invalid syntax


In [24]: for word in words:
    ...:     letter = word[0]
    ...:     if letter not in by_letter:
    ...:         by_letter{letter] = [word]
  File "<ipython-input-24-ebb6492b1df4>", line 4
    by_letter{letter] = [word]
             ^
SyntaxError: invalid syntax


In [25]: for word in words:
    ...:     letter = word[0]
    ...:     if letter not in by_letter:
    ...:         by_letter[letter] = [word]
    ...:     else:
    ...:         by_letter[letter].append(word)
    ...:

In [26]: by_letter
Out[26]: {'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}

In [27]: str = "string"

In [28]: str[2]
Out[28]: 'r'

In [29]: # str[i]: 文字列のi番目を表示

In [30]: # str[i]: 文字列のi番目を指定

In [31]: by_letter = {}

In [32]: for word in words:
    ...:     letter = word[0]
    ...:     by_letter.setdefault(letter, []).append(word)
    ...:

In [33]: by_letter
Out[33]: {'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}

In [34]: for word in words:
    ...:     letter = word[0]
    ...:     by_letter.setdefault(letter, []).append(word)
    ...:     print(by_letter)
    ...:
{'a': ['apple', 'atom', 'apple'], 'b': ['bat', 'bar', 'book']}
{'a': ['apple', 'atom', 'apple'], 'b': ['bat', 'bar', 'book', 'bat']}
{'a': ['apple', 'atom', 'apple'], 'b': ['bat', 'bar', 'book', 'bat', 'bar']}
{'a': ['apple', 'atom', 'apple', 'atom'], 'b': ['bat', 'bar', 'book', 'bat', 'bar']}
{'a': ['apple', 'atom', 'apple', 'atom'], 'b': ['bat', 'bar', 'book', 'bat', 'bar', 'book']}

In [35]: by_letter = {}

In [36]: for word in words:
    ...:     letter = word[0]
    ...:     by_letter.setdefault(letter, []).append(word)
    ...:     print(by_letter)
    ...:
{'a': ['apple']}
{'a': ['apple'], 'b': ['bat']}
{'a': ['apple'], 'b': ['bat', 'bar']}
{'a': ['apple', 'atom'], 'b': ['bat', 'bar']}
{'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}

In [37]: # default value - Example

In [38]: fruits = {"apple": 100, "banana": 200, "orange": 300}

In [39]: fruit = "cherry"

In [40]: def FruitPrice():
    ...:     fruits.get(fruit, "price is unknown")
    ...:

In [41]: FruitPrice("cherry")
----------------------------------------------------------------------
TypeError                            Traceback (most recent call last)
<ipython-input-41-68479a925c25> in <module>()
----> 1 FruitPrice("cherry")

TypeError: FruitPrice() takes 0 positional arguments but 1 was given

In [42]: def FruitPrice(fruit):
    ...:     fruits.get(fruit, "price is unknown")
    ...:

In [43]: FruitPrice("cherry")

In [44]: def FruitPrice(fruit):
    ...:     print(fruits.get(fruit, "price is unknown"))
    ...:
    ...:

In [45]: FruitPrice("sherry")
price is unknown

In [46]: FruitPrice("apple")
100

In [47]: FruitPrice("banana")
200

In [48]: hash("string")
Out[48]: 6380633148619599989

In [49]: hash([1,2,3])
----------------------------------------------------------------------
TypeError                            Traceback (most recent call last)
<ipython-input-49-35e31e935e9e> in <module>()
----> 1 hash([1,2,3])

TypeError: unhashable type: 'list'

In [50]: # set

In [51]: set([2,2,2,1,3,3,])
Out[51]: {1, 2, 3}

In [52]: {2,2,2,1,3,3}
Out[52]: {1, 2, 3}

In [53]: a = set(list(range(5)))

In [54]: a
Out[54]: {0, 1, 2, 3, 4}

In [55]: a = set(list(range(1:6)))
  File "<ipython-input-55-e04adade734d>", line 1
    a = set(list(range(1:6)))
                        ^
SyntaxError: invalid syntax


In [56]: a
Out[56]: {0, 1, 2, 3, 4}

In [57]: a = set(list(range(1,6)))

In [58]: a
Out[58]: {1, 2, 3, 4, 5}

In [59]: b = set(list(range(3, 9)))

In [60]:

In [60]: b
Out[60]: {3, 4, 5, 6, 7, 8}

In [61]: a.union(b)
Out[61]: {1, 2, 3, 4, 5, 6, 7, 8}

In [62]: a | b
Out[62]: {1, 2, 3, 4, 5, 6, 7, 8}

In [63]: a.intersection(b)
Out[63]: {3, 4, 5}

In [64]: a & b
Out[64]: {3, 4, 5}

In [65]: a.issubset(b)
Out[65]: False

In [66]: b.issubset(a)
Out[66]: False

In [67]: a.issuperset(b)
Out[67]: False

In [68]: a.isdisjoint(b)
Out[68]: False

In [69]: a.diferrence(b)
----------------------------------------------------------------------
AttributeError                       Traceback (most recent call last)
<ipython-input-69-9756a3eb78b8> in <module>()
----> 1 a.diferrence(b)

AttributeError: 'set' object has no attribute 'diferrence'

In [70]: a.differrence(b)
----------------------------------------------------------------------
AttributeError                       Traceback (most recent call last)
<ipython-input-70-a00db427d097> in <module>()
----> 1 a.differrence(b)

AttributeError: 'set' object has no attribute 'differrence'

In [71]: a.difference(b)
Out[71]: {1, 2}

In [72]: a - b
Out[72]: {1, 2}

In [73]: a.symmetric_differecne(b)
----------------------------------------------------------------------
AttributeError                       Traceback (most recent call last)
<ipython-input-73-3226bef3de4a> in <module>()
----> 1 a.symmetric_differecne(b)

AttributeError: 'set' object has no attribute 'symmetric_differecne'

In [74]: a.symmetric_difference(b)
Out[74]: {1, 2, 6, 7, 8}

In [75]: a ^ b
Out[75]: {1, 2, 6, 7, 8}










































































































In [76]: quit()
mba:~ yuichiyamamoto$
























  [Restored Jun 14, 2018 11:16:25]
Last login: Mon Jun 11 01:01:31 on ttys000
Restored session: Thu Jun 14 05:48:03 JST 2018
mba:~ yuichiyamamoto$ ipython
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 120 % 100
Out[1]: 20

In [2]: 340 % 100
Out[2]: 40

In [3]: 120 %% 5
  File "<ipython-input-3-0ed961281368>", line 1
    120 %% 5
         ^
SyntaxError: invalid syntax


In [4]: 120 / 5
Out[4]: 24.0

In [5]: 120 // 50
Out[5]: 2

In [6]:
  [Restored Jun 14, 2018 19:01:58]
Last login: Thu Jun 14 18:53:30 on console
Restored session: Thu Jun 14 18:52:12 JST 2018
mba:~ yuichiyamamoto$ ¬
mba:~ yuichiyamamoto$ ¬ipython
-bash: ¬ipython: command not found
mba:~ yuichiyamamoto$ ipython
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 5 % 24
Out[1]: 5

In [2]: quit()
mba:~ yuichiyamamoto$ jupyter notebook
[I 22:18:44.603 NotebookApp] Serving notebooks from local directory: /Users/yuichiyamamoto
[I 22:18:44.603 NotebookApp] 0 active kernels
[I 22:18:44.603 NotebookApp] The Jupyter Notebook is running at:
[I 22:18:44.603 NotebookApp] http://localhost:8888/?token=7aed5a1cbafaa6c2ccc7701f12ba0f388335fb21516aca43
[I 22:18:44.603 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 22:18:44.604 NotebookApp]

    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=7aed5a1cbafaa6c2ccc7701f12ba0f388335fb21516aca43&token=7aed5a1cbafaa6c2ccc7701f12ba0f388335fb21516aca43
[I 22:18:46.031 NotebookApp] Accepting one-time-token-authenticated connection from ::1
[I 22:18:51.053 NotebookApp] Creating new notebook in
[I 22:18:52.642 NotebookApp] Kernel started: 8a388e8f-f8c5-4dd6-a16b-a352b72771f1
[I 22:18:53.632 NotebookApp] Adapting to protocol v5.1 for kernel 8a388e8f-f8c5-4dd6-a16b-a352b72771f1
[I 22:20:52.574 NotebookApp] Saving file at /Untitled5.ipynb
[I 22:22:52.559 NotebookApp] Saving file at /Untitled5.ipynb
[I 22:24:52.557 NotebookApp] Saving file at /Untitled5.ipynb
[I 22:26:52.554 NotebookApp] Saving file at /Untitled5.ipynb
[I 22:28:52.552 NotebookApp] Saving file at /Untitled5.ipynb
[I 10:34:55.464 NotebookApp] Saving file at /Untitled5.ipynb
[I 10:36:55.404 NotebookApp] Saving file at /Untitled5.ipynb
[I 10:38:55.399 NotebookApp] Saving file at /Untitled5.ipynb
[I 10:40:55.398 NotebookApp] Saving file at /Untitled5.ipynb
[I 10:42:55.396 NotebookApp] Saving file at /Untitled5.ipynb
[I 10:44:55.396 NotebookApp] Saving file at /Untitled5.ipynb
[I 10:46:55.389 NotebookApp] Saving file at /Untitled5.ipynb
[I 10:49:41.098 NotebookApp] Saving file at /Untitled5.ipynb
[I 10:49:44.114 NotebookApp] Saving file at /Untitled5.ipynb
[I 10:50:05.193 NotebookApp] Starting buffering for 8a388e8f-f8c5-4dd6-a16b-a352b72771f1:a66732cea49941ddaf8f0ce56efd2746
[W 10:50:08.271 NotebookApp] Forbidden
[W 10:50:08.272 NotebookApp] 403 GET /api/sessions?_=1528982326396 (::1) 2.14ms referer=http://localhost:8888/tree
[W 10:50:08.274 NotebookApp] Forbidden
[W 10:50:08.275 NotebookApp] 403 GET /api/terminals?_=1528982326397 (::1) 1.22ms referer=http://localhost:8888/tree

  [Restored Jun 15, 2018 10:50:57]
Last login: Thu Jun 14 22:17:13 on ttys001
Restored session: Fri Jun 15 10:50:26 JST 2018
mba:~ yuichiyamamoto$ ipython
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.




























In [1]: some_tuple = [(1,2,3), (4,5,6), (7,8,9)]

In [2]: flattened = [x for tup in some_tuples for x in tup]
----------------------------------------------------------------------
NameError                            Traceback (most recent call last)
<ipython-input-2-1ab8bfde65dc> in <module>()
----> 1 flattened = [x for tup in some_tuples for x in tup]

NameError: name 'some_tuples' is not defined

In [3]: flattened = [x for tup in some_tuple for x in tup]

In [4]: flattened
Out[4]: [1, 2, 3, 4, 5, 6, 7, 8, 9]

In [5]: some_fruits = ["apple", "banana", "orange", "cherry"]

In [6]: some_fruits = [["apple", "banana"], ["orange", "cherry"]]

In [7]: fruits = [x for block in some_fruits for fruit in block]
----------------------------------------------------------------------
NameError                            Traceback (most recent call last)
<ipython-input-7-addf314cb5ea> in <module>()
----> 1 fruits = [x for block in some_fruits for fruit in block]

<ipython-input-7-addf314cb5ea> in <listcomp>(.0)
----> 1 fruits = [x for block in some_fruits for fruit in block]

NameError: name 'x' is not defined

In [8]: fruits = [fruit for block in some_fruits for fruit in block]

In [9]: fruits
Out[9]: ['apple', 'banana', 'orange', 'cherry']

In [10]: # same

In [11]: fruits = []
    ...: for block in some_fruits:
    ...:     for fruit in block:
    ...:         fruits.append(fruit)
    ...:
    ...:

In [12]: fruits
Out[12]: ['apple', 'banana', 'orange', 'cherry']

In [13]: def my_function(x, y, z=5)
  File "<ipython-input-13-1ebcd6e2e77d>", line 1
    def my_function(x, y, z=5)
                              ^
SyntaxError: invalid syntax


In [14]: def my_function(x, y, z=5):
    ...:     return x + y + z
    ...:
    ...:

In [15]: my_function(1, 2)
Out[15]: 8

In [16]: my_function(1, 2, 6)
Out[16]: 9

In [17]: # x, y: positional argument, z: keyword argument

In [18]: # invalid

In [19]: a = None

In [20]: def bind_a_variable():
    ...:     global a
    ...:     a = []
    ...:

In [21]: bind_a_variable
Out[21]: <function __main__.bind_a_variable()>

In [22]: bind_a_variable()

In [23]: a
Out[23]: []

In [24]: # invalid

In [25]: def bind_a_variable():
    ...:     b = []
    ...:

In [26]: bind_a_variable()

In [27]: b
----------------------------------------------------------------------
NameError                            Traceback (most recent call last)
<ipython-input-27-89e6c98d9288> in <module>()
----> 1 b

NameError: name 'b' is not defined

In [28]: b = None

In [29]: def bind_b_bariable():
    ...:     b = []
    ...:

In [30]: bind_b_bariable()

In [31]: b

In [32]: b

In [33]: b

In [34]: b

In [35]: b

In [36]: b

In [37]: b

In [38]: b

In [39]:

In [39]: # b is None.

In [40]: def f():
    ...:     a = 5
    ...:     b = 6
    ...:     c = 7
    ...:     return a, b, c
    ...: f()
    ...:
    ...:
Out[40]: (5, 6, 7)

In [41]: x, y, z = f()

In [42]: x
Out[42]: 5

In [43]: y
Out[43]: 6

In [44]: z
Out[44]: 7

In [45]: s, t, u = (1,2,3)

In [46]: s
Out[46]: 1

In [47]: t
Out[47]: 2

In [48]: u
Out[48]: 3

In [49]: ruturn "aaaaaaa"
  File "<ipython-input-49-85ac0ef2bea0>", line 1
    ruturn "aaaaaaa"
                   ^
SyntaxError: invalid syntax


In [50]: return "hello"
  File "<ipython-input-50-bbaabe080c15>", line 1
    return "hello"
                  ^
SyntaxError: 'return' outside function


In [51]: outside function
  File "<ipython-input-51-59fcd44eca69>", line 1
    outside function
                   ^
SyntaxError: invalid syntax


In [52]: dict((i, i ** 2) for i in range(5))
Out[52]: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

In [53]: gen = (x ** 2 for  x in range(100))

In [54]: gen
Out[54]: <generator object <genexpr> at 0x104ac67d8>

In [55]: list(gen)
Out[55]:
[0,
 1,
 4,
 9,
 16,
 25,
 36,
 49,
 64,
 81,
 100,
 121,
 144,
 169,
 196,
 225,
 256,
 289,
 324,
 361,
 400,
 441,
 484,
 529,
 576,
 625,
 676,
 729,
 784,
 841,
 900,
 961,
 1024,
 1089,
 1156,
 1225,
 1296,
 1369,
 1444,
 1521,
 1600,
 1681,
 1764,
 1849,
 1936,
 2025,
 2116,
 2209,
 2304,
 2401,
 2500,
 2601,
 2704,
 2809,
 2916,
 3025,
 3136,
 3249,
 3364,
 3481,
 3600,
 3721,
 3844,
 3969,
 4096,
 4225,
 4356,
 4489,
 4624,
 4761,
 4900,
 5041,
 5184,
 5329,
 5476,
 5625,
 5776,
 5929,
 6084,
 6241,
 6400,
 6561,
 6724,
 6889,
 7056,
 7225,
 7396,
 7569,
 7744,
 7921,
 8100,
 8281,
 8464,
 8649,
 8836,
 9025,
 9216,
 9409,
 9604,
 9801]

In [56]:
