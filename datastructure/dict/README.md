# dict

## 初期化

```py
dct1: dict[int, int] = {}
dct2: dict[int, int] = dict()
dct3: dict[str, int] = {"one": 1, "two": 2, "three": 3}
```

## 出力

```py
numbers: dict[str, int] = {"one": 1, "two": 2, "three": 3}
for key, value in numbers.items():
    print(key, "=>", value)
```

## メソッド

- `dict.keys()` - キーの一覧を返す
- `dict.values()` - 値の一覧を返す
- `dict.items()` - キーと値の一覧を返す
- `dict.get(key, default)` - 指定キーkeyに対応する値を返す。存在しない場合デフォルト値defaultを返す
- `dict.pop(key)` - 指定キーkeyに対応する値を取り出す
- `dict.popitem(key)` - 指定キーkeyに対応するキーと値のペアを取り出す
- `dict.update(d)` - 辞書型dで更新
- `dict.setdefault(key, default)` - 指定キーkeyに対応する値を返す。存在しない場合キーとデフォルト値defaultを追加
- `dict.fromkeys(iterable, value = None)` - 指定したキーのリストiterableから辞書を作成し、全てのキーに指定された値valueを割り当てる
- `dict.copy()` - 浅いコピー
- `dict.clear()` - 要素を全て削除

## 内包表記

```py
numbers = {int(v): v*10 for v in range(5)}
```
