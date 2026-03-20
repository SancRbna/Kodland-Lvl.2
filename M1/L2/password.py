import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length = int(input("Ingresa el largo de la contraseña: "))

password = ""

for i in range(length):

    password += random.choice(characters)

print("Tu contraseña es: " + password)
