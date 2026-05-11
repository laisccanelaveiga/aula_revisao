# Um mercado deseja desenvolver um sistema simples para controlar os gastos de seus clientes. 
# Crie um programa que mostre o gasto de 3 pessoas, recebendo o valor de duas compras realizadas por cada uma. 
# O sistema deverá calcular o valor total gasto por cada pessoa somando as duas compras informadas. 
# Ao final de cada cadastro, o programa deverá exibir o total gasto pelo cliente. 

cliente = 0
contador = 1

while cliente < 3:
    compra1 = float(input("Insira o valor da primeira compra: "))
    compra2 = float(input("Insira o valor da segunda compra: "))
    soma = compra1 + compra2
    print(f'\n==Total de Compras==')
    print(f'Cliente {contador}: {soma}\n')

    contador += 1
    cliente += 1
        