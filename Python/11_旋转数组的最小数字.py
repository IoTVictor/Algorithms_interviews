# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        left = 0
        right = len(rotateArray) - 1
        minVal = rotateArray[0]

        # 特例：排序数组本身，把前面0个元素搬到最后面（未反转）
        if rotateArray[left] < rotateArray[right]:
            return rotateArray[left]
        else:
            while left+1 < right:  # 必须这么写
                mid = left + (right - left)//2
                # mid = (left + right)//2
                if rotateArray[mid] > rotateArray[right]:  # 3,4,5,1,2
                    left = mid
                elif rotateArray[mid] < rotateArray[left]:  # 5,1,2,3,4
                    right = mid
                # 特例：如果三个数相等，此事只能顺序查找
                elif rotateArray[left] == rotateArray[mid] and rotateArray[mid] == rotateArray[right]:
                    for i in range(1, len(rotateArray)):
                        if rotateArray[i] < minVal:
                            minVal = rotateArray[i]
                            right = i
            minVal = rotateArray[right]
            return minVal
Test = Solution()
print(Test.minNumberInRotateArray([3, 4, 5, 1, 2]))
print(Test.minNumberInRotateArray([1, 2, 3, 4, 5]))
print(Test.minNumberInRotateArray([1, 1, 1, 0, 1]))
print(Test.minNumberInRotateArray([1, 0, 1, 1, 1]))
print(Test.minNumberInRotateArray([]))
print(Test.minNumberInRotateArray([1]))
