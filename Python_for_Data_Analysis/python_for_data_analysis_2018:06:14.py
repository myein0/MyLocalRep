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

In [76]:
