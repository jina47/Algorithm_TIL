# 입력 A, B
A, B = map(int, input().split())

cnt = 0
while A != B:
    # B의 끝 숫자가 1이면 제거
    if str(B)[-1] == '1':
        B = int(str(B)[:-1])
        cnt += 1
    # B가 2로 나눠지면 나누기
    elif B % 2 == 0:
        B //= 2
        cnt += 1
    # 위의 두 경우가 아니면 cnt = -1
    else:
        cnt = -1
        break
    
    # A와 B가 같으면 cnt += 1, B가 A보다 작아지면 cnt = -1
    if A == B:
        cnt += 1
        break
    elif A > B:
        cnt = -1
        break

# 출력
print(cnt)
    