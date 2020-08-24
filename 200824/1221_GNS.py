import sys
import pprint
sys.stdin = open('input_data/1221.txt')


#T = int(input())

# main = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#
# for test_case in range(1, T + 1):
#     x,y = list(input().split())
#     lists = list(input().split())
#
#     for i in range(len(lists)):
#         if lists[i] == "ZRO":
#             pass
#         else:
#             for k in range(i, len(lists)):
#                 if lists[k] in main[:main.index(lists[i])]:
#                     lists[i], lists[k] = lists[k], lists[i]
#     print("{}".format(x))
#     for u in lists:
#        print(u, end=' ')
#     print("")


T = int(input())
main = {"ZRO": 0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}


for test_case in range(1, T + 1):
    x,y = list(input().split())
    lists = list(input().split())

    counts = [0] * 10
    for i in lists:
        counts[main[i]] += 1
    print(x)
    for idx, n in enumerate(main.keys()):
        print('{} '.format(n)*counts[idx], end='')
    print("")
