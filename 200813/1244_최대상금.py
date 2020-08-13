import sys
import pprint
sys.stdin = open('input_data/1244.txt')



T = int(input())


for test_case in range(1, T + 1):


    n, k = list(map(int, input().split()))

    num=[]
    for i in (str(n)):
        num.append(int(i))

    if len(num) >= k:
        for i in range(k):
            max = num[i]
            idx = i
            for u in range(i, len(num)):
                if max < num[u]:
                    max = num[u]
                    idx = u

                num[0], num[idx] = num[idx], num[0]
    else:
        print(num)
        for i in range(len(num)):
            max = num[i]
            idx = i
            for u in range(i, len(num)):
                if max < num[u]:
                    max = num[u]
                    idx = u
                num[0], num[idx] = num[idx], num[0]
            print(num)
        for i in range(k-len(num)):
            num[len(num)-1], num[len(num)-2] = num[len(num)-2], num[len(num)-1]
        print(k)
        print(num)
    result =''
    for i in num:
        result += '{}'.format(i)

    print('#{} {}'.format(test_case, result))