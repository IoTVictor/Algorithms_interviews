# -*- coding:UTF-8 -*-
'''
两个队列实现栈: 先进先出，实现栈的“后进先出”
'''
class Solution:
    def __init__(self):
        # 两个队列交替辅助
        self.queue1 = []
        self.queue2 = []
    # 入栈
    def push(self, x):
        if self.queue2 == []:
            self.queue1.append(x)
        else:
            self.queue2.append(x)
    # 出栈
    def pop(self):
        if self.queue1 == [] and self.queue2 == []:
            return
        # 现将队列前（length-1）个依次出队进入辅助空队列，在pop掉最后进来的元素
        if self.queue1 != []:
            length = len(self.queue1)
            for i in range(length-1):
                # queue2辅助,存储queue1先出来的元素length-1个
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop(0)  # 弹出queue1最后一个元素，至此queue1为空
        if self.queue2 != []:
            length = len(self.queue2)
            for i in range(length-1):
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop(0)

s = Solution()
s.push(10)
s.push(11)
s.push(12)
print(s.pop())
s.push(13)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())



