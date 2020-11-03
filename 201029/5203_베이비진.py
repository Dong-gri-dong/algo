import sys
sys.stdin = open("input_data/5203_베이비진.txt")

T = int(input())



def check_run(arr):
    new_arr = list(set(sorted(arr)))
    for i in range(len(new_arr)):
        if i + 2 <= len(new_arr)-1:
            if new_arr[i + 2]  == new_arr[i + 1]+1 == new_arr[i]+2:
                return 1
    return 0

def check_triplet(arr):

    new_arr = sorted(arr)
    for i in range(len(new_arr)):
        if i + 2 <= len(new_arr)-1:
            if new_arr[i + 2] == new_arr[i + 1] == new_arr[i]:
                return 1
    return 0

for test_case in range(1, T+1):
    result = 0
    arrs = list(map(int, input().split()))

    one = []
    two =[]
    for i in range(len(arrs)):
        if i % 2:
            two.append(arrs[i])
            if check_run(two) or check_triplet(two):
                result = 2
                break
        else:
            one.append(arrs[i])
            if check_run(one) or check_triplet(one):
                result = 1
                break


    print('#{} {}'.format(test_case, result))







