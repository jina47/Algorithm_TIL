# 입력값의 각 자리수를 담는 리스트 N
N = [int(s) for s in str(input())]

# N을 내림차순 정렬
N.sort(reverse=True)

# 원하는 수 출력
print(int(''.join(map(str,N))))
