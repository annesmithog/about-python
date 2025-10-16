# list

## 初期化

```py
lst1: list[int] = []                                    # []
lst2: list[int] = list()                                # []
lst3: list[str] = ["one", "two"]                        # ['one', 'two']
lst4: list[int] = list(range(3))                        # [0, 1, 2]
lst5: list[str] = list("abc")                           # ['a', 'b', 'c']
lst6: list[int] = [x for x in range(0, 10, 2)]          # [0, 2, 4, 6, 8]
lst7: list[int] = [x for x in range(10) if x % 2 == 1]  # [1, 3, 5, 7, 9]
lst8: list[list[int]] = [[10, 20], [30, 40]]            # [[10, 20], [30, 40]]
```

## 出力

```py
numbers = ["one", "two", "three"]
for number in numbers:
    print(number)
```

## メソッド

- `list.append(x)` - 要素xを末尾に追加
- `list.extend(iterable)` - イテラブル要素iterableを追加しリストを拡張
- `list.insert(i, x)` - 位置iに要素xを追加
- `list.remove(x)` - 最初に見つかった要素xを削除、存在しない場合ValueError
- `list.pop([i])` - 末尾の要素を取り除く
- `list.clear()` - 全要素を削除
- `list.index(x[, start[, end]])` - 要素xの位置
- `list.count(x)` - 要素xの出現回数
- `list.sort(*, key=None, reverse=False)` - リストをソート、reverse=Trueの場合逆順ソート
- `list.copy()` - 浅いコピーを返す
- `del list[i]` - 位置iの要素を削除
- `del list` - リストそのものを削除

## 内包表記

```py
# 一般的
numbers: list[int] = []
for x in range(5):
    numbers.append(x)

# 内包表記
numbers: list[int] = [int(v) for v in range(5)]
```

## 用途

**スタックとして扱う**
```py
stack: list[int] = [10, 20, 30]
stack.append(40)    # [10, 20, 30, 40]
stack.append(50)    # [10, 20, 30, 40, 50]
stack.pop()         # [10, 20, 30, 40]
stack.pop()         # [10, 20, 30]
```
