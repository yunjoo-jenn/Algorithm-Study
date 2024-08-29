import sys

def dfs(x, y, graph):
    graph[y][x] = 2

    dx = [1, -1, 0 , 0 ]
    dy = [0, 0, 1, -1]

    for i in range(4):
        if x + dx[i] >=0 and x+dx[i] <M and y+dy[i] >=0 and y+dy[i]<N:
            if graph[y+dy[i], x+dx[i]] == 1:
                dfs(x+dx[i], y+dy[i], graph)
    


T = int(sys.stdin.readline())

for _ in range(T):

    M, N, K = map(int, sys.stdin.readline().strip().split())

    graph = [[0]*M for _ in range(N)]

    for _ in range(K):
        x1, y1 = map(int, sys.stdin.readline().strip().split())
        graph[y1][x1] = 1



    count = 0
    for i in range(M):
        for j in range(N):
            if graph[j][i] == 1:
                dfs(i, j, graph)
                count +=1
    print(count , end = ' ')
        