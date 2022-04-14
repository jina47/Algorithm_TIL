n = int(input()) # 입력 데이터 수
disk_num = input().split()
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
disk = [a,b,c]
# for i in range(n):
#     if i+1 in a:
#         print(1)
#     elif i+1 in b :
#         print(2)
#     else:
#         print(3)
if n in a:
    print(1)
elif n in b:
    print(2)
else:
    print(3)
    

