# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == None or q == None:
            return
        if p == q:
            return p
        pVal = p.val
        qVal = q.val

        node = root

        while node != None:
            if qVal > node.val and pVal > node.val:
                node = node.right
            elif qVal < node.val and pVal < node.val:
                node = node.left
            else:
                # (qVal - node.val)*(pVal - node.val) <= 0
                return node
        return False

pNode1 = TreeNode(6)
pNode2 = TreeNode(2)
pNode3 = TreeNode(8)
pNode4 = TreeNode(0)
pNode5 = TreeNode(4)
pNode6 = TreeNode(7)
pNode7 = TreeNode(9)
pNode8 = TreeNode(3)
pNode9 = TreeNode(5)


pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7
pNode5.left = pNode8
pNode5.right = pNode9

S = Solution()
print(S.lowestCommonAncestor(pNode1, pNode2, pNode5).val)

