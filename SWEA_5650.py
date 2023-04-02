#-*- coding: utf-8 -*-
"""
Daesik Jang
daesik0320@gmail.com
"""

def game(row, col, dir, board, wormhole):
     direction = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 방향 상(0), 우(1) 하(2) 좌(3)
     # 블럭에 부딪혔을 때 바뀌는 진행방향
     block = [
         (2, 3, 1, 0),
         (1, 3, 0, 2),
         (3, 2, 0, 1),
         (2, 0, 3, 1),
         (2, 3, 0, 1),
     ]
     score = 0
     start_point = (row, col)
     while True:
        row += direction[dir][0]
        col += direction[dir][1]

        # 출발 위치로 돌아오거나, 블랙홀을 만난 경우 게임 끝, 점수 반환
        if (row, col) == start_point or board[row][col] == -1:
            return score
        elif 1 <= board[row][col] <= 5:
            dir = block[board[row][col]-1][dir]
            score += 1
        elif 6 <= board[row][col] <= 10:
            row, col = wormhole[board[row][col]][(row, col)]

def solution(N, board, wormhole):
    answer = 0
    # 시작 위치는 임의 선정 가능
    for row in range(1, N+1):
        for col in range(1, N+1):
            if board[row][col] == 0:
                for dir in range(4): # 시작 방향 4가지 중 임의 선정 가능
                    answer = max(answer, game(row, col, dir, board, wormhole))
    return answer


T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 게임판 크기 5 <= N <= 100
    wormhole = dict()
    # 보드판 상하좌우 5번 블럭 벽 만들기
    board = [[5] * (N+2)]
    for r_idx in range(1, N+1):
        board.append([5] + list(map(int, input().split())) + [5])
        # wormhole 찾기
        for c_idx, num in enumerate(board[-1]):
            if 6 <= num <= 10: # board 중 6 ~ 10은 웜홀
                if num not in wormhole:
                    wormhole[num] = (r_idx, c_idx)
                else:
                    wormhole[num] = {
                        wormhole[num]: (r_idx, c_idx),
                        (r_idx, c_idx): wormhole[num]
                    }
    board.append([5] * (N+2))
    print('#{} {}'.format(test_case, solution(N, board, wormhole)))