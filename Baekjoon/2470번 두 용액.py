N = int(input())
liquid = list(map(int, input().split()))
# liquid를 오름차순으로 정렬
liquid.sort()
# 시작점은 0 끝점은 N-1로 설정
start = 0
end = N-1
# left 는 start에 해당하는 용액, right는 end에 해당하는 용액
left = liquid[start]
right = liquid[end]

# start가 end를 넘지 않을 때까지
while start < end:
    # 만약 left와 right의 합(특성값) 절댓값이 새로 지정해준 start와 end의 용액의 합 절댓값보다 크면 left right 갱신
    if abs(left + right) > abs(liquid[start]+ liquid[end]):
        left = liquid[start]
        right = liquid[end]
    
    # start와 end의 용액 값 합이 0이면 그대로 break 
    if liquid[start] + liquid[end] == 0:
        break

    # start용액은 알칼리성이고 end용액도 알칼리성인 경우 start += 1
    elif liquid[start] < 0 and liquid[end] < 0:
        start += 1
    # start용액은 알칼리성 end용액은 산성인 경우
    elif liquid[start] < 0 and liquid[end] > 0:
        # 두 용액의 합이 0 이상이면 end -= 1
        if liquid[start] + liquid[end] > 0:
            end -=1
        # 두 용액의 합이 0 이하이면 start += 1
        else:
            start += 1
    # start 용액과 end 용액 모두 산성인 경우 end -= 1
    elif liquid[start] > 0 and liquid[end] > 0:
        end -=1 

# left, right 출력
print(left, right)
