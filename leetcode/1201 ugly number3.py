class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ugly = []
        max_in = max(a, b, c)
        max_num = n * max_in

        
        return 