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


def find(x):
    if x == parents[x]:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    rx = find(x)
    ry = find(y)

    if rx == ry:
        return
    
    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry



V, E = map(int, input().split())

edges = []
for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append((s, e, w))

edges.sort(key=lambda x : x[2])


parents = [i for i in range(V)]

cnt = 0
min_weight = 0

for s, e, w in edges:
    if find(s) == find(e):
        continue

    union(s, e)
    cnt += 1
    min_weight += w    
    
    if cnt >= V - 1:
        break

print(min_weight)