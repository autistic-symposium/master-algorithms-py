# Given the root of a binary tree, return the level order traversal of its nodes' values. 
# (i.e., from left to right, level by level).


def level_order(root: Optional[TreeNode]) -> list[list[int]]:
        
        if root is None:
            return []
        
        queue = collections.deque()
        queue.append(root)
        result = []
        
        while queue:
            
            this_level = []
            
            for _ in range(len(queue)):
                
                current = queue.popleft()
                
                if current:
                    this_level.append(current.val)
                    queue.append(current.left)
                    queue.append(current.right)
            
            if this_level:
                result.append(this_level)
        
        return result
