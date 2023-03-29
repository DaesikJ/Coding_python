#-*- coding: utf-8 -*-
"""
Daesik Jang
daesik0320@gmail.com
"""

def solution(N, A, B, C):
    """
    N (int) : 시험장 개수 (1<= N <= 1,000,000)
    A (list) : 각 시험장에 있는 응시자 수 (1 <= A <= 1,000,000)
    B (int) : 총감독관이 감시할 수 있는 응시자 수 (1 ≤ B ≤ 1,000,000)
    C (int) : 부감독관이 감시할 수 있는 응시자 수 (1 ≤ C ≤ 1,000,000)
    """
    answer = N

    for a in A:
        # 총감독관이 감독할 수 있는 응시자 수 제외
        a -= B
        # 총 감독관이 해당 시험장의 응시생들을 모두 감시하지 못하는 경우
        if a > 0: 
            # 부감독관을 추가했을 때 딱 맞게 모든 응시생을 감독할 수 있는 경우
            if a % C == 0: 
                answer += (a // C)
            else:
                answer += (a // C) + 1

    return answer

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

print(solution(N, A, B, C))