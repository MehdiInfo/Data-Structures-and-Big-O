import sys
sys.path.append("Data-Structures-and-Big-O/LinkedList")
from LinkedList import Node
class Queue:
    # O(1)
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    # O(n)
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    # O(1)
    def make_empty(self):
        self.first = None
        self.last = None
        self.length = 0
    # O(1)
    def enqueue(self, value):
        if(self.length == 0):
            self.__init__(value)
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node
            self.length += 1
        return True
    # O(1)
    def dequeue(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            tmp = self.first
            self.first = None
            self.last = None
        else:
            tmp = self.first
            self.first = self.first.next
        self.length -= 1
        return tmp



my_queue = Queue(1)
print(f"Dequeued : {my_queue.dequeue().value}")
my_queue.print_queue()

