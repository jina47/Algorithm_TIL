from typing import List
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 모든 티켓을 다 써서 lexical order를 만족하는 valid itinerary 찾기
        # cycle 있는 건 나중에 추가 가능 -> 어떻게 cycle 감지?!
        tickets.sort()
        visited = [0 for _ in range(len(tickets))]


        def dfs(cur):
            dep, arr = cur
            path.append(arr)
            if len(path) == len(tickets)+1:
                return True

            for j, next_ticket in enumerate(tickets):
                if arr == next_ticket[0] and visited[j] == 0:
                    visited[j] = 1
                    if dfs(next_ticket):
                        return True
                    visited[j] = 0

            path.pop()
            return False


        for i, ticket in enumerate(tickets):
            if ticket[0] == "JFK":
                path =["JFK"]
                visited[i] = 1
                if dfs(ticket):
                    return path
                visited[i] = 0



# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         graph = collections.defaultdict(list)
#         for a, b in sorted(tickets):
#             graph[a].append(b)

#         route = []
#         def dfs(a):
#             while graph[a]:
#                 dfs(graph[a].pop(0))
#             route.append(a)

#         dfs('JFK')
#         return route[::-1]