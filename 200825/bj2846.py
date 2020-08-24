import sys

sys.stdin = open('input_data/bj_2846.txt')

T = int(input())

street = list(map(int, input().split()))


up_street = []
result = 0
max_result = 0
for i in range(0, len(street)-1):

    a = street[i + 1] - street[i]
    if a > 0:
        result += a
        if i == len(street)-2:
            if max_result < result:
                max_result = result
    else:
        if max_result < result:
            max_result = result
        result = 0
print(max_result)


