
N, K = map(int, input().split())

people = [i for i in range(1, N+1)]
answer = []
while people:
    if len(people) > K-1 :
        answer.append(people.pop(K-1))
        people = people[K-1:] + people[:K-1]
    else:
        for _ in range(K-1):
            people.append(people.pop(0))
        answer.append(people.pop(0))

print('<'+ ', '.join(map(str, answer)) + '>')
        
        

