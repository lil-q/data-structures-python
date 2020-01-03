'''堆
* Author: lil-q
* Date:   2019-11-17
*
* Reference: 
*   https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/pai-xu-by-powcai-2/
*   https://blog.csdn.net/guoweimelon/article/details/50904346
'''


class max_heap:
    def __init__(self, nums):

        # 创建最大堆，属性heap表示一个最大堆数组
        self.heap = self.build_heap(nums)
    
    # 维护最大堆
    def adjust_heap(self, idx, max_len, nums):
        left = 2 * idx + 1
        right = 2 * idx + 2
        max_loc = idx
        if left < max_len and nums[max_loc] < nums[left]:
            max_loc = left
        if right < max_len and nums[max_loc] < nums[right]:
            max_loc = right
        if max_loc != idx:
            nums[idx], nums[max_loc] = nums[max_loc], nums[idx]
            self.adjust_heap(max_loc, max_len, nums)
   
    # 建立最大堆
    def build_heap(self, nums):
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            self.adjust_heap(i, n, nums)
        return nums
   
    # 最大堆插入
    def heap_insert(self, num):
        self.heap = self.heap+[num]
        n = len(self.heap)
        i = n-1
        while i > 0 and self.heap[(i-1)//2] < num:
            self.heap[i] = self.heap[(i-1)//2]
            i = (i-1)//2
        self.heap[i] = num
        return self.heap
   
    # 最大堆删除
    def heap_delete(self, idx,):
        n = len(self.heap)
        self.heap[idx], self.heap[-1] = self.heap[-1], self.heap[idx]
        self.adjust_heap(idx, n - 1, self.heap)
        self.heap.pop()
        return self.heap


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    maxHeap = max_heap(nums)
    print("初始堆：", maxHeap.heap)
    print("插入6： ", maxHeap.heap_insert(6))
    print("删除0： ", maxHeap.heap_delete(0))
