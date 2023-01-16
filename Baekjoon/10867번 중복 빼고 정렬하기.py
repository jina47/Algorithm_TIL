N = int(input())
numbers = list(map(int, input().split()))
numbers = list(set(numbers))
numbers.sort()
for num in numbers:
    print(num, end= ' ')