class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def partition_list(self,x):
        if(self.length > 0):
            greater_node = LinkedList(0)
            smaller_node = LinkedList(0)
            greater_node.make_empty()
            smaller_node.make_empty()
            
            walker = self.head
            while(walker is not None):
                if(walker.value < x):
                    if(smaller_node.length == 0):
                        smaller_node.head = walker
                    else:
                        curr_node_s.next = walker
                    smaller_node.length += 1
                    curr_node_s = walker
                else:
                    if(greater_node.length == 0):
                        greater_node.head = walker
                    else:
                        curr_node_g.next = walker
                    greater_node.length += 1
                    curr_node_g = walker
                walker = walker.next

            if(smaller_node.length > 0):
                self.head = smaller_node.head
                if(greater_node.length > 0):
                    curr_node_s.next = greater_node.head
                    curr_node_g.next = None
                else:
                    curr_node_s.next = None
            elif(greater_node.length > 0):
                self.head = greater_node.head

ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)

print("LL before partition_list:")
ll.print_list() # Output: 3 5 8 10 2 1

ll.partition_list(5)

print("LL after partition_list:")
ll.print_list() # Output: 3 2 1 5 8 10


"""
    EXPECTED OUTPUT:
    ----------------
    LL before partition_list:
    3
    5
    8
    10
    2
    1
    LL after partition_list:
    3
    2
    1
    5
    8
    10
    
"""
