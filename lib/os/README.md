# os

**インポート**
```py
import os
```

`os.path.isfile(path)` - ファイルパスpathが存在する場合Trueを返す
```py
x = os.path.isfile("src/test.py")
print(x)    # True
```

`os.path.isfir(dir)` - ディレクトリdirが存在する場合Trueを返す
```py
x = os.path.isdir("lib/functions/builtin")
print(x)    # True
```

`os.path.exists(path)` - ファイルパスpathが存在する場合Trueを返す
```py
x = os.path.exists("src/test.py")
print(x)    # True
```

`os.mkdir(path)` - ファイルパスpathを指定してディレクトリを作成。存在する場合エラー
```py
os.mkdir("py_test")
```

`os.remove(path)` - ファイルパスpathを指定してファイル削除。存在しない場合エラー
```py
os.remove("py_test/test.py")
```

`os.path.getatime(path)` - ファイルパスpathの最終アクセス時刻を返す

`os.path.getmtime(path)` - ファイルパスpathの最終更新時刻を返す

`os.path.getctime(path)` - ファイルパスpathの、最後にメタデータが変更された時刻を返す
