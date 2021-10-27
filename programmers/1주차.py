def solution(price, money, count):
    totalprice = price * count * (count + 1) / 2
    if totalprice >= money :
        return totalprice - money
    else:
        return 0