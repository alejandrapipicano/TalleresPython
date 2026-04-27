
def calcular_nivel(python, matematicas):
    return (python + matematicas) / 2


def evaluar(nivel, experiencia):
    if nivel >= 85 and experiencia == True:
        return "Acceso Total"
    
    elif nivel >= 70:
        return "Acceso Limitado"
    
    else:
        return "Acceso Denegado"



def sistema_ia(nombre, python, matematicas, experiencia=False):
    nivel = calcular_nivel(python, matematicas)  
    decision = evaluar(nivel, experiencia)        
    
    return f"{nombre}: {decision}"



print(sistema_ia(nombre="Ronal", python=90, matematicas=95, experiencia=True))
print(sistema_ia(nombre="Aleja", python=70, matematicas=75))
print(sistema_ia(nombre="Alexander", python=50, matematicas=60))
