# abrir e ler o arquivo
with open('day-3/preproinsulin-seq.txt') as f:
    insulinFile = f.read()

# mostrar os dados lidos no arquivo
print('----- DADO ORIGINAL -----')
print(insulinFile)

#funcao para limpar os dados
def clean_text(string):
    # remover o ORIGIN
    string = string.replace("ORIGIN", "")
    
    # remover o 61
    string = string.replace("61", "")
    
    # remover o 1
    string = string.replace("1", "")
    
    # remover o //
    string = string.replace("//", "")
    
    # remover os espacos em branco
    string = string.replace(" ", "")
    
    # remover a quebra de linha
    string = string.replace("\n", "")
    
    # retornar a string formatada
    return string

# limpar o dado
cleanInsulin = clean_text(insulinFile)

# mostrar o dado limpo
print('----- DADO LIMPO -----')
print(cleanInsulin)

# contagem de caracteres
print('------ CONTAGEM DE CARACTERES --------')
print('Quantidade de caracteres: {}'.format(len(cleanInsulin)))