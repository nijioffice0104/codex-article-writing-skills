---
name: ut-analysis
description: Analyze completed UT user-test evidence and create a traceable analysis report that separates observations from interpretation, combines relevant usability and impact frameworks, identifies evidence strength, and converges individual findings into root issues. Use when the user asks "UT分析レポートを作って", "UT結果を分析して", or wants a previous and current UT compared. Do not use for unit tests. The product name "目付" (Metsuke) and the nickname "健診" are aliases for this UT workflow.
license: Proprietary. See ../ut-shared/LICENSE.txt
compatibility: Designed for Claude Code and Codex CLI/Desktop with access to UT run files and project context. Web access is optional for source verification.
metadata:
  version: "2.2.2"
  package: "ut-user-test-skills"
---

# UT Analysis

最初に`../ut-shared/SKILL.md`、`../ut-shared/references/observation-schema.md`、対象プロジェクトの`ut.config.yaml`を読む。

## 分析の立場

目的は、観察された事実から課題を構造化し、根本課題を同定することである。改善案の量産を主目的にしない。

次を分離する。

- 観察事実
- 参加者の発話
- 受入条件との差
- 分析者の解釈
- 根本課題の仮説
- 改善案（求められた場合のみ別枠）

## 入力を確定する

1. `session.json`
2. `results.jsonl`
3. `UT結果ログ_<date>.md`
4. participant／moderatorシナリオ
5. 設定された要件、設計、実装コンテキスト
6. 前回のUT分析レポート（比較時）

欠けている入力を一覧化し、取得できるものは先に読む。ログの欠損を推測で補完しない。

## データ整合チェック

分析前に次を確認する。

- sessionの完了IDとresultsのIDが一致する
- 重複レコードがない、または更新履歴として説明できる
- participant IDが匿名化されている
- 観察事実と解釈が分離されている
- 証拠リンクが実在する
- cleanup結果をUX問題として誤分類していない
- モードに合った状態値が使われている

不整合はレポートの制約として明記する。

## 分析枠組み

設定された枠組みを使うが、適用対象を無理に広げない。

### Nielsenの10ヒューリスティック

UIのユーザビリティ課題を横断分類する。可視性、実世界との一致、制御と自由、一貫性、エラー予防、認識、効率、最小限の設計、エラー回復、ヘルプの観点を使う。

非UIの要件欠落、データ不整合、権限設計などに無理なヒューリスティック番号を付けない。

### インパクト分析

各課題が次へ与える影響を分ける。

- 効果: タスクを達成できるか
- 効率: 余計な時間、操作、迷いがあるか
- 満足・信頼: 不安、誤解、不信を生むか

発生頻度と証拠の確信度を混同しない。参加者が少ない場合は頻度を一般化せず、タスクへの重大性と証拠強度を優先する。

### UX5段階

課題を次の層へ位置付ける。

- 表層: 視覚表現
- 骨格: 配置、ナビゲーション、導線
- 構造: 情報設計、操作フロー
- 要件: 必要機能、コンテンツ
- 戦略: 製品目的、ユーザー価値

深い層ほど設計判断と広い影響範囲を伴う可能性がある。ただし深い層を自動的に最優先としない。

### 受入確認の差分

`acceptance`または`hybrid`では、機能上のNGをユーザビリティ問題と分離する。

- 要件／期待結果との差
- 実装不具合
- 環境・データ起因
- 手順または要件の曖昧さ
- 未判定

## 個別観察を整理する

各観察に次を付ける。

- observation ID
- scenario ID
- participant IDまたはAI観点
- task status
- acceptance status
- 観察事実
- 発話
- 証拠
- 証拠強度
- 適用可能なヒューリスティック
- インパクト
- UX層
- 前回との関係

AIが独立に画面確認した結果は、参加者の観察と区別して`AI observation`と記録する。AIを人間参加者数へ加算しない。

## 根本課題へ収束する

1. 表層事象を、共通メカニズム、違反原則、影響、UX層でグルーピングする。
2. 根本課題へ短い名前を付ける。
3. 観察から帰結までの因果連鎖を1文で示す。
4. 根拠となるobservation IDとscenario IDを列挙する。
5. 確信度を`high`、`medium`、`low`で付け、理由を書く。
6. 反証や別解釈があれば併記する。

目標件数は設定を目安にする。小規模UTを無理に5件へ増やしたり、大規模UTを無理に8件へ圧縮したりしない。

確信度の目安:

- `high`: 複数の独立した観察、参加者、証拠種別が一致
- `medium`: 明確な直接観察はあるが、範囲または再現性が限定的
- `low`: 解釈依存、証拠不足、別原因の可能性が高い

## 再UT比較

前回レポートがある場合、各根本課題と個別観察を次に分類する。

- `resolved`
- `improved-but-remains`
- `recurred`
- `new`
- `not-tested`

前回とシナリオや環境が異なる場合、単純な件数比較をしない。

## レポート構成

`../ut-shared/assets/analysis-report-template.html`を使い、次を含める。

1. A. 分析方法とデータ範囲
2. B. エグゼクティブサマリー
3. C. 観察結果の分布
4. D. 根本課題
5. E. インパクト分析
6. F. UX層別分析
7. G. 個別観察
8. H. 参加者・観点別の寄与
9. I. 結論
10. 付録. 証拠と追跡対応

モードに応じて受入差分の章を追加する。

## 書き方

- 冒頭にデータ範囲、参加者数、モード、制約を書く。
- 件数だけで重要度を決めない。
- 参加者の発話を過度に一般化しない。
- 根本課題ごとに確信度と根拠を示す。
- 改善案を求められた場合は、分析結果と分けた「次工程への論点」として書く。
- 要件、設計、外部事実を参照した場合は出典を付ける。

## 品質チェック

- 全resultsレコードが個別観察表へ対応している
- 根本課題から元観察へ逆引きできる
- acceptance NGとUX摩擦を混同していない
- Nielsen分類を非UI課題へ強制していない
- 確信度に根拠がある
- n=1の結果を頻度として一般化していない
- 推測表現を事実として断定していない
- HTMLをブラウザで表示し、表、改ページ、文字切れを確認した
- 旧版を保持し、更新版の関係を明記した

## 完了報告

- レポートの保存場所
- 観察件数と根本課題数
- 最重要の根本課題と確信度
- データ上の制約
- 前回比較の有無
- 次工程で議論すべき論点

## Hard NEVERs

- 個別課題を束ねず、そのまま根本課題と呼ぶ
- AI観点を人間参加者数として数える
- 単一参加者の結果を母集団頻度として一般化する
- 機能不具合とユーザビリティ摩擦を同じ判定へ潰す
- 観察されていない原因を断定する
- 改善案を分析事実として混ぜる
