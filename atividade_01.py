produtos = []
pesos = [] 
total = 0

while True:
    produto = input('Informe o Produto: ')

    if produto.lower() == "fim":
        break

    peso = float(input(f'Informe o peso do produto {produto}: '))
    produtos.append(produto)
    pesos.append(peso)

    peso_total = sum(pesos)
    print(produtos)
    print(pesos)
    print(peso_total)

    for e in produtos:
        print(e)

#for e, p in produtos:
# print(e)
        
    for indice, produto in enumerate(produtos):
        print(f'produto {indice+1}: {produto}, peso: {pesos[indice]} Kg')

print(f'Peso Total {peso_total}')


