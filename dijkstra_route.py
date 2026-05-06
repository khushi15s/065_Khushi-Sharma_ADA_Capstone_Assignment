import heapq

graph = {
    0:[(1,10),(2,15),(3,20)],
    1:[(0,10),(3,25)],
    2:[(0,15),(3,30)],
    3:[(1,25),(2,30)]
}

def dijkstra(start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    
    pq = [(0,start)]
    
    while pq:
        d,node = heapq.heappop(pq)
        
        for neighbor,weight in graph[node]:
            if d + weight < dist[neighbor]:
                dist[neighbor] = d + weight
                heapq.heappush(pq,(dist[neighbor],neighbor))
    
    return dist

print(dijkstra(0))
