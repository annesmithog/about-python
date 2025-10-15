# コンテナ

## 目次

- [リスト](#リスト)
- [タプル](#タプル)
- [辞書型](#辞書型)

[⬆︎目次トップに戻る](#目次)

## リスト

- `append` - 末尾に要素を追加
```py
lst = ["A", "B", "C"]
lst.append("D") # A, B, C, D
```
- `insert` - インデックスを指定して要素を挿入
```py
lst = ["A", "B", "C"]
lst.insert(1, "D")  # A, D, B, C
```
- `remove` - 指定した要素を削除
```py
lst = ["A", "B", "C"]
lst.remove("B") # A, C
```
- `pop` - 末尾の要素を抜き出す／インデックスを指定して要素を抜き出す
```py
lst = ["A", "B", "C", "D"]
lst.pop()   # A, B, C
lst = ["A", "B", "C", "D"]
lst.pop(1)  # A, C, D
```
- `index` - 指定した要素と一致する最初のインデックスを返す
```py
lst = ["A", "B", "C", "D", "C", "E"]
print(lst.index("C"))       # 2
print(lst.index("C", 3))    # 4
```
- `count` - 指定した要素の出現回数を返す
```py
lst = ["A", "A", "B", "C", "A", "A"]
print(lst.count("A"))   # 4
```
- `sort` - ソート
```py
lst = [30, 40, 10, 20, 50]
lst.sort()
print(lst)  # 10, 20, 30, 40, 50
```
- `sorted` - ソートして返す
```py
lst = [30, 40, 10, 20, 50]
lst = sorted(lst)
print(lst)  # 10, 20, 30, 40, 50
```
- `スライス` - リストをスライスする
```py
lst = [10, 20, 30, 40, 50]
lst = lst[0:3]
print(lst)  # [10, 20, 30]
```
- `要素の削除` - 指定したインデックスの要素を削除する
```py
lst = [10, 20, 30, 40, 50]
del lst[2]
print(lst)  # [10, 20, 40, 50]
```
- `clear` - 全要素を削除する
```py
lst = [10, 20, 30, 40, 50]
lst.clear()
```

[⬆︎目次に戻る](#目次)

## タプル
- アンパック
```py
tpl = (10, 20, 30)
a, b, c = tpl
print(a, b, c)
```
- アクセス
```py
tpl = (10, 20, 30)
print(tpl[0])   # 10
print(tpl[-1])  # 30
```
- スライスによるアクセス
```py
tpl = (10, 20, 30, 40, 50)
print(tpl[0:2])     # 10, 20
print(tpl[2:])      # 30, 40, 50
print(tpl[:2])      # 10, 20
print(tpl[:])       # 10, 20, 30, 40, 50
print(tpl[::2])     # 10, 30, 50
```

[⬆︎目次に戻る](#目次)

## 辞書型

```py
student = {"name": "Anne", "age": 17}

# 要素の存在チェック
if "age" in student:
    print("ageはあります")

student["height"] = 160                 # 要素の追加
height = student["height"]              # 要素の取得
gender = student.get("gender", "???")   # 要素の取得 (+ 存在しない場合用のデフォルト値)
del student["height"]                   # 要素の削除
x = student.pop("name", "Unknown")      # 要素の抜き出し (+ 存在しない場合用のデフォルト値)

info = {"country": "USA"}
student.update(info)                    # 他の辞書と結合
scopy = student.copy()                  # 浅いコピー
scopy.clear()                           # 辞書を削除し、空の辞書にする
x = student.setdefault("weight", 40)    # キーに対応する値を取得 (存在しない場合、デフォルト値を返し辞書に追加)
dct_len = len(student)                  # キーの数を返す
k, v = student.popitem()                # キーと値を抜き出す
```

[⬆︎目次に戻る](#目次)

## セット

```py
prefectures = {"Hokkaido", "Aomori", "Akita"}
prefectures.add("Iwate")            # 要素の追加
prefectures.remove("Hokkaido")      # 要素の削除
prefectures.discard("Tokyo")        # 要素の削除 (存在しない場合もエラーにならない)
```

[⬆︎目次に戻る](#目次)
