import sys

# 테스트 케이스 갯수
n = int(sys.stdin.readline())

for _ in range(n):
    text = sys.stdin.readline()
    text_reversed = text[::-1].split()
    text_reversed = text_reversed[::-1]
    print(''.join(text_reversed))



