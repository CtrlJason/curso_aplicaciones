edad_user = int(input("Cual es su edad?: "))
user_patrimonio = int(input("De cuanto es su patrimonio?:$ "))

if edad_user < 18:
    print(f"Usted tiene un patrimonio de ${user_patrimonio}. Al ser menor de edad no debe declara renta")
elif user_patrimonio >= 160232000 and edad_user < 18:
    print(f"Usted tiene un patrimonio de ${user_patrimonio} el cual excede el limite pero al ser menor de edad no debe declara renta")
elif user_patrimonio >= 160232000 and edad_user >= 18:
    print(f"Usted tiene un patrimonio de ${user_patrimonio}. Debe declarar renta")
elif user_patrimonio < 160232000 and edad_user >= 18:
    print(f"Usted tiene un patrimonio de ${user_patrimonio}, pero al ser menor a $160232000")