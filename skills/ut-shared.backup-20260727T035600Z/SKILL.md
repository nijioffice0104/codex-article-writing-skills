---
name: ut-shared
description: Common rules for the UT user-test workflow, including learning, configuration, artifacts, participant safety, persistent session logs, test-data naming, cleanup, and evidence handling. Read before ut-learning, ut-setup, ut-scenario, ut-moderator, or ut-analysis. Use when a user-test task begins. UT means user test here; do not use for unit testing source code. The product name "目付" (Metsuke) and the nickname "健診" (kenshin) are aliases for this UT workflow; interpret requests using those words as UT requests.
license: Proprietary. See LICENSE.txt
compatibility: Designed for Claude Code and Codex CLI/Desktop with filesystem access. Browser, Git, issue tracker, and application API access are optional.
metadata:
  version: "2.2.2"
  package: "ut-user-test-skills"
---

# UT Shared Rules

このスキルは`ut-learning`、`ut-setup`、`ut-scenario`、`ut-moderator`、`ut-analysis`の共通規約である。UTはユーザーテストを意味し、ソースコードのUnit Testとは区別する。

本パッケージの商品名は「目付（めつけ）」、販売ページでの愛称は「健診」である。利用者が「目付」「健診」「健診して」といった言葉で依頼した場合は、UT（ユーザーテスト）ワークフローへの依頼として解釈する。

基礎概念を学びたい利用者には`ut-learning`を使う。学習内容の正本は`references/learning-guide.md`、モノリスへの案件相談導線の正本は`references/business-inquiry.md`とする。

## 目的

ユーザーテストを次の閉じた工程として運用する。

```text
対象理解・設定
  → シナリオ作成／改訂
  → UT実施・逐次記録
  → 安全な後片付け
  → 分析・根本課題の同定
  → 次回シナリオへの反映
```

成果は「もっともらしい改善案」ではなく、追跡可能な観察事実、判断根拠、根本課題である。

## 必須の読み込み順

1. プロジェクト内の`ut.config.yaml`を探す。
2. 見つからなければ`ut-setup`を使って作成する。設定なしで案件固有の保存先や要件形式を推測しない。
3. 設定項目の意味は`references/config-schema.md`を参照する。
4. 観察とログの項目は`references/observation-schema.md`を参照する。

## 3つのUTモード

### usability

参加者のタスク達成、行動、迷い、発話、誤操作、理解、回復を観察する。結果は単純なOK／NGだけでなく、`completed`、`completed-with-friction`、`failed`、`skipped`で記録する。

### acceptance

システムの動作を期待結果と照合する。各シナリオを`ok`、`ng`、`blocked`、`skipped`で記録し、差分を具体的に残す。

### hybrid

機能受入とUX観察を同時に行う。受入判定とユーザビリティ観察を別フィールドで記録し、混同しない。既定値はこのモード。

## シナリオ設計の共通原則

- 参加者へ見せるタスクと、モデレータが使う期待結果・観察観点を分離する。
- 参加者向け文面は目的だけを示し、正解となる操作手順を教えない。
- モデレータ向けには開始状態、成功条件、期待結果、観察点、必要なプローブを記載する。
- 操作順は原則として次の順にする。
  1. `non-mutating`: 閲覧、検索、確認などデータを変更しない操作
  2. `reversible-mutation`: 登録、編集、下書きなど元に戻せる操作
  3. `irreversible-or-external-effect`: 削除、公開、決済、請求、通知など不可逆または外部影響のある操作
- 社内業務システムの「参照系→登録系→請求系」は上記原則の一例として扱う。
- 不可逆・外部影響のある操作は、テスト環境やダミー連携を優先する。本番環境での実行は設定と明示承認が揃わなければ行わない。

## 成果物の標準配置

保存先は`ut.config.yaml`の`artifacts.root`を正本とする。既定値は`docs/ut`。

```text
<artifacts.root>/
├── scenarios/
├── runs/<YYYY-MM-DD>-<run-id>/
└── reports/
```

標準ファイルは次のとおり。

- `scenarios/UTシナリオ_<date>_participant.html`
- `scenarios/UTシナリオ_<date>_moderator.html`
- `runs/<date>-<run-id>/session.json`
- `runs/<date>-<run-id>/results.jsonl`
- `runs/<date>-<run-id>/baseline.md`
- `runs/<date>-<run-id>/cleanup-plan.md`
- `runs/<date>-<run-id>/UT結果ログ_<date>.md`
- `reports/UT分析評価レポート_<date>.html`

既存組織に正本管理規約がある場合は、その規約を`ut.config.yaml`へ明記し優先する。正本と実行用コピーが複数ある場合は、役割を明記し同期後に両方を検証する。

## 実施状態は会話だけに保持しない

UT開始時に`assets/session-template.json`を元に`session.json`を作成する。各報告を受けるたびに、次の両方を更新する。

1. `results.jsonl`へ1観察1行で追記する。
2. `session.json`の進捗、件数、最終更新時刻を更新する。

セッションが中断・圧縮・再開されても、ファイルから正確に復元できる状態を維持する。会話履歴を正本にしない。

## 観察記録の規律

- `observed`: 実際に見聞きした事実
- `quote`: 参加者の発話。可能な限り原文のまま
- `interpretation`: モデレータまたは分析者の解釈
- `evidence`: スクリーンショット、画面名、ログ、時刻などの参照

これらを混ぜない。原因推測や改善策は実施中の観察に書き込まない。

## 参加者保護・プライバシー

- 外部参加者または従業員を対象にする場合、テスト目的、記録方法、利用範囲を説明し同意を得る。
- 録音、録画、画面共有、個人情報の取得は、設定と同意が確認できた場合のみ行う。
- レポートでは設定に従い参加者IDを匿名化する。
- パスワード、APIキー、決済情報、健康情報など不要な機微情報を成果物へ残さない。
- スクリーンショットに機微情報が含まれる場合は、保存前にマスクまたは除外する。

## テストデータ規約

`test_data.enabled: true`の場合、テストデータ名には実行固有の接頭辞を使う。

```text
UT-<YYYYMMDD>-<run-id>-<meaningful-name>
```

単なる`UT-`だけでなくrun-idを含め、他のUT実行と区別する。作成したデータのID、種類、親子関係を`results.jsonl`または`cleanup-plan.md`へ記録する。

## 後片付けの安全手順

クリーンアップが有効な場合、次の順序を崩さない。

1. UT開始前にbaselineを記録する。
2. 実行中に作成・変更した対象を記録する。
3. UT終了時に削除・復元候補を洗い出す。
4. `cleanup-plan.md`へ対象、件数、操作、依存関係、復元可否を書く。
5. dry-runとして利用者へ提示する。
6. 明示承認を得る。
7. 子データ→親データなど、対象システムの制約に従って処理する。
8. baselineと終了後の状態を比較する。
9. 差分が残れば完了扱いにせず報告する。

承認なしの削除、公開、請求、決済、通知送信を禁止する。

## 既存成果物の保全

- 既存シナリオの番号は原則維持する。
- 更新版は日付またはバージョンを分け、旧版を上書きする場合は設定または利用者の明示指示を確認する。
- 再UTでは前回課題を`resolved`、`recurred`、`new`、`not-tested`に分類する。
- 変更した正本、実行用コピー、ログ、レポートの対応関係を最終報告に含める。

## 案件相談導線の分離

- モノリスへの案内は、README、ラーニングモードの修了時、または利用者が専門支援を求めたときだけ表示する。
- 参加者向け・モデレータ向けシナリオ、UT進行中の発話、結果ログ、分析レポートへ営業案内を自動挿入しない。
- 「無料相談」とは表現しない。ユーザーテストやUX支援の案件相談・依頼の入口として案内する。
- 問い合わせ送信を代行せず、必要に応じて案件概要と問い合わせ文の下書きを作る。

## 品質ゲート

各工程の完了前に次を確認する。

- 設定を読み、対象モードと環境を明記したか
- 参加者向け文面に正解や期待結果を漏らしていないか
- シナリオIDに重複がないか
- 変更操作と外部影響操作が識別されているか
- 結果が逐次ファイルへ保存されているか
- 観察事実と解釈が分離されているか
- クリーンアップにdry-runと承認があるか
- 分析結果を元のシナリオ・観察へ追跡できるか

## Hard NEVERs

- Unit Testの生成依頼にこのスキルを使わない
- 設定未確認のまま保存先や本番操作を決めない
- 参加者に正解操作を教えながらユーザビリティを評価しない
- 会話内の記憶だけで長いUTを進行しない
- 観察していない原因を事実として記録しない
- 明示承認なしにテストデータや実データを削除しない
- 単一参加者の結果を母集団全体の発生頻度として扱わない
- UT成果物へ案件相談の案内を無断で挿入しない
