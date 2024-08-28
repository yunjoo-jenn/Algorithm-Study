import sys

def dfs(graph, visited, node):
    visited[node] = 1
    for v in graph[node]:
        if not visited[v]:
            dfs(graph, visited, v)


N, M = map(int, sys.stdin.readline().strip().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

    if i == 0:
        start = n1



visited = [0] * (N+1)
visited[0] = 1
count = 0

count = 0 # 연결 노드의 수
for i in range(1, N+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1 # dfs 한 번 끝날 때마다 count+1
