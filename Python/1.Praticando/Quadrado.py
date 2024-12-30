linhas = int(input('Digite o número de linhas: '))
colunas = int(input('Digite o número de colunas: '))
pergunta = input(f'Digite o carctere à se repetir: ')
caractere = str(' ' + pergunta + ' ')

for l in range(linhas):
    for c in range(colunas):
        print(caractere, end='')
    print()