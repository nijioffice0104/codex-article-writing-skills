# `ut.config.yaml`設定スキーマ

設定ファイルは対象プロジェクトのルート、または`docs/ut/ut.config.yaml`に置く。プロジェクトルートにあるものを優先する。

## 必須項目

### `version`

設定スキーマのバージョン。現在は`"2.0"`。

### `project`

- `name`: プロジェクト名
- `type`: `web-app`、`mobile-app`、`internal-business-system`、`ecommerce`、`game`、`content-service`、`other`など
- `root`: リポジトリまたは対象資料の基準パス

### `test`

- `mode`: `usability`、`acceptance`、`hybrid`
- `environment`: `local`、`development`、`staging`、`production`など
- `base_url`: 対象URL。無い場合は空文字または省略
- `participant_profile`: 想定参加者または実参加者の属性
- `participant_count`: 予定人数
- `moderator`: 実施者の呼び名または役割
- `locale`: 成果物の言語・地域

## 情報源

### `sources`

- `requirements`: 要件、仕様、受入条件のファイル一覧
- `design`: 画面設計、情報設計、業務フローなど
- `change_sources`: `git`、`github`、`gitlab`、`jira`、`linear`、`manual`など
- `requirement_id_pattern`: 要件IDがある場合のパターン。無ければ空にする

要件IDをでっち上げない。Issue、画面名、機能名など追跡可能な識別子で代替できる。

## 成果物

### `artifacts`

- `root`: 成果物の正本ルート。既定値`docs/ut`
- `format`: `html`または`markdown`
- `create_participant_view`: 参加者向けシナリオを作るか
- `create_moderator_view`: モデレータ向けシナリオを作るか

ユーザビリティUTでは両方を`true`にすることを推奨する。

## 実施順序と本番安全

### `execution`

- `order`: 通常は`non-mutating`、`reversible-mutation`、`irreversible-or-external-effect`
- `allow_production_mutation`: 本番データ変更を許可するか。既定値`false`
- `require_confirmation_for_external_effects`: 外部影響操作の都度確認。既定値`true`

`allow_production_mutation: true`でも、削除・公開・決済・通知などは実行直前の明示承認を省略しない。

## テストデータ

### `test_data`

- `enabled`: テストデータを作るか
- `prefix`: 既定値`UT-{date}-{run_id}-`
- `cleanup`: `assisted`、`manual`、`disabled`
- `require_baseline`: 開始前状態を記録するか
- `require_dry_run`: 後片付け前に対象一覧を提示するか
- `require_explicit_approval`: 実行前承認を必須にするか

販売版の安全な既定値はすべて`true`、cleanupは`assisted`。

## 観察

### `observation`

- `capture_task_time`: タスク時間を記録するか
- `capture_quotes`: 発話を記録するか
- `capture_screenshots`: `required`、`optional`、`disabled`
- `anonymize_participants`: 参加者を匿名化するか
- `recording`: `enabled-with-consent`または`disabled`

## 分析

### `analysis`

- `frameworks`: 使用する分析枠組み
- `root_issue_target`: 根本課題の目安。件数に応じて増減可能
- `confidence_levels`: 通常は`high`、`medium`、`low`

Nielsenの10原則はUIのユーザビリティに適用する。非UI課題へ無理に割り当てない。

## 省略時の安全な既定値

- `test.mode`: `hybrid`
- `artifacts.root`: `docs/ut`
- `execution.allow_production_mutation`: `false`
- `execution.require_confirmation_for_external_effects`: `true`
- `test_data.cleanup`: `assisted`
- `test_data.require_baseline`: `true`
- `test_data.require_dry_run`: `true`
- `test_data.require_explicit_approval`: `true`
- `observation.anonymize_participants`: `true`

