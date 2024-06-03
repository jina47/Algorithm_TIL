class Solution:
    def reverseVowels(self, s: str) -> str:
        j = len(s)-1
        answer = ''
        for i in range(len(s)):
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                while j >= 0:
                    if s[j] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                        answer += s[j]
                        j -= 1
                        break
                    j -= 1
            else:
                answer += s[i]

        return answer
