---
name: ut-moderator
description: Moderate a live UT user-test session, keep prompts neutral, receive scenario-by-scenario observations, persist every result to session files, track progress, prepare a safe cleanup dry-run, and close the run. Supports usability, acceptance, and hybrid modes. Use when the user says "UTを始めます", reports results such as "B-5 OK" or an observed behavior, asks to resume UT, or says "UT終了". Do not use for unit tests. The product name "目付" (Metsuke) and the nickname "健診" are aliases for this UT workflow.
license: Proprietary. See ../ut-shared/LICENSE.txt
compatibility: Designed for Claude Code and Codex CLI/Desktop with write access to the configured UT artifacts directory. UI automation and application API access are optional.
metadata:
  version: "2.2.2"
  package: "ut-user-test-skills"
---

# UT Moderator

最初に`../ut-shared/SKILL.md`、`../ut-shared/references/observation-schema.md`、対象の`ut.config.yaml`を読む。

モデレータは進行と観察記録を担当する。原因分析や改善案作成は`ut-analysis`または後工程へ分離する。

## 開始

### 1. シナリオを確定する

- モデレーター版シナリオを読む。
- シナリオ総数、セクション、UTモード、環境を確認する。
- 変更操作、不可逆操作、外部影響操作を一覧化する。
- 参加者へ見せるのはparticipant viewだけとする。

### 2. runを作る

- `YYYY-MM-DD`と短い一意IDからrun-idを作る。
- 設定の成果物ルートに`runs/<date>-<run-id>/`を作る。
- `../ut-shared/assets/session-template.json`を使って`session.json`を作る。
- 空の`results.jsonl`を作る。
- シナリオ内の`{run_id}`プレースホルダーを確定値として実施メモに記録する。

### 3. baselineを記録する

テストデータまたは状態変更がある場合、開始前に確認可能な基準値を`baseline.md`へ保存する。

例:

- 対象一覧の件数
- 合計金額
- 対象レコードの状態
- 公開／非公開状態
- テスト用アカウントの初期状態

確認できない値を推測で埋めない。取得できないものは「未取得」と書く。

### 4. 参加者条件を確認する

- 参加者IDを割り当てる。
- 外部参加者や従業員を記録する場合、同意の有無を確認する。
- 録音・録画・スクリーンショットの扱いを設定と同意に合わせる。
- 本番環境の場合は、変更操作を行わない安全設定を再確認する。

### 5. 開始案内

利用者へ次だけを簡潔に伝える。

- 全件数とセクション
- UTモード
- データ変更・外部影響のある範囲
- 結果を逐次保存するrunの場所

参加者には「システムを評価しているのであり、参加者を評価していない」と伝える。

## 進行中

### 中立性

- 参加者が詰まっても、すぐ正解を教えない。
- 「次は保存ボタンでは？」のような誘導をしない。
- 必要なプローブは「今、何を探していますか」「そう思った理由を教えてください」のように中立にする。
- 安全上の危険、個人情報漏えい、実課金などが発生しそうな場合は中断する。

### 報告を受けたら

各報告を`results.jsonl`へ直ちに保存し、`session.json`を更新する。後回しにしない。

#### usability

次を記録する。

- タスク状態
- 観察事実
- 発話
- 迷い、誤操作、回復
- 所要時間（設定で有効な場合）
- 証拠参照

#### acceptance

次を記録する。

- `ok`、`ng`、`blocked`、`skipped`
- 期待結果との差
- 表示、数値、状態変化
- 証拠参照

#### hybrid

`task_status`と`acceptance_status`を別々に記録する。機能的にはOKでも迷いがあれば、`acceptance_status: ok`かつ`task_status: completed-with-friction`となる。

### 深掘り

不足がある場合だけ1〜2問に留める。

- 何が起きたか
- 何を期待していたか
- どの時点で迷ったか
- 同じ操作を再現できるか

原因を断定せず、改善案を議論し始めない。

### まとめ報告

「B-1〜B-4全部OK」のような報告は、各IDの個別レコードへ展開して保存する。ただし同一の推測や観察文を捏造して複製しない。

### 外部影響操作

公開、通知、決済、請求、削除などに到達したら、操作対象と影響を示して実行直前の明示承認を得る。設定で禁止されていれば実施せず、`blocked-by-policy`として記録する。

## 一時停止・再開

一時停止時は`session.json`を`paused`にし、次のシナリオIDと未処理の観察を記録する。

再開時は会話履歴ではなく、次を読む。

1. `session.json`
2. `results.jsonl`
3. モデレーター版シナリオ

完了済みIDを照合し、次のIDを提示する。

## 「UT終了」

### 1. 実施サマリー

モードに応じて件数とIDを集計する。

- 完了
- 摩擦あり完了
- 失敗／NG
- blocked
- skipped
- 未実施

### 2. 結果ログ

`results.jsonl`から、人が読める`UT結果ログ_<date>.md`を生成する。各項目をシナリオへ追跡できるようにする。

### 3. cleanup dry-run

テストデータがある場合、`cleanup-plan.md`を作る。

- 対象ID・名前
- 種類
- 作成／変更／復元の別
- 親子関係
- 実行順序
- baselineへの影響
- 削除・復元できない可能性

利用者へ対象と件数を提示し、承認を得るまで操作しない。

### 4. 承認後の後片付け

- dry-runに記載した対象だけを処理する。
- 削除制約に従い子→親など安全な順で行う。
- 操作結果をcleanup planへ追記する。
- baselineと比較する。
- 差分が残れば`cleanup_status: incomplete`とする。

### 5. runを閉じる

すべて保存し、状態を`closed`へ変更する。クリーンアップ未完了なら`cleanup-pending`のままにする。

完了報告には次を含める。

- runディレクトリ
- 結果サマリー
- cleanup結果
- baseline復帰の確認
- 分析可能なログの場所

## Hard NEVERs

- 実施結果を会話だけに保持する
- 参加者へ期待結果を先出しする
- 原因推測を観察事実として保存する
- 明示承認なしにデータを削除・公開・送信・課金する
- 本番環境で設定を無視して変更操作を行う
- 参加者の同意なく録音・録画する
- 重大な安全問題をテスト継続のために無視する
