import sys
from collections import deque

def bfs(graph, start, visited):
    
    que = deque([start])
    visited[start] = True  

    while que:
        node = que.popleft()
        print(node, end = ' ')
        for i in graph[node]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


def dfs(graph, v, visited):
    visited[v] = True
    print(v , end = ' ')

    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

N, M, start = map(int , sys.stdin.readline().strip().split())

# (1) 그래프 생성
graph = [[] for _ in range(N+1)]

for i in range(M):
    n1 , n2 = map(int, sys.stdin.readline().strip().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited1 = [False] * (N + 1)
visited2 = visited1.copy()


dfs(graph, start, visited1)
print()
bfs(graph, start, visited2)



