import sys

# 입력값 N와 K
N, K = map(int,input().split())

# 숫자 데이터 data에 입력
data = list(map(int, sys.stdin.readline().split()))

# 병합 정렬 이용
def mergesort(data):
    if len(data) <= 1:
        return data
    
    i = len(data) //2
    left = data[:i]
    right = data[i:]

    l = mergesort(left)
    r = mergesort(right)

    mergelst = []
    i, j = 0, 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            mergelst.append(l[i])
            i += 1
        else:
            mergelst.append(r[j])
            j += 1
    
    if i == len(l):
        for j in range(j, len(r)):
            mergelst.append(r[j])
    
    if j == len(r):
        for i in range(i, len(l)):
            mergelst.append(l[i])

    return mergelst

print(mergesort(data)[K-1])





# # 퀵 정렬을 이용하여 오름차순 정렬
# ## 기준값을 정하고 기준값보다 작은 값을 왼쪽 리스트, 기준값보다 큰 값을 오른쪽 리스트로 정렬
# ## 왼쪽 리스트 오른쪽 리스트를 1개 값만 가질 때까지 반복

# def quicksort(data, K):
#     # data 값이 1개라면 return
#     if len(data) <= 1:
#         return data[0]
    
#     # data 값이 2개 이상이면 정렬
#     else:
#         # 기준값을 pivot으로 설정
#         i = len(data)//2 
#         pivot = data[i]

#         # 숫자들을 나누어 담을 리스트 설정
#         left = []
#         equal = []
#         right = []
        
#         for num in data:
#             # pivot보다 작으면 left에 저장
#             if num < pivot:
#                 left.append(num)
#             # pivot보다 크면 right에 저장
#             elif num > pivot:
#                 right.append(num)
#             # pivot과 같은 값이면 equal에 저장
#             else:
#                 equal.append(num)
        
#         if K < len(left):
#             return quicksort(left, K)
#         elif K < len(left) + len(equal):
#             return equal[0]
#         else:
#             return quicksort(right, K-len(left)-len(equal))


# # data를 퀵정렬한 결과를 answer에 저장
# answer = quicksort(data, K-1)
# # 원하는 값 answer[K]를 출력
# print(answer)
