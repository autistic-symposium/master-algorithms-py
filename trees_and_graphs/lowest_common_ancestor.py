'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
'''

class ThisTree:
    def lowest_common_ancestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root, p, q):

            if not root:
                return False
            
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            mid = root == p or root == q

            if mid + left + right >= 2:
                self.answer = root
            
            return left or right or mid
                
        dfs(root, p, q)
        
        return self.answer
    
