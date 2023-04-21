my_list = [11,3,23,7]
print(my_list[0])
my_list.append(9)
my_list.pop()
# ---> O(1)
print(my_list)
# O(n) worst case because we have to slide everything
my_list.pop(0)
print(my_list)
my_list.insert(0,11)
# au bout on fait une seul oppération
# vu qu'on doit tt réindexé on une compléxité de O(n)
# Liste rajoute à la fin
# O mesure le worst case
# L'accés mémoire indexé si on veut la valeur à un endroit de la mémoire 
# O(1)
# si on cherche une valeur dans une liste
# O(n) => worst case :)
# O(n^2) => loop within a loop
# O(n) => propotional
# O(log n) => Divide and Conquer
# O(1) => constant
# https://www.bigocheatsheet.com/