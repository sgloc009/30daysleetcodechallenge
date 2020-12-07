# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def recur(count, curr_node):
    if(curr_node==None):
        return count
    count = count + 1
    right_count = recur(count, curr_node.right)
    left_count = recur(count, curr_node.left)
    if(right_count > left_count):
        count = right_count
    else:
        count = left_count
    return count

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return recur(0, root)
