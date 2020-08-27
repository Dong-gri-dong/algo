#T = int(input())


def fibo(n, zero, one):
    global memo

    if n == 0:
        zero.append(1)
    if n == 1:
        one.append(1)



    if n >= 2 and len(memo) <= n:



        memo.append(fibo(n-1, zero, one)[0] + fibo(n-2, zero, one)[0])

    return memo[n], sum(zero), sum(one)

memo = [0, 1]

# def fibo(n):
#     f =[0,1]
#
#     for i in range(2, n+1):
#         print(i)
#         f.append(f[i-1]+ f[i-2])
#     return f[n]



#for _ in range(T):

print(fibo(4, zero=[], one=[]))
print("")
#print(fibo(4))
#print("")
#print(fibo(5))


    #print("{} {}".format(a.count(0), a.count(1)))
