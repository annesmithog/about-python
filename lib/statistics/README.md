# statistics

**インポート**
```py
import statistics
```

`mean(list)` - 平均値
```py
lst = [100, 90, 80, 10, 5]
print(statistics.mean(lst)) # 57
```

`median(list)` -  中央値
```py
lst = [100, 90, 80, 10, 5]
print(statistics.median(lst)) # 80
```

`median_low(list)` - 中央値 (要素数が偶数の場合、小さい方)
```py
lst = [100, 90, 80, 60, 10, 5]
print(statistics.median_low(lst)) # 60
```

`median_high(list)` - 中央値 (要素数が偶数の場合、大きい方)
```py
lst = [100, 90, 80, 60, 10, 5]
print(statistics.median_high(lst)) # 80
```

`median_grouped(list)` - 補間メジアン
```py
lst = [100, 90, 80, 60, 10, 5]
print(statistics.median_grouped(lst)) # 79.5
```

`mode(list)` - 最頻値 (複数ある場合、最初に登場した値)
```py
lst = [10, 10, 10, 20, 30, 30, 30]
print(statistics.mode(lst)) # 10
```

`multimode(list)` - 最頻値 (複数ある場合、リストで返す)
```py
lst = [10, 10, 10, 20, 30, 30, 30]
print(statistics.multimode(lst)) # [10, 30]
```
