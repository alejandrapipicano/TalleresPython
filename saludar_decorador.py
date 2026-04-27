#def decorador(funcion):
   
#def nueva_funcion():
        #print("Antes de ejecutar la función")
        #funcion()
        #print("Después de ejecutar la función")
    #return nueva_funcion



#@decorador
#3def saludar():
    #print("Hola")

#saludar()




import time

def decorador(funcion):
    def nueva_funcion():
        inicio = time.time()  # hora de inicio
        
        print("Iniciando función...")
        funcion()
        
        fin = time.time()  # hora final
        
        print("Finalizando función...")
        print("Tiempo de ejecución:", fin - inicio, "segundos")
    
    return nueva_funcion


@decorador
def saludar():
    print("Hola")
    time.sleep(2)  # simula que se demora 2 segundos


saludar()
