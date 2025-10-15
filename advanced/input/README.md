# 入力

**"abc"の場合**
```py
x = input()         # "abc"
x = list(input())   # ['a', 'b', 'c']
```

**"1 2 3"の場合**
```py
x, y, z = input().split()                   # x='1', y='2', z='3'
x, y, z = list(map(int, input().split()))   # x=1, y=2, z=3
```

**"1 2 3...n"とスペース区切り＆要素数不明の場合**
```py
x = input().split()                 # ['1', '2', '3', '4', '5']
x = list(map(int, input().split())) # [1, 2, 3, 4, 5]
```

**"ABxCxDEF"のように特定の文字で区切られる場合**
```py
x = input().split("x")  # ['AB', 'C', 'DEF']
```

**行数がわかる＆複数行の場合**
```py
n = int(input())                    # 3
x = [input() for _ in range(n)]     # ['10', '20', '30']
```

**行数指定されない場合?**
```py
x = []
while True:
    try:
        line = list(map(int, input().split()))
        x.append(line)
    except:
        break
```
