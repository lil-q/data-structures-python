'''图的遍历
* Author: lil-q
* Date:   2019-12-27
*
* Reference: 
*   1. https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)
'''


class graph:
	
    def __init__(self, num_vertexs, adjacencylists):
        self.num_vertexs = num_vertexs
        self.adjacencylists = adjacencylists

    def dfs(self, start):
        # 记录节点是否已经访问
        visited = [False] * self.num_vertexs
        res = []

        def helper(v):
            if visited[v]:
                return
            visited[v] = True
            res.append(v)
            for i in self.adjacencylists[v]:
                helper(i)
        helper(start)
        return res

    def bfs(self, start):
        visited = [False] * self.num_vertexs
        visited[start] = True
        res = [start, ]
        queue = [start, ]
        while queue:
            cur = queue.pop(0)
            for i in self.adjacencylists[cur]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    res.append(i)
        return res


if __name__ == '__main__':
    # 设置总节点数
    num_vertexs = 7
    # 建立邻接表
    adjacencylists = [[1, 2, 3],
                      [0, 4, 5],
                      [0, 6],
                      [0, 6],
                      [1, 5],
                      [1, 4, 6],
                      [2, 3, 5]]
    # 实例化
    graph = graph(num_vertexs, adjacencylists)

    t1 = graph.dfs(0)
    print("深度优先搜索：", t1)
    t2 = graph.bfs(0)
    print("广度优先搜索：", t2)

    vertexs = ["A", "B", "C", "D", "E", "F", "G"]
    t3 = list(map(lambda x: vertexs[x], t1))
    print("深度优先搜索：", t3)
    t4 = list(map(lambda x: vertexs[x], t2))
    print("广度优先搜索：", t4)
