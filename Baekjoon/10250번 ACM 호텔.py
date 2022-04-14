T = int(input())
for _ in range(T):
    H, W, N= map(int, input().split())
    room = (N-1) // H
    floor = (N-1) % H
    if room+1 >= 10:
        print(str(floor+1)+str(room+1))
    else:
        print(str(floor+1)+'0'+str(room+1))