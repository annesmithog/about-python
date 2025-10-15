# random

**インポート**
```py
import random
```

`random.random()` - 0.0~1.0の浮動小数点数を返す
```py
print(random.random())  # 0.23553565840533286
```

`random.uniform(a, b)` - a<=bまたはb<=aの浮動小数点数を返す
```py
print(random.uniform(1, 3)) # 2.71618966645406
```

`random.randrange(start[, stop, step])` - range(start, stop, step)の要素からランダムに返す
```py
print(random.randrange(0, 10, 2))   # 6
```

`random.randint(a, b)` - randrange(a, b + 1)と同義
```py
print(random.randint(0, 10))    # 5
```
