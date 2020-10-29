arr = 'ABC'
N = 3



perm = []
for i in range(N):
    if arr[i] in perm:
        continue
    perm.append(arr[i])


    for j in range(N):
        if arr[j] in perm:
            continue
        perm.append(arr[j])

        for k in range(N):
            if arr[k] in perm:
                continue
            perm.append(arr[k])
            print(perm)

            perm.pop()
        perm.pop()

    perm.pop()

perm = []

def backtrack(k):
    if k == N:
        print(perm)
    else:


        for i in range(N):
            if arr[i] in perm:
                continue
            perm.append(arr[i])
            backtrack(k+1)
            perm.pop()


backtrack(0)