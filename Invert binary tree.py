# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        queue=[]
        queue.append(root)
        while(len(queue)):
            currentNode=queue.pop(0)
            currentNode.left,currentNode.right=currentNode.right,currentNode.left
            
            if(currentNode.left):
                queue.append(currentNode.left)
            if(currentNode.right):
                queue.append(currentNode.right)
        
        return root
