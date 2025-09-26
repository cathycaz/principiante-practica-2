contact = {
    "fullname": "Jane Doe",
    "phone": "321-321-4321",
    "email": "test@test.com"
}

# Your code here

for key, value in contact.items():
    print(f"{key}: {value}")


""" TAMBIEN PUEDES ACCEDER A CADA PAR CLAVE-VALOR POR SEPARADO 
for key in contact.keys():
    print(key)

for value in contact.values():
    print(value)""" 