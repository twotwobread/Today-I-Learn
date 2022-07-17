# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 노드의 개수가 최대 2000개 이기 때문에 queue 자료 구조를 이용해서 null이 아닌 경우에만 담아서 처리를 해보자.
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return None
        q = deque()
        q.append((root, 1))
        result = []
        while q:
            node, index = q.popleft()
            if len(result) < index: result.append([node.val])
            else: result[index-1].append(node.val)
            
            if node.left != None: q.append((node.left, index+1))
            if node.right != None: q.append((node.right, index+1))
        return result
            
