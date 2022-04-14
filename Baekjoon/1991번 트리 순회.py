from collections import deque as dq

# 전위 순회
def preorder(graph):
    que = dq(['A'])
    pre = ''
    while que:
        node = que.popleft()
        if node != '.':
            pre += node
            if node in graph:
                for adjnode in graph[node][::-1]:
                    que.appendleft(adjnode)
    return pre

# 중위 순회
def inorder(graph, start):
    temp = start
    if start in graph:
        a, b = graph[start][0], graph[start][1]
        if a != '.':
            temp = inorder(graph, a) + temp
        if b != '.':
            temp = temp + inorder(graph, b)
    return temp 

# 후위 순회
def postorder(graph, string):
    tp = string
    if string in graph:
        c, d = graph[string][0], graph[string][1]
        if d != '.':
            tp = postorder(graph, d) + tp
        if c != '.':
            tp = postorder(graph, c) + tp
    return tp

N = int(input()) # 노드의 개수
graph = {}
for _ in range(N):
    [p, l, r] = input().split()
    graph[p] =[l, r]

# 출력
print(preorder(graph))
print(inorder(graph, 'A'))
print(postorder(graph, 'A'))
