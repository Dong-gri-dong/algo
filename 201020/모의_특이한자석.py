import sys
sys.stdin = open("input_data/모의_특이한자석.txt")

T = int(input())

def rotate(arrs, n, direct):
    if direct == 1:
        temp = arrs[n].pop()
        new_arr = [temp]
        new_arr.extend(arrs[n])

        arrs[n] = new_arr
    else:
        temp = arrs[n].pop(0)
        arrs[n].append(temp)



for test_case in range(1, T+1):
    K = int(input())

    arrs = [list(map(int , input().split())) for _ in range(4)]
    rotate_status = [ list(map(int, input().split())) for _ in range(K)]

    # for i in arrs:
    #     print(*i)

    for i in rotate_status:
        n, direct = i
        n -= 1

        center = n
        center_d = direct

        right = []
        left = []
        while n < 3 and arrs[n][2] != arrs[n+1][6]:
            right.append(n+1)
            n += 1
            if n == 3:
                break
        n = center

        while n >0 and arrs[n][6] != arrs[n-1][2]:
            if n == 0:
                break
            left.append(n-1)
            n -= 1
            if n == 0:
                break


        for j in range(len(right)):
            direct = direct * - 1
            rotate(arrs, right[j], direct)

        direct = center_d
        for j in range(len(left)):
            direct = direct * - 1
            rotate(arrs, left[j], direct)

        rotate(arrs, center, center_d)

        # print()
        # for i in arrs:
        #     print(*i)


    sums = 0
    for i in range(len(arrs)):
        sums += 2**i * arrs[i][0]
    print('#{} {}'.format(test_case, sums))