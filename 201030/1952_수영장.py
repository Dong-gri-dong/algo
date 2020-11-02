import sys
sys.stdin = open("input_data/1952_수영장.txt")

T = int(input())

T = 1
for test_case in range(1, T+1):
    price = list(map(int, input().split()))
    arrs = list(map(int, input().split()))

    print(price)
    print(arrs)


    def money(k):
        if k >= 12:
            return
        else:
            for i in range(k, 12):
                if arrs[i]:
                    print(arrs[i])
                    money(k+11)

    money(0)


