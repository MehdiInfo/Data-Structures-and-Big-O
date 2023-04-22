class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True
    # O(n)
    def swap_pairs(self):
        if self.length > 0:
            node1 = self.head
            node2 = self.head.next
            self.head = node2
            print("-----------")
            while node1 is not None and node2 is not None:
                
                node1.next = node2.next
                tmp = node1.prev
                node1.prev = node2
                node2.prev = tmp
                node2.next = node1
                if node1.next is not None:
                    node1.next.prev = node1
                if tmp is not None:
                    tmp.next = node2
                node1 = node1.next
                if node1 is not None:
                    node2 = node1.next

                



my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1
    2
    3
    4
    my_dll after swap_pairs:
    2
    1
    4
    3

"""