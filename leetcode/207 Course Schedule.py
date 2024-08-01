from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # cycle 있는지 확인 후에 있으면 바로 false 다 돌아서 없으면 true
        neighbors = {}
        for i in range(numCourses):
            neighbors[i] = []
        for a, b in prerequisites:
            neighbors[a].append(b)
        

        def dfs(course):
            # cycle 있으면 False 
            if path[course] == 1:
                return False
            # 이미 방문했으면 탐색하지 않아도 됨
            if visited[course] == 1:
                return True
            
            path[course] = 1
            for neighbor in neighbors[course]:
                if not dfs(neighbor):
                    return False
                
            path[course] = 0

            # dfs 후 방문 표시
            visited[course] = 1
            return True

        
        path = [0 for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]

        for start in range(numCourses):
            # 탐색하지 않은 course만 dfs 
            if visited[start] == 0:
                flag = dfs(start)
                if flag == False:
                    return False

        return True
    


# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         graph = collections.defaultdict(list)
#         for x, y in prerequisites:
#             graph[x].append(y)

#             traced = set()
#             visited = set()

#         def dfs(i):
#             if i in traced:
#                 return False
#             if i in visited:
#                 return True
            
#             traced.add(i)
#             for y in graph[i]:
#                 if not dfs(y):
#                     return False
            
#             traced.remove(i)
#             visited.add(i)
#             return True

        
#         for x in list(graph):
#             if not dfs(x):
#                 return False

#         return True