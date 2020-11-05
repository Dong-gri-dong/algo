import sys
sys.stdin = open("input_data/3316_동아리실관리하기.txt")

T = int(input())

for test_case in range(1, T+1):
    arr = list(input())
    N = len(arr)

    people = ['A', 'B', 'C', 'D']

    def dongari(k, j, rooms, room):
        global result
        if k == N:

            result += 1
            return
        else:
            if j == 4:
                if room:
                    if arr[k] in room and len(room) > 1 :
                        if k > 0:
                            count = 0
                            for i in rooms[k-1]:
                                if i in room:
                                    count += 1
                            if count:
                                dongari(k + 1, 0, rooms + [room], [])
                                #dongari(k + 1, 0, rooms + [room], [])
                            else:
                                return
                        else:
                            dongari(k + 1, 0, rooms + [room], [])

                else:
                    return
            else:
                dongari(k, (j+1)%5, rooms, room + [people[j]])
                dongari(k, (j+1)%5, rooms, room)




    result = 0
    dongari(0, 0, [], [])
    print(result%1000000007)

