class Node:
    def __init__(self,value):
        self.value= value
        self.left= None
        self.right= None
# binary tree
# full tree each node point to two or none nodes
# perfect tree each node point all levels point to two or 0 nodes
# complete tree is a tree where we feel the nodes from left two right
# a node is parent if it has child
# each node can have one parent
# a node with no children is a leaf
## binary search tree
## left child is smaller then parent and right child is greater
## for each node all that are on the right are bigger and vice versa
# Big O => divde and conquer for a 2^n - 1(aprox) nodes we do n steps
# to remove, find and add nodes which means that we do in a O(log n)
# really efficient for big trees
# worst scenario let's assume we have a none perfect tree 
# succesive line of node (only bigger) technicaly O(n)
# lookup, remove in linked_list O(n)
# there is no data structure that is perfect for all situation
class BinarySearchTree:
    def __init__(self):
        self.root = None
    # O(log n)
    def insert(self, value):
        new_node = Node(value)
        if(self.root is None):
            self.root = new_node
        else:
            tmp = self.root
            not_done = True
            print("ready")
            while(not_done):
                if(value > tmp.value):
                    if tmp.right is None:
                        tmp.right = new_node
                        not_done = False
                    else:
                        tmp = tmp.right
                elif(value < tmp.value):
                    if tmp.left is None:
                        tmp.left = new_node
                        not_done = False
                    else:
                        tmp = tmp.left
                else:
                    print("Already exist")
                    return False
            return True

def printer(parent):
    print(parent.value)
    if parent.left is not None:
        printer(parent.left)
    if parent.right is not None:
        printer(parent.right)
bst = BinarySearchTree()
bst.insert(5)
bst.insert(15)
bst.insert(25)
bst.insert(2)
bst.insert(3)
bst.insert(1)
bst.insert(1)
printer(bst.root)


