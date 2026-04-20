# Lista de aeropuertos (diccionarios) y tuplas 
aeropuertos = [
    {"codigo": "SKBO", "ciudad": "Bogota", "pais": "Colombia", "coord": (4.76, -54.1)},
    {"codigo": "SKRG", "ciudad": "Medellin", "pais": "Colombia", "coord": (6.19, -35.42)},
    {"codigo": "SKCL", "ciudad": "Cali", "pais": "Colombia", "coord": (3.59, -76.53)}
]

#LISTA DE AEROPUERTOS 
print("AEROPUERTOS:")
for aeropuerto in aeropuertos:
    print(aeropuerto)

# Agregar un nuevo aeropuerto
nuevo = {
    "codigo": "SKSM",
    "ciudad": "Santa Marta",
    "pais": "Colombia",
    "coord": (11.1, -74.2)
}

aeropuertos.append(nuevo)


#lista actualizada
for aeropuerto in aeropuertos:
    print(aeropuerto)
    

# Set de códigos OACI
print("Sets")
codigos = {"SKBO", "SKRG", "SKCL", "SKBO"}
print(codigos)

#Agrego
codigos.add("SKCG")
print(codigos)

#Elimino
codigos.remove("SKRG")
print(codigos)



#verifico si el codigo existe
print("SKBO" in codigos)

