"""for element in range(20):
  print(ele"""

for element in range(60,71):
  print(element)

my_tuple = ('julian','carlos','ernesto')
for i in my_tuple:
  print(i)

product = { 'name' : 'camisa', 'precio': '60.000'}

for key in product.values():
  print(key)

for key, velue in product.items():
  print(key, '=>', velue)

people = [
  {
  'name': 'nico',
  'age' : 'seventeen' ,
  'favorite animal' : 'dog'
  },
  {        
  'name': 'lucas',
  'age' : 'twelve' ,
  'favorite animal' : 'horse'
  },
         
  {'name': 'veronica',
  'age' : 'twenty one' ,
  'favorite animal' : 'own'
  }]

for persona in people:
  print(persona['name'])

for persona in people:
  print(persona['age'])

for persona in people:
  print(persona['favorite animal'])