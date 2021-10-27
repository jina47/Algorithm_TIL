def solution(s):
    if s.isdecimal() == True:
        return int(s)
    else:
        answer = []
        num_en = {"zero" :'0', "one" :'1', "two" : '2', "three" : '3', "four" : '4', "five" : '5', "six" : '6', "seven" : '7', "eight" : '8', "nine" : '9'}
        slist = [k for k in s]
        num_str = ''
        for i in slist:
            if i.isdecimal() == True:
                answer.append(i)
            else:
                num_str += i
                if num_str in num_en.keys():
                    answer.append(num_en[num_str])
                    num_str = ''
        return int(''.join(answer))