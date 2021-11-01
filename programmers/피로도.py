from itertools import permutations

def solution(k, dungeons):
    answer = -1
    # dungeons를 모든 경우로 조합하여 나열하기(permutations 이용)
    dg_list = list(permutations(dungeons, len(dungeons))) 
    
    # 하나의 던전 탐색 순서를 dg로 지정
    for dg in dg_list:
        t = k
        cnt = 0
        for dungeon in dg:
            # dungeon[0]보다 t가 크면 최소 필요 피로도가 k보다 큰 경우이므로 던전 탐험 불가
            if dungeon[0] > t:
                continue
            # 최소 필요 피로도가 k 이하인 경우 던전 탐험 가능
            # cnt는 던전 탐험 순서이므로 +1 해주고 t에서 소모 피로도를 빼줌
            else:
                cnt += 1
                t -= dungeon[1]
        
        # answer보다 cnt가 큰 경우 answer을 cnt로 지정
        if answer < cnt:
            answer = cnt
        
        # 만약에 answer가 dungeons의 길이만큼의 값을 가지면 최댓값을 가지는 것이므로 더 탐색하지 않고 break
        if answer == len(dungeons):
            break

    return answer
