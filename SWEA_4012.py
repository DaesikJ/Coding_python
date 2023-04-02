#-*- coding: utf-8 -*-
"""
Daesik Jang
daesik0320@gmail.com
"""

def combination(array, n):
    result = list()
    if n > len(array):
        return result
    
    if n == 1:
        result = [[i] for i in array]
    elif n > 1:
        for i in range(len(array)-n+1):
            for j in combination(array[i+1:], n-1):
                result.append([array[i]] + j)
    return result

def making_food(synergy_info, ingredient):
    # 모든 시너지들의 합 구하기
    synergy = 0
    for f1, f2 in combination(ingredient, 2):
        synergy += synergy_info[f1][f2] + synergy_info[f2][f1]
    
    return synergy

def solution(N, synergy_info):
    answer = 9e10
    # 식재료를 N // 2개씩 나누어 두 요리를 진행
    # 조합을 활용하여 N//2개 임의 선택 경우의 수 생성
    for ingredient_A in combination(list(range(N)), N//2):
        ingredient_B = list(set(range(N)) - set(ingredient_A))
        food_A = making_food(synergy_info, ingredient_A)
        food_B = making_food(synergy_info, ingredient_B)

        answer = min(answer, abs(food_A-food_B))

    return answer

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    synergy_info = [list(map(int, input().split())) for _ in range(N)]
    
    print('#{} {}'.format(test_case, solution(N, synergy_info)))
