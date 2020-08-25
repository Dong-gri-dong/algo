import sys

sys.stdin = open("input_data/7701.txt")


T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    names = [input() for i in range(n)]
    names = sorted(set(names))
    names = sorted(names, key=len)

    print("#{}".format(test_case))
    for k in names:
        print(k)
