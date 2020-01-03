'''图的最短路径-Prim
* Author: lil-q
* Date:   2020-1-1
*
* Reference: 
*   1. https://github.com/muzixing/graph_algorithm/blob/master/prim.py
'''


def prim(graph, root):
    assert type(graph) == dict

    nodes = list(graph)
    nodes.remove(root)

    visited = [root]
    path = []
    next = None

    while nodes:
        distance = float('inf')
        for s in visited:
            for d in graph[s]:
                if d in visited or s == d:
                    continue
                if graph[s][d] < distance:
                    distance = graph[s][d]
                    pre = s
                    next = d
        path.append((pre, next))
        visited.append(next)
        nodes.remove(next)

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
    path = prim(graph_dict, 'A')
    print("path:", path)
