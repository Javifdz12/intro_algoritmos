x=float(input("escribe un numero"))
y=float(input("escribe otro numero"))
z=float(input("escribe un ultimo numero"))
def media_aritmetica(x,y,z):
    return(x+y+z)/3
print(f'la media aritmetica de los numeros dados es {media_aritmetica(x,y,z)}')


def media(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma / len(lista)

def crearlista():
    n = int(input('Tamaño de nuestra lista'))
    lista = []
    print(f'Introduce {n} números a la lista:')
    for i in range(n):
        lista.append(float(input(f'{i+1} - ')))
    return lista
lista = crearlista()
print(lista)
print(f'La media es {media(lista)}')

def mediaponderada(lista, ponderadas):
    lista_final = []
    suma1=0
    suma2=0
    for i in range(len(lista)):
        lista_final.append(lista[i]*ponderadas[i])
    for i in range(len(lista_final)):
        suma1 += lista_final[i]
    for i in range(len(ponderadas)):
        suma2 += ponderadas[i]
    return suma1/suma2

opcion = input('Si desea crear una nueva lista pulse s')
if  opcion == 's':
    crearlista()
ponderadas = []
print('Ahora vamos a introducir los coeficientes de ponderación de cada valor')
for i in range(len(lista)):
    ponderadas.append(float(input(f'{i+1} - El coeficiente de ponderación de {lista[i]} es'))) 

print(f'Nuestra media ponderada es {mediaponderada(lista, ponderadas)}')