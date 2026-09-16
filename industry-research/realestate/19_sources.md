# 19_sources.md — 不動産業 出典一覧（初版：Phase A）

> 本ファイルは `common/methodology.md` §10 の形式に従って、
> `01_overview.md` / `02_industry-structure.md` / `03_company-structure.md` / `04_end-to-end-process.md`
> で使用した出典を記録したものです。
>
> **記載しているURLは、2026-09-17 に実際にアクセスしたもののみです。**
> **内容を読めたものと、所在の確認しかできていないものを明確に分けています**（§6 参照）。
> 後続フェーズ（Phase B / C / D）で出典を追加する場合は、本ファイルに追記してください。

---

## 1. 法令（e-Gov法令検索・法令API）

すべて e-Gov 法令API（`https://laws.e-gov.go.jp/api/1/lawdata/<法令ID>`）から
**条文本文を取得して確認**しています。人が読む形のURLは `https://laws.e-gov.go.jp/law/<法令ID>` です。

```
- source_title   : 宅地建物取引業法（昭和二十七年法律第百七十六号）
  organization   : e-Gov法令検索（デジタル庁）／法令所管：国土交通省
  url            : https://laws.e-gov.go.jp/law/327AC1000000176
                   （API）https://laws.e-gov.go.jp/api/1/lawdata/327AC1000000176
  published_date : 昭和27年6月10日公布（本プロジェクト取得時点の最新版）
  accessed_date  : 2026-09-17
  used_for       : ・第2条第2号（宅地建物取引業の定義。自ら貸借は含まれない）
                     ［01_overview 1-6／02_industry-structure ★(1)］
                   ・第2条第4号（宅地建物取引士の定義）［02_industry-structure 11-1］
                   ・第3条第1項（大臣免許・知事免許）、第2項（有効期間5年）、
                     第3項〜第5項（更新）［01_overview 1-1／02_industry-structure ★(1)］
                   ・第12条（無免許事業等の禁止）［02_industry-structure ★(1)］
                   ・第25条（営業保証金の供託等。第5項：届出後でなければ事業開始不可、
                     第6項・第7項：催告と免許取消）［02_industry-structure ★(5)］
                   ・第31条の3（宅地建物取引士の設置。第1項：省令で定める数、
                     第2項：役員が宅建士のときのみなし規定、第3項：2週間以内の是正）
                     ［01_overview 1-7／02_industry-structure ★(2)／03_company-structure 3-1・3-4］
                   ・第32条（誇大広告等の禁止）［02_industry-structure ★(6)／04 A-02・B-06］
                   ・第33条（広告の開始時期の制限）［02_industry-structure 11-3(4)・★(6)］
                   ・第34条の2（媒介契約。第1項各号：書面の記載事項、第2項：価額の意見の根拠、
                     第3項・第4項：専任媒介の有効期間3か月、第5項：指定流通機構への登録、
                     第6項：登録を証する書面の引渡し、第7項：成約時の通知、
                     第8項：申込みがあったときの報告、第9項：業務処理状況の報告
                     〈専任2週間に1回以上／専属専任1週間に1回以上〉、第10項：反する特約は無効、
                     第11項・第12項：電磁的方法）
                     ［02_industry-structure 11-2(2)(3)／04 B-03・B-05・B-06・B-15］
                   ・第35条（重要事項の説明等。第1項各号：説明事項、第4項：宅建士証の提示、
                     第5項：記名、第6項：相手方が業者の場合の読替え、第8項：電磁的方法）
                     ［01_overview 1-2／02_industry-structure ★(3)／04 A-07・B-10］
                   ・第35条の2（供託所等に関する説明）［02_industry-structure ★(3)／04 B-10］
                   ・第37条（書面の交付。第1項各号：売買・交換の記載事項、
                     第2項：貸借の記載事項、第3項：宅建士の記名、第4項・第5項：電磁的方法）
                     ［02_industry-structure ★(3)／04 A-08・B-11］
                   ・第37条の2（クーリング・オフ。8日、引渡し＋代金全部支払、
                     第3項：金銭の返還、第4項：不利な特約は無効）［02_industry-structure ★(7)／04 B-11］
                   ・第39条（手付の額の制限等。第1項：代金の10分の2、
                     第2項：手付解除、第3項：不利な特約は無効）［02_industry-structure ★(7)／04 B-11］
                   ・第41条・第41条の2（手付金等の保全措置）［02_industry-structure ★(7)／04 B-11］
                   ・第46条（報酬。第1項：大臣の定めるところによる、第2項：超過受領の禁止、
                     第3項：告示、第4項：事務所ごとの掲示）
                     ［01_overview 1-5／02_industry-structure ★(4)］
                   ・第47条（業務に関する禁止事項。第2号：不当に高額の報酬の要求 等）
                     ［02_industry-structure ★(4)(6)］
                   ・第48条（従業者証明書の携帯、従業者名簿の備付け）［02_industry-structure ★(6)］
                   ・第49条（帳簿の備付け。取引のあったつど記載）［02_industry-structure ★(6)／04 B-15］
                   ・第50条（標識の掲示等、案内所等の届出）［02_industry-structure ★(6)］
                   ・第64条の9（弁済業務保証金分担金の納付等。第2項：事務所増設時2週間以内、
                     第3項：地位の喪失）［02_industry-structure ★(5)］
```

```
- source_title   : 宅地建物取引業法施行令（昭和三十九年政令第三百八十三号）
  organization   : e-Gov法令検索（デジタル庁）
  url            : https://laws.e-gov.go.jp/law/339CO0000000383
                   （API）https://laws.e-gov.go.jp/api/1/lawdata/339CO0000000383
  published_date : 昭和39年12月28日公布（取得時点の最新版）
  accessed_date  : 2026-09-17
  used_for       : ・第2条の4（営業保証金の額。主たる事務所1,000万円、その他の事務所500万円）
                     ［02_industry-structure ★(5)／03_company-structure 3-1］
                   ・第3条の5（手付金等の保全措置が不要となる額の上限＝1,000万円）
                     ［02_industry-structure ★(7)／04 B-11］
                   ・第7条（弁済業務保証金分担金の額。主たる事務所60万円、その他の事務所30万円）
                     ［02_industry-structure ★(5)／03_company-structure 3-1］
```

```
- source_title   : 宅地建物取引業法施行規則（昭和三十二年建設省令第十二号）
  organization   : e-Gov法令検索（デジタル庁）
  url            : https://laws.e-gov.go.jp/law/332M50004000012
                   （API）https://laws.e-gov.go.jp/api/1/lawdata/332M50004000012
  published_date : 昭和32年7月22日公布（取得時点の最新版）
  accessed_date  : 2026-09-17
  used_for       : ・第15条の5の3（法第31条の3第1項の国土交通省令で定める数＝
                     事務所において業務に従事する者の数に対する宅建士の数の割合が5分の1以上）
                     ［01_overview 1-7／02_industry-structure ★(2)／03_company-structure 3-1］
                   ・第15条の9（媒介契約の書面の記載事項。第2号：専属専任媒介契約の定義、
                     第4号：標準媒介契約約款に基づくものか否かの別）
                     ［02_industry-structure 11-2(3)］
                   ・第15条の10（指定流通機構への登録期間＝専任媒介7日／専属専任媒介5日。
                     第2項：休業日数は算入しない）
                     ［02_industry-structure 11-2(2)(3)／04 B-05］
                   ・第15条の11（指定流通機構への登録事項）［02_industry-structure 11-2(2)］
```

```
- source_title   : 賃貸住宅の管理業務等の適正化に関する法律（令和二年法律第六十号）
  organization   : e-Gov法令検索（デジタル庁）／法令所管：国土交通省
  url            : https://laws.e-gov.go.jp/law/502AC0000000060
                   （API）https://laws.e-gov.go.jp/api/1/lawdata/502AC0000000060
  published_date : 令和2年6月19日公布（取得時点の最新版）
  accessed_date  : 2026-09-17
  used_for       : ・第2条（賃貸住宅・賃貸住宅管理業・賃貸住宅管理業者・
                     特定賃貸借契約・特定転貸事業者の定義）
                     ［02_industry-structure ★賃貸住宅管理業法(1)(6)］
                   ・第3条第1項（国土交通大臣の登録。省令で定める規模未満は除く）、
                     第2項（5年ごとの更新）
                     ［01_overview 1-6／02_industry-structure ★賃貸住宅管理業法(2)］
                   ・第12条（業務管理者の選任。第1項：営業所・事務所ごとに1人以上、
                     第3項：他の営業所との兼任不可、第4項：要件）
                     ［02_industry-structure ★賃貸住宅管理業法(3)／03_company-structure 3-1］
                   ・第13条（管理受託契約の締結前の書面の交付・説明）
                     ［02_industry-structure 11-3(3)・★賃貸住宅管理業法(4)］
                   ・第16条（分別管理）
                     ［02_industry-structure 11-2(5)・★賃貸住宅管理業法(5)／04 A-12］
                   ・第20条（委託者への定期報告）の存在［02_industry-structure 11-3(3)／04 A-16］
  note           : 第20条は施行規則第13条第5号（業務管理者の職務）の中で
                   「法第20条の規定による定期報告に関する事項」として参照されていることを確認した。
                   条文本文そのものは本フェーズでは未取得。報告の具体的な時期・様式は
                   Phase B 以降で条文・省令を直接確認すること。
```

```
- source_title   : 賃貸住宅の管理業務等の適正化に関する法律施行規則
  organization   : e-Gov法令検索（デジタル庁）
  url            : https://laws.e-gov.go.jp/law/502M60000800083
                   （API）https://laws.e-gov.go.jp/api/1/lawdata/502M60000800083
  published_date : 令和2年（取得時点の最新版）
  accessed_date  : 2026-09-17
  used_for       : ・第3条（法第3条第1項の国土交通省令で定める規模＝
                     賃貸住宅管理業に係る賃貸住宅の戸数が200戸）
                     ［01_overview 1-6／02_industry-structure ★賃貸住宅管理業法(2)／
                      03_company-structure 3-1］
                   ・第13条（業務管理者の職務）［02_industry-structure ★賃貸住宅管理業法(3)］
                   ・第14条（業務管理者の要件＝管理業務に関し2年以上の実務経験を有する者で、
                     登録証明事業による証明を受けた者、または宅地建物取引士で
                     大臣指定の講習を修了した者）
                     ［02_industry-structure ★賃貸住宅管理業法(3)／03_company-structure 3-1］
                   ・第31条（管理受託契約の締結前の説明事項）
                     ［02_industry-structure ★賃貸住宅管理業法(4)］
  note           : 法令IDは e-Gov API v2 の法令一覧
                   （https://laws.e-gov.go.jp/api/2/laws?law_title=賃貸住宅）で特定した。
```

```
- source_title   : 借地借家法（平成三年法律第九十号）
  organization   : e-Gov法令検索（デジタル庁）
  url            : https://laws.e-gov.go.jp/law/403AC0000000090
                   （API）https://laws.e-gov.go.jp/api/1/lawdata/403AC0000000090
  published_date : 平成3年10月4日公布（取得時点の最新版）
  accessed_date  : 2026-09-17
  used_for       : ・第26条第1項（建物賃貸借契約の法定更新。期間満了の1年前から6月前まで）
                     ［02_industry-structure ★賃貸借(5)／04 A-17］
                   ・第28条（更新拒絶等の要件＝正当の事由）
                     ［02_industry-structure ★賃貸借(5)／04 A-13・A-17］
                   ・第32条（借賃増減請求権）［02_industry-structure ★賃貸借(5)／04 A-17］
                   ・第38条（定期建物賃貸借。第1項：書面による契約、第3項：事前の書面交付・説明、
                     第5項：説明しなかったときは定めが無効、第6項：終了通知、
                     第7項：200㎡未満の居住用建物のやむを得ない事情による解約）
                     ［02_industry-structure ★賃貸借(5)／04 A-08］
```

```
- source_title   : 民法（明治二十九年法律第八十九号）
  organization   : e-Gov法令検索（デジタル庁）
  url            : https://laws.e-gov.go.jp/law/129AC0000000089
                   （API）https://laws.e-gov.go.jp/api/1/lawdata/129AC0000000089
  published_date : 明治29年4月27日公布（取得時点の最新版）
  accessed_date  : 2026-09-17
  used_for       : ・第176条（物権の設定及び移転は意思表示のみによって効力を生ずる）
                     ［02_industry-structure 11-4］
                   ・第177条（不動産に関する物権の変動の対抗要件＝登記）
                     ［02_industry-structure 11-4／04 B-14］
                   ・第555条（売買）［04 B-08］
                   ・第557条（手付。放棄・倍額の現実の提供による解除、履行着手後は不可）
                     ［04 B-11］
                   ・第560条（権利移転の対抗要件に係る売主の義務）
                     ［02_industry-structure 11-4／04 B-14］
                   ・第601条（賃貸借の定義）［02_industry-structure ★賃貸借(1)］
                   ・第606条第1項（賃貸人による修繕義務。賃借人の責めに帰すべき事由は除く）
                     ［02_industry-structure ★賃貸借(2)／04 A-15］
                   ・第614条本文（賃料の支払時期。建物は毎月末＝後払いが原則）［04 A-09］
                   ・第621条（賃借人の原状回復義務。通常損耗・経年変化を除く）
                     ［02_industry-structure ★賃貸借(4)／04 A-20］
                   ・第622条の2（敷金の定義と返還）
                     ［02_industry-structure ★賃貸借(3)／04 A-09・A-21］
```

```
- source_title   : 不動産登記法（平成十六年法律第百二十三号）
  organization   : e-Gov法令検索（デジタル庁）
  url            : https://laws.e-gov.go.jp/law/416AC0000000123
                   （API）https://laws.e-gov.go.jp/api/1/lawdata/416AC0000000123
  published_date : 平成16年6月18日公布（取得時点の最新版）
  accessed_date  : 2026-09-17
  used_for       : ・第3条（登記することができる権利等。所有権・抵当権・賃借権 等）
                     ［02_industry-structure 11-1］
                   ・第60条（共同申請の原則）［02_industry-structure 11-1・11-4／04 B-14］
                   ・第63条（判決による登記、相続・合併による登記の単独申請）
                     ［02_industry-structure 11-4 関連］
```

```
- source_title   : 中小企業基本法（昭和三十八年法律第百五十四号）
  organization   : e-Gov法令検索（デジタル庁）
  url            : https://laws.e-gov.go.jp/law/338AC0000000154
                   （API）https://laws.e-gov.go.jp/api/1/lawdata/338AC0000000154
  published_date : 昭和38年7月20日公布（取得時点の最新版）
  accessed_date  : 2026-09-17
  used_for       : ・第2条第1項第1号〜第4号（中小企業者の範囲）、第5項（小規模企業者の定義）
                     ［01_overview 1-7］
  note           : 同条は業種を「製造業、建設業、運輸業その他の業種」「卸売業」「サービス業」
                   「小売業」と区分しているが、不動産業がどれに当たるかは条文上明示されていない。
                   本資料では条文どおりに表を示したうえで、不動産業の位置づけは【Inference】として
                   記述している。制度ごとの定義は当該制度の資料で確認すること。
```

---

## 2. 告示（国土交通省）

```
- source_title   : 宅地建物取引業者が宅地又は建物の売買等に関して受けることができる報酬の額
                   （昭和四十五年十月二十三日建設省告示第千五百五十二号）
                   最終改正：令和六年六月二十一日国土交通省告示第九百四十九号
  organization   : 国土交通省
  url            : https://www.mlit.go.jp/totikensangyo/const/content/001750229.pdf
                   （掲載ページ）https://www.mlit.go.jp/totikensangyo/const/1_6_bt_000266.html
  published_date : 昭和45年10月23日（最終改正 令和6年6月21日／令和6年7月1日施行）
  accessed_date  : 2026-09-17
  used_for       : ・第一（消費税等相当額の定義）
                   ・第二（売買・交換の媒介：200万円以下5.5%、200万円超400万円以下4.4%、
                     400万円超3.3%。依頼者の一方につき）
                     ［01_overview 1-5／02_industry-structure ★(4)／03_company-structure 3-1／
                      04 4-5］
                   ・第三（売買・交換の代理：媒介の2倍以内）［01_overview 1-5］
                   ・第四（貸借の媒介：双方合計で借賃1か月分の1.1倍以内。
                     居住用建物は承諾を得ている場合を除き一方から0.55倍以内）
                     ［01_overview 1-5／03_company-structure 3-1／04 A-09・4-4］
                   ・第五（貸借の代理：借賃1か月分の1.1倍以内）［01_overview 1-5］
                   ・第六（権利金の授受がある場合の特例。居住用建物を除く）［01_overview 1-5］
                   ・第七（低廉な空家等〈800万円以下〉の売買・交換の媒介：30万円の1.1倍まで）
                     ［01_overview 1-5］
                   ・第八（低廉な空家等の代理：第七の2倍以内）［01_overview 1-5］
                   ・第九（長期の空家等の貸借の媒介：双方合計で借賃1か月分の2.2倍まで）
                     ［01_overview 1-5］
                   ・第十（長期の空家等の貸借の代理）［01_overview 1-5］
                   ・第十一①（第二〜第十によるほか報酬を受けられない。ただし依頼者の依頼によって
                     行う広告の料金に相当する額は除く＝ADの根拠）
                     ［01_overview 1-5／02_industry-structure ★(4)／04 A-11］
                   ・第十一②（免税事業者の場合の算出方法）［01_overview 1-5 関連］
                   ・附則（令和6年6月21日告示第949号は令和6年7月1日から施行）
  note           : PDFのテキストを抽出して全文を確認した。
                   なお「代金×3％＋6万円」という速算式は告示本文には記載がなく、
                   第二の区分表から算術的に導かれるものであるため、
                   本資料では導出過程を示したうえで【Inference】として扱っている。
```

---

## 3. 国土交通省のウェブページ・資料

```
- source_title   : 建設産業・不動産業：宅地建物取引業法関係
  organization   : 国土交通省（不動産・建設経済局）
  url            : https://www.mlit.go.jp/totikensangyo/const/1_6_bt_000266.html
  published_date : 不明（ページ上に更新日の記載を確認できず）
  accessed_date  : 2026-09-17
  used_for       : ・報酬告示の正式名称・告示番号・改正履歴（令和6年6月21日国土交通省告示第949号、
                     令和6年7月1日施行）［01_overview 1-5／02_industry-structure ★(4)］
                   ・標準媒介契約約款の根拠と告示番号（平成2年1月30日建設省告示第115号、
                     最終改正 令和6年1月24日国土交通省告示第314号、令和6年4月1日施行）
                     ［02_industry-structure 11-2(3)］
                   ・宅地建物取引業法・施行令・施行規則の公布年月日と法令番号
                     ［本ファイル §1 の法令IDの裏取り］
                   ・宅地建物取引業者営業保証金規則・宅地建物取引業保証協会弁済業務保証金規則の
                     存在［02_industry-structure ★(5)関連］
```

```
- source_title   : 「原状回復をめぐるトラブルとガイドライン」（再改訂版）のダウンロード
                   および 第1章「原状回復にかかるガイドライン」
  organization   : 国土交通省（住宅局）
  url            : （ページ）https://www.mlit.go.jp/jutakukentiku/house/jutakukentiku_house_tk3_000021.html
                   （第1章 PDF）https://www.mlit.go.jp/common/000991391.pdf
                   （第2章 PDF）https://www.mlit.go.jp/common/000991392.pdf
  published_date : 再改訂版（ページ上に公表年の明示を確認できず。全173ページ）
  accessed_date  : 2026-09-17
  used_for       : ・本ガイドラインのポイント（原状回復は借りた当時の状態に戻すものではないこと、
                     経過年数を考慮して賃借人の負担を軽減する考え方）
                     ［02_industry-structure ★賃貸借(4)／04 A-20］
                   ・表2「原状回復の定義」（賃借人の居住、使用により発生した建物価値の減少のうち、
                     賃借人の故意・過失、善管注意義務違反、その他通常の使用を超えるような使用による
                     損耗・毀損を復旧すること）［02_industry-structure ★賃貸借(4)／04 A-20］
                   ・表1「建物価値の減少の考え方」の3区分
                     （①-A 経年変化／①-B 通常損耗／② 賃借人の故意・過失等）と負担の帰属
                     ［02_industry-structure ★賃貸借(4)／04 A-20］
                   ・次の入居者を確保する目的で行う設備交換・化粧直しは賃貸人が負担すべきとの考え方
                     ［04 A-20］
                   ・賃借人に特別の負担を課す特約の要件（必要性があり、暴利的でないなどの
                     客観的・合理的理由が存在すること）［04 A-20］
                   ・第2章：少額訴訟手続、裁判外紛争処理制度（ADR）、行政機関への相談
                     ［Phase B 以降で使用可能］
  note           : PDFのテキストを抽出して確認した。全文（173ページ）のうち
                   第1章・第2章を読了。Q&A・第3章（判例の動向）・参考資料は未読。
```

```
- source_title   : 賃貸住宅管理業法ポータルサイト
  organization   : 国土交通省
  url            : https://www.mlit.go.jp/tochi_fudousan_kensetsugyo/pm_portal/
  published_date : 不明（お知らせの最新は2025年12月1日）
  accessed_date  : 2026-09-17
  used_for       : ・業務管理者の配置（営業所又は事務所ごとに1名以上）の周知内容
                     ［02_industry-structure ★賃貸住宅管理業法(3)］
                   ・賃貸住宅管理業登録の制度の存在と申請経路
                     ［02_industry-structure ★賃貸住宅管理業法(2)］
```

```
- source_title   : 賃貸住宅管理業登録の方法
  organization   : 国土交通省
  url            : https://www.mlit.go.jp/tochi_fudousan_kensetsugyo/const/content/how_to_register260527.pdf
  published_date : 不明（ファイル名から2026年5月27日版と推定）
  accessed_date  : 2026-09-17
  used_for       : ・登録の有効期間が満了すると200戸以上の賃貸住宅管理業を行えなくなる旨
                     ［02_industry-structure ★賃貸住宅管理業法(2) の補強］
  note           : PDFからテキストを抽出したが、フォントの都合で一部の文字が欠落した。
                   200戸という数値自体は施行規則第3条（§1）で条文から確認済みであり、
                   本資料の記述は条文に依拠している。
```

```
- source_title   : 建設産業・不動産業：不動産業（トップページ）／宅地建物取引業
  organization   : 国土交通省（不動産・建設経済局）
  url            : https://www.mlit.go.jp/totikensangyo/const/1_6_bt_000246.html
                   https://www.mlit.go.jp/totikensangyo/const/1_6_bf_000009.html
  published_date : 不明
  accessed_date  : 2026-09-17
  used_for       : ・不動産業に関する国土交通省の所管領域の全体像
                     （宅地建物取引業／賃貸住宅管理業／マンション管理業／住宅宿泊管理業 等）の把握
                     ［02_industry-structure 11-1 のプレイヤー整理］
                   ・「宅地建物取引業者 企業情報検索システム」の存在
                     ［03_company-structure 3-1］
```

```
- source_title   : 日本標準産業分類（大分類K 不動産業，物品賃貸業）
  organization   : 総務省
  url            : https://www.soumu.go.jp/toukei_toukatsu/index/seido/sangyo/02toukatsu01_03000044.html
  published_date : 不明（ページ上に改定年の明示を確認できず）
  accessed_date  : 2026-09-17
  used_for       : ・大分類K 不動産業，物品賃貸業の構成
                     （中分類68 不動産取引業／69 不動産賃貸業・管理業／70 物品賃貸業）
                   ・小分類の内訳
                     （681 建物売買業，土地売買業／682 不動産代理業・仲介業／
                      691 不動産賃貸業〈貸家業，貸間業を除く〉／692 貸家業，貸間業／
                      693 駐車場業／694 不動産管理業）
                     ［01_overview 1-1・1-6］
```

---

## 4. 統計（不動産業統計集および原資料）

本フェーズでは、国土交通省・総務省・財務省の統計を**（公財）不動産流通推進センター「2026 不動産業統計集」
（3月期改訂）**に集約されたかたちで確認しました。同統計集は各表に原資料を明記しており、
本資料では**原資料名と統計集の両方を併記**しています。

```
- source_title   : 2026 不動産業統計集（3月期改訂）
                   [1] 不動産業の概況 ／ [3] 不動産流通 ／ [4] 不動産賃貸 ／ [5] 不動産管理
  organization   : 公益財団法人 不動産流通推進センター
  url            : （目次ページ）https://www.retpc.jp/chosa/tokei/
                   [1] https://www.retpc.jp/wp-content/uploads/toukei/202603/202603_1gaikyo.pdf
                   [3] https://www.retpc.jp/wp-content/uploads/toukei/202603/202603_3ryutsu.pdf
                   [4] https://www.retpc.jp/wp-content/uploads/toukei/202603/202603_4chintai.pdf
                   [5] https://www.retpc.jp/wp-content/uploads/toukei/202603/202603_5kanri.pdf
  published_date : 2026年3月期改訂
  accessed_date  : 2026-09-17
  used_for       : 下記の各表（原資料は表ごとに記載）
  note           : PDFからテキストと座標を抽出して表を復元した。
                   「本統計集に掲載されているデータの正確性については万全を期しているが、
                   何らかの理由により誤りがある可能性がある」旨が同統計集に明記されている。
                   Phase B 以降で重要な数値を再掲する場合は、可能な限り原資料に当たること。
```

### 4-1 事業所数・従業者数

```
- source_title   : 令和6年経済センサス‐基礎調査結果
  organization   : 総務省
  url            : （本プロジェクトでは（公財）不動産流通推進センター「2026 不動産業統計集」[1] 経由で確認）
                   https://www.retpc.jp/wp-content/uploads/toukei/202603/202603_1gaikyo.pdf
  published_date : 調査基準日＝2024年（令和6年）6月1日
  accessed_date  : 2026-09-17
  used_for       : ・不動産業の民営事業所数 250,462事業所、従業者数 1,150,413人、
                     1事業所あたり平均従業者数 4.6人（全産業 4,023,941事業所／56,285,043人／14.0人）
                     ［01_overview 1-1・1-7］
                   ・不動産業の業態別内訳（事業所数・構成比・従業者数・構成比・1事業所あたり人数）
                     貸家業，貸間業 95,114／38.0%／273,631人／23.8%／2.9人
                     不動産賃貸業（貸家業・貸間業を除く）48,973／19.6%／228,546人／19.9%／4.7人
                     不動産代理業・仲介業 41,093／16.4%／200,733人／17.4%／4.9人
                     不動産管理業 35,917／14.3%／256,022人／22.3%／7.1人
                     建物売買業，土地売買業 19,597／7.8%／142,563人／12.4%／7.3人
                     その他 9,768／3.9%／48,918人／4.3%／5.0人
                     ［01_overview 1-1・1-6］
                   ・従業者規模別事業所数（不動産業）
                     1〜4人 204,702（81.7%）／5〜9人 28,789（11.5%）／10人以上 15,430（6.2%）／
                     0人〈出向・派遣従業者のみ、等〉1,541（0.6%）／総数 250,462
                     （全産業：1〜4人 1,893,344／5〜9人 898,472／10人以上 1,205,872／
                      0人 26,253／総数 4,023,941）
                     ［01_overview 1-7／03_company-structure 3-1］
  note           : 原統計の注記として、令和6年調査では出向・派遣従業者を
                   出向元・派遣元事業所の従業員数に含めることとなったため、
                   以前の同調査と分類の枠組みが異なる旨が示されている。
                   また不動産業は「不動産取引業」と「不動産賃貸業・管理業」の計である。
```

### 4-2 宅地建物取引業者数・宅地建物取引士

```
- source_title   : 宅地建物取引業法の施行状況調査結果について
  organization   : 国土交通省
  url            : （本プロジェクトでは（公財）不動産流通推進センター「2026 不動産業統計集」[1] 経由で確認）
                   https://www.retpc.jp/wp-content/uploads/toukei/202603/202603_1gaikyo.pdf
  published_date : 令和6年度末（2025年〈令和7年〉3月31日現在）の数値
  accessed_date  : 2026-09-17
  used_for       : ・宅地建物取引業者数 132,291業者
                     （大臣免許 3,158〈法人3,156・個人2〉／知事免許 129,133〈法人116,746・個人12,387〉、
                      法人計 119,902／個人計 12,389）
                     ［01_overview 1-1・1-7／03_company-structure 3-1］
                   ・宅地建物取引業者数の推移（平成19年度〜令和6年度）
                     ［01_overview 1-1 の傾向記述］
                   ・宅地建物取引士の年度末登録者数 1,211,760人、
                     年度間の新規登録者数 30,336人（いずれも令和6年度）
                     ［01_overview 1-1］
  note           : 統計集の注記により、いずれも年度末の数字。
                   国土交通省の原報道発表ページのURLは本フェーズでは特定できなかった。
                   Phase B 以降で原典URLを確認して追記すること。
```

### 4-3 法人数・売上高・経常利益

```
- source_title   : 法人企業統計調査
  organization   : 財務省財務総合政策研究所
                   （令和4年度までは財務省「財政金融統計月報」－法人企業統計年報特集－）
  url            : （本プロジェクトでは（公財）不動産流通推進センター「2026 不動産業統計集」[1] 経由で確認）
                   https://www.retpc.jp/wp-content/uploads/toukei/202603/202603_1gaikyo.pdf
  published_date : 令和6年度（2024年度）の数値
  accessed_date  : 2026-09-17
  used_for       : ・不動産業の法人数 392,110社（令和6年度）、対前年増加率1.8%、
                     全産業に占める比率12.9%［01_overview 1-1］
                   ・不動産業の売上高 58.8兆円（令和6年度、対前年度＋4.2%）、
                     経常利益 8.0兆円（同＋8.7%）
                     （全産業 売上高1,692.4兆円／経常利益114.7兆円）［01_overview 1-1］
  note           : 原統計の注記により「全産業には金融業・保険業を含まない」。
```

### 4-4 指定流通機構（レインズ）

```
- source_title   : 指定流通機構の活用状況について
  organization   : 公益財団法人 不動産流通推進センター
  url            : （本プロジェクトでは同センター「2026 不動産業統計集」[3] 経由で確認）
                   https://www.retpc.jp/wp-content/uploads/toukei/202603/202603_3ryutsu.pdf
  published_date : 令和6年度（2024年度）の数値
  accessed_date  : 2026-09-17
  used_for       : ・売り物件 新規登録件数 総数 1,453,399件（令和6年度）
                     取引態様別：専任媒介 492,782／一般媒介 301,227／専属専任媒介 137,834／
                     売主 498,548／代理 23,008
                     ［02_industry-structure 11-2(2)］
                   ・売り物件 成約報告件数 総数 205,522件（令和6年度）
                     ［02_industry-structure 11-2(2)］
  note           : 原統計の注記により、平成31年3月から新規登録件数の収集方法が変更されている。
                   また中国・四国・九州について平成31年4月〜令和3年12月の数値と
                   令和4年1月以降の数値に連続性がない旨の注記がある。
                   本資料では令和6年度の単年の数値のみを引用しており、時系列比較は行っていない。
```

### 4-5 借家戸数

```
- source_title   : 住宅・土地統計調査
  organization   : 総務省統計局
  url            : （本プロジェクトでは（公財）不動産流通推進センター「2026 不動産業統計集」[4] 経由で確認）
                   https://www.retpc.jp/wp-content/uploads/toukei/202603/202603_4chintai.pdf
  published_date : 令和5年（2023年）の数値
  accessed_date  : 2026-09-17
  used_for       : ・民営借家 1,568万戸（全住宅ストックに占める割合28.2%）
                   ・公営・都市再生機構・公社借家 248万戸（同4.4%）
                     ［01_overview 1-1］
```

---

## 5. 本プロジェクト内の共通資料

```
- source_title   : common/base-statistics.md
  organization   : 本プロジェクト（原資料：中小企業庁「中小企業の企業数・事業者数」、
                   総務省・経済産業省「令和3年経済センサス‐活動調査」再編加工）
  url            : https://www.chusho.meti.go.jp/koukai/chousa/chu_kigyocnt/index.html
  published_date : 2023年12月13日公表／データは2021年6月1日時点
  accessed_date  : 2026-09-16（base-statistics.md 作成時）
  used_for       : ・「不動産業，物品賃貸業」の中小企業324,197社・大企業347社・合計324,544社
                     ［01_overview 1-1 の統計上の注意］
  note           : この区分には物品賃貸業（リース業・レンタル業）が含まれ、
                   不動産業単独の数値ではない。本資料ではその旨を明記したうえで引用している。
```

---

## 6. 所在の確認のみで、内容を読めていない資料

**以下は本文の根拠としては使用していません。** Phase B 以降で内容を確認する際の入口として記録します。

| 資料名 | 発行元 | URL | 状況 |
|---|---|---|---|
| 宅地建物取引業法施行規則の規定による標準媒介契約約款（平成2年1月30日建設省告示第115号／最終改正 令和6年1月24日国土交通省告示第314号） | 国土交通省 | https://www.mlit.go.jp/totikensangyo/const/content/001723420.pdf | **所在確認のみ**。告示番号・改正日は掲載ページのHTMLから確認したが、約款本文は未読 |
| 宅地建物取引業者の違反行為に対する監督処分の基準 | 国土交通省 | https://www.mlit.go.jp/totikensangyo/const/1_6_bt_000266.html 内のリンク | **所在確認のみ** |
| 宅地建物取引業法の解釈・運用の考え方 | 国土交通省 | https://www.mlit.go.jp/totikensangyo/const/1_6_bt_000266.html 内のリンク | **所在確認のみ**。Phase B の法規制・商習慣の記述で参照すべき重要資料 |
| ITを活用した重要事項説明及び書面の電子化について | 国土交通省 | http://www.mlit.go.jp/totikensangyo/const/sosei_const_tk3_000092.html | **所在確認のみ**（リンクのタイトルのみ確認）。04 A-07 で「ページが設けられている」旨のみ記述 |
| 宅地建物取引業者 企業情報検索システム | 国土交通省 | https://etsuran2.mlit.go.jp/TAKKEN/ | **所在確認のみ**（リンクのタイトルとURLのみ確認） |
| 宅地建物取引業者による人の死の告知に関するガイドライン | 国土交通省 | https://www.mlit.go.jp/tochi_fudousan_kensetsugyo/const/tochi_fudousan_kensetsugyo_const_tk3_000001_00061.html | **所在確認のみ**。Phase B の重要事項説明・商習慣で参照候補 |
| 不動産業ビジョン2030 | 国土交通省 | https://www.mlit.go.jp/report/press/totikensangyo16_hh_000190.html | **所在確認のみ**。※本プロジェクトは提案資料ではないため、施策的な記述の引用には注意 |
| 賃貸住宅の管理業務等の適正化に関する法律 第20条（委託者への定期報告）の条文本文 | e-Gov法令検索 | https://laws.e-gov.go.jp/law/502AC0000000060 | **未取得**。施行規則第13条第5号からの参照で存在を確認したのみ |
| 原状回復をめぐるトラブルとガイドライン（再改訂版）Q&A・第3章（判例の動向）・参考資料 | 国土交通省 | https://www.mlit.go.jp/jutakukentiku/house/jutakukentiku_house_tk3_000021.html | **未読**（第1章・第2章のみ読了） |
| 2026 不動産業統計集 [2] 不動産開発／[6] 土地／[7] 人口／[8] 経済 | （公財）不動産流通推進センター | https://www.retpc.jp/chosa/tokei/ | **未取得**（[1][3][4][5] のみ取得） |

---

## 7. 本フェーズの調査上の記録（Phase B 以降への申し送り）

| 事項 | 内容 |
|---|---|
| **法令の取得** | e-Gov法令API（`https://laws.e-gov.go.jp/api/1/lawdata/<法令ID>`）から素の curl で条文本文を取得できた。宅地建物取引業法は条文で確認すべき事項が多く、検索要約に頼らず条文で裏取りした |
| **法令IDの特定** | 法令IDが分からない場合、`https://laws.e-gov.go.jp/api/2/laws?law_title=<キーワード>` で法令名から法令IDを一覧取得できた（賃貸住宅管理業法施行規則 `502M60000800083` はこれで特定） |
| **官公庁サイトの取得** | mlit.go.jp・soumu.go.jp は `curl` にブラウザUser-Agentを付けて200で取得できた（`common/base-statistics.md` §3 のとおり） |
| **PDFの読み取り** | `common/base-statistics.md` §5 は「PDFのテキスト抽出手段がない」としているが、**本フェーズでは Python 標準ライブラリ（re・zlib）だけでPDFのテキストを抽出できた**。手順：(1) `N 0 obj ... endobj` でオブジェクトを収集、(2) `/Type /ObjStm` のストリームを zlib 展開して中のオブジェクトも展開（PDF 1.5以降は必須）、(3) `/ToUnicode` CMap を `beginbfchar`/`beginbfrange` から解析、(4) コンテンツストリームの `Tf`/`Tm`/`Td`/`TJ`/`Tj` を走査して文字コードを Unicode に変換。数値のセルは `/Encoding /WinAnsiEncoding` の単純フォントで `(1,234)Tj` の形になっているため、**リテラル文字列 `( )` も latin1 として拾う必要がある**。`Tm`/`Td` の座標でY座標ごとに行をまとめ、X座標で並べ替えると**表を復元できる**。これにより報酬告示の全文・原状回復ガイドライン・不動産業統計集の統計表を一次資料として読むことができた |
| **WebSearch** | 本セッション開始時点で既にセッション上限（200回）に達しており、一度も使用できなかった。すべて curl / WebFetch と e-Gov API で調査した |
| **未解決** | 国土交通省「宅地建物取引業法の施行状況調査結果について」の原報道発表ページのURLを特定できなかった（不動産流通推進センターの統計集経由で数値を確認した） |
