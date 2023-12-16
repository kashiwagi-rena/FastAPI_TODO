# FastAPI_TODO

## サービス概要
・TODOアプリ
・新しい項目を追加していって、終わったらチェックして取消線を入れられます
・取消線が入ったものは、１日経ったら自動的にブラウザから削除されます
・別画面にて、終わったものを一覧で確認できます

## メインターゲットユーザー
・日常的に忘れ物しやすい人
・タスク管理が苦手な人
・マルチタスクが苦手な人
・めんどくさがりやの方

## 実装予定の機能一覧
・Googleログイン機能
・TODOのCRUD処理
・チェックマークをつけた際に取消線が入る
・取消線がついているものを消すための12時に自動的に動かせるバッチ処理
・取り消したTODOの一覧処理
・[自動デプロイ機能](https://docs.github.com/ja/actions/deployment/about-deployments/deploying-with-github-actions)

## 使用言語・フレームワーク
・JavaScript
・HTML
・CSS
・Python
・FastAPI
・MySQL
・SQLAlchemy
・Docker