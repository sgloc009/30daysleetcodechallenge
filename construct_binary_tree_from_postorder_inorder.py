class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return(self.recur(postorder, inorder))
    
    def recur(self, postorder, inorder):
        if(len(postorder)==0):
            return
        tree = TreeNode()
        i = inorder.index(root_node)
        lhs_i = inorder[:i]
        rhs_i = inorder[i+1:]
        lhs_p = postorder[:len(lhs_i)]
        rhs_p = postorder[len(lhs_i):-1]
        tree.val = root_node
        tree.left = self.recur(lhs_p,lhs_i)
        tree.right = self.recur(rhs_p,rhs_i)
        return tree
