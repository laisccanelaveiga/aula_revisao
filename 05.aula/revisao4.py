valor = float(input("Informe o valor: "))
print('''
Formas de Pagamento
[1] - PIX (12% de desconto)
[2] - DÉBITO (8% de desconto)
[3] - CRÉDITO (5% de desconto)
[4] - DINHEIRO (15% de desconto)
      
''')

opcao = int(input("Informe a opção de pagamento: \n"))
desconto = 0

match opcao:
    case 1:
        desconto = valor * 0.12
        print("Forma Pgto: PIX - 12% de desconto")
        
    case 2:
        desconto = valor * 0.08
        print("Forma Pgto: Débito - 8% de desconto")

    case 3:
        desconto = valor * 0.05
        print("Forma Pgto: Crédito - 5% de desconto")

    case 4:
        desconto = valor * 0.15
        print("Forma Pgto: Dinheiro - 15% de desconto")

    case _:
        print("Forma de Pagamento Inválida")

if desconto != 0:
    print("\n-----Resultado-----")
    print(f'Valor da Compra: {valor:.2f}')
    print(f'Valor do Desconto: {desconto:.2f}')
    print(f'Valor à Pagar: {valor - desconto:.2f}')

else:
    print("Digite uma opção válida")

