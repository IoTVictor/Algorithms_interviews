'''
heapq默认最小堆
heappush(heap,item) #往堆中插入一条新的值
item = heappop(heap) #从堆中弹出最小值
heappushpop() #顾名思义，将值插入到堆中同时弹出堆中的最小值
'''
# -*- coding:utf-8 -*-
from heapq import *
class Solution:
    def __init__(self):
        self.heaps = [], []

    def Insert(self, num):
        # 大根堆存比中位数小的数，小根堆存比中位数大的堆，中位数就是大顶堆的根节点与小顶堆的根节点和的平均数
        small, large = self.heaps
        # print('****插入', num, '****')
        # print('small:', small, ',large:', large)
        heappush(small, -heappushpop(large, num))  # 将num放入大根堆large，并弹出大根堆large的最小值，取反，放入小根堆small
        # print('2small:', small, ',2large:', large)
        if len(large) < len(small):
            heappush(large, -heappop(small))  # 弹出small中最小的值，取反，放入large
        # print('3small:', small, ',3large:', large)

    def GetMedian(self, ss=None):
        # write code here
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0


t = Solution()
t.Insert(5)
print(t.GetMedian())
t.Insert(2)
print(t.GetMedian())
t.Insert(3)
print(t.GetMedian())
t.Insert(4)
print(t.GetMedian())
t.Insert(1)
print(t.GetMedian())
t.Insert(6)
print(t.GetMedian())
t.Insert(7)
print(t.GetMedian())
t.Insert(0)
print(t.GetMedian())
t.Insert(8)
print(t.GetMedian())