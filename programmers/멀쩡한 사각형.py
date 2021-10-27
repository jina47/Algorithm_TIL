import math

def solution(w,h):

    # 선이 지나가는 사각형
    # (w와 h의 최대공약수로 나눈 약수의 합 - 1) * 최대공약수
    # (w + h - gcd) 로 정리 가능

    gcd = math.gcd(w, h)
    rect = w + h - gcd

    return w*h - rect 