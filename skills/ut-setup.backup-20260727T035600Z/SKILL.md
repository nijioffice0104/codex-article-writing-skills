---
name: ut-setup
description: Set up the UT user-test workflow for a project by inspecting available requirements, design documents, change sources, environments, and storage conventions, then creating a project-specific ut.config.yaml. Use when the user says "UTをセットアップして", "このプロジェクトでUTを使えるようにして", "このプロジェクトを健診して", "このサイトを目付で見て" (product aliases: 目付/健診), or when another ut-* skill is requested but no configuration exists. Do not use for unit testing source code.
license: Proprietary. See ../ut-shared/LICENSE.txt
compatibility: Designed for Claude Code and Codex CLI/Desktop with read access to the target project and write access to the chosen documentation directory.
metadata:
  version: "2.2.2"
  package: "ut-user-test-skills"
---

# UT Setup

最初に`../ut-shared/SKILL.md`と`../ut-shared/references/config-schema.md`を読む。

## 目的

スキル本体を書き換えず、対象プロジェクトごとの差分を`ut.config.yaml`へ分離する。設定はプロジェクトごとに作成し、別案件へ暗黙に流用しない。

## セットアップ手順

### 1. 既存設定を探す

次の順に確認する。

1. プロジェクトルートの`ut.config.yaml`
2. `docs/ut/ut.config.yaml`
3. 利用者が指定した設定ファイル

既存設定がある場合は上書きせず、現在のプロジェクト構成と比較して変更案を提示する。

### 2. プロジェクトを読み取り専用で把握する

可能な範囲で次を確認する。

- README、プロジェクト説明、対象ユーザー
- 要件、仕様、ユーザーストーリー、受入条件
- 画面設計、サイトマップ、業務フロー、DBやAPIの概要
- package情報やフレームワークから分かる製品種別
- Git履歴、変更履歴、Issue／PR／チケットの所在
- ローカル、開発、staging、本番などの環境情報
- 既存のUT、QA、テスト成果物と保存規約
- 既存のテストデータ命名・削除ルール

GitHub等の外部サービスが利用できない場合は、ローカルGitや変更文書で代替する。接続のために作業を止めない。

### 3. UTモードを選ぶ

証拠から次を決める。

- 行動・迷い・理解を主に見る → `usability`
- 明確な期待結果との一致を主に見る → `acceptance`
- 両方必要 → `hybrid`

判断できなければ`hybrid`を既定値とし、設定サマリーで明記する。

### 4. 必要な確認だけを行う

ファイルから解決できない項目のうち、結果を大きく変えるものだけ利用者へ確認する。通常は次の最大3点で足りる。

- 誰を参加者として想定するか
- どの環境で実施するか
- 本番データ変更や外部通知を含むか

保存先、ID形式、成果物形式は既存規約から推定できれば質問せず設定案を作る。

### 5. 設定ファイルを作る

`../ut-shared/assets/ut.config.example.yaml`と設定スキーマを基に作成する。プロジェクト固有の実在パスだけを書く。存在しない要件書やID体系を作らない。

安全な既定値:

- `mode: hybrid`
- `artifacts.root: docs/ut`
- `allow_production_mutation: false`
- 外部影響操作は都度確認
- baseline、dry-run、明示承認を有効
- 参加者を匿名化

### 6. 保存先を準備する

設定で指定した成果物ルートに次を作る。

```text
scenarios/
runs/
reports/
```

既存ファイルは削除・移動しない。

### 7. 設定を検証する

- YAMLとして読み取れるか
- 記載したローカルパスが存在するか
- `test.mode`が3モードのいずれかか
- 本番環境で`allow_production_mutation: true`になっていないか。なっている場合は利用者の明示指示を記録したか
- 成果物ルートが広すぎるディレクトリやプロジェクト外を誤って指していないか

## 完了報告

次を短く報告する。

- 設定ファイルの場所
- UTモード、対象環境、想定参加者
- 読み込む要件・設計・変更情報
- 成果物の保存先
- テストデータと外部影響操作の扱い
- 未確定項目

## Hard NEVERs

- スキル本体の個人名置換でプロジェクト設定を済ませない
- 存在しないFR-ID、要件書、環境URLを作らない
- 本番データ変更を安全な既定値にしない
- 認証情報や秘密値を設定ファイルへ書かない
- 既存設定を確認せず上書きしない
