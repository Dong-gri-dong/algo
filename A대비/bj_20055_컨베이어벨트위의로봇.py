import sys
from collections import deque
sys.stdin = open("input_data/bj_20055_컨베이어벨트위의로봇")

N, K = map(int, input().split())
arrs = deque(map(int, input().split()))

check = K

print(arrs)

while K > 0:
    arrs.rotate(1)
    if arrs != 0:
        arrs[0] -= 1
    if arrs[0] == 0:
        K -= 1

print()

