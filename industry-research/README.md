# 業界別「中小企業の仕事がわかる」資料プロジェクト

日本の**中小企業**について、その業界をまったく知らない人が
「仕事・組織・商流・業務・ヒト・モノ・カネ・情報」を体系的に理解できる
PowerPoint資料の元データを、業界ごとに作成するプロジェクト。

> **この資料はDX提案資料ではありません。**
> AI活用・システム導入・業務改善の提案は対象外です。目的は純粋な**業界・業務理解**です。

## まず読むもの

| ファイル | 内容 |
|---|---|
| [`research-plan.md`](research-plan.md) | 実行計画・バッチ構成・業界粒度 |
| [`common/methodology.md`](common/methodology.md) | **全体の憲法**。調査方法・確度タグ・部署別15項目・完成条件 |
| [`common/design-system.md`](common/design-system.md) | スライド設計と画像生成の共通デザインシステム |
| [`common/terminology-rules.md`](common/terminology-rules.md) | 用語・表記の共通ルール |
| [`common/base-statistics.md`](common/base-statistics.md) | 全業界共通の基礎統計（産業別企業数・中小企業の定義）＋官公庁サイト取得方法 |

## 各業界フォルダの構成

```
01_overview.md            業界概要
02_industry-structure.md  業界構造（プレイヤー／商流／バリューチェーン）
03_company-structure.md   典型的な中小企業像＋組織・機能
04_end-to-end-process.md  全社業務フロー（受注〜入金）
05_departments.md         部署別業務（最重要）
06_people.md              ヒトの流れ
07_goods.md               モノの流れ
08_money.md               カネの流れ
09_information.md         情報の流れ
10_documents.md           帳票・書類
11_systems.md             システム
12_business-model.md      お金・ビジネスモデル
13_periodic-work.md       定期業務
14_kpi.md                 KPI・数字
15_rules-customs.md       法規制・商習慣
16_glossary.md            用語集＋初心者が間違えやすいこと
17_slides.md              スライド原稿
18_image-prompts.md       画像生成プロンプト
19_sources.md             出典一覧
20_qa.md                  QA結果
```

## 進捗

凡例：`-` 未着手 / `A` 基盤 / `B` 本体 / `C` スライド・画像 / `D` QA完了 / `✅` 完成

| # | 業界 | フォルダ | 状態 |
|---|---|---|---|
| 1 | 製造業 | `manufacturing/` | - |
| 2 | 建設業 | `construction/` | - |
| 3 | 卸売業 | `wholesale/` | - |
| 4 | 小売業 | `retail/` | - |
| 5 | 運輸・物流業 | `logistics/` | - |
| 6 | 飲食業 | `restaurant/` | - |
| 7 | 宿泊業 | `hotel/` | - |
| 8 | 不動産業 | `realestate/` | - |
| 9 | 医療 | `medical/` | - |
| 10 | 介護・福祉 | `care/` | - |
| 11 | 情報通信業 | `ict/` | - |
| 12 | 専門サービス業 | `professional/` | - |

最終成果物：`industry-index.md`（全12業界完了後に作成）
