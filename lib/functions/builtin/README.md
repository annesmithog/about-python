# 組み込み関数

## 目次

- [文字列](#文字列)
- [数値](#数値)
- [組み込み](#組み込み)
- [attr](#attr)

[⬆︎目次トップに戻る](#目次)

## 文字列

- `s.capitalize()` - 最初を大文字、その他を小文字にして返す
- `s.lower()` - 全て小文字にして返す
- `s.upper()` - 全て大文字にして返す
- `s.title()` - タイトルケースにして返す
- `s.swapcase()` - 大文字を小文字、小文字を大文字にして返す
- `ljust`, `center`, `rjust` - 指定桁に対して左|中央|右揃えにして、指定文字で残りを埋める
```py
s = "Hello"
print(s.ljust(10))      # "Hello     "
print(s.center(10))     # "  Hello   "
print(s.rjust(10, "*")) # "*****Hello"
```
- `s.isalnum()` - 英数字の場合Trueを返す
- `s.isalpha()` - 英字の場合Trueを返す
- `s.isdecimal()` - 10進数の場合Trueを返す
- `s.islower()` - 全て小文字の場合Trueを返す
- `s.isupper()` - 全て大文字の場合Trueを返す
- `s.istitle()` - タイトルケースの場合Trueを返す
- `s.isspace()` - 全てスペースの場合Trueを返す
- `s.count(sub[, start, end])` - start~end間のsubの出現回数
```py
s = "*****"
print(s.count("*"))         # 5
print(s.count("*", 2, 5))   # 3
```
- `s.find(sub[, start, end])` - start~end間のsubの出現位置
```py
s = "ABCDE"
print(s.find("C"))          # 2
print(s.find("C", 2, 5))    # 2
print(s.find("C", 3))       # -1
```
- `s.rfind(sub[, start, end])` - `find`を右から実行
- `s.index(sub[, start, end])` - エラー時にValueErrorを返す`find`
- `s.rindex(sub[, start, end])` - `index`を右から実行
- `strip`, `lstrip`, `rstrip` - 指定文字を除去したコピーを返す
```py
s = "    hello,   muhfucker  "
print(s.strip())                # "hello,   muhfucker"
print(s.lstrip())               # "hello,   muhfucker  "
print(s.rstrip())               # "    hello,   muhfucker"
print(s.rstrip("muhfucker "))   # "    hello,"
```
- `s.replace(old, new[, count])` - oldをnewに置換する (count回)
- `s.split(sep, maxsplit)` - sepで区切った単語のリストを返す (maxsplit回分割)
```py
s = "90|60|80"
lst = s.split("|")
print(lst)  # ['90', '60', '80']
```
- `s.partition(sep)` - 文字列をsepの最初の出現位置で区切り、３要素のタプルを返す
```py
s = "HELLO WORLD"
x = s.partition(" ")
print(x)    # ('HELLO', ' ', 'WORLD')
```
- `s.rpartition(sep)` - `partition`を右から実行
- `s.splitlines([keepends])` - 改行部分で分解し、各行からなるリストを返す
- `s.join(iterable)` - 指定されたiterableを結合
```py
x = ["AB", "CD", "EF"]
print("".join(x))   # ABCDEF
print(".".join(x))  # AB.CD.EF
```
- `s.startswith(prefix[, start, end])` - start~end間で指定されたprefixで始まる場合Trueを返す
- `s.endswith(suffix[, start, end])` - start~end間で指定されたsuffixで始まる場合Trueを返す
- `s.removeprefix(prefix)` - 文字列がprefixで始まる場合、該当部分を削除
- `s.encode([encoding="utf-8", errors=strict])` - 文字列をbytesにエンコード
- `s.expandtabs(tabsize=8)` - 文字列の全てのタブ文字が１つ以上のスペースに置換されたコピーを返す
- `s.translate(table)` - 文字列のマッピング
- `s.format(*args, **kwargs)` - 文字列整形
- `s.format()` - 左詰め、中央詰め、右詰め、n進数等

## 数値

- `i.bit_length()` - 2進数で表すために必要なビット数
- `i.bit_count()` - 2進数表現における1の数

## 組み込み

- `abs(x)` - xの絶対値を返す
- `all(iterable)` - iterableの全要素がTrueであればTrueを返す
- `any(iterable)` - iterableのいずれかがTrueであればTrueを返す
- `bin(x)` - xを2進文字列にして返す
- `hex(x)` - xを16進文字列にして返す
- `oct(x)` - xを8進文字列にして返す
- `divmod(a, b)` - a, bの商と余りをタプルで返す
- `eval(expression[, ...])` - 文字列expressionを式として実行
- `exec(object)` - objectをコードオブジェクトとして実行
- `format(value, format_spec)` - 文字列整形
- `isinstance(obj, cls)` - objがclsの型またはサブクラスの場合Trueを返す
- `issubclass(obj, cls)` - objがclsのサブクラスである場合Trueを返す
- `len(s)` - sの長さ
- `map(f, iterable, *iterables)` - fをiterableの全要素に適用した結果を返す
- `max(...)` - 要素の最大値
- `min(...)` - 要素の最小値
- `sum(iterable)` - iterableの要素を左から右へ合計し、総和を返す
- `type(object)` - objectの型を返す
- `next(iterator)` - イテレータを次に進める
```py
x = iter([2, 3, 4])
print(next(x))  # 2
print(next(x))  # 3
print(next(x))  # 4
```
- `print(*objects, sep="", end="\n", file=None, flush=False)` - 出力。sep(区切り文字)、end(最後の文字)、flush(フラッシュ・即時表示)
- `round(number, ndigits=None)` - numberを小数点以下ndigits桁の精度で丸めた値を返す
```py
print(round(5.44, 1))   # 5.4
print(round(5.45, 1))   # 5.5
print(round(5.4))       # 5
print(round(5.5))       # 6
print(round(9494, 0))   # 9494
print(round(9494, -1))  # 9490
print(round(9494, -2))  # 9500
```
- `zip(*iterables, strict=False)` - *iterablesを並行に反復処理する
```py
for z in zip(["A", "B", "C"], ["a", "b", "c"]):
    print(z)
```
- `filter(function, iterable)` - iterableのうち、functionが真であるものからイテレータを構築する
```py
heights = [199, 211, 161, 204]
for tall in filter(lambda h: h > 200, heights):
    print(tall)

def is_tall(height):
    return height > 200
talls = list(filter(is_tall, heights))
for tall in talls:
    print(tall)
```

## attr

**基本**
```py
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"
    
person = Person("Anne", 30)
```

`setattr(object, name, value)`
```py
setattsetattr(person, "age", 33)
print(person)
```

`getattr(object, name)`
```py
print(getattr(person, "age"))
```

`getattr(object, name, default)` - 値が存在しない場合、defaultを返す
```py
print(getattr(person, "death", 0))
```

`delattr(object, name)` - objectのname属性を削除する
```py
print(getattr(person, "age", "DEFAULT"))    # 33
delattr(person, "age")
print(getattr(person, "age", "DEFAULT"))    # DEFAULT
```

`hasattr(object, name)` - objectのname属性が存在する場合Trueを返す
```py
print(hasattr(person, "name"))      # True
print(hasattr(person, "number"))    # False
```
