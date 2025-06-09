# Escreva um código que mostre na tela um "MENU" de opções de operações matematicas (Adição, Subtração, Divisão e Multiplicação)
# O usuário deve escolher uma das opções e depois inserir dois números para serem calculados de acordo com a operação escolhida.
# No fim mostre o resultado da operação

# OUTPUT ESPERADO:

#----------------------------------------- Exemplo 1 (Soma)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 1
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 20.0

# ----------------------------------------- Exemplo 2 (Multiplicação)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 3
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 100.0

# ----------------------------------------- Exemplo 3 (Opção inválida)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 6
# | Digite o primeiro número:1
# | Digite o segundo número:2
# | ERRO. Escolha uma opção válida.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
print('Calculadora')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão ')
opcao=int(input('Escolha uma das opções: '))
if opcao==1:
    numero=float(input('Digite o primeiro número: '))
    numero2=float(input('Digite o segundo número: '))
    print(f'O resultado é: {numero+numero2}')
elif opcao==2:
    numero=float(input('Digite o primeiro número: '))
    numero2=float(input('Digite o segundo número: '))
    print(f'O resultado é: {numero-numero2}')
elif opcao==3:
    numero=float(input('Digite o primeiro número: '))
    numero2=float(input('Digite o segundo número: '))
    print(f'O resultado é: {numero*numero2}')
elif opcao==4:
    numero=float(input('Digite o primeiro número: '))
    numero2=float(input('Digite o segundo número: '))
    print(f'O resultado é: {numero/numero2}')
else:
    numero=float(input('Digite o primeiro número: '))
    numero2=float(input('Digite o segundo número: '))
    print('ERRO. Escolha uma opção válida.')

