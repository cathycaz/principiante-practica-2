celsius_values = [-2, 34, 56, -10]

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
    # The magic happens here
   

result = list(map(celsius_to_fahrenheit, celsius_values))

print(result)

"""" EL MAPEO SE UTILIZA PARA APLICAR UNA FUNCIÓN 
A CADA ELEMENTO DE UNA LISTA Y DEVOLVER UNA NUEVA LISTA CON LOS RESULTADOS. """