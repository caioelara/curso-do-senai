nome=input('qual eseu nome? ')
idade=float(input('qual esua idade? '))

if idade>=18:
    cardeira=input('possui carteira de motorista sim(1)nao(2): ')
    if cardeira=='1':
        print('pode dirgir')
    else:
        print('nao pode dirigir')
else:
    print('menor de idade')