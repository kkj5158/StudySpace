def solution(participant, completion):
    answer = {} # 딕셔너리 공부하기 -> 딕셔너리로 해쉬 구현 가능 하다. # answer = dict() 와 같은 방식으로도 선언이 가능하다. 
    for i in participant:
        answer[i] = answer.get(i, 0) + 1
    for j in completion:
        answer[j] -= 1
    for k in answer:
        if answer[k] : 
            return k

