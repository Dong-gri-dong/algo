import sys

sys.stdin = open("input_data/1868.txt")

T = int(input())
T = 1
for test_case in range(1, T+1):
    N = int(input())
    print(N)
    #arr = [ list(input()) for i in range(N) ]

    for i in range(N):
        count = 0
        for k in list(input()):
            if k == '*':
                print(i,count)
            count += 1


