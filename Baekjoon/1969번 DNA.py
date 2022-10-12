# 입력
N, M = map(int, input().split())
dna = []
for _ in range(N):
    dna.append(input())

# 매 인덱스마다 가장 많은 글자 answer에 추가 (같은 수가 있다면 사전 순으로 앞선 글자)
answer = ''
hamming = 0
for i in range(M):
    # A, C, G, T 개수 담는 temp
    temp = [0, 0, 0, 0]
    for j in range(N):
        if dna[j][i] == 'A':
            temp[0] += 1
        elif dna[j][i] == 'C':
            temp[1] += 1
        elif dna[j][i] == 'G':
            temp[2] += 1
        elif dna[j][i] == 'T':
            temp[3] += 1
    # temp 최댓값 인덱스 idx
    idx = temp.index(max(temp))
    if idx == 0:
        answer += 'A'
    elif idx == 1:
        answer += 'C'
    elif idx == 2:
        answer += 'G'
    elif idx == 3:
        answer += 'T'
    # answer에 더해준 글자가 아닌 개수 hamming에 더하기
    hamming += (sum(temp)-temp[idx])

# answer, hamming 출력
print(answer)
print(hamming)




