start_Point = '*'
end_Point = '@'
obstacle = 'X'
arrayData = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,obstacle,0,0,0,0],[0,0,obstacle,end_Point,0,0,0],[0,0,obstacle,obstacle,obstacle,0,0],[0,0,0,0,0,0,0], [start_Point,0,0,0,0,0,0]]


for x in range(len(arrayData)):
    for y in range(len(arrayData[x])):
        print(arrayData[x][y], end =' ')
    print()
"""

def Astar_pathfinding():
"""    
    
    







