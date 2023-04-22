import sys
sys.path.append('Data-Structures-and-Big-O\LinkedList')
from LinkedList import Node
class Node(Node):
    def __init__(self, value):
        super().__init__(value)
        self.prev = None
class DoublyLinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    # O(1)
    def make_empty(self):
        self.length = 0
        self.head = None
        self.tail = None
    # O(n)
    def print_list(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next
    # O(1)
    def append(self, value ):
        if(self.length == 0):
            self.__init__(value)
            return True
        else:
            new_node = Node(value)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return True
    # O(1)
    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            popped = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
        else:
            popped = self.tail
            popped.prev.next = None
            self.tail = popped.prev
            self.length -= 1
        return popped
    #  O(1)
    def prepend(self, value):
        if self.length == 0:
            self.__init__(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
        return True
    #  O(1)
    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            popped = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
        else:
            popped = self.head
            popped.next.prev = None
            self.head = popped.next
            self.length -= 1
        return popped
    # O(n)
    def get(self, index):
        if self.length == 0 or index >= self.length or index < 0:
            temp = None
        else:
            temp = self.head
            i = 0
            while i < index:
                i += 1
                temp = temp.next
        return temp
    # O(n)
    def set_value(self, index, value):
        node_to_set = self.get(index)
        if node_to_set is not None:
            node_to_set.value = value
            return True
        return False
    # O(n)
    def insert(self, index, value):
        if(index == 0):
            return self.prepend(value)
        elif(index == self.length):
            return self.append(value)
        else:
            temp = self.get(index)
            if temp is not None :
                new_node = Node(value)
                temp.prev.next = new_node
                new_node.prev = temp.prev
                temp.prev = new_node
                new_node.next = temp
                self.length += 1
                return True
        return False
    # O(n)
    def remove(self, index):
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            temp = self.get(index)
            if temp is not None:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                self.length -= 1
                return temp
        return None


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

print('DLL before remove():')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() in middle:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(0).value)
print('DLL after remove() of first node:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() of last node:')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before remove():
    1
    2
    3
    4
    5

    Removed node:
    3
    DLL after remove() in middle:
    1
    2
    4
    5

    Removed node:
    1
    DLL after remove() of first node:
    2
    4
    5

    Removed node:
    5
    DLL after remove() of last node:
    2
    4

"""