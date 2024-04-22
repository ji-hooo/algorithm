def solution(n, lost, reserve):
    reserve_after = set(reserve) - set(lost)
    lost_after = set(lost) - set(reserve)
    
    for i in reserve_after:
        if i - 1 in lost_after:
            lost_after.remove(i-1)
        elif i + 1 in lost_after:
            lost_after.remove(i+1)
            
    return n - len(lost_after)