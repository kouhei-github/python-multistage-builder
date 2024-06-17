# messanger-handling
FaceBook Messangerにログインして、データを取得するためのコード

---

## 環境構築

Pythonのイメージは **container/Dockerfile**に記載している。

マルチステージビルドでイメージの軽量化起動の高速化を実現している。

### Dockerfileからコンテナの作成
```shell
docker compose build
```

### コンテナの起動
```shell
docker compose up -d
```

### コンテナへ接続
```shell
docker compose exec python ash
```

### コンテナ環境でPythonの実行
```shell
sh bin/start.sh
```

### Python ライブラリのインストール方法
[参考: Pipenvを使ったPython開発まとめ](https://qiita.com/y-tsutsu/items/54c10e0b2c6b565c887a)
```shell
python -m pipenv install ライブラリ名
python -m pipenv requirements > requirements.txt

```

### Python ライブラリのアンインストール方法
```shell
python -m pipenv uninstall ライブラリ名
python -m pipenv requirements > requirements.txt
```