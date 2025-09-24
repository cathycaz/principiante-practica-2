people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name):

    updated_people = list(people)
    for person in updated_people:
        if person_name in updated_people:
            updated_people.remove(person_name)
    
    return updated_people

print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))

""" PARA ITERAR Y ENCONTRAR LA POSICION DE UN ELEMENTO
for person in people:
    if person.lower() == 'daniella':
        print(people.index(person))"""


"""NO SE HACE ASI PORQUE IRIA ELIMINANDO LOS NOMBRES DE LAS LISTAS DE ACUERDO A LA EJECUCION
 DE LOS PRINT Y LAS LISTAS SE MODIFICA AUTOMATICAMENTE PARA LA PROXIMA EJECUCION Y ES IMPORTANTE PONER LIST DELANTE 
 PORQUE SI NO SE MODIFICA LA LISTA ORIGINAL IGUALMENTE

def delete_person(name):
    for person in people:
        if name in people:
            people.remove(name)
    
    return people"""
