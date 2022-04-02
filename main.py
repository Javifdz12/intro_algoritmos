from clases.ejercicio8 import beneficio_mensual,incluir_iva,precio_sin_iva,unidades_en_staking,rot
from ejercicio9 import media_aritmetica,media,mediaponderada,x,y,z,lista,ponderadas
from ejercicio10 import area_triangulo,triangulo1,triangulo2,base,altura
from ejercicio11 import suma,salario_anual_bruto
from ejercicio12 import cuenta_bancaria

if __name__ == "__main__":
    print("el precio con iva incluido es:",incluir_iva(precio_sin_iva))
    print(f'el beneficio mensual sera de {beneficio_mensual(unidades_en_staking,rot)} dolares')
if __name__ == '__main__':
    print(f'la media aritmetica de los numeros dados es {media_aritmetica(x,y,z)}')
    print(f'La media es {media(lista)}')
    print(f'Nuestra media ponderada es {mediaponderada(lista, ponderadas)}')
if __name__ == '__main__':
    print(f'el area del triangulo es {area_triangulo(base,altura)}')
    triangulo1=triangulo1(4,3,90)
    triangulo2=triangulo2(4,3)
    triangulo1.area()
    triangulo2.area()
if __name__ == '__main__':
    print("el salario extra anual es ",suma,"por tanto el salario anual total es ",suma+salario_anual_bruto)
if __name__ == '__main__':
    cuenta_1=cuenta_bancaria("javi",500.0)
    cuenta_1.imprimir()
    cuenta_1.ingresar(400.0)
    cuenta_1.retirar(100.0)
    cuenta_1.imprimir()