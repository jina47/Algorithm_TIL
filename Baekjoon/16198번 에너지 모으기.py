answer = []
def findMax(W, energy):
    # W 길이가 2이면 answer에 energy 추가
    if len(W) == 2:
        answer.append(energy)
        return
    # W의 첫 번째와 마지막 에너지 구슬 빼고 하나 고르기 
    for x in range(1, len(W)-1):
        # x를 골랐을 때 W[x-1]*W[x+1] 에너지를 모을 수 있음
        new_energy = energy + (W[x-1] * W[x+1])
        # x를 제거한 새로운 리스트 new_W
        new_W = W[:x] + W[x+1:]
        # 새로운 리스트와 새로운 에너지로 함수 실행
        findMax(new_W, new_energy)


#입력
N = int(input())
weights = list(map(int, input().split()))

# 초기 무게 리스트와 에너지 0을 입력값으로 하는 findMax 함수 실행
findMax(weights, 0)
print(max(answer))