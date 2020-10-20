import sys
sys.stdin = open("input_data/bj_1068")
N = int(input())
arr = list(map(int, input().split()))
del_node = int(input())

T = [ [-1,-1,-1] for _ in range(N)]


for i in range(N):
    print(arr[i])
    # 부모가 없을때
    if arr[i] == -1:
        pass

    # 부모가 있을때