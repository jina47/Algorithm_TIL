import sys

# 회원수 N
N = int(input())

# 회원 나이와 이름 리스트로 담기
people = []
idx = 0
for _ in range(N):
    age, name = sys.stdin.readline().strip().split()
    age = int(age)
    people.append([idx, age, name])
    idx += 1

sorting = sorted(people, key=lambda x: (x[1], x[0]))

for [idx, age, name] in sorting:
    print(age, name)
