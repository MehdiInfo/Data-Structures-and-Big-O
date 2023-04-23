from Stack_list import *
# O(n)
def is_balanced_parentheses(input):
    my_stack = Stack()
    is_b = True
    for i in range(0,len(input),1):
        
        if input[i] == '(':
            my_stack.push(0)
        elif input[i] == ')':
            if my_stack.is_empty():
                is_b = False
                break
            my_stack.pop()
    print(len(input) - 1, i)
    if my_stack.is_empty() and is_b:
        return True
    else:
        return False
    

balanced_parentheses = '(((())))'
unbalanced_parentheses = '(()))'

print( is_balanced_parentheses(balanced_parentheses) )

print( is_balanced_parentheses(unbalanced_parentheses) )



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False

"""