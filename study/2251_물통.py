import sys
sys.stdin = open("input_data/2251_물통")

arrs = list(map(int, input().split()))

temp =[arrs[0], arrs[1], abs(arrs[2]- arrs[0]), abs(arrs[2]- arrs[1]), arrs[2]]
# if arrs[2] > arrs[0]:
#     temp.append(arr)


for i in sorted(temp):
    print(i, end=' ')