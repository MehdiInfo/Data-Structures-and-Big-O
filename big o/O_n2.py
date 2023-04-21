def print_items(n):
    for i in range(n):
        for j in range(n):
            # nested for loop - boucle imbriquée
            print(i,j)
print_items(10)
# pour chaque item de n on fera n opérations 
# ce qui fait qu'on aura o(n*n) = o(n^2) moins efficace d'un point de vue
# de complexité temporelle
# comp : O(n^2)