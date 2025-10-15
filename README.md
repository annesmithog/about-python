# about-python

## 目次

- [前提](#前提)
- [変数](#変数)
- [制御構造](#制御構造)
- [式](#式)
- [キャスト](#キャスト)
- [コンテナ](#コンテナ)
- [列挙型](#列挙型)
- [関数](#関数)
- [オブジェクト指向](#オブジェクト指向)
- [Extra](#extra)

[⬆︎目次トップに戻る](#目次)

## 前提

**出力** - このリポジトリでは、説明のため出力を多用します。
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

**変数** - 一般的な変数です。定数は使用できません。

```py
name = "Anne"
age = 21
```

[⬆︎目次に戻る](#目次)

## 制御構造

`if`, `elif`, `else`
```py
num = 0

if num == 0:
    print("A")
elif num > 0:
    print("B")
else:
    print("C")
```

`while`
```py
i = 0

while (i < 5):
    print(i)
    i += 1
```

`for`
```py
nums = [10, 20, 30]

for num in nums:
    print(num)  # 10, 20, 30
for i in range(4):
    print(i)    # 0, 1, 2, 3
for c in "CHAR":
    print(c)    # C, H, A, R
for index, num in enumerate(nums):
    print(f"{index}=>{num}")   # 0=>10, 1=>20, 2=>30
```

`for`の結果を使用しない場合の習慣として、`_`に代入する方法があります。
```py
for _ in range(3):  # `_`自体は普通に使える...
    print("Hello")
```

`break`・`continue` - ループを抜ける時、forの開始位置に戻る時に使用します。

`match`
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
    print("Wow!")
```

**集合演算**
```py
x = {1, 2, 3}
y = {3, 4, 5}
print(x | y)            # 和集合: {1, 2, 3, 4, 5}
print(x & y)            # 積集合: {3}
print(x ^ y)            # 対象差: {1, 2, 4, 5}
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

**リスト(動的配列)** - 要素の変更が可能なコンテナです。
```py
# 初期化・宣言
lst1 = []
lst2 = list()
lst3 = ["one", "two", "three"]              # ['one', 'two', 'three']
lst4 = list(range(3))                       # [0, 1, 2]
lst5 = list("abc")                          # ['a', 'b', 'c']
lst6 = [x for x in range(0, 10, 2)]         # [0, 2, 4, 6, 8]
lst7 = [x for x in range(10) if x % 2 == 1] # [1, 3, 5, 7, 9]
lst8 = [[10, 20], [30, 40]]                 # [[10, 20], [30, 40]]

# 出力例
nums = ["one", "two", "three"]
for num in nums:
    print(num)

# 内包表記
nums = [str(v) for v in range(5)]
```

**タプル** - 要素や要素数の変更が不可能なコンテナです。タプル同士の結合は可能です。使われる場面として、アプリの設定やCSVのレコードデータ保持などが挙げられます。
```py
# 初期化・宣言
tpl1 = ()
tpl2 = tuple()
tpl3 = 10, 20, 30           # (10, 20, 30)
tpl4 = (10, 20, 30)         # (10, 20, 30)
tpl5 = ("ten", 20, 30)      # ('ten', 20, 30)

# 出力例
tpl = (10, 20, 30)
for t in tpl:
    print(t)
```

**辞書型** - データを構造化したい場合に用いるコンテナです。
```py
# 初期化・宣言
dct1 = {}
dct2 = dict()
dct3 = {"one": 1, "two": 2, "three": 3}

# 出力例
dct = {"one": 1, "two": 2, "three": 3}
for key, value in dct.items():
    print(key, value)

# 内包表記
dct = {str(v): v*10 for v in range(5)}
```

**セット** - インデックス参照不可能で値が重複しない、高速なコンテナです。
```py
# 初期化・宣言
st1 = set()
st2 = {"ONE", "TWO", "THREE"}   # {'TWO', 'ONE', 'THREE'}
st3 = set([10, 20, 30])         # {10, 20, 30}
st4 = set({10, 20, 30})         # {10, 20, 30}
st5 = set("abc")                # {'c', 'b', 'a'}

# 出力例
st = {10, 20, 30}
for x in sorted(st):
    print(x)

# 内包表記
nums = {v for v in range(5)}
```

**不変セット** - 不変のセットです。
```py
fst1 = frozenset([10, 20, 30])  # frozenset({10, 20, 30})
fst2 = frozenset({10, 20, 30})  # frozenset({10, 20, 30})
fst3 = frozenset("Hi")          # frozenset({'H', 'i'})
```

**array** - 効率的な数値配列が表現できるコンテナです。`b`: int, `d`: double, `f`: float等
```py
from array import array

arr1 = array("b", [0, 1])           # array('b', [0, 1])
arr2 = array("d", [0.1, 0.2])       # array('d', [0.1, 0.2])
arr3 = array("f", [0.1, 0.1, 0.2])  # array('f', [0.10000000149011612, 0.10000000149011612, 0.20000000298023224])
```

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
from enum import Flag

class Color(Flag):
    RED = 1
    GREEN = 2
    BLUE = 3
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
def sum(a, b):
    return a + b

print(sum(10, 20))  # 30
```

`*args` - 可変長引数です。
```py
def output(*args):
    for arg in args:
        print(arg)

print("Hi", "Im", "Anne")   # Hi Im Anne
```

`**kwargs` - 可変長のキーワード引数です。
```py
def output(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}=>{value}")

output(name="Anne", age=21) # name=>Anne, age=>21
```

**キーワードのみ引数** - `*`の後ろに定義した引数にキーワード指定を強制します。
```py
def hello(name, *, has_exclamation):
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
    def wrapper(txt: str):
        bad_words = ["fuck", "bitch", "ass", "shit"]
        for bad_word in bad_words:
            txt = txt.replace(bad_word, "*" * len(bad_word))
        v = f(txt)
        return v
    return wrapper

@hiding
def chant(quote):
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
    def greeting(cls):
        print(cls.greet)

Human.greeting()        # HELLO
Human.greet = "こんにちは"
Human.greeting()        # こんにちは
print(Human.greet)      # こんにちは
```

**静的メソッド** - 継承クラスでも動作が変わらない場合に用いられます。
```py
class Date:
    def __init__(self, date) -> None:
        self.date = date

    def get_date(self):
        return self.date
    
    @staticmethod
    def to_slash_date(d):
        return d.replace("-", "/")
    
d1 = Date("2025-12-31")
print(d1.date)                      # 2025-12-31
d2 = Date.to_slash_date("2025-12-31")
print(d2)                           # 2025/12/31
```

**継承** - クラスを継承できます。以下の例にはオーバーライドが含まれます。
```py
class Animal:
    def __init__(self, name) -> None:
        self.name = name
    def speak(self):
        print(f"私の名前は{self.name}です。")

class Dog(Animal):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
    def speak(self):
        super().speak()
        print(f"犬です。{self.type}です。")

dog = Dog("Doggo", "Shiba")
dog.speak()
```

- `__init__(self)` - インスタンス生成時に実行されます。
- `__del__(self)` - デストラクタです。
- `__new__(cls)` - インスタンスを作る前に実行されます。
- `__repr__(self)` - オブジェクトを表す公式の文字列を計算して返します。基本はデバッグに使用します。
```py
class Animal:
    def __init__(self, name) -> None:
        self.name = name
    def __repr__(self):
        return f"Animal(Name: {self.name})"

animal = Animal("Dick")
print(animal)           # Animal(Name: Dick)
```
- `__str__(self)` - `__repr__`みたいなものです。
- `__add__(self)` - `math.trunc()`の動作
- `__sub__(self)` - `math.ceil()`の動作
- `__mul__(self)` - `math.floor()`の動作
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

[⬆︎目次に戻る](#目次)
