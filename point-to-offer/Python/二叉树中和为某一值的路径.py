#!/usr/bin/python
# -*- coding:utf-8 -*-

# 题目描述
# 输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.pathList = []

    def fun(self, root, expectNumber, path):
        if not root:
            return
        
        path.append(root.val)
        if root.left == None and root.right == None and root.val == expectNumber:
            self.pathList.append(path)
        
        self.fun(root.left, expectNumber - root.val, path[:])
        self.fun(root.right, expectNumber - root.val, path[:])


    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        path = []
        self.fun(root, expectNumber, path)
        return self.pathList
    
if __name__ == "__main__":
    root = TreeNode(10)
    node = TreeNode(5)
    root.left = node     
    node = TreeNode(12)
    root.right = node
    node = TreeNode(4)
    root.left.left = node
    node = TreeNode(7)
    root.left.right = node
    # node = TreeNode(1)
    # root.right.left = node 
    # node = TreeNode(4)
    # root.right.right = node
        
    so = Solution()
    ret = so.FindPath(root, 22)
    print(ret)