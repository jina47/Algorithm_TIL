# 별찍는 함수 만들기
def square(number):

    # 주어지는 number가 3일 때가 가장 기본 형태 
    if number == 3:
        star = ['  *  ',' * * ','*****']
        return star

    # number가 3이 아닐 때 재귀함수 이용
    else:
        # 리스트 star의 길이는 number
        star = [''] * number
        
        # square(number//2)의 리스트로부터 number에 대한 star을 만들어줌
        for i, s in enumerate(square(number//2)):

            # 새로운 star는 square(number//2)의 2배 길이이므로 i, i+number//2마다 규칙성 생김
            # star[i]는 number//2만큼의 공백 + s + number//2만큼의 공백
            # star[i+number//2]은 s + ' ' + s 의 값
            star[i] = ' ' * (number//2) + s + ' ' * (number//2)
            star[i + number//2] = s + ' ' + s

        return star


number = int(input())

# square(number)는 number길이 만큼의 리스트 형태이므로 요소별로 출력
for s in square(number):
    print(s)
