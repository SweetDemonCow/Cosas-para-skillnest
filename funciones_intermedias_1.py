def iteiterarDiccionario(lista):
    for c in lista:
        print(f"nombre - {c["nombre"]}, pais - {c["pais"]}") 
def iterarDiccionario2(llave, lista):
    for c in lista:
        print(c[llave])
def info(diccionario):
    for c,valores in diccionario.items(): #dos cosas que recorren el diccionario
        contador = 0
        for v in valores:#contador de elementos
            contador = contador + 1
        print(contador,c.upper()) # imprime cantidad de elementos y su categoria
        for v in valores: #imprime elementos 
            print(v) #imprime lo que son los elementos 
        
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}    
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
matriz[1][0] = 6
print(matriz)
cantantes[0]["nombre"]= "Enrique Martin Morales"
print(cantantes[0]["nombre"])
ciudades["México"][2] = "Monterrey"
print(ciudades["México"])
coordenadas[0]["latitud"] = 9.9355431
print(coordenadas[0]["latitud"])
iteiterarDiccionario(cantantes)
iterarDiccionario2("nombre",cantantes)
info(costa_rica)