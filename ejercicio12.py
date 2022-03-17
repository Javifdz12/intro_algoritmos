class cuenta_bancaria:

    def __init__(self, titular,fondos):
        if isinstance(titular,str):
            self.titular=titular
        else:
            self.titular="nombre"
        if isinstance(fondos,float):
            self.fondos=fondos
        else:
            self.fondos=0

    def imprimir(self):
        print("el cliente",self.titular,"tiene",self.fondos)
    def ingresar(self,x):
        if x<0:
            print("cantidad erronea")
        else:
            self.fondos=x+self.fondos
            print("ahora tienes",self.fondos)

    def retirar(self,y):
        if y>self.fondos:
            print("retirada cancelada")
        elif y<0:
            print("cantidad erronea")
        else:
            self.fondos=self.fondos-y
            print("te quedan",self.fondos)


cuenta_1=cuenta_bancaria("javi",500.0)
cuenta_1.imprimir()
cuenta_1.ingresar(400.0)
cuenta_1.retirar(100.0)
cuenta_1.imprimir()