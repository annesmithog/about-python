# tuple

## 初期化

```py
tpl1 = ()
tpl2 = tuple()
tpl3 = 10, 20, 30
tpl4 = (10, 20, 30)
tpl5 = ("ten", 20, 30)
```

## 出力

```py
numbers = ("one", "two", "three")
for number in numbers:
    print(number)
```

## メソッド

- `tuple.index(x, [start[, end]])` - 要素xの位置

## 内包表記

```py
numbers = tuple(int(v) for v in range(5))
```


