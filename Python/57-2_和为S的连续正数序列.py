# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # 滑动窗口法（slide window）
        if tsum < 3:
            return []
        small = 1
        big = 2
        middle = (tsum + 1)//2
        curSum = small + big
        output = []
        while small < middle:  # 序列至少有两个数字
            if curSum == tsum:
                output.append(list(range(small, big+1)))
                # 打破平衡，继续寻找下一组和为s的序列
                big += 1
                curSum += big
            elif curSum > tsum:
                curSum -= small  # 原small值划出窗口
                small += 1
            else:
                big += 1
                curSum += big  # 滑入新的big值
        return output

s = Solution()
print(s.FindContinuousSequence(15))
print(s.FindContinuousSequence(100))