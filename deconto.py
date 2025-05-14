produto=input('nome do produto: ')
po=float(input("preço: "))
pd=float(input('desconto: '))
vt=po*(pd/100)         
pf=po-vt
print(f'o {produto} com {pd} de desconto:{pf}')