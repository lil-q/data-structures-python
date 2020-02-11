'''并查集(Union-find algorithm)
* Author: lil-q
* Date:   2020-1-1
*
* Reference: 
*   1.https://blog.csdn.net/Guo15331092/article/details/78702686
*   2.https://www.jianshu.com/p/72da76a34db1
*   3.https://blog.csdn.net/dm_vincent/article/details/7655764
'''


class QuickFind(object):
    id = []
    count = 0

    def __init__(self, n):
        self.count = n
        for i in range(n):
            self.id.append(i)

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        return self.id[p]

    def union(self, p, q):
        idp = self.find(p)
        idq = self.find(q)
        if idp != idq:
            for i in range(len(self.id)):
                if self.id[i] == idq:  # 将q所在组内的所有节点的id都设为p的当前id
                    self.id[i] = idp
            self.count -= 1


qf = QuickFind(10)

print("QuickFind:")
print("initial id list is %s" % (",").join(str(x) for x in qf.id))

pairs = [(1, 2), (0, 1), (0, 3), (4, 7), (5, 6), (5, 7), (7, 8), (8, 9)]

for k in pairs:
    p = k[0]
    q = k[1]
    qf.union(p, q)
    print("%d and %d is connected? %s" % (p, q, str(qf.connected(p, q))))

print("final id list is %s" % (",").join(str(x) for x in qf.id))
print("count of components is: %d \n\n" % qf.count)


class QuickUnion(object):
    id = []
    count = 0

    def __init__(self, n):
        self.count = n
        for i in range(n):
            self.id.append(i)

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        while (p != self.id[p]):
            p = self.id[p]
        return p

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p != root_q:
            self.id[root_q] = root_p
            self.count -= 1


qu = QuickUnion(10)

print("QuickUnion:")
print("initial id list is %s" % (",").join(str(x) for x in qu.id))

pairs = [(1, 2), (0, 1), (0, 3), (4, 7), (5, 6), (5, 7), (7, 8), (8, 9)]

for k in pairs:
    p = k[0]
    q = k[1]
    qu.union(p, q)
    print("%d and %d is connected? %s" % (p, q, str(qu.connected(p, q))))

print("final parent list is %s" % (",").join(str(x)
                                             for x in qu.id))  # 此时输出的是每个元素的父节点，不再是组号。
print("count of components is: %d \n\n" % qu.count)


class WeightedQuickUnion(object):
    id = []
    count = 0
    sz = []

    def __init__(self, n):
        self.count = n
        for i in range(n):
            self.id.append(i)
            self.sz.append(1)  # inital size of each tree is 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        while (p != self.id[p]):
            p = self.id[p]
        return p

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p != root_q:
            if self.sz[root_p] < self.sz[root_q]:
                self.id[root_p] = root_q
                self.sz[root_q] += self.sz[root_p]
            else:
                self.id[root_q] = root_p
                self.sz[root_p] += self.sz[root_q]
            self.count -= 1


wqu = WeightedQuickUnion(10)

print("WeightedQuickUnion:")
print("initial parent list is %s" % (",").join(str(x) for x in wqu.id))

pairs = [(1, 2), (0, 1), (0, 3), (4, 7), (5, 6), (5, 7), (7, 8), (8, 9)]

for k in pairs:
    p = k[0]
    q = k[1]
    wqu.union(p, q)
    print("%d and %d is connected? %s" % (p, q, str(wqu.connected(p, q))))

print("final parent list is %s" % (",").join(str(x) for x in wqu.id))
print("size: ", wqu.sz)
print("count of components is: %d \n\n" % wqu.count)


class WeightedQuickUnionWithPC(object):
    id = []
    count = 0
    sz = []

    def __init__(self, n):
        self.count = n
        for i in range(n):
            self.id.append(i)
            self.sz.append(1)  # inital size of each tree is 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        while (p != self.id[p]):
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def union(self, p, q):
        idp = self.find(p)
        idq = self.find(q)
        if idp != idq:
            if self.sz[idp] < self.sz[idq]:
                self.id[idp] = idq
                self.sz[idq] += self.sz[idp]
            else:
                self.id[idq] = idp
                self.sz[idp] += self.sz[idq]
            self.count -= 1


wqupc = WeightedQuickUnionWithPC(10)

print("WeightedQuickUnion:")
print("initial id list is %s" % (",").join(str(x) for x in wqupc.id))

pairs = [(1, 2), (0, 1), (0, 3), (4, 7), (5, 6), (5, 7), (7, 8), (8, 9)]

for k in pairs:
    p = k[0]
    q = k[1]
    wqupc.union(p, q)
    print("%d and %d is connected? %s" % (p, q, str(wqupc.connected(p, q))))

print("final parent/id list is %s" % (",").join(str(x) for x in wqupc.id))
print("size: ", wqupc.sz)
print("count of components is: %d" % wqupc.count)
