# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('SISTEMA DE PROVAS')
nome=input('Nome do aluno: ')
nota1=float(input('Nota da primeira prova:'))
nota2=float(input('Nota da segunda prova:'))
nota3=float(input('Nota da terceira prova:'))
media=nota1+nota2+nota3
total=media/3
print(f'aluno: {nome}')
print(f'Média: {total:.2f}')
if media>=5:
    print('aluno aprovado')
else:
    print('aluno reprovado')
