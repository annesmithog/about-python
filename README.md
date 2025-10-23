# about-python

## 目次

- [前提](#前提)
- [変数](#変数)
- [定数](#定数)
- [制御構造](#制御構造)
- [型](#型)
- [式](#式)
- [キャスト](#キャスト)
- [コンテナ](#コンテナ)
- [列挙型](#列挙型)
- [関数](#関数)
- [オブジェクト指向](#オブジェクト指向)
- [例外](#例外)
- [Extra](#extra)
- [データ構造](#データ構造)
- [アルゴリズム](#アルゴリズム)

[⬆︎目次トップに戻る](#目次)

## 前提

**環境** - Python3.13で実行しています。

**出力** - このリポジトリでは、説明のために出力を多く使用します。
```py
print("Hello")
```

**コメントアウト** - 以下の方法でコメントアウトできます。
```py
# Comment 1

"""
Comment 2
"""
```

[⬆︎目次に戻る](#目次)

## 変数

一般的な変数です。

```py
name = "Anne"
age = 21
```

[⬆︎目次に戻る](#目次)

## 定数

Pythonでは、**定数は言語仕様として存在しません**！！しかし、慣例として大文字とアンダースコアで表現します。

```py
PI = 3.14
```

[⬆︎目次に戻る](#目次)

## 制御構造

`if`, `elif`, `else` - 条件分岐
```py
num = 0

if num == 0:
    print("A")
elif num > 0:
    print("B")
else:
    print("C")
```

`while` - 繰り返し
```py
i = 0

while (i < 5):
    print(i)
    i += 1
else:
    print("END OF CODE")
```

`for` - ループ処理
```py
nums = [10, 20, 30]

# 配列を出力 (他のコンテナも同様に出力可能)
for num in nums:
    print(num)  # 10, 20, 30

# 範囲を出力
for i in range(4):
    print(i)    # 0, 1, 2, 3

# 範囲を出力 (指定値からスタート)
for i in range(1, 5):
    print(i)    # 1, 2, 3, 4

# 範囲を出力 (間隔を使用)
for i in range(1, 5, 2):
    print(i)    # 1, 3

# 文字列を１文字ずつ出力
for c in "CHAR":
    print(c)    # C, H, A, R

# インデックス＋配列を出力
for index, num in enumerate(nums):
    print(f"{index}=>{num}")   # 0=>10, 1=>20, 2=>30

# ファイルを一行ずつ出力
for line in open("sample.txt"):
    print(line, end="")

# ループの最後にelseを実行
for i in range(3):
    print(i)
else:
    print("END OF FOR") # 0, 1, 2, END OF FOR

# 代入しない場合`_`を使用
for _ in range(3):  # `_`自体は普通に使える...
    print("Hello")
```

`match` - 条件分岐
```py
score = 5

match score:
    case 1 | 2:
        print("Low")
    case 3:
        print("Mid")
    case 4 | 5:
        print("High")
    case _:
        print("Dunno")
```

`del` - オブジェクトを削除します。
```py
s = "Hello"
del s
```

`exec` - 文字列をスクリプトとして実行します。
```py
s = "print('This is exec.')"
exec(s)
```

`break` - 繰り返し処理を強制終了します。

`continue` - 繰り返し処理をスキップします。

[⬆︎目次に戻る](#目次)

## 型

`type(x)` - xの型を返す
```py
x = 10
print(type(x))  # <class 'int'>
```

**標準データ型**
```py
print(type(1))              # <class 'int'>
print(type(1.1))            # <class 'float'>
print(type("aa"))           # <class 'str'>
print(type(True))           # <class 'bool'>
print(type([10, 20, 30]))   # <class 'list'>
print(type((10, 20)))       # <class 'tuple'>
print(type({"A":1, "B":2})) # <class 'dict'>
print(type({"aa", "bb"}))   # <class 'set'>
```

[⬆︎目次に戻る](#目次)

## 式

**条件式** - `A if B else C`, BであればA、そうでなければCを返します。
```py
country = "ja"
print("Konichiwa" if country == "en" else "Hello")
```

**代入式** - 代入の結果を式として評価します。
```py
s = "ABCDEF"

if (x := len(s)) > 5:
    print("Wow!")       # Wow!
print(x)                # 6
```

**算術演算**
```py
a = 5
b = 2
print(a % b)    # a/bの余り: 1
print(a ** b)   # aのb乗: 25
print(a // b)   # 切り捨て除算: 2
```

**集合演算**
```py
x = {1, 2, 3}
y = {3, 4, 5}
print(x | y)            # 和集合: {1, 2, 3, 4, 5}
print(x & y)            # 積集合: {3}
print(x ^ y)            # 対称差: {1, 2, 4, 5}
print({1, 2, 3} <= x)   # {1, 2, 3}がxの部分集合か: True
print({1, 2, 4} <= x)   # {1, 2, 4}がxの部分集合か: False
```

**内包表記**
```py
even_nums = [v for v in range(10) if v % 2 == 0]
print(even_nums)    # [0, 2, 4, 6, 8]
```

**ビット操作**
```py
x = 3                   # 0b11
y = 6                   # 0b110
print(bin(x<<1))        # 左シフト: 0b110
print(bin(x>>1))        # 右シフト: 0b1
print(bin(x & y))       # AND:     0b10
print(bin(x | y))       # OR:      0b111
print(bin(x ^ y))       # XOR:     0b101
print(bin(~x))          # NOT:    -0b100
```

[⬆︎目次に戻る](#目次)

## キャスト

```py
x = str(5)      # int to str
x = float(5)    # int to float
x = int('7')    # str to int
```

[⬆︎目次に戻る](#目次)

## コンテナ

データ構造については[データ構造](#データ構造)の一覧を参照してください。

**イテレータを使う**
```py
tpl = ("one", "two", "three")
tpl_iter = iter(tpl)
print(next(tpl_iter))   # one
print(next(tpl_iter))   # two
print(next(tpl_iter))   # three
```

[⬆︎目次に戻る](#目次)

## 列挙型

血液型やトランプの記号などの「どの値を使うか」が決まっているものを表現する時に有用です。

**Enum**
```py
from enum import Enum

class Suit(Enum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4

print(Suit.CLUBS.name)  # CLUBS
print(Suit.CLUBS.value) # 3
```

**IntEnum** - Enumクラスとintのサブクラスです。intと比較できます。
```py
from enum import IntEnum

class Outfielder(IntEnum):
    LEFT = 7
    CENTER = 8
    RIGHT = 9

ramirez = Outfielder.LEFT.value

if Outfielder.LEFT.value == 7:
    print("レフト")
```

**Flag** - Enumクラスの機能とビット演算子が使用可能です。
```py
from enum import Flag, auto

class Color(Flag):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    PURPLE = RED | BLUE
    WHITE = RED | GREEN | BLUE

def get_color(color: Color):
    match(color):
        case Color.PURPLE:
            return "purple"

x = Color.RED | Color.BLUE
print(get_color(x)) # purple
```

**IntFlag** - Flagクラスのint版で、intと比較可能です。
```py
from enum import IntFlag, auto

class Color(IntFlag):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    PURPLE = RED | BLUE

print(int(Color.PURPLE))    # 5
```

`unique` - 同じ値の定義を禁止
```py
from enum import Enum, unique

@unique
class Test(Enum):
    A = 1
    B = 2
    C = 2   # <- エラー
```

**血液型**: (サンプルコード)
```py
from enum import Enum

class BloodType(Enum):
    A = "A型"
    B = "B型"
    O = "O型"
    AB = "AB型"

    def __str__(self):
        return self.name

    @classmethod
    def show_all(cls) -> list[str]:
        return list(map(lambda color: color.value, cls))

print(BloodType.show_all())     # ['A型', 'B型', 'O型', 'AB型']
```

[⬆︎目次に戻る](#目次)

## 関数

**関数**
```py
def sum(a: int, b: int) -> int:
    return a + b

print(sum(10, 20))  # 30
```

`*args` - 可変長引数です。
```py
def output(*args: str) -> None:
    for arg in args:
        print(arg)

output("Hi", "Im", "Anne")   # Hi\n Im\n Anne\n
```

`**kwargs` - 可変長のキーワード引数です。
```py
def output(**kwargs: str|int) -> None:
    for key, value in kwargs.items():
        print(f"{key}=>{value}")

output(name="Anne", age=21) # name=>Anne, age=>21
```

**キーワードのみ引数** - `*`の後ろに定義した引数にキーワード指定を強制します。
```py
def hello(name: str, *, has_exclamation: bool) -> None:
    exclamation = ""
    if has_exclamation:
        exclamation = "!!!"
    print(f"Hello, {name}{exclamation}")

hello("Anne", has_exclamation=True)     # Hello, Anne!!!
hello("Anne", has_exclamation=False)    # Hello, Anne
hello("Anne", True)                     # エラー
```

**デコレータ** - オブジェクト構造を変更せずに既存のオブジェクトに新しい機能を追加できます。
```py
def hiding(f):
    def wrapper(txt: str) -> str:
        bad_words = ["fuck", "bitch", "ass", "shit"]
        for bad_word in bad_words:
            txt = txt.replace(bad_word, "*" * len(bad_word))
        v = f(txt)
        return v
    return wrapper

@hiding
def chant(quote: str) -> None:
    print(quote)

chant("Ayo fuck you bitch ass bro") # Ayo **** you ***** *** bro
```

**lambda**
```py
def output(characters, f):
    for character in characters:
        print(f(character))

characters = ["Goku", "Naruto", "Denji"]
output(characters, lambda c: c.upper())     # GOKU, NARUTO, DENJI
```

[⬆︎目次に戻る](#目次)

## オブジェクト指向

**クラス**
```py
class Human:
    def __init__(self, name) -> None:
        self.name = name

    def output(self) -> None:
        print(f"Name: {self.name}")
```

**インスタンス**
```py
gob = Human("ゴブリン")
gob.output()    # Name: ゴブリン
```

**プロパティ・セッター** - クラスの値を外から簡単に変えられなくさせ、取り出しは行えるようにします。
```py
class Human:
    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value != "":
            self._name = value

tanaka = Human("田中")
print(tanaka.name)      # 田中
tanaka.name = ""
print(tanaka.name)      # 田中
tanaka.name = "田中Jr"
print(tanaka.name)      # 田中Jr
```

**クラスメソッド** - クラスから直接使用できるメソッドです。継承クラスで動作が変わる場合などに用いられます。
```py
class Human:
    greet = "HELLO"

    @classmethod
    def greeting(cls) -> None:
        print(cls.greet)

Human.greeting()        # HELLO
Human.greet = "こんにちは"
Human.greeting()        # こんにちは
print(Human.greet)      # こんにちは
```

**静的メソッド** - インスタンスやクラスに依存しません。継承クラスでも同じ動作を期待する場合に用いられます。
```py
class Date:
    def __init__(self, date: str) -> None:
        self.date = date

    def get_date(self):
        return self.date

    @staticmethod
    def to_slash_date(d: str) -> str:
        return d.replace("-", "/")

d1 = Date("2025-12-31")
print(d1.date)                      # 2025-12-31
d2 = Date.to_slash_date("2025-12-31")
print(d2)                           # 2025/12/31
```

**継承** - クラスを継承できます。以下の例にはオーバーライドが含まれます。
```py
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name
    def speak(self):
        print(f"私の名前は{self.name}です。")

class Dog(Animal):
    def __init__(self, name: str, type: str):
        super().__init__(name)
        self.type = type
    def speak(self):
        super().speak()
        print(f"犬です。{self.type}です。")

dog = Dog("Doggo", "Shiba")
dog.speak()
```

- `__init__(self)` - インスタンス生成時に実行されます。
- `__del__(self)` - 破棄したタイミングに実行されます。破棄はGC依存です。
- `__new__(cls)` - インスタンスを作る前に実行されます。
- `__repr__(self)` - オブジェクトを表す公式の文字列を計算して返します。基本はデバッグに使用します。
```py
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name
    def __repr__(self):
        return f"Animal(Name: {self.name})"

animal = Animal("Dick")
print(animal)           # Animal(Name: Dick)
```
- `__str__(self)` - `__repr__`みたいなものです。
- `__sizeof__(self)` - オブジェクトのサイズを返します。

**インターフェース**
```py
from abc import ABCMeta, abstractmethod
import math

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self) -> float:
        raise NotImplementedError()

class Rectangle(Shape):
    width: float
    height: float
    def area(self):
        return self.width * self.height

class Circle(Shape):
    radius: float
    def area(self):
        return self.radius * self.radius * math.pi
```

[⬆︎目次に戻る](#目次)

## 例外

`try`・`except`・`finally`
```py
try:
    ans = 1 / 0
except Exception as e:
    print(e)        # division by zero
finally:
    print("END.")
```

**例外スロー**
```py
try:
    if 1 == 1:
        raise
except Exception as e:
    print(e)
```

[⬆︎目次に戻る](#目次)

## Extra

主要ライブラリ
- [関数(組み込み)](/lib/functions/builtin/README.md)
- [関数(コンテナ)](/lib/functions/container/README.md)
- [関数(ファイル操作)](/lib/functions/file/README.md)
- [re](/lib/re/README.md) - 正規表現
- [os](/lib/os/README.md) - ファイル操作などのOSタスク
- [random](/lib/random/README.md) - 乱数
- [math](/lib/math/README.md) - 数学関連
- [time](/lib/time/README.md) - 時間関連
- [sys](/lib/sys/README.md) - 操作関連
- [collections](/lib/collections/README.md) - コンテナに代わるデータ構造
- [statistics](/lib/statistics/README.md) - 統計関連
------------------------------------------------------------------------------
応用
- [パッケージ](/advanced/pkg/README.md)
- [仮想環境](/advanced/venv/README.md)
- [高速化](/advanced/speedup/README.md)
- [入力](/advanced/input/README.md)
------------------------------------------------------------------------------
<!--
フレームワーク
- Pyramid
- FastAPI
- Django
- Flask
- Tornado
- Synchronous
- Asynchronous
- gevent
- AIOHTTP
- Sanic
------------------------------------------------------------------------------
機械学習
- sklean
- PyTorch
- TensorFlow
------------------------------------------------------------------------------
データ分析
- NumPy (数値計算)
- matplotlib
- seaborn
------------------------------------------------------------------------------
業務効率化
- OpenPyXL (Excel操作)
- pandas (データ分析)
- selenium (Webブラウザ操作)
- win32com (WindowsのExcel操作)
- PyAutoGUI (GUI自動化)
- BeautifulSoup (HTML, XMLのデータ抽出)
- Tesseract (OCR)
- camelot (PDFデータ抽出)
- pypdf (PDF操作)
------------------------------------------------------------------------------
デスクトップアプリ
- Tkinter
- PySimpleGUI
- Kivy
------------------------------------------------------------------------------
その他
- OpenCSV
- Pillow
- pygame
------------------------------------------------------------------------------
-->

[⬆︎目次に戻る](#目次)

## データ構造

- [list](/datastructure/list/README.md) - 要素の変更が可能
- [tuple](/datastructure/tuple/README.md) - 要素や要素数の変更が不可能
- [dict](/datastructure/dict/README.md) - データを構造化
- [set](/datastructure/set/README.md) - インデックス参照不可能、値重複なし、高速
- [frozenset](/datastructure/frozenset/README.md) - 不変のset
- [array](/datastructure/array/README.md) - 効率的な数値配列が表現できる

[⬆︎目次に戻る](#目次)

## アルゴリズム

探索
- [線形探索](/src/algorithms/search/linear_search.py) - 配列を先頭から順番に調べ、目的の要素の位置を探します。
- [二分探索](/src/algorithms/search/binary_search.py) - ソート済みの配列を二分しながら効率的に要素を探し、目的の要素の位置を返します。
- [指数探索](/src/algorithms/search/exponential_search.py) - ソート済みの配列で範囲を指数的に広げながら二分探索し、目的の要素の位置を返します。
- [貪欲法 (例: コイン問題)](/src/algorithms/search/greedy_coin_change.py) - その場で最適な選択を繰り返し、解を求めます。コイン問題では、用意されたコインの種類と求める合計をもとに必要なコインの種類を返します。
--------------------------------------------------------------------------------------------------
ツリー
- [幅優先探索 (BFS)](/src/algorithms/tree/bfs.py) - キューを使用して与えられたノードから近いノードを順に探索し、最短経路を返します。
- [深さ優先探索 (DFS)](/src/algorithms/tree/dfs.py) - スタックや再帰を使用してできる限り深く探索し、到達可能な経路を返します。
--------------------------------------------------------------------------------------------------
グラフアルゴリズム
- [BFSを使用した迷路探索](/src/algorithms/graph/bfs_maze.py) - BFSを使用して最短経路を見つけ、最短距離を返します。
- [DFSを使用した迷路探索](/src/algorithms/graph/dfs_maze.py) - DFSを使用して到達可能な経路を見つけ、その距離を返します。
- [ダイクストラ法](/src/algorithms/graph/dijkstra.py) - 負の辺がない場合のみ、単一の始点から各頂点への最短経路を求めて、各地点への最短距離を返します。
- [ベルマンフォード法](/src/algorithms/graph/bellman_ford.py) - 負の辺があっても問題ないが負閉路の場合以外に限り、単一の始点から各頂点への最短経路を求めて、各地点への最短距離を返します。
- [ワーシャル–フロイド法](/src/algorithms/graph/floyd_warshall.py) - 全ての頂点間の最短経路を求めて返します。
- [プリム法](/src/algorithms/graph/prim.py) - 貪欲法で最小全域木を求めて返します。
- [クラスカル法](/src/algorithms/graph/kruskal.py) - 辺が小さい順に選び、最小全域木を求めて返します。
- [トポロジカルソート](/src/algorithms/graph/topological_sort.py) - 有向非巡回グラフのノードを依存関係に従って並べて返します。
--------------------------------------------------------------------------------------------------
ソート
- [バブルソート](/src/algorithms/sorting/bubble_sort.py) - 隣り合う要素を比較しながら必要に応じて入れ替えを繰り返すソートです。
- [選択ソート](/src/algorithms/sorting/selection_sort.py) - 未ソート部分から最小または最大の要素を選び先頭と交換するソートです。
- [挿入ソート](/src/algorithms/sorting/insertion_sort.py) - 適切な位置を見つけて要素を挿入し、部分的に整列させるソートです。
- [ヒープソート](/src/algorithms/sorting/heap_sort.py) - ヒープ構造を利用する効率的なソートです。
- [マージソート](/src/algorithms/sorting/merge_sort.py) - 分割統治法を利用した安定したソートです。
- [クイックソート](/src/algorithms/sorting/quick_sort.py) - 分割統治法を利用した不安定で高速なソートです。
- [シェルソート](/src/algorithms/sorting/shell_sort.py) - 挿入ソートを改良し、間隔を縮めながら整列させるソートです。
- [カウントソート](/src/algorithms/sorting/counting_sort.py) - 値の範囲が限られている場合に有効な非比較ソートです。
- [基数ソート](/src/algorithms/sorting/radix_sort.py) - 整数の各桁ごとに処理する安定したソートです。
--------------------------------------------------------------------------------------------------

[⬆︎目次に戻る](#目次)
