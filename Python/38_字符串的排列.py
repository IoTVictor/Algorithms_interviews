# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        if len(ss) == 0:
            return []
        if len(ss) == 1:
            return list(ss)

        charList = list(ss)
        charList.sort()
        retStr = []
        for i in range(len(charList)):
            # charList[i]作为固定的首位字符
            if i > 0 and charList[i] == charList[i-1]:
                continue
            # 除首位字符外的“后面所有字符排序”（递归）
            temp = self.Permutation(''.join(charList[:i]) + ''.join(charList[i+1:]))
            for j in temp:
                retStr.append(charList[i] + j)
        return retStr
#ss = 'acb'
ss = 'aab'
S = Solution()
print(S.Permutation(ss))