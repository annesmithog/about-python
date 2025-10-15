# re

**インポート**
```py
import re
```

**コンパイルなし** - コードが短いが処理速度が遅い
```py
ptn = "Fuck.*,"
txt = r"Fuck JavaScript, Python better."
result = re.match(ptn, txt)
print(result)   # <re.Match object; span=(0, 16), match='Fuck JavaScript,'>
```

**コンパイルあり** - 処理速度が速いがコードが長い
```py
ptn = "Fuck.*,"
txt = r"Fuck JavaScript, Python better."
re_ptn = re.compile(ptn)
result = re_ptn.match(txt)
print(result)   # <re.Match object; span=(0, 16), match='Fuck JavaScript,'>
```

`re.match` - 文字列の先頭がパターンにマッチする場合、対応するMatchを返す
```py
result1 = re.match("hello", "HelloWorld")
result2 = re.match("Hello", "HelloWorld")
result3 = re.match("hello", "HelloWorld", re.IGNORECASE)
print(result1)  # None
print(result2)  # <re.Match object; span=(0, 5), match='Hello'>
print(result3)  # <re.Match object; span=(0, 5), match='Hello'>
```

`re.search` - 文字列を走査しパターンにマッチする場合、対応するMatchを返す
```py
result1 = re.search("owo", "HelloWorld")
result2 = re.search("oWo", "HelloWorld")
result3 = re.search("OWO", "HelloWorld", re.IGNORECASE)
print(result1)  # None
print(result2)  # <re.Match object; span=(4, 7), match='oWo'>
print(result3)  # <re.Match object; span=(4, 7), match='oWo'>
```

`re.fullmatch` - 文字列全体がパターンにマッチする場合、対応するMatchを返す
```py
result1 = re.fullmatch("a", "ab")
result2 = re.fullmatch("ab", "ab")
print(result1)  # None
print(result2)  # <re.Match object; span=(0, 2), match='ab'>
```

`re.findall` - 文字列中のパターンにマッチする文字列をリスト形式で返す
```py
result1 = re.findall("@[a-z]+", "@Anne | @hiroyuki | @Tanka")
result2 = re.findall("@[A-z]+", "@Anne | @hiroyuki | @Tanka")
print(result1)  # ['@hiroyuki']
print(result2)  # ['@Anne', '@hiroyuki', '@Tanka']
```

`re.sub` - パターンにマッチする文字列を置き換える
```py
ptn = "fuck|hoe|shit"
repl = "****"
txt = "hello muhfucka fuck shit"
result = re.sub(ptn, repl, txt)
print(result)   # hello muh****a **** ****
```

`re.split` - パターンにマッチする文字列を区切り文字として、文字列を分割する
```py
ptn = r"\W+"
txt = "Helium, Neon, Argon"
result = re.split(ptn, txt)
print(result)   # ['Helium', 'Neon', 'Argon']
```
