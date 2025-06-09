# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
dias=int(input('Por quantos dias o carro foi alugado: '))
km=float(input('Quantos km o carro rodou: '))
total_d=dias*60
todal_km=km*0.15
print(f'Você andou {km}km por {dias} dias, então o preço a pagar é R${total_d+todal_km}.')
