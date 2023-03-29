#-*- coding: utf-8 -*-
"""
Daesik Jang
daesik0320@gmail.com
"""

def solution(N, schedules):
    """
    N (int) : 퇴사 전 근무일 수 (1 ≤ N ≤ 15)
    schedules (list) : (T, P) pair 각 상담을 완료하는데 걸리는 기간 및 받을 수 있는 금액  (1 ≤ T ≤ 5, 1 ≤ P ≤ 1,000)
    """
    dp = [0 for _ in range(N+1)]

    # 날짜 뒤에서 부터 계산
    for idx in range(N-1, -1, -1):
        if idx + schedules[idx][0] > N: # idx 날짜에 상담하는 일이 퇴사일을 넘기면 진행 X
            dp[idx] = dp[idx+1]
        else: # idx 날짜에 상담을 하지 않았을 때 금액과 상담을 할 때 금액 비교
            dp[idx] = max(dp[idx+1], dp[idx+schedules[idx][0]] + schedules[idx][1])

    return dp[0]

N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, schedules))