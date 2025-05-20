print('escolha a conversao')
print('1-coversao em dolar')
print('2-conversao em reais')
opcao= int(input("qual escoleu:"))
valor=float(input('valor do dolar: '))
if opcao == 1:
    dollares=float(input('valor pra converder: '))
    print(f'valor convedito: ${dollares*valor:.2f}')
elif opcao== 2:
    reais=float(input('valor pra converder: '))
    print(f'valor convedito: R${reais/valor:.2f}')
else:
    print('errrrrrrrrrrrrrrrrrooooooooooooouuuuuuuuuu')