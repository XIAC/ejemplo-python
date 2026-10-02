nombre = input("Ingrese nombre:")
dinero = 100
dignidad = 50
hambre = 0

print (f'Bienvenido {nombre} a este juego')
print (f'Tienes {dinero} monedas')

print (f'Que desea hacer con ese dinero?')
print ("1. Gastar")
print ("2. invertir")
print ("3. Ayudar")

opcion = input("Selecciona una opcion :")
if opcion == "1":
    dinero = 0
    dignidad -=5
    print(f"Te quedaste sin dinero :{dinero} y reduciste tu dignidad :{dignidad}")
elif opcion == "2":
    dinero += 50
    print(f"Gracias a tu inversion dispones de {dinero} monedas")
elif opcion == "3":
    dinero += 10
    dignidad += 50
    print(f"Gracias a tu ayuda dispones de {dinero} monedas y tu digniddad de  {dignidad}")

