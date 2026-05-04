# Ether合同会社 / Ether LLC — Website

[https://ether-llc.com](https://ether-llc.com) で公開している、Ether合同会社の組織サイトです。

## スタック

- Python 3.12+ / Django 6
- uv (依存管理)
- Vercel Python Runtime (`manage.py` 自動検出によるデプロイ)
- Bootstrap 5 + 自前 CSS (Material 3 風)

## ローカル開発

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

`http://localhost:8000/` にアクセス。

## デプロイ (Vercel)

`vercel.json` は不要です。Vercel が `manage.py` を自動検出し、WSGI と静的ファイルを構成します。

初回のみ、Django 用の Secret Key を環境変数として登録します:

```bash
uv run python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())' | vercel env add -y DJANGO_SECRET_KEY prod
```

以降は `git push` で `main` ブランチがマージされるたびに自動デプロイされます。

## ディレクトリ構成

```
config/         — Django プロジェクト (settings.py, urls.py, wsgi.py)
ether/
  templates/    — JA テンプレート + en/ サブディレクトリ
  static/       — CSS/JS/画像
manage.py
pyproject.toml  — 依存定義 (django のみ、dev に djlint と ruff)
```

## URL 構成

| パス | 内容 |
|---|---|
| `/`, `/en/` | ホーム |
| `/vision/`, `/en/vision/` | 会社のビジョン |
| `/holdings/`, `/en/holdings/` | Ethereum 保有方針 |
| `/software/`, `/en/software/` | プロダクト紹介 (GratefulMoments) |
| `/business/`, `/en/business/` | 定款の事業目的 23 項目 |
| `/company/`, `/en/company/` | 法定の会社情報 |
| `/contact/`, `/en/contact/` | お問い合わせ窓口 |
| `/legal/privacy/`, `/legal/cookies/` | プライバシー/Cookieポリシー |
| `/robots.txt`, `/sitemap.xml` | クローラ向け |
| `/admin/` | Django 管理画面 |

## Lint / Format

```bash
uv run ruff check .            # Python
uv run djlint ether/templates/ # Django テンプレート
uv run djlint ether/templates/ --reformat
```
