# 테스트 케이스 개수 T, 카드의 개수 N, 알파벳 A
T = int(input())
for _ in range(T):
    N = int(input())
    A = input().split()
    # 원하는 문자열 answer
    answer = ''
    for i, alphabet in enumerate(A):
        # 첫 번째 알파벳은 그냥 가져옴
        if i == 0:
            answer += alphabet
        # 두 번째 알파벳부터 왼쪽에 넣을지 오른쪽에 넣을지 결정
        else:
            # answer의 첫 번째 글자보다 사전순으로 뒤에 있으면 뒤에 붙여줌
            if ord(answer[0]) < ord(alphabet):
                answer += alphabet
            # answer의 첫 번째 글자와 같거나 사전순으로 앞에 있으면 앞에 붙여줌
            else:
                answer = alphabet + answer
    # answer 출력
    print(answer)