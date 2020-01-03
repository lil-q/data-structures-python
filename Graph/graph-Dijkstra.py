'''图的最短路径-Dijkstra
* Author: lil-q
* Date:   2019-12-30
*
* Reference: 
*   1. https://github.com/vterron/dijkstra/blob/master/dijkstra.py
'''
import heapq

class Graph:
    
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, name, edges):
        self.vertices[name] = edges
    
    def shortest_path(self, start, finish):
        distances = {} # 记录各点到起点距离
        previous = {}  # 记录先前路径，注意：对于求最小路径时，每个点的先前路径是唯一的。
        nodes = [] # 优先队列

        for vertex in self.vertices:
            if vertex == start: # 原点 s 的路径权重被赋为 0 （dis[s] = 0）。把到其他顶点的路径长度设为无穷大。
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = float('inf')
                heapq.heappush(nodes, [float('inf'), vertex])
            previous[vertex] = None

        while nodes:
            smallest = heapq.heappop(nodes)[1] # pop优先队列的第一个节点
            if smallest == finish: # 保存路径
                path = []
                cur = smallest
                while cur: # 循环到起点，其先前节点为None，结束
                    path.append(cur)
                    cur = previous[cur]
                path.reverse()
            if distances[smallest] == float('inf'): # 剩余所有节点已不相邻
                break      
            for neighbor in self.vertices[smallest]: # 获取近邻节点
                alt = distances[smallest] + self.vertices[smallest][neighbor] 
                if alt < distances[neighbor]: # 得到的路径比之前的近，则更新nodes，previous
                    previous[neighbor] = smallest
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
            #print(distances,nodes)
        return distances[finish], path
        
    def __str__(self):
        return str(self.vertices)

if __name__ == '__main__':
    g = Graph()
    g.add_vertex('A', {'B': 4, 'C': 2, 'D': 3})
    g.add_vertex('B', {'A': 4, 'E': 2, 'F': 5})
    g.add_vertex('C', {'A': 2, 'G': 1})
    g.add_vertex('D', {'A': 3, 'G': 2})
    g.add_vertex('E', {'B': 2, 'F': 4})
    g.add_vertex('F', {'B': 5, 'E': 4, 'G': 3})
    g.add_vertex('G', {'C': 1, 'D': 2, 'F': 3})
    print(g.shortest_path('A', 'B'))
    print(g.shortest_path('A', 'C'))
    print(g.shortest_path('A', 'D'))
    print(g.shortest_path('A', 'E'))
    print(g.shortest_path('A', 'F'))
    print(g.shortest_path('A', 'G'))