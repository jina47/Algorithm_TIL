# 입력
N = int(input())
M = int(input())
if M != 0:
    broken = list(map(int, input().split()))

### 고려해야 하는 버튼 횟수
# N의 길이(숫자버튼으로 누를 수 있는 최소 버튼 횟수) 
# |100-N|의 크기(+,-로만 누를 수 있는 최소 버튼 횟수)
# 숫자버튼으로 N과 가장 가까운 수를 만들고 +,-를 누르는 횟수

# 고장난 버튼이 없으면 모든 버튼을 누를 수 있으므로 N의 길이와 |100-N| 중 최솟값 출력
if M == 0:
    print(min(len(str(N)), abs(100-N)))

# 고장난 버튼이 있는 경우
else:
    for s in str(N):
        # 원하는 채널의 숫자 버튼 중 고장난 버튼이 있는 경우
        if int(s) in broken:
            # low, high는 최댓값 500000으로 설정 (현재 채널 100에서 (500000-100)이 누를 수 있는 버튼의 최대 횟수)
            low, high = 500000, 500000
            
            # N에서 떨어져있는 간격을 plmi라고 해두고 이는 +나 -를 누르는 횟수
            for plmi in range(1, 500000-100+1):
                # N보다 작은 수를 만들때 dc, N보다 큰 수를 만들때 hc
                dc = N-plmi
                hc = N+plmi

                # dc는 0보다 작을 수 없음
                if 0 <= dc:
                    # dc 모든 숫자가 고장나지 않았으면 
                    # low를 dc를 만드는데 필요한 숫자 버튼 수와 +버튼 수를 더해 저장 후 break
                    for s in str(dc):
                        if int(s) in broken:
                            break
                    else:
                        low = len(str(dc))+plmi
                        break 
                
                # hc 모든 숫자가 고장나지 않았으면 
                # high를 hc를 만드는데 필요한 숫자 버튼 수와 -버튼 수를 더해 저장 후 break
                for s in str(hc):
                    if int(s) in broken:
                        break
                else:
                    high = len(str(hc))+plmi
                    break
            
            # abs(100-N), low, high 중 작은 수 출력
            print(min(abs(100-N), low, high)) 
            break
    
    # 원하는 채널의 숫자 버튼 모두가 고장나지 않은 경우
    else:
        print(min(len(str(N)), abs(100-N)))
