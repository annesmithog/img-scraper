# img-scraper
Python script for scraping Google images.

## 環境

1. Python: 3.13
2. OS: macOS
3. Browser: Google Chrome

## 手順

リポジトリのクローン
```sh
git clone https://github.com/annesmithog/img-scraper.git
```

プロジェクトルートに遷移
```sh
cd img-scraper
```

Pythonパッケージをインストール
```sh
pip install -r requirements.txt
```

実行
```sh
python main.py
Search Keyword: PHP Icon
Number of Images [300]: 8
```

---

実行 (オプション付き)

```sh
python main.py --keyword='Laravel Icon' --count=5
```

オプション確認

```sh
python main.py --help
```

## 開発者用コマンド

```sh
# 仮想環境作成・アクティベート
python -m venv venv
. venv/bin/activate

# ディアクティベート
deactivate

# パッケージ／バージョンの書き出し
pip freeze > requirements.txt

# requirements.txt から一括インストール
pip install -r requirements.txt

# pipアンインストール
pip freeze > piplist.txt
pip uninstall -r piplist.txt -y
rm -rf piplist.txt
```
