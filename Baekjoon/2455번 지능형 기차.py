people = []
for i in range(4):
    down, up = map(int, input().split())
    if i == 0:
        people.append(up)
    else:
        people.append(people[i-1]-down+up)
print(max(people))
