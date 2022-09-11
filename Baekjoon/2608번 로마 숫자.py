# 입력
x = input()
y = input()

# 숫자로 바꾸기
def ToNum(strings):
    tonum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV':4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM' : 900}
    i = 0
    answer = 0
    while True:
        if i == len(strings)-1:
            answer += tonum[strings[i]]
            break
        elif i >= len(strings):
            break
        if tonum[strings[i]] < tonum[strings[i+1]]:
            answer += tonum[strings[i]+strings[i+1]]
            i += 2
        else:
            answer += tonum[strings[i]]
            i += 1
    return answer

# 로마 기호로 바꾸기
def ToRoman(number):
    toroman = {1 :'I', 5: 'V', 10 :'X', 50 :'L', 100: 'C', 500 :'D', 1000 :'M', 4: 'IV', 9 :'IX', 40 :'XL', 90 : 'XC', 400 :'CD', 900 :'CM'}
    rev = str(number)[::-1]
    answer = ''
    for i, r in enumerate(rev):
        num = int(r)*10**i
        while num > 0:
            if num in toroman.keys():
                answer = toroman[num] + answer
                num -= num
            else:
                answer = toroman[10**i] + answer
                num -= 10**i
    return answer

# 숫자로 바꿔서 더해준 후 출력
total = ToNum(x) + ToNum(y)
print(total)
# 로마 기호로 출력        
print(ToRoman(total))
