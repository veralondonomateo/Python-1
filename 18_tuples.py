numbers = (1,2,3,4,5)
string = ('nico','zule','leo')

print(numbers[3])
print(string)
print(string.index('zule'))

#Podemos cambiar una tupla a una lista

my_list = list(string)
print(type(my_list))

string = tuple(my_list)