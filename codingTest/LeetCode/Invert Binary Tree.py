# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        q = deque()
        q.append(root)
        while q:
            now = q.popleft()
            if now.left != None or now.right!= None:
                temp = now.left
                now.left = now.right
                now.right = temp
            if now.left != None:
                q.append(now.left)
            if now.right != None:
                q.append(now.right)
        return root
