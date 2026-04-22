'''
정점 간선
start end weight

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


from heapq import heappop, heappush

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

        for new_w, new_n in graph[node]:
            if MST[new_n]:
                continue

            heappush(pq, (new_w, new_n))

    return min_weight


V, E = map(int, input().split())
graph = [[] for _ in range(V)]

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
    graph[e].append((w, s))

result = prim(0)
print('최소 비용 = ', result)