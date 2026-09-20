# 19_sources.md — 医療（出典一覧）

**最終更新**：2026-09-17
**記載方針**：`common/methodology.md` §10 の形式に従う。
**原則**：**実際にアクセスし、内容を読めた資料のみ**を記載する。読めなかったものは末尾の「取得できなかった資料」に、その旨を明記して残す。

**対象ファイル**：`01_overview.md` / `02_industry-structure.md` / `03_company-structure.md` / `04_end-to-end-process.md`

---

## 1. 法令（e-Gov法令検索・法令API）

取得方法：`https://laws.e-gov.go.jp/api/2/law_data/<法令ID>?response_format=json&elm=MainProvision`（JSON・本則）
閲覧用URL：`https://laws.e-gov.go.jp/law/<法令ID>`

```
- source_title   : 医療法（昭和二十三年法律第二百五号）
  organization   : e-Gov法令検索（デジタル庁）／所管：厚生労働省
  url            : https://laws.e-gov.go.jp/law/323AC0000000205
  api_url        : https://laws.e-gov.go.jp/api/2/law_data/323AC0000000205?response_format=json&elm=MainProvision
  published_date : 昭和23年7月30日公布（取得したのは現行の本則）
  accessed_date  : 2026-09-17
  used_for       : 01「医業は営利を目的としない」（第7条第7項、第39条、第54条）／病院・診療所の定義（第1条の5）／
                   開設の許可・届出（第7条第1項〜第4項、第8条第1項）／管理者（第10条第1項、第12条第1項・第2項）／
                   有床診療所の体制（第13条）／病院の人員・施設（第21条）／医療の理念（第1条、第1条の2）／
                   患者相談（第6条の2第2項）／医療事故の報告（第6条の10）／医療安全の措置（第6条の12）／
                   病床の種別（第7条第2項各号）
```

```
- source_title   : 医療法施行規則（昭和二十三年厚生省令第五十号）
  organization   : e-Gov法令検索（デジタル庁）／所管：厚生労働省
  url            : https://laws.e-gov.go.jp/law/323M40000100050
  api_url        : https://laws.e-gov.go.jp/api/2/law_data/323M40000100050?response_format=json&elm=MainProvision
  published_date : 昭和23年11月5日公布（取得したのは現行の本則）
  accessed_date  : 2026-09-17
  used_for       : 03 人員配置基準（第19条第1項第1号＝医師、第2項第1号＝薬剤師、第2項第2号＝看護師及び准看護師、第5項＝前年度の平均値）／
                   安全管理体制（第1条の11第1項各号、第2項第1号〜第3号）／
                   04 病院の「診療に関する諸記録」（第20条第10号）／臨床検査施設の委託（第20条第6号）
```

```
- source_title   : 医療法施行令（昭和二十三年政令第三百二十六号）
  organization   : e-Gov法令検索（デジタル庁）／所管：厚生労働省
  url            : https://laws.e-gov.go.jp/law/323CO0000000326
  api_url        : https://laws.e-gov.go.jp/api/2/law_data/323CO0000000326?response_format=json&elm=MainProvision
  published_date : 昭和23年10月27日公布（取得したのは現行の本則）
  accessed_date  : 2026-09-17
  used_for       : 04 立入検査の根拠の確認（第4条の4が「法第二十五条第一項の規定により……立ち入り、……診療録、助産録、帳簿書類その他の物件を検査させた」と規定していることを確認）
```

```
- source_title   : 医師法（昭和二十三年法律第二百一号）
  organization   : e-Gov法令検索（デジタル庁）／所管：厚生労働省
  url            : https://laws.e-gov.go.jp/law/323AC0000000201
  api_url        : https://laws.e-gov.go.jp/api/2/law_data/323AC0000000201?response_format=json&elm=MainProvision
  published_date : 昭和23年7月30日公布（取得したのは現行の本則）
  accessed_date  : 2026-09-17
  used_for       : 01・02・04 医業の独占（第17条）／応招義務（第19条第1項）／無診察治療等の禁止（第20条）／
                   処方箋の交付義務（第22条）／療養の指導（第23条）／診療録の記載と5年保存（第24条第1項・第2項）
```

```
- source_title   : 保健師助産師看護師法（昭和二十三年法律第二百三号）
  organization   : e-Gov法令検索（デジタル庁）／所管：厚生労働省
  url            : https://laws.e-gov.go.jp/law/323AC0000000203
  api_url        : https://laws.e-gov.go.jp/api/2/law_data/323AC0000000203?response_format=json&elm=MainProvision
  published_date : 昭和23年7月30日公布（取得したのは現行の本則）
  accessed_date  : 2026-09-17
  used_for       : 02・03・04 看護師の定義（第5条）／准看護師の定義（第6条）／業務独占（第31条第1項、第32条）／
                   主治の医師等の指示（第37条）
```

```
- source_title   : 薬剤師法（昭和三十五年法律第百四十六号）
  organization   : e-Gov法令検索（デジタル庁）／所管：厚生労働省
  url            : https://laws.e-gov.go.jp/law/335AC0000000146
  api_url        : https://laws.e-gov.go.jp/api/2/law_data/335AC0000000146?response_format=json&elm=MainProvision
  published_date : 昭和35年8月10日公布（取得したのは現行の本則）
  accessed_date  : 2026-09-17
  used_for       : 02・04 調剤の独占（第19条）／処方せんによる調剤（第23条）／疑義照会（第24条）／
                   処方せんの3年保存（第27条）／調剤録の3年保存（第28条第3項）
```

```
- source_title   : 健康保険法（大正十一年法律第七十号）
  organization   : e-Gov法令検索（デジタル庁）／所管：厚生労働省
  url            : https://laws.e-gov.go.jp/law/211AC0000000070
  api_url        : https://laws.e-gov.go.jp/api/2/law_data/211AC0000000070?response_format=json&elm=MainProvision
  published_date : 大正11年4月22日公布（取得したのは現行の本則）
  accessed_date  : 2026-09-17
  used_for       : 01・02・04 保険者（第4条、第5条、第6条）／療養の給付の範囲と保険医療機関の指定（第63条）／
                   保険医の登録（第64条）／保険医療機関の責務（第70条）／一部負担金の割合（第74条）／
                   費用の額の算定・審査・支払（第76条第1項〜第5項）／家族療養費と義務教育就学前の給付割合（第110条第2項第1号ロ）
```

```
- source_title   : 国民健康保険法（昭和三十三年法律第百九十二号）
  organization   : e-Gov法令検索（デジタル庁）／所管：厚生労働省
  url            : https://laws.e-gov.go.jp/law/333AC0000000192
  api_url        : https://laws.e-gov.go.jp/api/2/law_data/333AC0000000192?response_format=json&elm=MainProvision
  published_date : 昭和33年12月27日公布（取得したのは現行の本則）
  accessed_date  : 2026-09-17
  used_for       : 02 保険者（第3条第1項・第2項）／審査支払事務の国保連合会等への委託（第45条第5項）
```

```
- source_title   : 高齢者の医療の確保に関する法律（昭和五十七年法律第八十号）
  organization   : e-Gov法令検索（デジタル庁）／所管：厚生労働省
  url            : https://laws.e-gov.go.jp/law/357AC0000000080
  api_url        : https://laws.e-gov.go.jp/api/2/law_data/357AC0000000080?response_format=json&elm=MainProvision
  published_date : 昭和57年8月17日公布（取得したのは現行の本則）
  accessed_date  : 2026-09-17
  used_for       : 01・02 後期高齢者医療広域連合（第48条）／被保険者（第50条）／一部負担金の割合（第67条第1項）／
                   診療報酬の審査支払事務の委託（第70条第4項）
```

```
- source_title   : 保険医療機関及び保険医療養担当規則（昭和三十二年厚生省令第十五号。通称「療担規則」）
  organization   : e-Gov法令検索（デジタル庁）／所管：厚生労働省
  url            : https://laws.e-gov.go.jp/law/332M50000100015
  api_url        : https://laws.e-gov.go.jp/api/2/law_data/332M50000100015?response_format=json&elm=MainProvision
  published_date : 昭和32年4月30日公布（取得したのは現行の本則）
  accessed_date  : 2026-09-17
  used_for       : 01・02・04 療養の給付の範囲（第1条）／担当方針（第2条）／受給資格の確認（第3条第1項・第4項）／
                   一部負担金等の受領・大病院の選定療養（第5条第1項・第3項）／診療録の記載及び整備（第8条）／
                   帳簿等の保存＝3年／診療録5年（第9条）／診療の具体的方針（第20条第1号ロ・ハ・ホ・ヘ、第2号ヘ、第3号イ・ロ）
```

```
- source_title   : 療養の給付及び公費負担医療に関する費用の請求に関する命令（昭和五十一年厚生省令第三十六号）
  organization   : e-Gov法令検索（デジタル庁）／所管：こども家庭庁・厚生労働省
  url            : https://laws.e-gov.go.jp/law/351M50000100036
  api_url        : https://laws.e-gov.go.jp/api/2/law_data/351M50000100036?response_format=json&elm=MainProvision
  published_date : 昭和51年8月7日公布（取得したのは現行の本則）
  accessed_date  : 2026-09-17
  used_for       : 02・04 電子情報処理組織の使用による請求（第1条第1項）／公費負担医療の列挙（第1条第1項各号）／
                   **請求は各月分について翌月10日まで**（第2条第1項）／到達時期（第2条第2項）／請求の代行（第4条）
```

```
- source_title   : 廃棄物の処理及び清掃に関する法律（昭和四十五年法律第百三十七号）
  organization   : e-Gov法令検索（デジタル庁）／所管：環境省
  url            : https://laws.e-gov.go.jp/law/345AC0000000137
  api_url        : https://laws.e-gov.go.jp/api/2/law_data/345AC0000000137?response_format=json&elm=MainProvision
  published_date : 昭和45年12月25日公布（取得したのは現行の本則）
  accessed_date  : 2026-09-17
  used_for       : 02・04 特別管理産業廃棄物の定義（第2条第5項）／保管基準（第12条の2第2項）／
                   運搬・処分の委託先の制限（第12条の2第5項）／特別管理産業廃棄物管理責任者（第12条の2第8項）
```

```
- source_title   : 廃棄物の処理及び清掃に関する法律施行令（昭和四十六年政令第三百号）
  organization   : e-Gov法令検索（デジタル庁）／所管：環境省
  url            : https://laws.e-gov.go.jp/law/346CO0000000300
  api_url        : https://laws.e-gov.go.jp/api/2/law_data/346CO0000000300?response_format=json&elm=MainProvision
  published_date : 昭和46年9月23日公布（取得したのは現行の本則）
  accessed_date  : 2026-09-17
  used_for       : 02・04 感染性産業廃棄物が特別管理産業廃棄物であること（第2条の4第4号）
```

```
- source_title   : 労働者災害補償保険法（昭和二十二年法律第五十号）
  organization   : e-Gov法令検索（デジタル庁）／所管：厚生労働省
  url            : https://laws.e-gov.go.jp/law/322AC0000000050
  api_url        : https://laws.e-gov.go.jp/api/2/law_data/322AC0000000050?response_format=json&elm=MainProvision
  published_date : 昭和22年4月7日公布（取得したのは現行の本則）
  accessed_date  : 2026-09-17
  used_for       : 01 労災の療養補償給付（第12条の8第1項第1号、第13条第1項・第2項）
```

```
- source_title   : 自動車損害賠償保障法（昭和三十年法律第九十七号）
  organization   : e-Gov法令検索（デジタル庁）／所管：国土交通省
  url            : https://laws.e-gov.go.jp/law/330AC0000000097
  api_url        : https://laws.e-gov.go.jp/api/2/law_data/330AC0000000097?response_format=json&elm=MainProvision
  published_date : 昭和30年7月29日公布（取得したのは現行の本則）
  accessed_date  : 2026-09-17
  used_for       : 01 自賠責（第3条＝運行供用者の責任、第15条、第16条第1項＝被害者の保険会社に対する請求）
```

---

## 2. 政府統計

```
- source_title   : 令和6(2024)年 医療施設（動態）調査・病院報告の概況
  organization   : 厚生労働省 政策統括官付参事官付保健統計室
  url            : https://www.mhlw.go.jp/toukei/saikin/hw/iryosd/24/
  data_url       : https://www.mhlw.go.jp/toukei/saikin/hw/iryosd/24/dl/05sisetu06.xlsx （医療施設調査 表1〜9、図1〜5）
                   https://www.mhlw.go.jp/toukei/saikin/hw/iryosd/24/dl/06byouin06.xlsx （病院報告 表1〜4、図1）
                   https://www.mhlw.go.jp/toukei/saikin/hw/iryosd/24/dl/02sisetu06.pdf （本文PDF。縦書きのため数値はxlsxで確認）
  published_date : 令和6(2024)年10月1日現在（施設数・病床数）／令和6(2024)年 各年間（病院報告）
  accessed_date  : 2026-09-17
  used_for       : 01・03 施設の種類別施設数（表1）／開設者別施設数（表3）／病床規模別施設数（表4）／
                   病院の診療科目別施設数（表5）／病床の種類別病床数（表7）／
                   01 病床利用率・平均在院日数・1日平均在院患者数・1日平均外来患者数（病院報告 表1〜4）
  note           : xlsxの行ラベルは結合セル・ふりがな混在のため、セル参照つきで復元して読み取った。
```

```
- source_title   : 令和5(2023)年 医療施設（静態・動態）調査・病院報告の概況
  organization   : 厚生労働省 政策統括官付参事官付保健統計室
  url            : https://www.mhlw.go.jp/toukei/saikin/hw/iryosd/23/
  data_url       : https://www.mhlw.go.jp/toukei/saikin/hw/iryosd/23/dl/05sisetu05.xlsx （表1〜26、図1〜7）
                   https://www.mhlw.go.jp/toukei/saikin/hw/iryosd/23/dl/07sisetutoukei05.xlsx （統計表1〜14）
  published_date : 令和5(2023)年10月1日現在（施設）／令和5(2023)年9月中（在宅医療サービスの実施状況）
  accessed_date  : 2026-09-17
  used_for       : 01 診療所の診療科目別施設数（表6）／在宅医療サービスの実施状況（表18）
  note           : 静態調査は3年に1度の詳細調査。診療科目別の診療所数・在宅医療の実施状況は静態調査年のみ把握される項目を含む。
```

```
- source_title   : 令和5(2023)年度 国民医療費の概況
  organization   : 厚生労働省 政策統括官付参事官付保健統計室
  url            : https://www.mhlw.go.jp/toukei/saikin/hw/k-iryohi/23/index.html
  data_url       : https://www.mhlw.go.jp/toukei/saikin/hw/k-iryohi/23/dl/R05kekka.pdf （結果の概要）
  published_date : 令和5(2023)年度
  accessed_date  : 2026-09-17
  used_for       : 01・02 国民医療費48兆915億円・一人当たり38万6,700円・対GDP比8.08%／
                   財源別（公費18兆331億円37.5%、保険料24兆1,383億円50.2%、その他5兆9,201億円12.3%、うち患者負担5兆6,865億円11.8%）／
                   診療種類別（医科診療34兆5,498億円71.8%、入院17兆8,580億円37.1%、入院外16兆6,918億円34.7%、
                   歯科3兆2,945億円6.9%、薬局調剤8兆4,563億円17.6%、入院時食事・生活7,437億円1.5%、
                   訪問看護5,727億円1.2%、療養費等4,744億円1.0%）
  note           : PDFは `common/tools/pdftext.py` で本文を抽出して確認した。
```

```
- source_title   : 令和6年度 衛生行政報告例の概況（４ 薬事関係）
  organization   : 厚生労働省 政策統括官付参事官付保健統計室
  url            : https://www.mhlw.go.jp/toukei/saikin/hw/eisei_houkoku/24/
  data_url       : https://www.mhlw.go.jp/toukei/saikin/hw/eisei_houkoku/24/dl/kekka4.pdf
  published_date : 令和6(2024)年度末現在
  accessed_date  : 2026-09-17
  used_for       : 01 薬局数63,203施設（前年度比+375施設、+0.6%）、人口10万対51.1
  note           : PDFは `common/tools/pdftext.py` で本文を抽出して確認した。
```

---

## 3. 官公庁の公表資料

```
- source_title   : 種類別医療法人数の年次推移
  organization   : 厚生労働省 医政局（「医療法人・医業経営のホームページ」内 10.統計データ）
  url            : https://www.mhlw.go.jp/content/10800000/001714098.pdf
  parent_page    : https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/iryou/igyou/index.html
  published_date : 令和8(2026)年3月31日現在
  accessed_date  : 2026-09-17
  used_for       : 01 医療法人数59,893（社団59,514〈持分あり35,104、持分なし24,410〉、財団379）／持分なし法人の推移
  note           : PDFは `common/tools/pdftable.py` で表の配置を復元して読み取った。
                   注記「平成8年までは年末現在数、9年以降は3月31日現在数である」を確認済み。
```

```
- source_title   : 我が国の医療保険について
  organization   : 厚生労働省 保険局
  url            : https://www.mhlw.go.jp/content/12400000/001416337.pdf
  parent_page    : https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/iryouhoken/iryouhoken01/index.html
  published_date : 不明（ページ上に公表日の記載を確認できず）
  accessed_date  : 2026-09-17
  used_for       : 02 高額療養費の計算例（70歳未満・年収約370万〜約770万円、医療費1,000,000円、窓口負担300,000円、
                   自己負担限度額80,100円＋（1,000,000円−267,000円）×1％＝87,430円、高額療養費212,570円）／
                   医療保険の全体図（患者→保険料→保険者、受診・窓口負担、請求・支払の流れ）
  note           : PDFは縦書き・分割テキストのため、金額・比率は文字列抽出で確認できた範囲のみ引用した。
```

```
- source_title   : 令和6年度診療報酬改定について
  organization   : 厚生労働省 保険局医療課
  url            : https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000188411_00045.html
  published_date : 令和6(2024)年3月5日（厚生労働省告示第57号ほか）
  accessed_date  : 2026-09-17
  used_for       : 02・04 診療報酬改定が偶数年度に行われていることの確認／告示・通知の構成（制定文、別表第一＝医科点数表、
                   別表第二＝歯科点数表、別表第三＝調剤点数表、実施上の留意事項通知）
```

```
- source_title   : 診療報酬の算定方法の一部を改正する告示（令和6年厚生労働省告示第57号）制定文
  organization   : 厚生労働省
  url            : https://www.mhlw.go.jp/content/12404000/001218730.pdf
  published_date : 令和6(2024)年3月5日
  accessed_date  : 2026-09-17
  used_for       : 01 「診療報酬の算定方法」が厚生労働省告示であり、改定のたびに一部改正される形式であることの確認
  note           : 縦書きのため `common/tools/pdftable.py` で配置を復元して読み取った。本文は改正文であり、
                   点数と金額の換算ルールそのものは記載されていない（下の「取得できなかった資料」を参照）。
```

```
- source_title   : 診療報酬の算定方法 別表第一（医科診療報酬点数表）／令和4年度改定版
  organization   : 厚生労働省
  url            : https://www.mhlw.go.jp/content/12404000/000907834.pdf
  parent_page    : https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000188411_00037.html （令和4年度診療報酬改定について）
  published_date : 令和4(2022)年3月4日（厚生労働省告示第54号）
  accessed_date  : 2026-09-17
  used_for       : 01 医科診療報酬点数表が「第1章 基本診療料（初・再診料、入院料）」「第2章 特掲診療料（医学管理、在宅医療、
                   検査、画像診断、投薬、注射、リハビリテーション、処置、手術 等）」の構成をとることの確認
  note           : `common/tools/pdftext.py` で全文（約39,400行）を抽出し、目次構成を確認した。
                   個別の点数は改定ごとに変わるため、本資料では具体的な点数を引用していない。
```

```
- source_title   : 診療報酬改定について（改定年度の一覧ページ）
  organization   : 厚生労働省
  url            : https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000106602.html
  published_date : 不明（ページ上に更新日の記載を確認できず）
  accessed_date  : 2026-09-17
  used_for       : 02 平成22年度・24年度・26年度・28年度・30年度・令和2年度・令和4年度の各診療報酬改定ページ、
                   および令和3年度薬価改定ページが並んでいることの確認
  note           : 本ページには令和6年度・令和8年度改定へのリンクは掲載されていなかったため、
                   それらは個別ページ（下記）で所在を確認した。
```

```
- source_title   : 令和8年度診療報酬改定について（令和8年4月以降の改正について）
  organization   : 厚生労働省 保険局医療課
  url            : https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000188411_00074.html
  published_date : 不明
  accessed_date  : 2026-09-17
  used_for       : 02・04 令和8年度に診療報酬改定が行われていることの確認
  note           : **ページタイトルのみ確認**。本文の内容は読んでいない。
                   同様に「令和5年度薬価改定について」（.../0000188411_00042.html）、
                   「令和7年度薬価改定について」（.../0000188411_00063.html）もタイトルのみ確認した。
```

```
- source_title   : 医療施設調査（調査の概要ページ）／医療施設調査 結果の概要（年次一覧）
  organization   : 厚生労働省
  url            : https://www.mhlw.go.jp/toukei/list/79-1.html
                   https://www.mhlw.go.jp/toukei/list/79-1a.html
  published_date : 不明（一覧ページ）
  accessed_date  : 2026-09-17
  used_for       : 最新の医療施設調査（令和6年＝動態、令和5年＝静態・動態）の所在特定
```

```
- source_title   : 医療法人・医業経営のホームページ
  organization   : 厚生労働省 医政局
  url            : https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/iryou/igyou/index.html
  published_date : 不明
  accessed_date  : 2026-09-17
  used_for       : 01 「種類別医療法人数の年次推移」の所在特定
```

---

## 4. プロジェクト内の既存資料（再調査していないもの）

```
- source_title   : common/base-statistics.md
  organization   : 本プロジェクト内部資料
  url            : （ローカル）industry-research/common/base-statistics.md
  accessed_date  : 2026-09-17
  used_for       : 01 中小企業基本法上の中小企業の定義（サービス業＝資本金5千万円以下又は従業員100人以下）／
                   調査手法（官公庁サイトの取得方法、e-Gov法令API、PDF読取、e-Stat）
```

---

## 5. 取得できなかった資料（内容未読。本資料の記述の限界として明記する）

```
- source_title   : 診療報酬の算定方法（平成二十年厚生労働省告示第五十九号）本文
  organization   : 厚生労働省
  url            : （特定できず）
  accessed_date  : 2026-09-17（取得を試みたが到達できず）
  status         : **内容未読**
  影響する記述    : 01「診療報酬は点数で表され、1点＝10円として金額に換算される」（現在は【Typical】表記）
  経緯           : (a) e-Gov法令API（laws?law_title=診療報酬の算定方法）は該当0件。e-Gov法令検索は告示を収載していない。
                   (b) 厚生労働省の令和4年度・令和6年度診療報酬改定ページに掲載されているのは
                       「診療報酬の算定方法の**一部を改正する**告示」の制定文と別表であり、点数と金額の換算を定める本文は含まれていない。
                   (c) 令和4年度改定の別表第一（医科点数表）全文を抽出して「十円」「10円」を検索したが、該当箇所なし。
                   (d) 厚生労働省 法令等データベースは frame 構成で、検索フォームに到達できなかった。
  扱い           : **「1点＝10円」は本資料では `【Typical】` として扱う**（Phase D／2026-09-21 に全ファイルで統一を確認）。
                   上記告示の本文そのものは本作業では原文を確認できていないため、`【Fact】` として断定しない。
                   一方、費用の額が「厚生労働大臣が定めるところにより、算定する」ものであること（＝公定価格であること）は
                   健康保険法第76条第2項の条文で確認済みであり、そこまでを `【Fact】` の根拠としている。
                   Phase D で再取得を試みたが本文には到達できなかった（下記「再取得の試行」を参照）。
```

```
- source_title   : 医療経済実態調査（医療機関等調査）
  organization   : 厚生労働省 保険局／中央社会保険医療協議会
  url            : https://www.e-stat.go.jp/stat-search/files?page=1&toukei=00450381
                   （政府統計コード 00450381。最新は第25回／tstat=000001235362、令和7年5月実施・2025-11-26公表、公表ファイル10件）
  accessed_date  : 2026-09-21（Phase D。**所在は特定できたが、統計表そのものは未取得・内容未読**）
  status         : **所在特定のみ・内容未読**
  影響する記述    : 03 説明用モデル（無床診療所の職員数・1日患者数）
  経緯           : 2026-09-17 時点では所在すら特定できなかった。Phase D（2026-09-21）に e-Stat の
                   政府統計コード 00450381（医療経済実態調査・医療機関等調査）の一覧ページまで到達し、
                   第13回〜第25回の公表単位を確認した。ただし **個別ファイルのダウンロードURLは
                   JavaScript で生成されるため curl では取得できず**、e-Stat API は appId（利用者登録）が必要で、
                   WebSearch はセッション上限（200回）に達していたため、統計表本体には到達できなかった。
  扱い           : このため `03_company-structure.md` のモデルA・モデルBの職員数・患者数は
                   **統計に基づく値ではなく、説明用の架空設定（【Example】）** として明記したままとする。
                   **モデルの規模感を統計で裏づける作業は未了**。
                   次に取り組む際は、e-Stat の利用者登録（appId 取得）を行い、
                   `getStatsList` → `getStatsData` で第25回の統計表を取得することを推奨する。
```

```
- source_title   : 社会保険診療報酬支払基金 統計情報（審査統計・返戻／査定の件数）
  organization   : 社会保険診療報酬支払基金
  url            : https://www.ssk.or.jp/tokeijoho/index.html （目次までは到達）
  accessed_date  : 2026-09-17
  status         : **数値未取得**
  影響する記述    : 02・04 返戻・査定の説明
  経緯           : 統計情報の目次ページには到達したが、審査統計の実データ（件数・金額）には到達できなかった。
  扱い           : 返戻・査定の**件数・割合などの数値は本資料に一切記載していない**。
                   仕組みの説明は、健康保険法第76条第4項（審査の上、支払う）を根拠とし、
                   実務上の呼称と流れは【Typical】として記述している。
```

---

## 6. 本資料で意図的に「書かなかった」数値

`common/methodology.md` §2「禁止」および §3「数値の扱い」に従い、次の数値は確度を確認できなかったため記載していない。

| 書かなかった数値 | 理由 |
|---|---|
| 診療所の1施設あたり平均職員数・平均患者数 | 医療経済実態調査を取得できなかったため（上記）。モデルはすべて【Example】として架空と明記 |
| 診療報酬の入金日（何日に入金されるか） | 審査支払機関・地域により異なり、一次資料を確認できなかったため。「診療月の約2か月後」という時期のみ【Typical】【Inference】で記述 |
| 返戻率・査定率 | 支払基金の審査統計に到達できなかったため |
| 具体的な点数（初診料が何点か等） | 診療報酬改定ごとに変わり、かつ本資料の目的（業務・組織・お金の流れの理解）に必須でないため |
| 「医療，福祉」大分類の事業所数・売上高 | 介護・福祉と合算されており、医療のみの数値として提示できないため（`01_overview.md` 1-7に明記） |
| 医師数・看護師数の総数 | 医師・歯科医師・薬剤師統計、衛生行政報告例（就業医療関係者）を本作業では取得していないため |

---

## 7. Phase D（QA）で追加した出典

```
- source_title   : 中小企業の企業数・事業者数（統計表「産業別規模別企業数」）
  organization   : 中小企業庁（総務省・経済産業省「令和3年経済センサス‐活動調査」再編加工）
  url            : https://www.chusho.meti.go.jp/koukai/chousa/chu_kigyocnt/index.html
                   （データファイル：https://www.chusho.meti.go.jp/koukai/chousa/chu_kigyocnt/dl/kigyou2.xlsx）
  published_date : 2023-12-13（基準日 2021-06-01）
  accessed_date  : 2026-09-16（`common/base-statistics.md` §1 に整備済み。Phase D で参照）
  used_for       : 01「大分類『医療，福祉』の企業数 205,984／中小企業 205,710（99.87%）／大企業 274」。
                   **医療と介護・福祉は合算されており分離できない**旨、および企業数と施設数の違いを併記している。
```

```
- source_title   : 医療法施行規則 第19条（病院に置くべき医師・薬剤師・看護師等の員数の標準）
  organization   : e-Gov法令検索（デジタル庁）
  url            : https://laws.e-gov.go.jp/law/323M40000100050
  published_date : 昭和23年厚生省令第50号（現行：令和8年5月1日施行）
  accessed_date  : 2026-09-21
  used_for       : 03 のモデルBの員数計算。Phase D で条文本文を e-Gov法令API から再取得し、
                   **特定数の計算で 2.5 で除するのは外来患者の数だけである**ことを確認して計算例を訂正した。
```
