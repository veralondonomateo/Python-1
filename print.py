my_name = input('Ingresa tu nombre: ')
my_lastname = input('Ingresa tu apellido: ')
age = float(input('Cual es tu edad: '))
age = int(age)
print(f'tu nombre es {my_name} {my_lastname} y tienes {age} años')
print(type(my_name))
print(type(age))
 # Boolean dates
boolthing = True
print(type(boolthing))
print("i'm mateo")

template  = "Hi my name is {} and my last name  {} and i´m {} years old".format(my_name, my_lastname, age)
print(template)
