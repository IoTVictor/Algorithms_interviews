# -*- coding:utf-8 -*-
#import copy as cy
class Solution:
    def InversePairs(self, data):
        if data == None or len(data) <= 0:
            return 0
        # 法二
        #copy = cy.deepcopy(data)
        copy = [0] * len(data)
        for i in range(len(data)):
            copy[i] = data[i]

        #copy = data  # 错误写法，[7,5,6,4]被视为一个对象，data和copy均为这个对象的引用

        count = self.InversePairsCore(data, copy, 0, len(data)-1)
        return count

    def InversePairsCore(self, data, copy, low, high):
        if low == high:
            return 0
        mid = low + (high - low)//2
        leftCount = self.InversePairsCore(data, copy, low, mid)  #
        rightCount = self.InversePairsCore(data, copy, mid+1, high)
        # 初始化变量
        count = 0
        i = mid  # i初始化为前半段最后一个数字的下标, [0, mid]
        j = high  # j初始化为后半段最后一个数字的下标, [mid+1, high]
        indexCopy = high  # Copy数组的下标

        while i >= low and j >= mid+1:
            if data[i] > data[j]:
                copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j - mid
                # print(count)
            else:
                copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1
        # 剩余数组的靠背
        while i >= low:
            copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1
        while j >= mid+1:
            copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1
        # 赋值给data
        for s in range(low, high+1):
            data[s] = copy[s]

        return leftCount + rightCount + count

    # 使用数据的index进行求解
    def InversePairs2(self, data):
        if len(data) <= 0:
            return 0
        count = 0
        copy = []
        for i in range(len(data)):
            copy.append(data[i])
        copy.sort()
        i = 0
        while len(copy) > i:
            count += data.index(copy[i])
            data.remove(copy[i])
            i += 1
        return count

s = Solution()
data = [7, 5, 6, 4]
print(s.InversePairs2(data))
print(s.InversePairs2([364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]))
