# frozenset

## 初期化

```py
fst1 = frozenset([10, 20, 30])  # frozenset({10, 20, 30})
fst2 = frozenset({10, 20, 30})  # frozenset({10, 20, 30})
fst3 = frozenset("Hello")       # frozenset({'o', 'e', 'H', 'l'})
```

## 出力

```py
numbers = frozenset([1, 2, 3])
for number in numbers:
    print(number)
```

## メソッド

- `frozenset.copy` - 浅いコピー
- `frozenset.difference(*others)` - setに含まれる且つothersに含まれない要素を持つ集合を返す
- `frozenset.intersection(*others)` - setとothersに共通する要素を持つ新しい集合を返す
- `frozenset.symmetric_difference(other)` - setとotherのいずれか一方だけに含まれる要素を持つ新しい集合を返す
- `frozenset.union(*others)` - setと全てのotherの要素からなる新しい集合を返す
- `frozenset.isdisjoint(other)` - otherと共通の要素を持たない場合Trueを返す
- `frozenset.issubset(other)` - 全要素がotherに含まれるか判定
- `frozenset.issuperset(other)` - otherの全要素が含まれるか判定

## 内包表記

```py
numbers = frozenset({int(v): v*10 for v in range(5)})
```
