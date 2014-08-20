#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


def BinaryTreeList(r):
    ''' constructs a list with a root and 2 empty sublists for the children. To add a left subtree to the root of a tree, we need to insert a new list into the second position of the root list '''
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]



def main():
    '''
    3
    [5, [4, [], []], []]
    [7, [], [6, [], []]]
    '''

    r = BinaryTreeList(3)
    insertLeft(r,4)
    insertLeft(r,5)
    insertRight(r,6)
    insertRight(r,7)
    print(getRootVal(r)) 
    print(getLeftChild(r)) 
    print(getRightChild(r))    
    

if __name__ == '__main__':
    main()

