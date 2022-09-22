# multiplas variaveis
"""
myName = "Danilo"
myLastname = "Caetano"
myAge = 31

# mostrar informacao de forma organizada
print("Meu nome é: " + myName + " " + myLastname + ", tenho " + str(myAge) + " anos.")
"""

myName = input("Qual o seu nome? ")
myLastname = input("Qual o seu sobrenome? ")
myAge = input("Qual a sua idade? ")

# mostrar informacao de forma organizada
print("Meu nome é: " + myName + " " + myLastname + ", tenho " + myAge + " anos.")

# format
print("Meu nome é: {} {}, tenho {} anos.".format(myName, myLastname, myAge))

