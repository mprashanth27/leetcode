# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: optional[TreeNode], key: int) -> optional[TreeNode]:
        if (not root): # Empty tree
            return None
        
        curr = root
        while (True):
            if (key < curr.val):
                old_curr = curr
                curr = curr.left
            elif (key > curr.val):
                old_curr = curr
                curr = curr.right
            else:
                # point parent node to next node before deleting key node.
                if (curr < old_curr):
                    old_curr.left = curr
                else:
                    old_curr.right = curr
                curr.right.left = curr.left
                return root
        return root
    
obj = Solution()
print(obj.deleteNode([5,3,6,2,4,None,7], 3))