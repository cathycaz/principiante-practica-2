the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here

def nueva_lista(items):
    if items == 1:
        return "wiki"
    elif items == 0:
        return "woko"

resultado= map(nueva_lista, the_bools)
print(list(resultado))
    