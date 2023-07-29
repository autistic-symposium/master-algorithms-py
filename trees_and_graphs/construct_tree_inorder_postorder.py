# Given two integer arrays inorder and postorder where inorder is the inorder 
# traversal of a binary tree and postorder is the postorder traversal of the
# same tree, construct and return the binary tree.

def build_tree(inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        
        def fill_tree(i_left, i_right, inorder_map):
            
            if i_left > i_right:
                return None
            
            val = postorder.pop()
            root = TreeNode(val)

            index_here = inorder_map[val]

            root.right = fill_tree(index_here + 1, i_right, inorder_map)
            root.left = fill_tree(i_left, index_here - 1, inorder_map)
            
            return root

        inorder_map = {val: index for index, val in enumerate(inorder)}
  
        return fill_tree(0, len(inorder) - 1, inorder_map)
    
