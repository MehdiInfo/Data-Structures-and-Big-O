def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
print_items(10)

# here we have O(2n) for each item we are gonna do 2 operations
# so we can drop the cst which means O(2n) = O(n) = O(100n)
# comp : O(n)