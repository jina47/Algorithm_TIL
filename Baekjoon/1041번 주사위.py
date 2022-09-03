N = int(input())
numbers = list(map(int, input().split()))

# N이 2 이상일 때
if N >= 2:
    # 정육면체 면적의 최솟값
    # (N-2)*(N-2)*5 -> 1면 (numbers 최솟값)
    # (N-2)*4 -> 1면 (numbers 최솟값)
    # (N-2)*4*2 -> 2면 (AF, BE, CD 제외 붙어있는 두 면 최솟값)
    # 4 -> 3면 (ADE, ABD, ABC, ACE, FBD, FED, FBC, FCE 중 최솟값)
    # 4 -> 2면 (AF, BE, CD 제외 붙어있는 두 면 최솟값)

    answer = 0
    # 1면
    answer += ((N-2)*(N-2)*5 + (N-2)*4) * min(numbers)
    # 2면
    temp = []
    for i in range(6):
        for j in range(i+1, 6):
            if i == 0 and j == 5: # AF
                pass
            elif i == 1 and j == 4: # BE
                pass
            elif i == 2 and j == 3: # CD
                pass
            else:
                temp.append(numbers[i]+numbers[j])
    answer += ((N-2)*4*2 + 4) * min(temp)   
    # 3면
    temp = min([numbers[0]+numbers[3]+numbers[4], numbers[0]+numbers[1]+numbers[3], numbers[0]+numbers[1]+numbers[2], numbers[0]+numbers[2]+numbers[4],
            numbers[5]+numbers[3]+numbers[4], numbers[5]+numbers[1]+numbers[3], numbers[5]+numbers[1]+numbers[2], numbers[5]+numbers[2]+numbers[4]])
    answer += 4 * temp     

# N이 1일 때 맨 아래에 최댓값을 두면 됨
else:
    answer = sum(numbers) - max(numbers)


# 출력
print(answer)