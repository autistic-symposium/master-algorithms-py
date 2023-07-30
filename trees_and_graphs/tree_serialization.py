'''
Serialization is the process of converting a data structure or object into 
a sequence of bits so that it can be stored in a file or memory buffer, or 
transmitted across a network connection link to be reconstructed later in 
the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no 
restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and 
this string can be deserialized to the original tree structure.
'''


class Codec:

    def serialize(self, root):

        def helper(root, string):
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = helper(root.left, string)
                string = helper(root.right, string)
            return string
        
        return helper(root, '')
    
    def deserialize(self, data):

        def helper(data):
            if data[0] == 'None':
                data.pop(0)
                return None
            root_val = data.pop(0)
            root = TreeNode(root_val)
            root.left = helper(data)
            root.right = helper(data)
            return root

        root = helper(data.split(','))
        
        return root
