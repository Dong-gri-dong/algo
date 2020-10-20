import sys

sys.stdin = open("input_data/5176.txt")

# T = int(input())
#
# def binary(n):
#     global count
#     # 문제를 보면 LVR 중위순열순서로 값이 1씩 늘어난다.
#     # 그래서 이점을 count를 이용해 1씩증가시켜서 값을 넣어준다.
#     # 그러면 인덱스만 찾으면 되는데 인덱스는
#     # 왼쪽노드는 2배 오른쪽노드는 2배 +1의 특성을 가지고 있다.
#
#     # 일단 인덱스가 노드수가 넘지 않게
#     if n <= N:
#         #인덱스를 1부터 시작해서
#         # 왼쪽으로 가니깐 2배를 해줌 왼쪽이 없을때까지 돌림
#         # 즉 인덱스 범위를 넘지 않을때까지 2배 해주는데
#         # 노드수를 넘어 버리면 거기가 채워야할 칸이다.
#         binary(n*2)
#         # 노드수를 넘어 버려서 이제 2배가 더이상 안되므로
#         # 여기에서 그에 맞는 인덱스에 값을 넣어줌 제일 작은 값부터
#         T[n] = count
#
#         # 그리고 값을 늘려줘야함
#         count += 1
#         # 오른쪽 노드도 위와 같은 느낌으로 2배 + 1을 한다.
#         binary(n*2 + 1)
#
#
# for test_case in range(1, T+1):
#     N = int(input())
#     T = [0] * (N+1)
#     count = 1
#     binary(1)
#
#
#     print(T)
#     print('#{} {} {}'.format(test_case, T[1], T[N // 2]))


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr =[0] * (N+1)
    def tree(n):
        global count
        if n <= N:

            tree(2 * n)
            arr[n] = count
            count += 1
            tree(2 * n + 1)

    count = 1
    tree(1)

    print('#{} {} {}'.format(test_case, arr[1], arr[N//2]))