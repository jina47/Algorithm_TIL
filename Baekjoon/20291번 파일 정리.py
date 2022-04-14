import sys

# 파일의 개수 N
N = int(input())

files = {}
for _ in range(N):
    filename = sys.stdin.readline()
    _, exten = filename.strip().split('.')
    # 확장자가 딕셔너리에 존재하면 value += 1, 없으면 넣어주기
    if exten not in files.keys():
        files[exten] = 1
    else:
        files[exten] += 1
    
# 키 값 순서대로 정렬해서 출력
lst = sorted(files.items())
for l in lst:
    n, cnt = l
    print(n, cnt)