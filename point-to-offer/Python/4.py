# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return

        tree = TreeNode(pre[0])

        if len(pre) == 1:
            return tree
        
        mid = tin.index(pre[0])

        tree.left = self.reConstructBinaryTree(pre[1:(mid + 1)], tin[0:mid])
        tree.right = self.reConstructBinaryTree(pre[(mid + 1):], tin[(mid + 1):])
        return tree