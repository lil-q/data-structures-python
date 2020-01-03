'''图的最短路径-Prim
* Author: lil-q
* Date:   2020-1-1
*
* Reference: 
*   1. https://github.com/muzixing/graph_algorithm/blob/master/kruskal.py
*   2. https://lil-q.github.io/2020/01/02/%E6%9F%A5%E5%B9%B6%E9%9B%86-union-find-algorithm/
'''


# 最简单实现
'''
def find(id, p):
    while p != id[p]:
        p = id[p]
    return p

# 并，采用了Rank合并的优化
def union(id, p, q):
    root_p = find(id, p)
    root_q = find(id, q)
    id[root_p] = root_q

def kruskal(graph):
    assert type(graph) == dict

    edges = [(graph[u][v], u, v)
             for u in graph for v in graph[u] if graph[u][v] != float('inf')]
    path = []
    id = {u: u for u in graph}
    for _, u, v in sorted(edges):
        if find(id, u) != find(id, v):
            path.append((u, v))
            union(id, u, v)
    return path
'''


# 查，采用了Path Compression优化
def find(id, p):
    while p != id[p]:
        id[p] = id[id[p]]
        p = id[p]
    return p

# 并，采用了Rank合并的优化
def union(id, size, p, q):
    root_p = find(id, p)
    root_q = find(id, q)
    if root_p != root_q:
        if size[p] < size[q]:
            id[root_p] = root_q
            size[q] += size[p]
        else:
            id[root_q] = root_p
            size[p] += size[q]


def kruskal(graph):
    assert type(graph) == dict

    edges = [(graph[u][v], u, v)
             for u in graph for v in graph[u] if graph[u][v] != float('inf')]
    path = []
    id, size = {u: u for u in graph}, {u: 0 for u in graph}
    for _, u, v in sorted(edges):
        if find(id, u) != find(id, v):
            path.append((u, v))
            union(id, size, u, v)
    return path


if __name__ == '__main__':
    ini = float('inf')
    graph_dict = {'A': {'A': ini, 'B': 4,   'C': 2,   'D': 3,   'E': ini, 'F': ini, 'G': ini},
                  'B': {'A': 4,   'B': ini, 'C': ini, 'D': ini, 'E': 2,   'F': 5,   'G': ini},
                  'C': {'A': 2,   'B': ini, 'C': ini, 'D': ini, 'E': ini, 'F': ini, 'G': 1  },
                  'D': {'A': 3,   'B': ini, 'C': ini, 'D': ini, 'E': ini, 'F': ini, 'G': 2  },
                  'E': {'A': ini, 'B': 2,   'C': ini, 'D': ini, 'E': ini, 'F': 4,   'G': ini},
                  'F': {'A': ini, 'B': 5,   'C': ini, 'D': ini, 'E': 4,   'F': ini, 'G': 3  },
                  'G': {'A': ini, 'B': ini, 'C': 1,   'D': 2,   'E': ini, 'F': 3,   'G': ini},
                  }

    path = kruskal(graph_dict)
    print("path: ", path)
