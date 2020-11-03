arr = [69, 10, 30, 2, 16, 8, 31, 22]
sort = [0] * len(arr)
#mergeSort(0, len(arr) - 1) # 요건 불러오는 코드 보기 편하게 먼저 써봤음
def mergeSort(lo, hi): # lo와 hi는 초기값으로 배열의 left와 right를 의미
    if lo >= hi: # left가 더 커지면 그만한다. <- 정렬이 끝난경우 이므로
        return

    mid = (lo + hi) >> 1  # (lo + hi)//2 라고 생각하면 된다.
    mergeSort(lo, mid) # 이거는 나눈거 기준 왼쪽
    mergeSort(mid + 1, hi) # 나눈거 기준 오른쪽

    i, j, k = lo, mid + 1, lo  # 변수 초기값
    while i <= mid and j <= hi:
        # i 조건 lo(left)부터 mid까지 즉 나눈부분의 좌측 정렬 끝날때까지
        # j 조건 mid+1 부터 hi(right)까지 나눈 부분의 우측 정렬 끝날때까지지
       if arr[i] < arr[j]: # 이 조건문은 예를 들면 이런거 [1, 6] [4, 5]이 있을때
                           # 새로운 리스트에 좌측이 작으니깐 왼쪽값을 [1,  <- 요렇게 넣는 것
            sort[k] = arr[i] # 리스트에 넣고
            k, i = k + 1, i + 1  # 오른쪽으로 한칸 가게 함 [1, 6] <- 여기서 6을 가르키는것
        else:
            sort[k] = arr[j]  # 이 조건문은 이제 [6] [4, 5]가 있을때
                              # 새 리스트에 [1, 4 <- 이것을 넣어주는것
            k, j = k + 1, j + 1

    # 요 아래 코드는 위에서 조건이 끝났을경우 남은것들을 처리하는 코드
    # 예를들어서 우연히 [1, 2, 3, 4] [5, 6, 7, 8] 를 정렬해야할때
    # 왼쪽부터 다 정렬되고 오른쪽이 남는다 그럴때 오른쪽 부분을
    # 처리하는 코드라고 생각하면된다. <- 심하게 말해서 이거지 그냥 남는거 처리하는 코드

    while i <= mid:
        sort[k] = arr[i]
        k, i = k + 1, i + 1

    while j <= hi:
        sort[k] = arr[j]
        k, j = k + 1, j + 1

    # 마지막으로 arr에 다시 담아준다.
    for i in range(lo, hi + 1):
        arr[i] = sort[i]


mergeSort(0, len(arr) - 1)

print(arr)


#
# def mergeSort(arr):
#
#     if len(arr) <= 1:
#         return arr
#
#     mid = int(len(arr) / 2)
#
#     left = arr[:mid]
#     right = arr[mid:]
#
#     left = mergeSort(left)
#     right = mergeSort(right)
#
#     result = []
#
#     while len(left) > 0 and len(right) > 0:
#         if left[0] < right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#
#     if len(left) > 0:
#         result += left
#     else:
#         result += right
#
#     return result
#
#
# # unsort = [69, 10, 30, 2, 16, 8, 31, 22]
# # sort = mergeSort(unsort)
# # print(sort)
#
# print(6 >> 1)