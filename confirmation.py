def classify_confirmation(record: dict) -> str:
    """上の仕様に従い、READY / WAITING / REVIEW / BLOCKED のどれかを返す。"""
    # TODO: 自分またはAIと協力して実装。必ず上記の優先順位を守る。
    if record["cancelled"]:
      return "BLOCKED"
    elif record["needs_approval"]:
      return "REVIEW"
    elif record["reply"]=="confirmed":

      if (record["reply_version"]==record["booking_version"] and record["evidence_id"] is not None and record["evidence_id"].strip()!=""):
        return "READY"

      else: return "REVIEW"




    elif record["reply"]=="pending":

      if record["deadline_passed"]==False:
        return "WAITING"
      else:
        return "REVIEW"


    elif record["reply"]=="declined" or record["reply"]=="ambiguous":
      return "REVIEW"

    else : return "REVIEW"


    raise NotImplementedError("ここに実装してください")
