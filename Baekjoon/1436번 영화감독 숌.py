# 입력값 N
N = int(input())

movie = []
i = 1
while len(movie) < N:
    if '666' in str(i):
        movie.append(i)
    i += 1

print(movie[N-1])