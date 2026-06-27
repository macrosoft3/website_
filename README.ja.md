# Ether合同会社 ウェブサイト

[English README](README.en.md)

## Overview

Ether合同会社の組織サイト (`https://ether-llc.com`) のリポジトリです。日本語と英語の2言語対応の静的風サイトで、Django のテンプレート描画と Python Runtime (Vercel) でホストされます。

## 利用シーン

- 会社概要・事業目的・プライバシーポリシー等の公開情報を2言語で提供するために使われます。
- 組織方針（ビジョン、Ethereum 保有方針）やプロダクト紹介（GratefulMoments）を同一リポジトリで管理しています。
- readme は本リポジトリのドキュメント群の一部です（詳細は [`pyproject.toml`](pyproject.toml) を参照）。

## Quickstart

必要な環境:

- Python 3.12 以上（3.12 / 3.13 / 3.14 をサポートしています）
- `uv`

セットアップ手順:

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

`http://localhost:8000/` にて日本語版、`http://localhost:8000/en/` にて英語版を確認できます。

## テスト / ヘルプ

-  Smoke テスト: [`tests/test_pages.py`](tests/test_pages.py)
- テスト実行:

```bash
uv run pytest
```

- Lint / Format:

```bash
uv run ruff check .            # Python
uv run djlint ether/templates/ # Django テンプレート
uv run djlint ether/templates/ --reformat
```

不明点は上記テストファイル [`tests/test_pages.py`](tests/test_pages.py) や [`pyproject.toml`](pyproject.toml) を確認してください。

## 保守・コントリビューション

保守: Ether LLC ([so.masuda.2003@ether-llc.com](mailto:so.masuda.2003@ether-llc.com))

本リポジトリはオープンソースライセンスではありません。コントリビューションの受付可否は保守者に確認してください。

## ライセンス

© 2026 Ether LLC. All rights reserved. 本リポジトリは参照目的で公開しており、再利用・改変・再配布を許諾していません。利用の際は保守者にご確認ください。
