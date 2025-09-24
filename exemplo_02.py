
precos = []
total = 0
c = 0

c=  0
while True:
    resposta = input(f'Digite um número {c+1}: ')  #sair

    if resposta.upper() == 'SAIR':  #sair
        break

    preco = float(resposta)
    precos.append(preco)
    precos.sort()

    # total = total + preco
    total += preco

    
    
    print(f'Preço: {preco}')
    print(f'Valores: {precos}')
    c = c + 1 

#EXIBEO RESULTADO
print('\n======= RESUMO DA COMPRA =======')
print(f'Preços dos produtos: {precos}')
print(f'Valor Total: {total:.2}')







    