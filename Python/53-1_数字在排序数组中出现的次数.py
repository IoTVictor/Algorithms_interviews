# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        count = 0
        if data != None and len(data) > 0:
            first = self.GetFirstK(data, k)
            last = self.GetLastK(data, k)
            if first > -1:
                count = last - first + 1
        return count

    def GetFirstK(self, data, k):
        low, high = 0, len(data)-1
        while low <= high:
            mid = low + (high - low)//2
            if data[mid] == k:
                if mid == 0 or data[mid-1] != k:
                    return mid
                else:
                    high = mid - 1
            elif data[mid] > k:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    def GetLastK(self, data, k):
        low, high = 0, len(data)-1
        while low <= high:
            mid = low + (high - low)//2
            if data[mid] == k:
                if mid == len(data)-1 or data[mid+1] != k:
                    return mid
                else:
                    low = mid + 1
            elif data[mid] > k:
                high = mid - 1
            else:
                low = mid + 1
        return -1
s = Solution()
data = [1, 2, 3, 3, 3, 3, 4, 5]
data2 = [1, 2, 3, 4]
data3 = [1, 2, 4]
print(s.GetNumberOfK(data, 3))
print(s.GetNumberOfK(data2, 2))
print(s.GetNumberOfK(data3, 3))
