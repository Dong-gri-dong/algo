import sys
sys.stdin = open("input_data/5207_이진탐색.txt")

T = int(input())
T = 1
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))



    def check(ele, B):
        i = 0
        r = M
        m = (i+r)//2
        print(m)
        print(i)
        print(r)
        while i != m and r != m:

            if ele > B[m]:
                i = m + 1
                m = (i + r) // 2
            elif ele < B[m]:
                r = m - 1
                m = (i + r) // 2
            elif ele == B[m]:
                print(1111)
                return 1
        print()
        print(m)
        print(i)
        print(r)
    print(check(A[1], B))

