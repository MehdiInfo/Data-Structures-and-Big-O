def print_items(a, b):
    for i in range(a): # O(a)
        print(i)
    for j in range(b): # O(b)
        print(j)
# O(a) + O(b) = O(a+b)
def print_items2(a, b):
    for i in range(a): # O(a)
        for j in range(b): # O(a) * O(b) = O(a * b)
            print(i,j)
print_items(5,5)
print_items2(5,5)