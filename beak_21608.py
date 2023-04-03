# -*- coding: utf-8 -*-
"""
Daesik Jang
daesik0320@gmail.com
"""

def solution(N, students):
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 방향 상(0), 우(1) 하(2) 좌(3)
    seats = [[0] * N for _ in range(N)] # 좌석에 대한 배열
    score_dict = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000} # 점수 사전

    # 학생 앉히기!
    for student in students:
        available_seat = list()
        for row in range(N):
            for col in range(N):
                # 비어 있는 칸 여부 확인
                if seats[row][col] == 0:
                    like_student, blank_seat = 0, 0
                    # 인근 칸 확인
                    for i in range(4):
                        n_row = row + direction[i][0]
                        n_col = col + direction[i][1]
                        # 좌석 범위 확인
                        if 0 <= n_row < N and 0 <= n_col < N:
                            # 상하좌우 빈 자리 여부 확인
                            if seats[n_row][n_col] == 0:
                                blank_seat += 1
                            # 상하좌우에 좋아하는 학생 있는지 확인
                            elif seats[n_row][n_col] in student[1:]:
                                like_student += 1
                        available_seat.append((like_student, blank_seat, row, col))
        # 1순위 : 좋아하는 학생이 인근에 많을 수록
        # 2순위 : 비어있는 칸이 인근에 많을 수록
        # 3순위 : 행 번호가 작을수록
        # 4순위 : 열 번호가 작을수록
        available_seat = sorted(available_seat, key=lambda x:(x[0], x[1], -x[2], -x[3]), reverse=True)[0]
        seats[available_seat[-2]][available_seat[-1]] = student[0]

    # 인덱스로 접근하기 위한 정렬
    students = sorted(students, key=lambda x: x[0])
    answer = 0
    # 인근의 좋아하는 학생 수 확인하여 점수 계산
    for row in range(N):
        for col in range(N):
            like_student = 0
            for i in range(4):
                n_row = row + direction[i][0]
                n_col = col + direction[i][1]
                if 0 <= n_row < N and 0 <= n_col < N:
                    if seats[n_row][n_col] in students[seats[row][col]-1]:
                        like_student += 1
            answer += score_dict[like_student]

    return answer

N = int(input())
students = [list(map(int, input().split())) for _ in range(N**2)]
print(solution(N, students))