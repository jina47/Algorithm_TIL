# 별찍는 함수 만들기
def square(number):

    # number가 1일 떼 
    if number == 1:
        star = ['*']
        return star
    
    # number가 2일 때
    elif number == 2:
        star = ['*****', '*   *', '* * *', '*   *', '*****']
        return star

    # number가 3 이상일 때
    else:
        # 리스트 star의 길이는 number*4-3
        star = [''] * (number*4-3)
        
        for i, s in enumerate(square(number-1)):
            # square(number-1)의 가운데 값을 4개 추가하는 규칙이 있음
            # 인덱스가 짝수면 '*'을 4개 추가
            # 인덱스가 홀수면 ' '을 4개 추가
            if i % 2 == 0:
                if i <= (number-2)*2:
                    star[i] = s[:(number-2)*2+1] + '***' + s[(number-2)*2:]
                if i >= (number-2)*2:
                    star[i+4] = s[:(number-2)*2+1] + '***' + s[(number-2)*2:]
            else:
                if i <= (number-2)*2:
                    star[i] = s[:(number-2)*2+1] + '   ' + s[(number-2)*2:]
                if i >= (number-2)*2:
                    star[i+4] = s[:(number-2)*2+1] + '   ' + s[(number-2)*2:]
        
        # 가운데 3개는 따로 지정
        star[(number-1)*2-1] = '* ' * (number-1) + ' ' + ' *' * (number-1)
        star[(number-1)*2] = '* ' * (number-1)*2 + '*'
        star[(number-1)*2+1] = '* ' * (number-1) + ' ' + ' *' * (number-1)

        return star

number = int(input())

# square(number)는 리스트 형태이므로 요소별로 출력
for s in square(number):
    print(s)
