import sys

N = input()
road = list(sys.stdin.readline().strip())
road.pop(0)

target = ['B', 'O', 'J']
total = 0
dist = 1
now = 1

for i in road:
    now = now % 3
    if i == target[now]:
        total += dist ** 2
        now +=1
        dist = 1
    else:
        dist +=1

now = (now-1)%3
if target[now] != road[-1]:
    print(-1)
else:
    print(total)