import pwinput

password = '12345@'

def loginValidation():
    for enviar in range(3):    
        
        passwordInputed = pwinput.pwinput('Digite sua senha: ')
        count = 2 - enviar
        
        if password != passwordInputed:
            print(f'Senha incorreta. {count} tentativas restantes.')
            if count == 0:
                print('Usuário Bloqueado')
        else:
            print('Acesso concedido.')
            break
        
loginValidation()