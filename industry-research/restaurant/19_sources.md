# 19_sources.md — 飲食業 出典一覧（初版：01〜04 対応）

> `common/methodology.md` §10 の形式で記録しています。
> **本ファイルに掲載しているのは、実際に内容を読めた資料のみです。**
> 到達確認しかできていないもの・本文が取得できなかったものは、末尾の「§C 取得できなかった資料」に分けて記録しています。
>
> 取得日はすべて **2026-09-17** です。

---

## §A 統計（事業所数・従業者数・市場規模・営業許可）

```
- source_title   : 令和3年経済センサス‐活動調査 事業所に関する集計－産業
                   第2－1表 産業(中分類)、経営組織(8区分)別全事業所数、男女別従業者数及び常用雇用者数
                   －全国、都道府県、大都市
  organization   : 総務省・経済産業省（e-Stat 政府統計の総合窓口）
  url            : https://www.e-stat.go.jp/stat-search/file-download?statInfId=000040067802&fileKind=0
  published_date : 令和3年経済センサス‐活動調査（2021年6月1日現在）
  accessed_date  : 2026-09-17
  used_for       : 01_overview.md 1-1「飲食店（中分類76）の事業所数499,193・従業者数3,489,163人」
                   「持ち帰り・配達飲食サービス業56,686事業所・584,522人」「宿泊業45,327事業所・627,505人」
                   「大分類M 601,300事業所・4,701,797人」
                   01_overview.md 1-7「飲食店の個人経営311,574事業所（62.4％）・法人187,251事業所」
                   「個人経営の従業者920,531人／法人の従業者2,566,087人」
                   「全産業（民営）の個人経営1,640,810事業所（31.8％）」
                   03_company-structure.md 3-6 同上
                   ※ Excel形式。ブラウザUAを付けたcurlで取得し、全国行のみ抽出して確認した。
```

```
- source_title   : 令和6年経済センサス‐基礎調査 甲調査 事業所に関する集計－事業所数、従業者数
                   第4－2表 産業(小分類)、経営組織(4区分)別民営事業所数、従業者数及び常用雇用者数
                   (雇用者のいない個人経営の事業所を除く)－全国、都道府県、市区町村：全国
  organization   : 総務省（e-Stat 政府統計の総合窓口）
  url            : https://www.e-stat.go.jp/stat-search/file-download?statInfId=000040389326&fileKind=0
  published_date : 令和6年経済センサス‐基礎調査（2024年）
  accessed_date  : 2026-09-17
  used_for       : 01_overview.md 1-6「統計で見る業態の違い（1事業所あたりの従業者数）」の表全体
                   （食堂・レストラン／専門料理店／日本料理店／中華料理店／焼肉店／そば・うどん店／
                     すし店／酒場・ビヤホール／バー・キャバレー・ナイトクラブ／喫茶店／その他の飲食店／
                     ハンバーガー店／お好み焼・焼きそば・たこ焼店／持ち帰り・配達飲食サービス業ほか）
                   ※ この集計は「雇用者のいない個人経営の事業所を除く」ため、
                     令和3年経済センサス‐活動調査（全事業所ベース）と直接比較できない旨を本文に明記した。
```

```
- source_title   : 外食産業市場規模推移（外食産業市場規模推計の推移）
  organization   : 公益財団法人 食の安全・安心財団（推計：一般社団法人日本フードサービス協会）
  url            : http://anan-zaidan.or.jp/data/2024-1-2.xlsx
                   （掲載元ページ： http://anan-zaidan.or.jp/data/index.html ）
  published_date : 令和4年・5年（2022年・2023年）推計値の公表に伴う更新。系列は1975年〜2023年
  accessed_date  : 2026-09-17
  used_for       : 01_overview.md 1-1「2023年の外食産業市場規模24兆1,512億円」および内訳表全体
                   （給食主体部門202,793／営業給食171,052／飲食店141,313／食堂・レストラン94,810／
                     そば・うどん店13,774／すし店14,974／その他飲食店17,755／機内食等1,802／
                     宿泊施設27,937／集団給食31,741／学校4,832／事業所15,884／病院7,513／保育所3,512／
                     料飲主体部門38,719／喫茶店11,892／居酒屋・ビヤホール等9,152／料亭2,182／
                     バー・キャバレー・ナイトクラブ15,493／料理品小売業80,990）単位：億円
                   01_overview.md 1-4「料理品小売業（中食）の市場規模」
                   ※ Excel形式。行ラベルと合計値の整合（部門計＝内訳の合計）を確認したうえで採用した。
```

```
- source_title   : 外食率と食の外部化率の推移（～令和5年）
  organization   : 公益財団法人 食の安全・安心財団
                   （(1)(2)は内閣府「国民経済計算」、(4)は日本たばこ協会、(6)(7)は日本フードサービス協会の推計による）
  url            : http://anan-zaidan.or.jp/data/2025-1-3.xlsx
                   （掲載元ページ： http://anan-zaidan.or.jp/data/index.html ）
  published_date : 令和5年（2023年）まで
  accessed_date  : 2026-09-17
  used_for       : 01_overview.md 1-1「2023年の広義の外食市場規模31兆7,828億円」
                   「外食率30.3％」「食の外部化率39.9％」
                   01_overview.md 1-2「食の外部化率」
                   ※ 「広義の外食市場規模＝外食産業市場規模＋料理品小売業（弁当給食を除く）」であることを
                     数値の突合により確認した（241,512＋（80,990−4,674）＝317,828）。
```

```
- source_title   : 令和6年度衛生行政報告例 【食品衛生】第3表－1
                   改正食品衛生法に基づく許可を要する食品関係営業施設数・許可・廃業施設数・
                   処分・告発件数・調査・監視指導施設数，営業の種類別
  organization   : 厚生労働省（e-Stat 政府統計の総合窓口）
  url            : https://www.e-stat.go.jp/stat-search/file-download?statInfId=000040359184&fileKind=1
                   （統計の所在： https://www.mhlw.go.jp/toukei/list/36-19.html ）
  published_date : 令和6年度（2024年度）
  accessed_date  : 2026-09-17
  used_for       : 01_overview.md 1-1「飲食店営業の営業施設数946,451施設／食品関係営業施設の総数1,227,521施設」
                   「年度中の新規許可285,784施設／廃業62,116施設」
                   01_overview.md 1-7(4) 同上
                   ※ CSV形式（Shift_JIS）。統計表本体の注記（奈良県・盛岡市の集計上の取扱い）も確認した。
```

```
- source_title   : 令和6年度衛生行政報告例 【食品衛生】第1表－1
                   旧食品衛生法に基づく許可を要する食品関係営業施設数・許可・廃業施設数・
                   処分・告発件数・調査・監視指導施設数，営業の種類別
  organization   : 厚生労働省（e-Stat 政府統計の総合窓口）
  url            : https://www.e-stat.go.jp/stat-search/file-download?statInfId=000040359180&fileKind=1
  published_date : 令和6年度（2024年度）
  accessed_date  : 2026-09-17
  used_for       : 01_overview.md 1-1「旧法に基づく飲食店営業488,162施設（一般食堂・レストラン等266,065／
                   仕出し屋・弁当屋28,635／旅館14,911／その他178,551）、喫茶店営業27,223施設、総数676,718施設」
                   01_overview.md 1-7(4)「旧法に基づく飲食店営業の廃業施設数138,226施設」
                   ※ 統計表の注記（旧法から改正法へ移行した施設の廃業施設数への計上に自治体差がある旨）を
                     確認し、本文で「単純合算しない」「開業・廃業の実数として読めない」旨を明記した。
```

```
- source_title   : 中小企業の企業数・事業者数 統計表「産業別規模別企業数」
  organization   : 中小企業庁（総務省・経済産業省「令和3年経済センサス‐活動調査」再編加工）
  url            : https://www.chusho.meti.go.jp/koukai/chousa/chu_kigyocnt/index.html
  published_date : 2023年12月13日公表／2021年6月1日時点
  accessed_date  : 2026-09-16（common/base-statistics.md に集約済みの数値を参照）
  used_for       : 01_overview.md 1-1 および 1-7「宿泊業，飲食サービス業の中小企業424,543社・大企業513社・
                   中小企業比率99.88％」および「この統計から飲食業単独の企業数は分離できない」旨の記述
                   ※ 本業界エージェントは再調査せず、common/base-statistics.md §1 の値を引用した。
```

---

## §B 法令（すべて e-Gov 法令検索／法令APIで条文本文を確認）

```
- source_title   : 食品衛生法（昭和22年法律第233号）
  organization   : e-Gov法令検索（デジタル庁）
  url            : https://laws.e-gov.go.jp/law/322AC0000000233
  published_date : 昭和22年12月24日公布（取得時点の現行法令データ）
  accessed_date  : 2026-09-17
  used_for       : 第1条（目的）→ 01_overview.md 1-2(5)
                   第51条第1項第1号・第2号、第2項（公衆衛生上必要な措置の基準・遵守義務）
                     → 02_industry-structure.md 11-1(2)、03_company-structure.md 3-4⑫、
                       04_end-to-end-process.md 4-1 A-12「HACCPに沿った衛生管理」
                   第54条（都道府県が条例で定める施設の基準）、第55条（営業許可・不許可事由・有効期間）
                     → 01_overview.md 1-2(5)・1-7(5)、02_industry-structure.md 11-1(5)、
                       03_company-structure.md 3-3③・3-5(3)
                   第60条第1項（許可の取消し・営業の禁止・停止）、第61条（施設基準違反時の整備改善命令等）
                     → 04_end-to-end-process.md 4-2 A-C
                   第63条第2項（食中毒の調査）→ 04_end-to-end-process.md 4-2 A-C
                   ※ 法令API（https://laws.e-gov.go.jp/api/1/lawdata/322AC0000000233）で
                     本文XMLを取得し、該当条文を直接読んで確認した。
```

```
- source_title   : 食品衛生法施行令（昭和28年政令第229号）
  organization   : e-Gov法令検索（デジタル庁）
  url            : https://laws.e-gov.go.jp/law/328CO0000000229
  published_date : 取得時点の現行法令データ
  accessed_date  : 2026-09-17
  used_for       : 第34条の2第2号（飲食店営業等を「取り扱う食品の特性に応じた取組」の対象営業者とする政令の定め）
                     → 04_end-to-end-process.md 4-1 A-12
                   第35条第1号（許可を要する営業として飲食店営業を掲げる）
                     → 01_overview.md 1-2(5)、03_company-structure.md 3-5(3)
                   第36条（保健所長が行う食中毒の原因調査）→ 04_end-to-end-process.md 4-2 A-C
                   附則（令和2年政令第268号）第1条（改正法附則第1条第3号に掲げる規定の施行の日＝令和3年6月1日）、
                   第2条第1項（旧法の許可を受けて営業している者は、当該許可の有効期間の満了の日までは
                   なお従前の例により営業を行うことができる）→ 01_overview.md 1-7(4)
```

```
- source_title   : 食品衛生法施行規則（昭和23年厚生省令第23号）
  organization   : e-Gov法令検索（デジタル庁）
  url            : https://laws.e-gov.go.jp/law/323M40000100023
  published_date : 取得時点の現行法令データ
  accessed_date  : 2026-09-17
  used_for       : 第66条の2第1項・第2項・第3項（一般的な衛生管理の基準＝別表第17、
                     重要工程管理の基準＝別表第18、衛生管理計画・手順書・記録・検証）
                     → 03_company-structure.md 3-4⑫、04_end-to-end-process.md 4-1 A-12
                   第66条の3第1号（飲食店営業（喫茶店営業を含む）を行う者）
                     → 04_end-to-end-process.md 4-1 A-12
                   第66条の7（法第54条の施設基準＝別表第19・第20）→ 01_overview.md 1-7(5)
                   第67条第4号（許可申請書に食品衛生責任者の氏名・資格・受講講習会を記載）
                     → 03_company-structure.md 3-5(1)
                   別表第17第1号イ・ロ・ハ・ニ・ホ（食品衛生責任者の選任・資格要件・遵守事項・
                     営業者の意見尊重義務）→ 03_company-structure.md 3-5(1)、04_end-to-end-process.md 4-1 A-12
                   別表第17第2号（施設の衛生管理：清掃、内壁・天井・床、採光・照明・換気、便所の清掃消毒ほか）
                     → 03_company-structure.md 3-4⑫
                   別表第17第3号チ（手洗設備に石けん・ペーパータオル等および消毒剤を備えること）
                     → 03_company-structure.md 3-4⑫
                   別表第18（危害要因の分析／重要管理点の決定／管理基準の設定／モニタリング方法の設定／
                     改善措置の設定／検証方法の設定／記録の作成）→ 04_end-to-end-process.md 4-1 A-12
```

```
- source_title   : 消防法（昭和23年法律第186号）
  organization   : e-Gov法令検索（デジタル庁）
  url            : https://laws.e-gov.go.jp/law/323AC1000000186
  published_date : 取得時点の現行法令データ
  accessed_date  : 2026-09-17
  used_for       : 第8条第1項（防火管理者の選任と防火管理上必要な業務）、第2項（選任・解任の届出）
                     → 02_industry-structure.md 11-1(5)、03_company-structure.md 3-5(2)
```

```
- source_title   : 消防法施行令（昭和36年政令第37号）
  organization   : e-Gov法令検索（デジタル庁）
  url            : https://laws.e-gov.go.jp/law/336CO0000000037
  published_date : 取得時点の現行法令データ
  accessed_date  : 2026-09-17
  used_for       : 第1条の2第3項第1号ロ（別表第一(一)項〜(四)項で収容人員30人以上のもの）、第4項（収容人員の算定方法）
                   第3条第1項第1号・第2号（甲種・乙種防火管理者の資格。乙種は延べ面積300平方メートル未満）
                   第3条の2第1項（防火管理者による消防計画の作成と届出）
                   別表第一（三）項ロ「飲食店」
                     → 03_company-structure.md 3-5(2)、02_industry-structure.md 11-1(5)
```

```
- source_title   : 風俗営業等の規制及び業務の適正化等に関する法律（昭和23年法律第122号）
  organization   : e-Gov法令検索（デジタル庁）
  url            : https://laws.e-gov.go.jp/law/323AC0000000122
  published_date : 取得時点の現行法令データ
  accessed_date  : 2026-09-17
  used_for       : 第13条第1項（深夜＝午前0時から午前6時までの時間）
                   第33条第1項（深夜における酒類提供飲食店営業の届出事項）、
                   第33条第4項（都道府県が条例で地域を定めて深夜の酒類提供飲食店営業を禁止できる）
                     → 02_industry-structure.md 11-1(5)、03_company-structure.md 3-5(3)
```

```
- source_title   : 酒税法（昭和28年法律第6号）
  organization   : e-Gov法令検索（デジタル庁）
  url            : https://laws.e-gov.go.jp/law/328AC0000000006
  published_date : 取得時点の現行法令データ
  accessed_date  : 2026-09-17
  used_for       : 第9条第1項（酒類の販売業免許）および同項ただし書
                   （「酒場、料理店その他酒類をもつぱら自己の営業場において飲用に供する業」は免許不要）
                     → 02_industry-structure.md 11-1(1)、03_company-structure.md 3-5(3)
```

```
- source_title   : 労働基準法（昭和22年法律第49号）
  organization   : e-Gov法令検索（デジタル庁）
  url            : https://laws.e-gov.go.jp/law/322AC0000000049
  published_date : 取得時点の現行法令データ
  accessed_date  : 2026-09-17
  used_for       : 第37条第4項（午後10時から午前5時までの深夜労働に対する2割5分以上の割増賃金）
                     → 02_industry-structure.md 11-6(4)、03_company-structure.md 3-3⑤
```

```
- source_title   : 中小企業基本法（昭和38年法律第154号）
  organization   : e-Gov法令検索（デジタル庁）
  url            : https://laws.e-gov.go.jp/law/338AC0000000154
  published_date : 取得時点の現行法令データ
  accessed_date  : 2026-09-16（common/base-statistics.md §2 に集約済みの内容を参照）
  used_for       : 第2条（サービス業の中小企業者＝資本金5,000万円以下または従業員100人以下）、
                   第2条第5項（商業・サービス業の小規模企業者＝従業員5人以下）
                     → 01_overview.md 1-7(2)、03_company-structure.md 3-1
```

---

## §C 取得できなかった資料（所在確認のみ／本文未取得）

> `common/base-statistics.md` §5 のとおり、本作業環境には**PDFのテキスト抽出手段がありません。**
> 以下は所在を確認したのみで、**内容を読んでいないため、本文の根拠には使用していません。**

```
- source_title   : 令和3年経済センサス‐活動調査 産業別集計（サービス関連産業B）結果の概要
  organization   : 総務省・経済産業省
  url            : https://www.stat.go.jp/data/e-census/2021/kekka/pdf/kservice_outline.pdf
  published_date : 不明（ページ上で確認できず）
  accessed_date  : 2026-09-17
  used_for       : **所在確認のみ。** PDFのためテキストを抽出できず、数値は使用していない。
                   飲食店の売上高等が必要な場合の参照先として記録する。
```

```
- source_title   : 令和6年度衛生行政報告例の概況
  organization   : 厚生労働省
  url            : https://www.mhlw.go.jp/toukei/saikin/hw/eisei_houkoku/24/
  published_date : 令和6年度（2024年度）
  accessed_date  : 2026-09-17
  used_for       : **所在確認のみ。** 本概況の統計表（Excel）には精神保健福祉・栄養・生活衛生・薬事・
                   母体保護の各分野が収載されており、**食品衛生関係の営業許可施設数は含まれていない**ことを
                   Excelの内容を確認したうえで判断した。飲食店営業の施設数は §A に掲げた
                   e-Stat の統計表（第1表－1・第3表－1）から取得している。
```

```
- source_title   : 令和4年・5年外食産業規模推計値について
  organization   : 公益財団法人 食の安全・安心財団
  url            : http://anan-zaidan.or.jp/data/2024-1-1.pdf
  published_date : 不明（ページ上で確認できず）
  accessed_date  : 2026-09-17
  used_for       : **所在確認のみ。** PDFのためテキストを抽出できず、内容は使用していない。
                   数値は同じ財団が公表するExcel（§A）から取得している。
```

---

## §D 本ファイルの記録方針（後続エージェントへの申し送り）

1. **数値は必ず「どの調査の、いつ時点の、どの表の数字か」まで記録すること。**
   飲食業では、経済センサス（活動調査／基礎調査）、衛生行政報告例、
   外食産業市場規模推計という**3系統の数字**が混在します。系統をまたいだ比較はできません。

2. **飲食業単独の「企業数」は、本ファイル記載の出典からは取得できていません。**
   `common/base-statistics.md` の「宿泊業，飲食サービス業」は宿泊業との合算です。
   企業数が必要な場合は、**分離できない旨を明記する**か、事業所数・施設数で代替してください。

3. **法令はすべて e-Gov 法令API から条文本文を取得して確認しています。**
   条番号・号・項まで特定してあるため、後続ファイル（とくに `15_rules-customs.md`）では
   本ファイルの記載をそのまま引き継いで構いません。
   ただし**条例で定める事項**（施設基準、深夜営業の禁止地域など）は自治体により異なるため、
   全国一律の記述はできません。

4. **未取得の論点**（後続で調査が必要）
   - 飲食業の売上高・付加価値額（経済センサス産業別集計。PDFのみのため未取得）
   - 飲食店の開業率・廃業率（衛生行政報告例からは制度移行の影響で読めない）
   - デリバリープラットフォームの手数料率（公表資料が確認できず、`【Varies】` として記述）
   - FL比率・原価率の業態別水準（公的統計での確認ができず、`【Varies】` として記述）
   - 正社員／パート・アルバイトの構成比（業態別の公的統計が未確認）
