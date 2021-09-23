def solution(brown, yellow):
    answer = []
    ls = []

    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            ls += [[i, int(yellow / i)]]
            
    for j in ls:
        if (brown-(2*j[0]))%(j[1]+2) == 0:
            answer = [j[1]+2, j[0]+2]
            break

    return answer