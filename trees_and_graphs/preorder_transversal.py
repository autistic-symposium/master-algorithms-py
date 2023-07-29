# recursive and iterative inorder traversal

def preorder_recursive(root: Optional[TreeNode]) -> list[int]:
       
        if root == None:
                return []
        
        return [root.val] + preorder_recursive(root.left) + preorder_recursive(root.right)
    

def preorder_iterative(root: Optional[TreeNode]) -> list[int]:
        
        result = []
        stack = [root]
        
        while stack:
            
            current = stack.pop()
            result.append(current.val)
            
            if current.right:
                stack.append(current.right)
                
            if current.left:
                stack.append(current.left)
            
        return result
            
