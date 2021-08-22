def bin_num(number):
    bin_num = []
    while number != 1:
        bin_num.append(number % 2)
        number = number // 2
    bin_num.append(1)
    return bin_num

def solution(numbers):
    answer =[]
    for number in numbers:
        if number % 2 == 0:
            answer.append(number+1)
            continue
        bin = bin_num(number)
        if 0 not in bin:
            bin.insert(-1, 0)
        else:
            j = 1
            while bin[j] != 0:
                j += 1
            bin[j] = 1
            bin[j-1] = 0
        dif = 0
        for i, b in enumerate(bin):
            dif += b * (2**i)
        answer.append(dif) 
    return answer
