# collections

**インポート**
```py
import collections
```

`namedtuple` - タプルのサブクラスで、フィールドに名前を付けることができます
```py
Human = collections.namedtuple("Human", ["name", "age"])
human1 = Human(name="Bob", age=30)
human2 = Human(name="Ann", age=19)
```

`deque` - 両端に対する要素の追加、削除が高速なデータ構造です。
```py
dq = collections.deque()
dq.append(10)           # 要素を末尾に追加
dq.appendleft(5)        # 要素を先頭に追加
dq.insert(2, 20)        # インデックスを指定して要素を追加
x = dq.pop()            # 要素の末尾を取り出す
y = dq.popleft()        # 要素の先頭を取り出す
```

`Counter` - 辞書型のサブクラスで、要素の出現回数を数えられます。
```py
c = collections.Counter("Hello")
print(c)    # Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
```

`defaultdict` - 辞書型のサブクラスで、存在しないキーにアクセスしてもエラーにならずデフォルト値(0)を返し、リストに初期値を追加します。
```py
dd = collections.defaultdict(int)
dd["a"] = "one"
print(dd["a"])  # one
print(dd["b"])  # 0
print(dd)       # defaultdict(<class 'int'>, {'a': 'one', 'b': 0})
```

`OrderedDict` - 辞書型のサブクラスで、要素を追加した順序を保持します。
```py
odd = collections.OrderedDict()
odd["one"] = 1
odd["two"] = 2
odd["three"] = 3
print(odd)  # OrderedDict({'one': 1, 'two': 2, 'three': 3})
```
