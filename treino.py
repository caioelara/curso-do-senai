import os

treino={
     'treino':['supino reto com barra 4x12','flexcao 4x12'],
     'data':['30/06','01/07']
}

def mostrar_treino():
    for i in range(len(treino['treino'])):
        print(f'{i+1}. {treino['treino'][i]}- Data: {treino['data'][i]}')
        
def adicionar_exercicio():
    novo_ex=input('Adicionar exercicio: ')
    nova_data=input('adicine uma data: ')
    treino['treino'].append(novo_ex)
    treino['data'].append(nova_data)
    print('//--//  //--//  //--//  //--//  //--//')
    print(f'exercicio adicionado')

def remover_exercicio():
    mostrar_treino()
    print('//--//  //--//  REMOVER TREINO  //--//  //--//')
    posicao = int(input('| Digite o número de exercicio que quer remover: '))
    treino_removido = treino['treino'].pop(posicao-1)
    treino['data'].pop(posicao-1)
    print('//--//  //--//  //--//  //--//  //--//')
    print(f'| O {treino_removido} foi removido com sucesso!')


def menu():
    while True:
        os.system('cls')
        print('//--//  //--//  TREINO  //--//  //--//')
        print('(1)-Mostrar Treino')
        print('(2)-Adicionar exercicio')
        print('(3)-Remover Treino')
        print('(4)-Sair')
        print('//--//  //--//  //--//  //--//  //--//')
        opcao=int(input('digite um numero: '))

        if opcao==1:
            mostrar_treino()
            input('precione enter...')
        elif opcao==2:
            print('//--//  //--//  ADICIONAR EXERCICIO //--//  //--//')
            adicionar_exercicio()
            print('//--//  //--//  //--//  //--//  //--//')
            input('precione enter...')
        elif opcao==3:
            remover_exercicio()
            input('precione enter...')
        elif opcao==4:
            print('vc escolheu opção 4')
        else:
            print('Opção errada =(')

            
                

        
    



menu()






