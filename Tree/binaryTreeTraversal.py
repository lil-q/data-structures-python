'''二叉树遍历和序列化
* Author: lil-q
* Date:   2019-12-7
*
* Reference: 
*   1. https://zh.wikipedia.org/wiki/%E6%A0%91_(%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84)
*   2. https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/die-dai-he-di-gui-by-powcai/
*   3. https://zhuanlan.zhihu.com/p/26418233
'''


class Node(object):
    def __init__(self, value):
        self.val = value
        self.left = None  # 左节点
        self.right = None  # 右节点


'''
# 建一个二叉树
#           1 
#         /   \ 
#        2     3
#       / \   / \
#      4   5 6   7
'''
root = Node(1)
stack = [root]
value = 2
for i in range(3):
    cur = stack.pop(0)
    cur.left = Node(value)
    stack.append(cur.left)
    value += 1
    cur.right = Node(value)
    stack.append(cur.right)
    value += 1


# 前序遍历_递归
def preorderTraversal(root):
    if not root:
        return
    print(root.val, end=' ')
    preorderTraversal(root.left)
    preorderTraversal(root.right)


'''
# 前序遍历_迭代
# 方法一，
def preorderTraversalIter(root):
    if not root:
        return res
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end = ' ')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
'''


# 方法二
def preorderTraversalIter(root):
    if not root:
        return res
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            print(root.val, end=' ')
            root = root.left
        root = stack.pop()
        root = root.right


# 中序遍历_递归
def inorderTraversal(root):
    if not root:
        return
    inorderTraversal(root.left)
    print(root.val, end=' ')
    inorderTraversal(root.right)


# 中序遍历_迭代
def inorderTraversalIter(root):
    if not root:
        return res
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        print(root.val, end=' ')
        root = root.right


# 后序遍历_递归
def postorderTraversal(root):
    if not root:
        return
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.val, end=' ')


'''
# 后序遍历_迭代
# 方法一
def postorderTraversalIter(root):
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left :
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.val)
        return res[::-1]
'''


# 方法二
def postorderTraversalIter(root):
    res = []
    if not root:
        return res
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            res.append(root.val)
            root = root.right
        root = stack.pop()
        root = root.left
    return res[::-1]


# 层序遍历
def levelOrderTraversal(root):
    # 使用列表模拟先进先出队列queue
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        print(node.val, end=' ')


# 测试
print("\n前序遍历_递归：")
preorderTraversal(root)
print("\n前序遍历_迭代：")
preorderTraversalIter(root)
print("\n中序遍历_递归：")
inorderTraversal(root)
print("\n中序遍历_迭代：")
inorderTraversalIter(root)
print("\n后序遍历_递归：")
postorderTraversal(root)
print("\n后序遍历_迭代：")
for num in postorderTraversalIter(root):
    print(num, end=' ')
print("\n层序遍历：")
levelOrderTraversal(root)



# 序列化
def reconstruct(root):
    if not root:
        return res
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end=' ')
        if node.right:
            stack.append(node.right)
        else:
            print('#', end=' ')
        if node.left:
            stack.append(node.left)
        else:
            print('#', end=' ')


print("\n前序序列化：")
reconstruct(root)
