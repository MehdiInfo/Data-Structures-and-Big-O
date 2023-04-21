class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    # O(1)
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    # O(n)
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    # O(1)
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
    # O(1)
    def is_empty(self):
        return self.head is None and self.tail is None and self.length == 0
    # O(1)
    def append(self, value):
        """
        Rajoute un noeud à la fin de la liste
        """
        new_node = Node(value)
        
        if(self.is_empty()):
            self.head = self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True
    # O(n)
    def pop(self):
        """
        Pop the last element of the list and returns it !
        """
        tmp = self.head
        if(self.is_empty()):
            backup = None
        elif(self.length == 1):
            self.head = None
            self.tail = None
            self.length -= 1
            backup = tmp
        else:
            while(tmp.next != self.tail):
                tmp = tmp.next
            backup = self.tail
            tmp.next = None
            self.tail = tmp
            self.length -= 1
        return backup
    # O(1)
    def prepend(self,value):
        new_node = Node(value)
        if(self.is_empty()):
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return True
    # O(1)
    def pop_first(self):
        if(self.is_empty()):
            bakcup = None
        elif(self.length == 1):
            bakcup = self.head
            self.head = None
            self.tail = None
            self.length = 0
        else:
            bakcup = self.head
            self.head = self.head.next
            self.length -= 1

        return bakcup
    
    # O(n)
    def get(self, index):
        if(index < 0 or index >= self.length):
            backup = None
        else:
            i = 0
            tmp = self.head
            while(i <= index):
                if(i == index):
                    backup = tmp
                    break
                tmp = tmp.next
                i += 1
        return backup
    # O(n)
    def set_value(self, index, value):
        node = self.get(index)
        if(node is None):
            return False
        else:
            node.value = value
            return True
    # O(n)
    def insert(self, index, value):
        if(index == 0):
            
            return self.prepend(value)
        elif(index == self.length):
            
            return self.append(value)
        else:
            before_node = self.get(index - 1)
            new_node = Node(value)
            if(before_node is not None):
                tmp = before_node.next
                before_node.next = new_node
                new_node.next = tmp
                self.length += 1
                return True
        return False
    # O(n)
    def remove(self, index):
        if(not self.is_empty()):
            if(index == 0):
                return self.pop_first()
            elif(index == self.length - 1):
                return self.pop()
            else:
                tmp1 = self.get(index - 1)
                tmp2 = self.get(index)

                if(tmp2 is not None):
                    tmp1.next = tmp2.next
                    self.length -= 1
                    return tmp2
        return None
    # O(n^2)
    def reverse_2(self):
        if(not self.is_empty()):
            if(self.length != 1):
                index = self.length - 1
                while(index >= 0):
                    self.get(index).next = self.get(index-1)
                    index -= 1
                self.head.next = None
                tmp = self.tail
                self.tail = self.head
                self.head = tmp
    # O(n)
    def reverse(self):
        if(not self.is_empty()):
            if(self.length != 1):
                tmp1 = self.head
                tmp2 = self.head.next
                tmp3 = tmp2.next
                while(tmp2 != None):
                    tmp2.next = tmp1
                    tmp1 = tmp2
                    tmp2 = tmp3
                    if(tmp3 is not None):
                        tmp3 = tmp3.next
                self.head.next = None
                tmp = self.tail
                self.tail = self.head
                self.head = tmp
                    
                        





my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print('LL before reverse():')
my_linked_list.print_list()

my_linked_list.reverse()

print('\nLL after reverse():')
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    LL before reverse():
    1
    2
    3
    4

    LL after reverse():
    4
    3
    2
    1
    
"""