from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if i == 0:
                if len(flowerbed) > 1 and flowerbed[0] == 0 and flowerbed[1] == 0:
                    flowerbed[0] = 1
                    n -= 1
                elif len(flowerbed) == 1 and flowerbed[0] == 0:
                    flowerbed[0] = 1
                    n -= 1
            elif 0 < i < len(flowerbed)-1:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            elif i == len(flowerbed)-1:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n -=1
            
        if n <= 0:
            return True
        else:
            return False


