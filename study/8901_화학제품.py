import sys
sys.stdin = open("input_data/8901_화학제품")

T = int(input())

for test_case in range(1, T+1):
    nums = list(map(int, input().split()))
    prices = list(map(int, input().split()))
    temp = ['AB', 'BC', 'CA']
    alpha = ['A', 'B', 'C']

    score = dict()
    for i in range(3):
        score[temp[i]] = prices[i]

    def select(sums):
        global result

        if nums.count(0) == 2:
            if result <= sums:
                result = sums
            return
        else:
            for i in range(3):
                if i == 2:
                    j = 0
                else:
                    j = i + 1
                if nums[i] > 0 and nums[j] > 0:

                    nums[i] -= 1
                    nums[j] -= 1
                    select(sums + score[alpha[i]+alpha[j]])
                    nums[i] += 1
                    nums[j] += 1
    result = 0
    select(0)
    print(result)


