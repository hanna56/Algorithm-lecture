#피보나치 순열 구현
def solution(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return solution(x-1)+solution(x-2)
