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
