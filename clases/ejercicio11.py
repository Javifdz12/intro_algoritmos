salario_anual_bruto=float(input("¿salario anual?"))
salario_semanal_bruto=salario_anual_bruto/35
salario_porhora_bruto=salario_anual_bruto/(35*52)
def crearlista():
    n = int(input('¿semanas de trabajo?'))
    lista = []
    print(f'Introduce {n} números a la lista:')
    for i in range(n):
        lista.append(float(input(f'{i+1} - ')))
        if lista[i]<35:
            lista[i]=float(input(f'{i+1} - '))
        else:
            lista[i]=lista[i]   
    return lista

lista1=crearlista()

horas_extra=[]
for i in range(len(lista1)):
    horas_extra.append(lista1[i]-35)
print(horas_extra)
    
salario_semanal_extra=[]
for i in range(len(horas_extra)):
    if 0<horas_extra[i]<=8:
        salario_semanal_extra.append(horas_extra[i]*salario_porhora_bruto*1.25)
    elif horas_extra[i]>8:
        salario_semanal_extra.append((8*salario_porhora_bruto*1.25)+((horas_extra[i]-8)*salario_porhora_bruto*1.5))
    else:
        salario_semanal_extra.append(0)
print(salario_semanal_extra)
suma=0
for i in range(len(salario_semanal_extra)):
    suma+=salario_semanal_extra[i]

print("el salario extra anual es ",suma,"por tanto el salario anual total es ",suma+salario_anual_bruto)