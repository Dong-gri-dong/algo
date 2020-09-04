import sys

sys.stdin = open('input_data/bj_1713.txt')

N = int(input())
T = int(input())

num = list(map(int, input().split()))


#학생들이 추천을 시작하기 전에 모든 사진틀은 비어있다.

#어떤 학생이 특정 학생을 추천하면, 추천받은 학생의 사진이 반드시 사진틀에 게시되어야 한다.

#비어있는 사진틀이 없는 경우에는 현재까지 추천 받은 횟수가 가장 적은 학생의 사진을 삭제하고,
#그 자리에 새롭게 추천받은 학생의 사진을 게시한다. 이때, 현재까지 추천 받은 횟수가 가장 적은
# 학생이 두 명 이상일 경우에는 그러한 학생들 중 게시된 지 가장 오래된 사진을 삭제한다.

#현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가시킨다.
#사진틀에 게시된 사진이 삭제되는 경우에는 해당 학생이 추천받은 횟수는 0으로 바뀐다.
#후보의 수 즉, 사진틀의 개수와 전체 학생의 추천 결과가 추천받은 순서대로 주어졌을 때, 최종 후보가 누구인지 결정하는 프로그램을 작성하시오.


final = ''
result = []
#리스트를 넣을때  [ 사람, 시간, 횟수] 순으로

for hubo_time, hubo in enumerate(num):

    if len(result) < N: #사진틀에 3명이 안넘는경우
        # 1. 아무도 후보가 없을때
        if hubo_time == 0:
            result.append([hubo, hubo_time, 1])

        else:
                #겹치는게 있는지 없는지
            hubo_count = 0
            for i in range(len(result)):

                if result[i][0] == hubo:
                    hubo_count += 1
                    this = i

            if hubo_count: #겹쳐서 추천횟수 추가
                #result[this][1] = hubo_time
                result[this][2] +=1

            else:
                result.append([hubo, hubo_time, 1])

    else:     #사진틀에 3명이 넘는경우
        # 겹치는게 있는지 없는지
        hubo_count = 0

        for i in range(len(result)):

            if result[i][0] == hubo:
                hubo_count += 1
                this = i
        # 겹치는 경우
        if hubo_count:
            if hubo_count: #겹쳐서 추천횟수 추가
                #result[this][1] = hubo_time
                result[this][2] +=1

        # 겹치치 않는 경우 (추천횟수 적은거 빼기 추천횟수 적은게 2개 이상이면 오래된거 빼기)
        else:
            min_hubo = result[0][2]#추천횟수 작은거 찾기
            for k in range(len(result)):
                if min_hubo >= result[k][2]:
                    min_hubo = result[k][2]

            counts = 0
            min_hubo_list=[]
            for n in range(len(result)):
                if min_hubo == result[n][2]:
                    counts += 1
                    min_hubo_list.append(n)

            if counts:

                min_tu = result[min_hubo_list[0]][1]
                for j in min_hubo_list:
                    if min_tu >= result[j][1]:
                        min_tu = result[j][1]
                        min_tu_idx = j
                result.pop(min_tu_idx)
                result.append([hubo, hubo_time, 1])




            else:
                old_hubo = result[0][1]
                for u in range(len(result)):
                    if old_hubo >= result[u][1]:
                        old_hubo = result[u][1]
                        old_hubo_idx = u
                result.pop(u)
                result.append([hubo, hubo_time, 1])

k=[]
for i in range(len(result)):
    k.append(result[i][0])
k.sort()

for i in k:
    final += '{} '.format(i)

print(final)


