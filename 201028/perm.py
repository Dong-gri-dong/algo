arr = [1, 1, 4, 3, 1, 2]
N = 6

def perm(k):
    if k == N:
        cnt = 0
        if arr[0] == arr[1] == arr[2]:
            cnt += 1
        if arr[3] == arr[4] == arr[5]:
            cnt += 1
        if arr[0] + 2 == arr[1] + 1 == arr[2]:
            cnt += 1
        if arr[3] + 2 == arr[4] + 1 == arr[5]:
            cnt += 1
        return cnt == 2


    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            if perm(k+1): return True
            arr[k], arr[i] = arr[i], arr[k]

        return False

print(perm(0))
