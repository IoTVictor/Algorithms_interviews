# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        if pushV == [] or popV == []:
            return False
        stack = []  # 辅助栈
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if len(stack) == 0:
            return True
        else:
            return False

pushV = [1, 2, 3, 4, 5]
popV = [4, 5, 3, 2, 1]
popVF = [4, 5, 2, 1, 3]
S = Solution()
print(S.IsPopOrder(pushV, popVF))
