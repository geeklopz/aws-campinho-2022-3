# loops
"""
# importar modulo random
import random

# mostrar mensagem de boas vindas com as regras
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# gerar numero randomico entre 1-10
number = random.randint(1,10)

print(number)

# variavel de controle
isGuessRight = False

# loop
while isGuessRight != True:
    # pede ao usuario para digitar um numero entre 1-10
    guess = input("Guess a number between 1 and 10: ")
    
    # condicional para verificar se o numero eh o correto
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        # altera a variavel de controle
        isGuessRight = True
    # caso o numero nao seja advinhado
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

"""

# mostrar numero de 1 a 10
for x in range(1,11):
    print(x)