import matplotlib.pyplot as plt
import networkx as nx
'''二叉搜索树
* Author: lil-q
* Date:   2019-12-7
*
* Reference: 
*   1. https://zh.wikipedia.org/wiki/%E6%A0%91_(%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84)
*   2. https://python123.io/index/topics/data_structure/binary_tree
'''


class BinarySearchTree:
    
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    
    # 查找最小值
    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current
    
    # 查找最大值
    def find_max(self):
        current = self
        while current.right:
            current = current.right
        return current
  
    # 插入一个节点
    def insert(self, value):
        node = BinarySearchTree(value)
        current = self
        while True:
            if value < current.val:
                if current.left is None:
                    current.left = node
                    return
                current = current.left
            elif value > current.val:
                if current.right is None:
                    current.right = node
                    return
                current = current.right
            # 出现重复数字，返回
            else:
                return
    
    # 查找节点
    def find(self, value):
        current = self
        while current:
            if current.val == value:
                return current
            current = current.left if value < current.val else current.right
        # 此时current==None
        return current
    
    # 删除节点
    def delete(self, value):
        if self.find(value):
            if value < self.val:
                self.left = self.left.delete(value)
                return self
            elif value > self.val:
                self.right = self.right.delete(value)
                return self
                # 有两个子节点
                # 待删除结点的值替换为右子树的最小值，继续递归删除替换的节点
            elif self.left and self.right:
                val = self.right.find_min().val
                self.val = val
                self.right = self.right.delete(val)
                return self
            else:
                # 零个或一个子节点
                if self.left:
                    return self.left
                else:
                    return self.right
        else:
            return self


def mid_traverse(root):
    if root is None:
        return
    mid_traverse(root.left)
    print(root.val, end=' ')
    mid_traverse(root.right)


nums = [1, 0, 3, 4, 7, 6, 5, 8, 9, 2]
bst = BinarySearchTree(nums[0])
for num in nums:
    bst.insert(num)
max_node = bst.find_max()
min_node = bst.find_min()
print(f"Max node: {max_node.val}")
print(f"Min node: {min_node.val}")
print("中序遍历：")
mid_traverse(bst)
print("\n")
print("删除节点后的中序遍历：")
bst.delete(1)
mid_traverse(bst)



# 可视化部分
def create_graph(G, node, pos={}, x=0, y=0, layer=1):
    pos[node.val] = (x, y)
    if node.left:
        G.add_edge(node.val, node.left.val)
        l_x, l_y = x - 1 / 2 ** layer, y - 1
        l_layer = layer + 1
        create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
    if node.right:
        G.add_edge(node.val, node.right.val)
        r_x, r_y = x + 1 / 2 ** layer, y - 1
        r_layer = layer + 1
        create_graph(G, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
    return (G, pos)


def draw(node):   # 以某个节点为根画图
    graph = nx.DiGraph()
    graph, pos = create_graph(graph, node)
    fig, ax = plt.subplots(figsize=(8, 4))  # 比例可以根据树的深度适当调节
    nx.draw_networkx(graph, pos, ax=ax, node_size=300)
    plt.show()


draw(bst)
