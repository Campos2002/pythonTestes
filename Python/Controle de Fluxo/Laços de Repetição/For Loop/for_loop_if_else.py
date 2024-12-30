compraConfirmada = True
dadosCompra = 'Compra no valor de R$ 150,00 confirmada'

for count in range(3):
    if compraConfirmada:
        print(dadosCompra)
        print('Detalhes enviados para seu e-mail')
        break
else:
    print('A compra não pode ser finalizada')