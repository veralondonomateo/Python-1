names_class_math = ['carlos','esteban','juliana','camila','gonzalo','estefa','stiven','alejo','katerine','pablo', 'paulina']
notes_class = [4.6,4.1,3.0,4.9,5.0,4.5,4.8,2.3,3.1,3.0,1.2]
print(names_class_math[2])

names_class_math.append('mateo')
print(names_class_math)

names_class_math.insert(0,'Juan')
print(names_class_math)

new_names = names_class_math.index('carlos')
names_class_math[new_names] = 'ESTEBAN'
print(names_class_math)

notes_class.sort()
print(notes_class)

notes_class.reverse()
print(notes_class)
