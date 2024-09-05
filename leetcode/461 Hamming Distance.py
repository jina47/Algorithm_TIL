class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        answer = 0
        while z:
            answer += z % 2
            z = z >> 1
        return answer