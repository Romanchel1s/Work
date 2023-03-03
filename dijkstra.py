import math
R = [(5,1,3),(7,1,2),(8,2,3),(10,2,4),(12,2,5),(6,3,5),(1,4,5)]
map = [1,2,3,4,5]
vershiny = {1: 0 ,2: math.inf,3: math.inf,4: math.inf,5: math.inf}

for r in map:
     for road in R:
          if r == road[1] and vershiny[road[2]] > road[0]+vershiny[r]:
               vershiny[road[2]] = road[0] + vershiny[r]
print('расстояние от точки 1 до:')
print(vershiny)
