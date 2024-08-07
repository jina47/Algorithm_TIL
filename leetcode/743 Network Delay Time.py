from typing import List
import heapq
import collections


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i:[] for i in range(1, n+1)}
        for u, v, w in times:
            graph[u].append([v,w])

        mtime = [float('inf') for _ in range(n+1)]
        mtime[0] = 0

        visited = [0 for _ in range(n+1)]
        que = [[0, k]]
        while que:
            utime, u = heapq.heappop(que)
            visited[u] = 1
            mtime[u] = utime

            if sum(visited) == n:
                break

            for v, w in graph[u]:
                if visited[v] == 0:
                    heapq.heappush(que, [utime + w, v])


        if max(mtime) != float('inf'):
            return max(mtime)
        else:
            return -1
        

# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         graph = {i:[] for i in range(1, n+1)}
#         for u, v, w in times:
#             graph[u].append([v,w])

#         mtime = [float('inf') for _ in range(n+1)]
#         mtime[0] = 0
#         mtime[k] = 0

#         visited = set()
#         que = [[k, 0]]
#         while que:
#             u, _ = que.pop(0)
#             for v, w in graph[u]:
#                 mtime[v] = min(mtime[v], mtime[u]+w)
#                 if (u, v) not in visited:
#                     visited.add((u, v))
#                     que.append([v, w])
#                 else:
#                     continue
#             que.sort(key=lambda x: x[1])


#         if max(mtime) != float('inf'):
#             return max(mtime)
#         else:
#             return -1
        

# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         graph = collections.defaultdict(list)
#         for u, v, w in times:
#             graph[u].append((v, w))

#         Q = [(0, k)]
#         dist = collections.defaultdict(int)

#         while Q:
#             time, node = heapq.heappop(Q)
#             if node not in dist:
#                 dist[node] = time
#                 for v, w in graph[node]:
#                     alt = time + w
#                     heapq.heappush(Q, (alt, v))
        
#         if len(dist) == n:
#             return max(dist.values())
#         return -1

