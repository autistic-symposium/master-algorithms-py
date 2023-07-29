def max_depth(root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        return max(max_depth(root.left) + 1, max_depth(root.right)  + 1)
