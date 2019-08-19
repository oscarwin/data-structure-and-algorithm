#!/usr/bin/python
# -*- coding:utf-8 -*-

# 题目描述
# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。

class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []

        output = []
        nodeQueue = [root]
        while len(nodeQueue) != 0:
            curNode = nodeQueue[0]
            output.append(curNode.val)
            if curNode.left:
                nodeQueue.append(curNode.left)
            if curNode.right:
                nodeQueue.append(curNode.right)
            nodeQueue = nodeQueue[1:]
        
        return output

if __name__ == "__main__":
    so = Solution()
    root = None
    print(so.PrintFromTopToBottom(root))

    root = TreeNode(1)
    so = Solution()
    print(so.PrintFromTopToBottom(root))

    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    so = Solution()
    print(so.PrintFromTopToBottom(root))
        