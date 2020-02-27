# -*- coding:utf-8 -*-
'''
两个栈实现队列：一个栈负责入队，另一个负责出队
'''
class Solution:
    def __init__(self):
        self.stack1 = []  # 负责入队
        self.stack2 = []  # 负责出队
    # 入队
    def push(self, node):
        self.stack1.append(node)
    # 出队
    def pop(self):
        # return xx
        # 出栈为空时，则从入栈中导入到出栈中!
        if len(self.stack2) == 0:
            if len(self.stack1) == 0:
                return
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1[-1])  # 一次性全部入队
                self.stack1.pop()
        # 出栈不为空，出队
        xx = self.stack2[-1]
        self.stack2.pop()
        return xx

s = Solution()
s.push(10)
s.push(11)
s.push(12)
print(s.pop())
s.push(13)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())  # 排查异常