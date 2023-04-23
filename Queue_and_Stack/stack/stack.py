import sys
sys.path.append("Data-Structures-and-Big-O/LinkedList")
from LinkedList import Node
class Stack:
    # O(1)
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    # O(n)
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    # O(1)
    def make_empty(self):
        self.top = None
        self.height = 0
    # O(1)
    def push(self, value):
        if(self.height == 0):
            self.__init__(value)
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
            self.height += 1
        return True
    # O(1)
    def pop(self):
        if(self.height > 0):
            tmp = self.top
            self.top = self.top.next
            self.height -= 1
            return tmp
        return None
    


    

new_stack = Stack(5)
new_stack.push(3)
new_stack.push(3)
print(f" popped : {new_stack.pop().value}")

new_stack.print_stack()