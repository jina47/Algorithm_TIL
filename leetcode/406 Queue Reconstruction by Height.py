from typing import List
import heapq


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        answer = []
        people.sort(key=lambda x: (x[1], -x[0]))
   
        for h, k in people:
            if not answer:
                answer.append([h, k])
                
            else:
                cnt = 0
                for i in range(len(answer)):
                    if cnt == k:
                        answer = answer[:i] + [[h, k]] + answer[i:]
                        break
                    if answer[i][0] >= h:
                        cnt += 1
                else:
                    answer.append([h, k])
        
        return answer
    

# class Solution:
#     def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
#         heap = []
#         for person in people:
#             heapq.heappush(heap, (-person[0], person[1]))
   
#         result = []
#         while heap:
#             person = heapq.heappop(heap)
#             result.insert(person[1], [-person[0], person[1]])
        
#         return result