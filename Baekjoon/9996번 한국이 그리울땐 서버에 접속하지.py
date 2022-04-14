import sys

# 파일의 개수 N, 패턴 P, 문자열 S
N = int(input())
P = sys.stdin.readline()

# P를 '*' 기준으로 split
left, right = P.split('*')

for i in range(N):
    S = sys.stdin.readline()
    
    # S가 left로 시작하지 않으면 "NE" 출력
    if S.startswith(left):
        # S의 left 길이 뒤부터 탐색해서 right로 끝나면 "DA" 아니면 "NE"
        if S[len(left):].endswith(right):
            print("DA")
        else:
            print("NE")
    else:
        print("NE")
    