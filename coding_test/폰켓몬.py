# 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3
def solution(nums):
    answer = 0
    
    nums_set = set(nums)
    print(nums_set)
    if len(nums) // 2 >= len(nums_set):
        answer = len(nums_set)
    else:
        answer = len(nums) // 2
        
    
    return answer
