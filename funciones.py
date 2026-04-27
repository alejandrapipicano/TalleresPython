def saludar():
    print("Hola bienvenido a formacion")


def llego_tarde(aprendiz: str):
        respuesta = f'el aprendiz {aprendiz} llego tarde'
       # respuesta = 'el aprendiz jhon llego tarde'
        return respuesta

def dividir(a, b):
      return a/b

def multiplicar (m1, m2, m3, m4):
      return m1 * m2 * m3 * m4


def operar_numeros(n2, n3, n4, n1=1):
      return n1 + (n4*n2) - (n1+n3)
      
      


saludar()

llego_tarde('nicole')

print(llego_tarde('Nicole'))
print(llego_tarde('Robert'))

print(dividir(a=10,b=2))

resultado = multiplicar(m4=2, m1=3, m2=10, m3=1)
print(resultado)

resultado = operar_numeros(n2=3, n3=2,n4=4)
print(resultado)