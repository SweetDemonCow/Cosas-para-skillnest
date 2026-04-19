#Core
#codigo 1
for x in range(101):#imprimir del 0 al 100
    print(x)
#codigo 2
y = 0
while y < 500:# imprimir multiplos de 2 entre 2 y 500
    y+=2
    print(y)
z = 0
#codigo 3
while z < 100: #remplazar multiplos de 5 y 10
    z+=1
    if z % 10 == 0: 
        print("baby") #inicialmente puse el orden alreves y me confundi pero ahora si
    elif z % 5 == 0:
        print ("ice ice") #a correr
    else:
        print(z)
#coigo 4
u = 0
suma = 0
while u < 500000:
    u+=2
    suma+= u
print(suma)
#codigo 5
for v in range (2024,1,-3):
    print(v)
#codigo 6
numInicial = int(input("número inicial: "))
numFinal= int(input("número Final: "))
Multiplo = int(input("Multiplo: "))
for c in range(numInicial,numFinal+1):
    if c %Multiplo == 0:
        print(c)