n = int(input())
lst = []
for _ in range(n):
    name, dd, mm, yyyy = input().split()
    if len(dd) == 1:
        dd = '0' + dd
    if len(mm) == 1:
        mm = '0' + mm
    lst.append([int(yyyy+mm+dd), name])
lst.sort()

print(lst[n-1][1])
print(lst[0][1])