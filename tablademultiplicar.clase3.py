class tablademultiplicar:
    def __init__(self, numero):
        self.numero = numero

    def generartabla(self):
        for i in range(1,11):
            resultado = self.numero*i
            print(f"{self.numero} x {i} = {resultado}")


def main():
    numero = int(input("ingrese un numero: "))
    mitabla = tablademultiplicar(numero)
    mitabla.generartabla()
    
if __name__ == "__main__":
    main()
