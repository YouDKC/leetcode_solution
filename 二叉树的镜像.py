# https://www.nowcoder.com/ta/coding-interviews

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root: return
        # 如果少了这一行，就只有60%的正确率，最近笔试总是出现正确率不是100%的情况，
        # 分析这里主要是如果左右节点为空的话，根本不存在root.left和root.right，这种极端情况应该考虑在内
        root.left,root.right = root.right,root.left
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)