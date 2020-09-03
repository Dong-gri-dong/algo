import sys

sys.stdin = open("input_data/5099.txt")

T = int(input())

for test_case in range(1, 1+T):
    # N : 화덕 크기
    # M : 피자 개수
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))

    pizza = []
    for i in range(M):
        pizza.append([temp[i]] + [i+1])


    Q = [0] * N
    front = rear = 0



    Q = []
    for i in range(N):
        Q.append(pizza.pop(0))



    while Q:
        check = Q.pop(0)
        check[0] = check[0] // 2
        if check[0] == 0:
            if len(pizza) != 0:
                Q.append(pizza.pop(0))
        else:
            Q.append(check)

        if len(Q) == 1:
            result = Q[0][1]
            break
    print('#{} {}'.format(test_case, result))


    def enQ(item):
        global rear
        if (rear + 1) % N == front:
            print("full")
        else:
            rear = (rear + 1) % N
            Q[rear] = item

    def deQ():
        global front

        if front == rear:
            pass
        else:
            front = (front + 1) % N
            return Q[front]