# set

## 初期化

```py
st1: set[int] = set()                   # set()
st2: set[str] = {"ONE", "TWO", "THREE"} # {'ONE', 'TWO', 'THREE'}
st3: set[int] = set([10, 20, 30])       # {10, 20, 30}
st4: set[int] = set({10, 20, 30})       # {10, 20, 30}
st5 = set("abc")                        # {'b', 'a', 'c'}
```

## 出力

```py
numbers: set[int] = set([1, 2, 3])
for number in numbers:
    print(number)
```

## メソッド

- `set.add(elem)` - 要素elemを追加
- `set.remove(value)` - 値valueを削除
- `set.update(*others)` - イテラブル要素*othersを追加
- `set.discard(elem)` - 要素elemがあれば取り除く
- `set.copy()` - 浅いコピー
- `set.clear()` - 全ての要素を削除
- `set.difference(*others)` - setに含まれる且つothersに含まれない要素を持つ集合を返す
- `set.difference_update(*others)` - othersに含まれる要素を取り除き、setを更新
- `set.intersection(*others)` - setとothersに共通する要素を持つ新しい集合を返す
- `set.intersection_update(*others)` - 元のsetとothersに共通する要素だけを残してsetを更新
- `set.symmetric_difference(other)` - setとotherのいずれか一方だけに含まれる要素を持つ新しい集合を返す
- `set.symmetric_difference_update(other)` - どちらかにのみ含まれ、共通で持たない要素のみでsetを更新
- `set.isdisjoint(other)` - otherと共通の要素を持たない場合Trueを返す
- `set.issubset(other)` - 全要素がotherに含まれるか判定
- `set.issuperset(other)` - otherの全要素が含まれるか判定

## 内包表記

```py
numbers = {v for v in range(5)}
```
