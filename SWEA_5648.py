#-*- coding: utf-8 -*-
"""
Daesik Jang
daesik0320@gmail.com
"""
from collections import defaultdict

def solution(atoms):

    answer = 0
    # 방향: 상, 하, 좌, 우
    # 동시에 움직이는 상황에 .5 단위에서 충돌할 수 있음
    dir = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]
    # 충돌할 원소가 없을때 까지 반복
    while len(atoms) > 1:
        # 좌표별 원소
        atom_location = defaultdict(list)
        # 모든 원소 이동
        for atom in atoms:
            atom_location[(atom[0] + dir[atom[2]][0], atom[1] + dir[atom[2]][1])].append(
                [atom[0] + dir[atom[2]][0], atom[1] + dir[atom[2]][1], atom[2], atom[3]]
            )
        atoms = list()
        for loc in atom_location:
            # 같은 좌표에 2개 이상의 원소가 있는 경우 충돌!
            if len(atom_location[loc]) > 1:
                for a in atom_location[loc]:
                    answer += a[-1]
            else:
                # 범위 제한
                if -1000 <= loc[0] <= 1000 and -1000 <= loc[1] <= 1000:
                    atoms += atom_location[loc]

    return answer

T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 원자들의 수
    atoms = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(test_case, solution(atoms)))