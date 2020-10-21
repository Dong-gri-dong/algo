import sys
sys.stdin = open("input_data/1859_백만장자프로젝트.txt")


# T = int(input())
#
# for test_case in range(1, T+1):
#     result = 0
#     N = int(input())
#     arrs = list(map(int, input().split()))
#
#
#     max_value = max(arrs)
#     max_index = arrs.index(max_value)
#
#
#     for i in range(N-1):
#         if i < max_index:
#             result += max_value - arrs[i]
#         else:
#             max_value = max(arrs[i + 1:])
#             max_index = arrs[i + 1:].index(max_value) + (i+1)
#     print('#{} {}'.format(test_case, result))

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arrs = list(map(int, input().split()))
    result = 0
    max_value = arrs[-1]

    for j in arrs[::-1]:
        if max_value >= j:
            result += max_value - j
        else:
            max_value = j

    print('#{} {}'.format(test_case, result))