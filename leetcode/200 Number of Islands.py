from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        visited = [[0 for _ in range(n)] for _ in range(m)]
        cnt = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and visited[r][c] == 0:
                    cnt += 1

                    # dfs
                    stack = [[r, c]]
                    visited[r][c] = 1
                    dx = [-1, 1, 0, 0]
                    dy = [0, 0, 1, -1]
                    while stack:
                        x, y = stack.pop()
                        
                        for i in range(4):
                            nx, ny = x+dx[i], y+dy[i]
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1' and visited[nx][ny] == 0:
                                stack.append([nx, ny])
                                visited[nx][ny] = 1
        return cnt
    

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         m, n = len(grid), len(grid[0])

#         cnt = 0
#         for r in range(m):
#             for c in range(n):
#                 if grid[r][c] == '1':
#                     cnt += 1

#                     # dfs
#                     stack = [[r, c]]
#                     grid[r][c] = '0'
#                     dx = [-1, 1, 0, 0]
#                     dy = [0, 0, 1, -1]
#                     while stack:
#                         x, y = stack.pop()
                        
#                         for i in range(4):
#                             nx, ny = x+dx[i], y+dy[i]
#                             if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
#                                 stack.append([nx, ny])
#                                 grid[nx][ny] = '0'
#         return cnt