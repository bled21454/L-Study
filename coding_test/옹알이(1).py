# 프로그래머스 - 옹알이(1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120956
from itertools import permutations
all = []
def solution(babbling):
    answer = 0
    a = ["aya", "ye", "woo", "ma" ]
    for i in range(1,5):
        for j in permutations(a, i):
            tmp = ''
            for k in j:
                tmp += k
            all.append(tmp)

    for b in babbling:
        if b in all:
            answer += 1
    
    return answer
