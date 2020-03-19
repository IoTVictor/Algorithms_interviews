# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if numbers == None or len(numbers) <= 0:
            return False
        for i in numbers:
            if i < 0 or i > len(numbers)-1:
                return False
        for i, val in enumerate(numbers):
            if i != val:
                if numbers[numbers[i]] == val:
                    duplication[0] = val
                    return True
                numbers[i] = numbers[val]
                numbers[val] = val  # val放在对应位
        return False

test = [2, 3, 1, 0, 2, 5, 3]
s = Solution()
dupulication = [0]
print(s.duplicate(test, dupulication))

