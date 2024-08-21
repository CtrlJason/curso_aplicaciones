num_user1 = int(input("Escribe el primer numero: "))
num_user2 = int(input("Escribe el segundo numero: "))

def DEVUELVE_MAX(num1, num2):
    if num1 > num2:
        print(f"El numero mayor es {num1}")
    elif num1 < num2:
        print(f"El numero mayor es {num2}")
    elif num1 == num2:
        print(f"El numero mayor es {num1}")
    

DEVUELVE_MAX(num_user1, num_user2)
