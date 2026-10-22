# Gappy Lab 1 Practice

予約確認の完了状態を判定するPythonプログラムの練習用リポジトリ。

## ファイル構成

- `confirmation.py`：READY / WAITING / REVIEW / BLOCKEDを判定する関数
- `test_confirmation.py`：空白のみのEvidence IDに対する反例テスト

## テスト実行方法

Python 3を使用する。

2つのPythonファイルがあるディレクトリで次のコマンドを実行する。

`python test_confirmation.py`

`AssertionError`が発生しなければ、このテストはPASS。

## 修正前の検証結果（Red）

最初の実装では、Evidence IDが`None`または空文字列でないことを確認していた。

既存の12件のテストはすべてPASSした。

しかし、追加の組合せテストで以下の問題を発見した。

- テスト総数：128通り
- 不正なREADY判定：**1件**
- 反例：`evidence_id=" " * 100`
- 期待結果：`REVIEW`
- 実際の結果：`READY`

この反例に対する`assert`で`AssertionError`が発生することを確認した。

## 修正内容

Evidence IDの判定に`.strip()`を追加した。

修正前：

`record["evidence_id"] != ""`

修正後：

`record["evidence_id"].strip() != ""`

これにより、空白文字のみのEvidence IDを無効とする。

なお、空白のみの文字列を無効とすることは、元の演習仕様に対する追加の安全条件である。

## 修正後の検証結果（Green）

- 空白100個の反例テスト：**PASS**
- 既存12件のテスト：**12/12 PASS**
- 組合せテスト：**128通り**
- 不正なREADY判定：**0件**

修正前に発見した反例が解消され、既存12件の判定結果も維持されていることを確認した。

追加検証はGoogle Colabの別ノートブックで実施した。

## 制約・残課題

- 128通りの検証は選択した入力の組合せについての結果であり、すべての入力を網羅した証明ではない。
