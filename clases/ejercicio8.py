#primer apartado
precio_sin_iva=float(input("¿precio sin iva?"))
print("Seleccione el tipo de IVA que quieres aplicar\n 1 - 4%\n 2 - 10%\n 3 - 21%\n")
iva = int(input())
while not iva in list(range(1, 4)):
    iva = int(input('Vuelva a introducir un valor correcto'))
if iva == 1:
    iva = 4
elif iva == 2:
    iva = 10
else:
    iva = 21
print(f'El iva que se va a aplicar es del {iva} %')
def incluir_iva(x):
    porcentaje_a_cobrar=100.0+iva
    return (x*porcentaje_a_cobrar)/100.0
print("el precio con iva incluido es:",incluir_iva(precio_sin_iva))

#segundo apartado: El segundo apartado del ejercicio 8 lo voy a aplicar a las criptomonedas ya que a mi parecer lo que me estan pidiendo es basicamente que si 
# por ejemplo hago staking durante 2 años de cardano(a traves de alguna pool) a un 5% anual y he metido en staking 1000 cardanos(suponemos que cada cardano vale 1 dolar y no se revaloriza con el tiempo) , ¿cuántos cardanos gano al mes?
#1000x5/100=50 cardanos al año, 50/12=4,16 cardanos al mes que serían 4,16 dolares.

unidades_en_staking=float(input("¿Cuantas unidades has metido en staking?"))
valor_en_dolares_por_unidad=float(input("¿Cuanto vale cada unidad en dolares?"))
rot=float(input("¿ROT?"))#rot = return of token(anual), porcentaje

def beneficio_mensual(unidades_en_staking,rot):
    beneficio_anual=(unidades_en_staking*rot)/100.0
    return (beneficio_anual/12)*valor_en_dolares_por_unidad
print(f'el beneficio mensual sera de {beneficio_mensual(unidades_en_staking,rot)} dolares')