print('''
[1] - Criança
[2] - Adolescente
[3] - Adulto
   
''')

opcao = int(input("Escolha a opção: "))

match opcao:
    case 1:
        print("Criança")

    case 2:
        print("Adolescente")
    
    case 3:
        print("Adulto")
    
    case _:
        print("Opção Inválida")