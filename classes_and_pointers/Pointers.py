print("---Integers---")
num1 = 11
num2 = num1
# what happens when we do num2 = num1
print(num1,num2)
print(id(num1),id(num2))
# when we set a new variable that gets another variable
# they point to the same memory
# once one of them is modified, a new memory adress is set
# for the changed variable
num1 = 12
print(num1,num2)
print(id(num1),id(num2))
num2 = 13
print(num1,num2)
print(id(num1),id(num2))
# integer are not mutable
# for instance when i change the value of num2 it's adress change too
print("---Dictionaries---")
dict1 = {
            'value': 11
        }
dict2 = dict1
print("Before value is updated :")
print(f"dict1 = {dict1} \ndict2= {dict2}")
print(f"&dict1 = {id(dict1)} \n&dict2= {id(dict2)}")
dict2['value'] = 22
print("After value is updated :")
print(f"dict1 = {dict1} \ndict2= {dict2}")
print(f"&dict1 = {id(dict1)} \n&dict2= {id(dict2)}")
# the value is updated in both dictionaries and they still point to the same adress
# when no variable is pointing to a dictionary
# the dictionarie is removed using garbage collection
# What happens to integers when none variable is pointing to it ?
# the intger become a candidate for garbage collection (process of freeing up memory that is no longer used by the program)
# periodically checks for objects that are no longer being used
# modifier la valeur d'une variable avec un integer crée un nouveau objet integer