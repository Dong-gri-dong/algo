import sys

sys.stdin = open("input_data/4861.txt")


T = int(input())
for t in range(1, T+1):
    N, M = list(map(int, input().split()))

    arr = [input() for _ in range(N)]
    # 행 확인
    # 맨 앞과 맨 뒤를 확인
    i = 0
    new_list = []
    # 다르면 맨 앞의 것 +1
    # 같으면 새로운 리스트에 맨 뒤의 값 저장
    # 맨 앞거 +1, 맨 뒤의 것 -1
    # 새로운 리스트의 길이가 M과 같으면 탈출
    for _ in range(N):
        j = 0
        k = 0
        while len(new_list) != M and j <= N - 1 - j and j < N:
            if arr[i][j] != arr[i][N - 1 - k]:
                j += 1
            else:
                new_list.append(arr[i][N - 1 - k])
                j += 1
                k += 1
        if j == N:
            j = 0
        i += 1
        if len(new_list) != M:
            new_list = []


    i = 0
    new_list2 = []
    for _ in range(N):
        j = 0
        k = 0
        while len(new_list2) != M and j != N - 1 - j and j < N:
            if arr[j][i] != arr[N - 1 - k][i]:
                j += 1
            else:
                new_list2.append(arr[N - 1 - k][i])
                j += 1
                k += 1
        if j == N:
            j = 0
        i += 1
        if len(new_list2) != M:
            new_list2 = []

    my_list = new_list + new_list2
    my_result = ''.join(my_list)
    print("#{} {}".format(t, my_result))