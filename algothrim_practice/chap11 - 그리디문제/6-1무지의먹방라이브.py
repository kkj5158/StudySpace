#https://programmers.co.kr/learn/courses/30/lessons/42891
import heapq


def solution(food_times, k):
    
    if(sum(food_time)>=k):
        return -1
    
    q = []
    
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
        
sum_value = 0
previous = 0 

length = len(food_times) # 남은 음식의 갯수 

while sum_value + ((q[0][[0]] - previous)*length) <= k:
    now = heapq.heapop(q)[0]
    sum_value += (now-previous)*length
    length -= 1
    previous = now
    
result = sorted(q, key = lambda x : x[1])
return result[(k - sum_value)% length][1]
