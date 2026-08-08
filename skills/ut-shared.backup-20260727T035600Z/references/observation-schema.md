# UT観察・結果スキーマ

## `session.json`

UT全体の状態を保持する。

必須項目:

- `schema_version`
- `run_id`
- `project_name`
- `test_mode`
- `environment`
- `scenario_source`
- `started_at`
- `updated_at`
- `status`: `prepared`、`running`、`paused`、`completed`、`cleanup-pending`、`closed`
- `participant_ids`
- `scenario_counts`
- `completed_scenario_ids`
- `pending_scenario_ids`
- `cleanup_status`

## `results.jsonl`

1観察または1判定を1行のJSONで保存する。後から追記でき、途中終了にも耐えられる形式とする。

推奨項目:

```json
{
  "timestamp": "2026-07-21T10:00:00+09:00",
  "run_id": "a1b2c3",
  "scenario_id": "B-5",
  "participant_id": "P01",
  "task_status": "completed-with-friction",
  "acceptance_status": "ok",
  "observed": "保存ボタンを2回押した",
  "quote": "保存できたか分からない",
  "interpretation": null,
  "evidence": ["screenshots/B-5-01.png"],
  "created_test_data": [],
  "tags": ["visibility", "duplicate-action"]
}
```

### 状態値

ユーザビリティ:

- `completed`
- `completed-with-friction`
- `failed`
- `blocked`
- `skipped`

受入確認:

- `ok`
- `ng`
- `blocked`
- `not-applicable`
- `skipped`

ハイブリッドでは両方を記録する。

## 観察と解釈の分離

良い記録:

- observed: 「参加者は検索欄を見つけるまで一覧上部を14秒見回した」
- quote: 「絞り込みはどこですか」
- interpretation: 空欄。分析工程で記入する

悪い記録:

- observed: 「検索UIが分かりにくいので改善すべき」

後者は観察、解釈、改善策が混ざっている。

## 証拠強度

分析時に次を区別する。

- `direct`: 画面、発話、ログで直接確認
- `corroborated`: 複数参加者・複数証拠で一致
- `inferred`: 観察からの解釈
- `unknown`: 情報不足

単一参加者で起きた事象は重要になり得るが、発生頻度の推定には使わない。

## 個人情報

- 実名ではなく`P01`などの参加者IDを使用する。
- 発話引用から個人や顧客が特定される場合は匿名化する。
- 不要なメールアドレス、電話番号、住所、認証情報を記録しない。

