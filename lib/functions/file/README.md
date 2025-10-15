# ファイル操作

`open` & `close` - ファイルを開き、ファイルオブジェクトを返す
```py
f = open("sample.txt", "r", encoding="utf-8")
f.close()
```

`read` - ファイルを読み込む
```py
f = open("sample.txt", "r", encoding="utf-8")
data = f.read()
print(data)
f.close()
```

`with` & `read` - ファイル全体を文字列として読み込む
```py
with open("sample.txt", "r", encoding="utf-8") as f:
    print(f.read())
"""
aaa
bbb
"""
```

`with` & `readlines` - ファイル全体をリストとして読み込む
```py
with open("sample.txt", "r", encoding="utf-8") as f:
    print(f.readlines())
"""
['aaa\n', 'bbb\n']
"""
```

`with` & `readline` - ファイルを一行ずつ読み込む
```py
with open("sample.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1)
    print(line2)
"""
aaa
bbb
"""
```

`write` & mode=`w` - ファイルに書き込む
```py
with open("sample2.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")
    f.write("World\n")
```

`write` & pass - 空ファイル作成
```py
with open("sample3.txt", "w", encoding="utf-8") as f:
    pass
```
