person = {'name': 'mateo' , 'last_name' : 'vera', 'langs' : ['python','java','php'], 'age' : 17}

print(person)

person ['name'] = 'lucho'
person ['age'] += 29

print(person)

person['langs'].append('django')

print(person)

del person ['last_name']
person.pop('age')
del person['name']
person.pop('langs')
print(person)
