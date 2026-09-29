def summarise_amounts(raw_values):
    total = 0
    rejected = 0
    for raw in raw_values:
        try:
            if int(raw) >= 0:
               total += int(raw)
        except:
           rejected = rejected + 1
    return {"total": total, "rejected": 0}
print(summarise_amounts(["10", " 5 ", "bad", "-3", "0", ""]))



