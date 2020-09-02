
# card 카드 정보
# student_now 지금 학생 번호
# student_num 총 학생수
# before_pick 그 전에 고른 모양

def pseudocode(card, student_now,student_num, before_pick, value):
    global minValue
    picks = [0, 1, 2, 3] # 고르는 모양 순서대로[ 클로버, 하트. 스페이드. 다이아몬드]

    # 종료 조건 지금 현재 학생 번호와 총학생수-1(파이썬 index는 0부터시작)가 같을때
    if student_now == student_num-1:

        # 가지고 있는 카드중에 하나를 고름
        for i in picks:
            if i == before_pick: # 그 전에 카드와는 달라야하기 때문에 조건문 넣어줌
                continue
            value += card[student_now][i] # card에서 학생의 현재 번호와 고른 식을 이용해 수를 출력하고 값과 더함

            if minValue >= value: # 최소 값과 비교해서 최소값을 출력함
                minValue = value
                return minValue
            return minValue # 아닐시에 이전의 최소 값출력

    # 첫번째 학생일 경우
    elif student_now == 0:
        # 4가지 문양 모두다 가능하므로 다음과같이 조건문 없이 for문 진행
        for i in picks:

            before_pick = i # 지금 선택한 문양을 다음 학생에게 넘겨 주기 위한 변수
            value = card[student_now][i] # 첫번째 학생의 값을 넣어줌
            student_now += 1 # 계산기 끝나고 다음 학생으로
            pseudocode(card, student_now,student_num, before_pick, value) # 다음 학생을 위한 함수를 출력

    # 나머지 학생의 경우
    else:
        print(student_now)
        for i in picks: # 전의 모양과 다른 것들을 출력해야하므로 다음과같이 함

            if i == before_pick:

                continue
            before_pick = i # 다음 학생에게 지금 고른 모양의 정보를 넘겨줌
            value += card[student_now][i] # 값을 더해줌

            student_now += 1 # 학생 번호를 다음으로 넘김
            pseudocode(card, student_now, student_num, before_pick, value) # 다음 학생을 위한 함수 출력






def pseudocode(card, student_now,student_num, before_pick, value):
    global minValue
    picks = [0, 1, 2, 3] # 고르는 모양 순서대로[ 클로버, 하트. 스페이드. 다이아몬드]

    # 종료 조건 지금 현재 학생 번호와 총학생수-1(파이썬 index는 0부터시작)가 같을때
    if student_now == student_num-1:

        # 가지고 있는 카드중에 하나를 고름
        for i in picks:
            if i == before_pick: # 그 전에 카드와는 달라야하기 때문에 조건문 넣어줌
                continue
            value += card[student_now][i] # card에서 학생의 현재 번호와 고른 식을 이용해 수를 출력하고 값과 더함

            if minValue >= value: # 최소 값과 비교해서 최소값을 출력함
                minValue = value
                return minValue
            return minValue # 아닐시에 이전의 최소 값출력

    # 첫번째 학생일 경우
    elif student_now == 0:
        # 4가지 문양 모두다 가능하므로 다음과같이 조건문 없이 for문 진행
        for i in picks:

            before_pick = i # 지금 선택한 문양을 다음 학생에게 넘겨 주기 위한 변수
            value = card[student_now][i] # 첫번째 학생의 값을 넣어줌
            student_now += 1 # 계산기 끝나고 다음 학생으로
            pseudocode(card, student_now,student_num, before_pick, value) # 다음 학생을 위한 함수를 출력

    # 나머지 학생의 경우
    else:

        for i in picks: # 전의 모양과 다른 것들을 출력해야하므로 다음과같이 함

            if i == before_pick:

                continue
            before_pick = i # 다음 학생에게 지금 고른 모양의 정보를 넘겨줌
            value += card[student_now][i] # 값을 더해줌

            student_now += 1 # 학생 번호를 다음으로 넘김
            pseudocode(card, student_now, student_num, before_pick, value) # 다음 학생을 위한 함수 출력


