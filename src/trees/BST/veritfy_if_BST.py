#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


from BT import BT

def is_bst(root, min=float('-inf'), max=float('inf')):
    left, right, value = root.left, root.right, root.value
    if min < value < max:
        if left and right:
            return is_bst(left, min, value) and is_bst(right, value, max)
        elif left:
            return is_bst(left, min, value)
        elif right:
            return is_bst(right, value, max)
        return True
    return False


def main():
    """
    BST
          4
       2     6
     1   3 5   7

    BT
          4
       2     6
     1   8 5   7
    """
    bst = BT(4)
    bst.insert_left(2)
    bst.insert_right(6)
    bst.get_left().insert_left(1)
    bst.get_left().insert_right(3)
    bst.get_right().insert_left(5)
    bst.get_right().insert_right(7)
    print('is_bst(bst) =', is_bst(bst))   
     
    bt = BT(4)
    bt.insert_left(2)
    bt.insert_right(6)
    bt.get_left().insert_left(1)
    bt.get_left().insert_right(8)
    bt.get_right().insert_left(5)
    bt.get_right().insert_right(7)
    print('is_bst(bt) =', is_bst(bt))
    

if __name__ == '__main__':
    main()
    
    

