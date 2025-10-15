# 高速化

- データに応じてコンテナを使い分ける
- `while` better than `for`
- 内包表記を使う
- リストで大量のデータを扱い一度の処理で一つのデータを使用する場合、ジェネレータを使用する
- 無限ループは`while 1`よりも`while True`を使う
- 文字列連結は`join`を優先して使う
```py
# BAD
txt = "A" + "B" + "C"
print(txt)  # ABC

# GOOD
txt = "".join(["A", "B", "C"])
print(txt)  #ABC
```
- 必要なモジュールのみインポートする
```py
# BAD
import collections

# GOOD
from collections import namedtuple
```
- 乗算を随時する場合は以下を使用
```py
from operator import mul
from itertools import accumulate

data = [1, 2, 3, 4, 5]
print(list(accumulate(data, mul)))  # [1, 2, 6, 24, 120]
```
- 最大値を随時設定する場合
```py
from itertools import accumulate

data = [1, 3, 5, 2, 4]
print(list(accumulate(data, max)))  # [1, 3, 5, 5, 5]
```
