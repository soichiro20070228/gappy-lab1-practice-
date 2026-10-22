# confirmation.pyから、自分で作った判定関数を読み込む
from confirmation import classify_confirmation

# テスト用の予約データを作成する
record = {
    "booking_version": 7,
    "reply_version": 7,
    "reply": "confirmed",
    "evidence_id": " " * 100,  # 空白100個
    "needs_approval": False,
    "cancelled": False,
    "deadline_passed": False
}

# 空白しかないEvidence IDはREVIEWになるべき
assert classify_confirmation(record) == "REVIEW"

# テストに合格した場合だけ表示される
print("Red test: PASS")
