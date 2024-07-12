# Google Calendar を Raspberry Pi Pico W と e-paer で表示する

## 準備

### 必要なもの

- [Raspberry Pi Pico WH — スイッチサイエンス](https://www.switch-science.com/products/8172?_pos=1&_sid=5aa1a1afe&_ss=r)

- [Raspberry Pi Pico用 2.13インチ e-Paper ディスプレイ（白黒赤）212×104 — スイッチサイエンス](https://www.switch-science.com/products/7322)


### あるといいもの

microBタイプのケーブルがなければ注文。また、電池式のモバイルバッテリーで給電すると使い勝手もよく便利だった。

- [USBケーブル（C-microBタイプ）50cm — スイッチサイエンス](https://www.switch-science.com/products/7965?variant=42382193950918)
- [Amazon.co.jp: エレコム エコ USBケーブル 2.0 A-microB 0.15m U2C-JAMB015BK : パソコン・周辺機器](https://www.amazon.co.jp/gp/product/B00XKB9UM0/ref=ppx_yo_dt_b_search_asin_title?psc=1)
- [Amazon | エレコム モバイルバッテリー 乾電池式 単3電池×4本付属 Type-A×1 ホワイト DE-KD01WH | エレコム(ELECOM) | 乾電池](https://www.amazon.co.jp/gp/product/B09C1NTR46/ref=ppx_yo_dt_b_search_asin_title?th=1)


## 追加するコード

日本語フォント（16pxのみ）。設置方法などは以下を参照。
[Raspberry Pi Pico W で e-paper に日本語を表示する その2（大きめのフォント表示） #micropython - Qiita](https://qiita.com/kenji0302/items/8da4c075dff974d1dc6f)


https://github.com/waveshareteam/Pico_ePaper_Code/blob/main/python/Pico_ePaper-2.13_V4.py をダウンロード。 `EPD_2in13_B_V4_Portrait.py` として設置。

## 要編集ファイル

- index.php
- secret.py

