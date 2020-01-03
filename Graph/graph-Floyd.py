'''图的最短路径-Floyd
* Author: lil-q
* Date:   2019-12-31
*
* Reference: 
*   1. https://github.com/muzixing/graph_algorithm/blob/master/floyd.py
'''

def floyd(graph):
    length = len(graph)
    path = {}
    # 建立初始路径path
    for i in range(length):
        path[i] = {}
        for j in range(length):
            if i != j and graph[i][j] != float('inf'):
                path[i][j] = [i, j]
    # i为选取的中间节点
    for i in range(length):        
        # j为中间节点i的前节点
        for j in range(length):
            if i == j:
                continue
            # k为中间节点i的后节点
            for k in range(length):
                if k == i or k == j:
                    continue
                new_len = graph[j][i] + graph[i][k]
                if graph[j][k] > new_len:
                    graph[j][k] = new_len
                    new_node = i
                    # 合并路径
                    path[j][k] = path[j][i][:-1] + path[i][k]
    return graph, path


if __name__ == '__main__':
    ini = float('inf')
    graph_list = [  
                    [0, ini, -2, ini],
                    [4, 0, 3, ini],
                    [ini, ini, 0, 2],
                    [ini, -1, ini, 0]
                 ]
    new_graph, path = floyd(graph_list)
    print(new_graph, '\n\n\n', path)