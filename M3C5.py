# Ejercicio_1
numeros = [1, 2, 3]
for num in numeros:
    print(num)

# Ejercicio_2
def suma(num_uno, num_dos, num_tres):
    suma = num_uno + num_dos + num_tres
    print(suma)     

suma(1,2,3)

# Ejercicio_3
suma = lambda num_uno, num_dos, num_tres: num_uno + num_dos + num_tres
resultado = suma(1,2,3)

print(resultado)

# Ejercicio_4_versión_1
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']
nombre = 'Enrique' 
if nombre in lista_nombre:
    print('Está')
else:
    print('No está')


# Ejercicio_4_versión_2
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']
nombre = 'Enrique'
encontrado = False

for nom in lista_nombre:
    if nom == nombre:
        encontrado = True  
if encontrado:
    print(f'{nombre} está en la lista.')
else:
    print(f'{nombre} no está en la lista.')
