class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == '' and str2 == '':
            return ''
        elif str1 and str2 == '':
            return str1
        elif str2 and str1 == '':
            return str2
        else:
            # 길이 긴 문장을 str1에 저장
            if len(str1) < len(str2):
                temp = str1 
                str1 = str2
                str2 = temp
            if str1[:len(str2)] == str2:
                return self.gcdOfStrings(str1[len(str2):], str2)
            else:
                return ''

        
            