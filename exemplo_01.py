# while true 
c=  0
while True:
    print(f'Estou no while {c+1}...')
    
    resp = input('Digite um número: ')  #sair

    if resp.upper() == 'SAIR':  #sair
        break

    c=  c + 1 