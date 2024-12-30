# RETURN salva o dado, assim podendo usa-lo em uma variável.

def soma():
    numA = 2
    numB = 3
    return numA + numB

result = soma() + 10
print(result)

# PRINT apenas imprimi o dado na tela, não sendo possível usa-lo em outra parte do código.

def soma2():
    numA = 6
    numB = 4
    print(numA + numB)    
    
soma2()