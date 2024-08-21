simbolo = "+"
user = int(input("Escribe el tamaño que quieres que tenga la piramide en numeros: "))


for i in range(user):
    print(simbolo)
    simbolo += "+"
for i in range(user+1):
    print(simbolo)
    simbolo = simbolo[0:-1]
        