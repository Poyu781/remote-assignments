def avg(data):
    sum = 0
    amount = len(data["products"])
    for i in range(amount):
        sum += data["products"][i]["price"]
    avg = sum/amount
    return round(avg,3)