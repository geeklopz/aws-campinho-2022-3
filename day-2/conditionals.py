# condicionais

"""
# recuperar informacao do usuario
userReply = input("Voce precisa enviar algo? (yes or no): ")

# condicional com IF (se)
if userReply == "yes":
    print("Nos podemos enviar o pacote!")
elif userReply == "no":
    print("Por favor retorne depois.")
else:
    print("Digite yes ou no")
"""

# utilizando o elif na condicional
userReply = input("Digite stamps, envelope ou copy com quantidade: ")

if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    # digitar a quantidade de copias desejadas
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
    
