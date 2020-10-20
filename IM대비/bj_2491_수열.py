import sys
sys.stdin = open("input_data/bj_2491")

N = int(input())
arr = list(map(int, input().split()))

maxs = 0
count = 0
flag = 0
before = arr[0]
for i in range(1, N+1):
    # before <= i #큰거

    # before >= i #작은거



