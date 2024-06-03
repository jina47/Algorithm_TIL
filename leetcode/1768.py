class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = min(len(word1), len(word2))
        answer = ''
        for i in range(a):
            answer += word1[i] + word2[i]
        if a < len(word1):
            answer += word1[a:]
        elif a < len(word2):
            answer += word2[a:]
        return answer