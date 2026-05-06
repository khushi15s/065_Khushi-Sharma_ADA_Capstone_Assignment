import itertools

graph = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]

n = len(graph)

min_cost = float('inf')

for perm in itertools.permutations(range(1,n)):
    cost = 0
    k = 0
    
    for j in perm:
        cost += graph[k][j]
        k = j
    
    cost += graph[k][0]
    min_cost = min(min_cost,cost)

print("Optimal Cost:", min_cost)
