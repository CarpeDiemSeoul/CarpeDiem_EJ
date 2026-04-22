'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

from heapq import heappop, heappush

def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [INF] * V
    dists[start_node] = 0

    while pq:
        dist, node = heappop(pq)

        if dists[node] < dist:
            continue
    
        for nw, nn in graph[node]:
            next_dist = dist + nw

            if dists[nn] <= next_dist:
                continue

            dists[nn] = next_dist
            heappush(pq, (next_dist, nn))

    return dists


INF = int(21e8)

V, E = map(int, input().split())
graph = [[] for _ in range(V)]

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))

result = dijkstra(0)

print(result)