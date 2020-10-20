import sys
sys.stdin = open("input_data/kakao_7")


def solution(sales, links):
    T = [[[], []] for _ in range(1+len(sales))]
    for i in range(len(sales)-1):
        p, c = links[2*i], links[2*i+1]
        T[p][0].append(c)
        T[c][1].append(p)

    # for i in T:
    #     print(*i)

    group_list = []
    for i in range(1, len(sales)+1):
        g = []
        if T[i][0]:
            g.append(i)
            for j in T[i][0]:
                g.append(j)
            group_list.append(g)



    # def money(k, n, m, S):
    #     global result
    #     if result <= m:
    #         return
    #     if k == n:
    #         #if result >= m:
    #         result = m
    #         return
    #     else:
    #         for i in group_list[k]:
    #             if i in S:
    #                 money(k + 1, n, m, S)
    #             else:
    #                 money(k + 1, n, m + sales[i - 1], S + [i])
    visit = [0] * (sum(sales) + 1)
    print(visit)
    for i in len(group_list):
        for j in group_list[i]:

    #money(0, len(group_list), 0, [])
    return None


T = int(input())

for test_case in range(1, T+1):
    sales = list(map(int, input().split()))
    links= list(map(int, input().split()))
    #result = 1000
    solution(sales, links)