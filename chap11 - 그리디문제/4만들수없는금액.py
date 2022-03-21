n = int(input())

coins = list(map(int, input().split))

max = sum(coins)

for i in range(1,max):
    


""" 집합 활용해서 , 범위 넓혀나가면서 그 범위까지의 원소들이 만들수 있는 숫자들을 집합으로 저장하는, 다이나믹 프로그래밍 형태 채택해서 풀이 도전해보기  """