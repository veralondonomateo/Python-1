# crud = posibilidad de crear, leer y eliminar

numbers = [1,2,3,4,5,6]
print(numbers[0])

numbers [1 ] = 90
print(numbers)

# Append es para crear un nuevo elemento dentro de la lista

numbers.append(900)
print(numbers)
#Insertar un numero en una posición
numbers.insert(0, 'Hola')
print(numbers)

task = ['homwork 1' , 'homework 2']

# Concatenar dos listas
new_list = numbers + task

#La función index nos ayuda a ver la posición de un elemento
index = new_list.index('homework 2')
new_list[index] = 'Todo changed'
print(new_list)

# Elimina un elemento especifico
new_list.remove(90)
print(new_list)

# Se borra aútomaticamente el último elemento de la lista 
new_list.pop()
print(new_list)

# Poner la lista de adelante paar atras
new_list.reverse()
print(new_list)

numbers_a = [1,9,8,2,5,7]
numbers_a.sort()
print(numbers_a)

