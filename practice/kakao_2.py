import sys
sys.stdin = open("input_data/kakao_2")

def solution(orders, course):

    def select(k, n, menu, limit, i):

        if len(menu) == int(n):
            if menu in my_dict.keys():
                my_dict[str(menu)] += 1
            else:
                my_dict[str(menu)] = 1
            return
        if k == len(orders[i]):
            return

        else:
            select(k + 1, n, menu+orders[i][k], limit, i)
            select(k + 1, n, menu, limit, i)
    new = []
    for i in orders:
        new.append(''.join(sorted(i)))
    orders = new



    result =[]
    for n in course:
        my_dict = dict()
        for i in range(len(orders)):
            select(0, n, '', len(orders[i]), i)
        if not my_dict:
            pass
        else:
            dic_max = max(my_dict.values())
            if dic_max >= 2:
                for key, value in my_dict.items():
                    if dic_max == value:
                        result.append(key)


    result.sort()
    return result




T = int(input())

for test_case in range(1, 1+T):
    orders = list(input().split())
    course = list(input().split())
    print(solution(orders, course))
    #solution(orders, course)


