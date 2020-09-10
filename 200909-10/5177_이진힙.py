import sys

sys.stdin = open("input_data/5177.txt")


def push(item):
    global hsize
    hsize += 1
    H[hsize] = item
    c, p = hsize, hsize // 2
    while p:
        if H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
            c = p
            p = c // 2
        else:
            break
    pass

def parents(n):
    global count
    if n >= 1:
        parents(n//2)
        if n < N:
            count += H[n]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    H = [0] * (N + 1)
    hsize = 0

    for i in arr:
        push(i)
    count = 0
    parents(N)
    print('#{} {}'.format(test_case, count))