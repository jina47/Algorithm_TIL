from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 가장 긴 path를 찾아서 절반을 하는게 minimum height 일 것 같은데 
        # 가장 긴 path를 찾아서 중간에 있는 노드를 모두 return 
        # leaf 노드를 제거해가면서 남아 있는 노드들을 return 
        if n <= 2:
            return [i for i in range(n)]        
        
        # edge로 그래프 만들기 (collections.defaultdict 이용하면 key에 대해 값이 없어도 기본값 유지?)
        G = dict()
        for i in range(n-1):
            a, b = edges[i]
            if a not in G:
                G[a] = [b]
            else:
                G[a].append(b)
            if b not in G:
                G[b] = [a]
            else:
                G[b].append(a)

        # leaf 노드 제거하면서 최종적으로 남는 leaf return
        leaves = []
        for i in range(n):
            if len(G[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            # 현재 leaf들의 neighbor(parent)의 이웃 리스트 에서 현재 leaf를 제거
            for leaf in leaves:
                parent = G[leaf].pop()
                G[parent].remove(leaf)
                
                if len(G[parent]) == 1:
                    new_leaves.append(parent)

            leaves = new_leaves

        return leaves


# 모두 탐색 돌아가는 것 같지만 time limit
# class Solution:
#     def dfs(self, curnode, visited, G, depth, max_depth):
#         for neighbor in G[curnode]:
#             if visited[neighbor] == 0:
#                 break
#         else:
#             return max(max_depth, depth)

#         for neighbor in G[curnode]:
#             if visited[neighbor] == 0:
#                 visited[neighbor] = 1
#                 max_depth = self.dfs(neighbor, visited, G, depth+1, max_depth)
#                 visited[neighbor] = 0
#         return max_depth
    

#     # dfs 길이가 최대인 그래프들 중에서 그 길이가 가장 짧은 것 return 
#     # 자식 순 많은 노드부터 탐색하면 되지 않나?
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         if n <= 2:
#             return [i for i in range(n)]
        
#         # edge로 그래프 만들기
#         G = dict()
#         for i in range(n-1):
#             a, b = edges[i]
#             if a not in G:
#                 G[a] = [b]
#             else:
#                 G[a].append(b)
#             if b not in G:
#                 G[b] = [a]
#             else:
#                 G[b].append(a)

#         node_depth = [0 for _ in range(n)]
#         visited = [0 for _ in range(n)]
#         for root in range(n):
#             visited[root] = 1
#             node_depth[root] = self.dfs(root, visited, G, 0, 0)
#             visited[root] = 0
        
#         min_height = min(node_depth)
#         answer = []
#         for node in range(n):
#             if node_depth[node] == min_height:
#                 answer.append(node)
#         return answer
    

if __name__ == '__main__':
    problem = Solution()
    ans1 = problem.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])
    ans2 = problem.findMinHeightTrees(1, [])
    print(ans1)
    print(ans2)


# c++ 버전
# class Solution {
# public:
#     vector<int> findMinHeightTrees(int n, vector<vector<int>>& E) {
#         if(!size(E)) return {0};
#         vector<vector<int>> G(n);
#         for(auto& e : E) 
#             G[e[0]].push_back(e[1]), 
#             G[e[1]].push_back(e[0]);
#         vector<int> leaves, newLeaves, inDegree;
#         for(int i = 0; i < n; i++) {
#             if(size(G[i]) == 1)
#                 leaves.push_back(i);
#             inDegree.push_back(size(G[i]));        // used to determine which nodes become leaves
#         }
#         while(n > 2) {                             // process will continue till more than 2 nodes are remaining to be deleted
#             for(auto leaf : leaves) 
#                 for(auto adj : G[leaf])            // find all nodes which are adjacent to current leaf node
#                     if(--inDegree[adj] == 1)       // if adj becomes leaf node after removing leaf, 
#                         newLeaves.push_back(adj);  // add it as new leaf
#             n -= size(leaves);                     // subtract the deleted leaf nodes 
#             leaves = move(newLeaves);
#         }
#         return leaves;
#     }
# };