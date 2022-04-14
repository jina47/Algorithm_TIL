import sys

while True:
    N, M = map(int, sys.stdin.readline().split())
    if (N, M) == (0,0):
        break
    else:
        if N % M == 0:
            print('multiple')
        elif M % N == 0:
            print('factor')
        else:
            print('neither')
