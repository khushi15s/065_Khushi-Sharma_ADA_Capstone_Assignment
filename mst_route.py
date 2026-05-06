import heapq

graph = {
    0: [(2,1),(6,3)],
    1: [(2,0),(3,2)],
    2: [(3,1)],
    3: [(6,0)]
}

def prim(start):
    visited = set()
    heap = [(0,start)]
    cost = 0
    
    while heap:
        w,node = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            cost += w
            for wt,nbr in graph[node]:
                heapq.heappush(heap,(wt,nbr))
    
    return cost

print("MST Cost:", prim(0))
