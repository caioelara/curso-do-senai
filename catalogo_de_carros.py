import os

catalogo = {
    'modelo' : ['Fusca', 'Civic'],
    'ano' : [2006, 2015],
    'preco' : [20000, 65000]
}

def mostrar_catalogo():
    barra = f'|{30*"-"}|'
    print(barra)
    print('| Lista de veículos')
    print(barra)
    for i in range(len(catalogo['modelo'])):
        print(f'| {i+1}. {catalogo['modelo'][i]}({catalogo['ano'][i]}) - R${catalogo['preco'][i]}')
    print(barra)

def adicionar_carro():
    barra = f'|{30*"-"}|'
    print(barra)
    modelo = input('| Digite o nome do modelo: ')
    ano = int(input('| Digite o ano: '))
    preco = int(input('| Digite o preço do carro: '))

    catalogo['modelo'].append(modelo)
    catalogo['ano'].append(ano)
    catalogo['preco'].append(preco)
    print(barra)
    print(f'| {modelo} adicionado com sucesso!')
    print(barra)

def remover_carro():
    mostrar_catalogo()
    barra = f'|{30*"-"}|'
    print(barra)
    posicao = int(input('| Digite o número do carro que deseja remover: '))
    modelo_removido = catalogo['modelo'].pop(posicao-1)
    catalogo['ano'].pop(posicao-1)
    catalogo['preco'].pop(posicao-1)
    print(f'| O {modelo_removido} foi removido com sucesso!')

def menu():
    while True:
        os.system('cls')
        barra = f'|{30*"-"}|'
        print(barra)
        print('| Catálogo automotivo')
        print(barra)
        print('| (1) Mostrar catálogo')
        print('| (2) Adicionar carro')
        print('| (3) Remover carro')
        print('| (4) Sair')
        print(barra)
        try:
            opc = int(input('| Digite o número da opção: '))
            if opc == 1:
                os.system('cls')
                mostrar_catalogo()
                input('| Pressione enter para continuar')

            elif opc == 2:
                os.system('cls')
                adicionar_carro()
                input('| Pressione enter para continuar')

            elif opc == 3:
                os.system('cls')
                remover_carro()
                input('| Pressione enter para continuar')

            elif opc == 4:
                print('| Encerrando o programa.')
                print(barra)
                break
            else:
                print('| Opção inválida')
                print(barra)
                input('| Pressione enter para continuar')
        except:
            print('| ERRO! INFORME UM NÚMERO DE OPÇÃO VÁLIDO! ')
            input('| Pressione enter para continuar')

menu()