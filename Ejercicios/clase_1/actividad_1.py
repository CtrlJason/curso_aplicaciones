user_edad = int(input("Cual es su edad?: "))
if user_edad < 12:
    print("Eres un niño")
elif user_edad < 18:
    print("Eres un adolescente")
elif user_edad < 64:
    print("Eres un adulto")
elif user_edad > 64:
    print("Eres un adulto mayor")