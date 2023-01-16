import sys
from heapq import *

N = int(sys.stdin.readline())
left, right = [], []

for i in range(N):
    num = int(sys.stdin.readline())
    # 맨 처음 숫자는 바로 중간값
    if i == 0:
        mid = num
    # 외친 숫자의 개수가 짝수개일 때
    elif i%2 != 0:
        # 새로 외친 숫자가 mid보다 크면 right에 넣어줌
        if mid <= num:
            heappush(right, num)
        # 새로 외친 숫자가 mid보다 작으면 mid 갱신
        else:
            heappush(right, mid)
            # left에서 mid를 꺼낼 때 최소 힙이므로 음수로 넣어주고 뺌
            heappush(left, -num)
            mid = -heappop(left)
    # 외친 숫자의 개수가 홀수개일 때
    else:
        # 새로 외친 숫자가 mid보다 작으면 left에 넣어줌
        if mid >= num:
            heappush(left, -num)
        # 새로 외친 숫자가 mid보다 크면 mid 갱신
        else:
            heappush(left, -mid)
            heappush(right, num)
            mid = heappop(right)

    print(mid)
    
        
        

