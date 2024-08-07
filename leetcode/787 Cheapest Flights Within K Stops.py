from typing import List
import heapq
import collections


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}
        for f, t, p in flights:
            graph[f].append([t, p])
        
        prices = [float('inf') for _ in range(n)]
        que = [[0, src, 0]] # [depth, node, price]
        while que:
            depth, node, price = heapq.heappop(que)
            prices[node] = min(price, prices[node])
                
            for neighbor, nprice in graph[node]:
                if prices[neighbor] > price+nprice and depth <= k:
                    heapq.heappush(que, [depth+1, neighbor, price+nprice])
            

        if prices[dst] != float('inf'):
            return prices[dst]
        else:
            return -1
        

# TLE
# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         graph = {i: [] for i in range(n)}
#         for f, t, p in flights:
#             graph[f].append([t, p])
        
#         prices = [float('inf') for _ in range(n)]
#         que = [[0, src, 0]] # [price, node, depth]
#         while que:
#             price, node, depth = heapq.heappop(que)
#             prices[node] = price
#             if node == dst:
#                 return price
                
#             for neighbor, nprice in graph[node]:
#                 if depth <= k: # and prices[neighbor] > price + nprice 를 조건으로 추가하면 wrong answer
#                     heapq.heappush(que, [price+nprice, neighbor, depth+1])
            
#         return -1
    

# TLE (book's solution)
# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         graph = collections.defaultdict(list)
#         for u, v, w in flights:
#             graph[u].append((v, w))
        
#         Q = [(0, src, k)]

#         while Q:
#             price, node, k = heapq.heappop(Q)
#             if node == dst:
#                 return price
#             if k >= 0:
#                 for v, w in graph[node]:
#                     alt = price + w
#                     heapq.heappush(Q, (alt, v, k-1))
        
#         return -1


# ChatGPT modified version -> why?
# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         graph = {i: [] for i in range(n)}
#         for f, t, p in flights:
#             graph[f].append((t, p))
        
#         # Priority queue: (price, node, stops)
#         que = [(0, src, 0)]
#         # Dictionary to keep the best prices at a given stop count
#         best = {(src, 0): 0}
        
#         while que:
#             price, node, stops = heapq.heappop(que)
            
#             if node == dst:
#                 return price
            
#             if stops <= k:
#                 for neighbor, cost in graph[node]:
#                     new_price = price + cost
#                     if (neighbor, stops + 1) not in best or new_price < best[(neighbor, stops + 1)]:
#                         best[(neighbor, stops + 1)] = new_price
#                         heapq.heappush(que, (new_price, neighbor, stops + 1))
        
#         return -1
