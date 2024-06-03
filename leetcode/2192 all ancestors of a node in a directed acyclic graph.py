from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def dfs(start, curnode, ans):
            for neighbor in parent[curnode]:
                if neighbor not in ans[start]:
                    dfs(start, neighbor, ans)
                    ans[start].append(neighbor)

        parent = [[] for _ in range(n)]
        for u, v in edges:
            parent[v].append(u)

        ans = [[] for _ in range(n)]

        for node in range(n):
            dfs(node, node, ans)

        ans = list(map(lambda x: sorted(x), ans))
        return ans
    

if __name__ == '__main__':
    solution = Solution()
    ans = solution.getAncestors(n = 5, edges = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])
    print(ans)