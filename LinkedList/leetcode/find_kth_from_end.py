class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  
  
        
def find_kth_from_end(ll, k):
    i = 0
    slow = fast = ll.head
    while(i < k and fast is not None):
        i += 1
        fast = fast.next
    # means that the list is shorter then k
    if(i < k and fast is None):
        return None
    while(fast is not None):
        slow = slow.next
        fast = fast.next
    return slow
    





my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 5
result = find_kth_from_end(my_linked_list, k)
if(result is not None):
    print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

