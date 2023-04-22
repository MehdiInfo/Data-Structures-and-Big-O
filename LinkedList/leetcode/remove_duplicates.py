class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
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
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1


    # O(n^2)
    def remove_duplicates(self):
        if(self.length > 0):
            brain = self.head
            while(brain is not None):
                foot_1 = brain
                foot_2 = brain.next
                while(foot_2 is not None):
                    if(foot_2.value == brain.value):
                        foot_1.next = foot_2.next
                        foot_2 = foot_1.next
                        self.length -= 1
                    else:
                        foot_1 = foot_1.next
                        foot_2 = foot_2.next
                brain = brain.next

    # i could implement another version who does the same thing in O(n) using a hash table or a list
    # that will give me infos about if the current element was seen or not => more space complexity


my_linked_list = LinkedList(1)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list.remove_duplicates()

my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    3
    4
    
"""
