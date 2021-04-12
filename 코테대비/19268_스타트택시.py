import sys
sys.stdin = open("19268_스타트 택시")


N, M, G = map(int, input().split())

arrs = [list(map(int, input().split())) for _ in range(N)]


y, x = map(int, input().split())
y -= 1
x -= 1

people = []
for i in range(M):
    a, b, c, d = map(int, input().split())
    people
