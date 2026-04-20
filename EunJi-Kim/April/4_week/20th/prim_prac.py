'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

from heapq import heappush, heappop

def prim(start_node):
    pq = [(0, start_node)]
    MST = [0] * V
    min_weight = 0

    while pq:
        weight, node = heappop(pq)

        if MST[node]:
            continue

        MST[node] = 1
        min_weight += weight

        for next_weight, next_node in graph[node]:
            if MST[next_node]:
                continue

            heappush(pq, (next_weight, next_node))

    return min_weight


V, E = map(int, input().split())
graph = [[] for _ in range(V)]

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end))
    graph[end].append((weight, start))

result = prim(4)

print(f'최소 비용 = {result}')