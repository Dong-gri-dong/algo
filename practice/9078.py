import sys

sys.stdin = open('input_data/9708.txt')

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())

    arr = list(map(int, input().split()))

    arr = sorted(arr)

    a = []

    for i in range(len(arr)):
        b = []
        for k in arr[i+1:]:
            if k % arr[i] == 0:
                b.append(k)

        a.append(b)
    print(a)