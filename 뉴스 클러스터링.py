def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    ls1 = []
    ls2 = []
    for i in range((len(str1))-1):
        if (str1[i] + str1[i+1]).isalpha() == True:
            ls1.append(str1[i] + str1[i+1])

    for i in range((len(str2))-1):
        if (str2[i] + str2[i+1]).isalpha() == True:
            ls2.append(str2[i] + str2[i+1])
            
    N = 0
    P = 0
    ls = list(set(ls1) | set(ls2))
    
    for i in ls:
        N += min(ls1.count(i), ls2.count(i))
        P += max(ls1.count(i), ls2.count(i))
        
    if N == 0 and P == 0:
        return 65536
    else:
        return int(N/P*65536)