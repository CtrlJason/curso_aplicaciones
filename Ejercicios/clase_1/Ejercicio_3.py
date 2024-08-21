num_user1 = int(input("Escribe el primer numero"))
num_user2 = int(input("Escribe el segundo numero"))

def DEVUELVE_MAX(num1, num2):
    if num1 > num2:
        print(f"El numero mayor es {num1} el numero menor es {num2}")
    elif num1 < num2:
        print(f"El numero mayor es {num2} el numero menor es {num1}")
    elif num1 == num2:
        print(f"El numero {num1} es igual que el numero {num2}")
    

DEVUELVE_MAX(num_user1, num_user2)
