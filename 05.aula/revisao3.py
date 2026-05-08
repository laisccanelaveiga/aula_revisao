print('''
Classificação de Idade

Adulto: 18 anos ou mais
Adolescente: 12 a 17 anos
Criança: 11 anos ou menos 
''')

opcao = int(input("Informe a idade: "))

match opcao:
    case opcao if 0 <= opcao < 12:
        print("Criança")

    case opcao if 12 <= opcao < 18:
        print("Adolescente")
    
    case opcao if opcao >= 18:
        print("Adulto")
    
    case _:
        print("Opção Inválida")