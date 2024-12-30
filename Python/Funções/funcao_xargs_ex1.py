num1 = int(input("Digite o 1º número:"))
num2 = int(input("Digite o 2º número:"))
num3 = int(input("Digite o 3º número:"))

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
        
    return f"A soma dos números inseridos é {resultado}"

print(soma(num1, num2, num3))