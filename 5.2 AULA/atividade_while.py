# variável de controle
contador = 0

# o bloco será repetido enquanto contador for menor que 10

while contador < 3:
    numero = int(input("Informe um número: "))
    dobro = numero * 2
    triplo = numero * 3
    quadruplo = numero ** 2

    print(f'\nNúmero digitado : {numero}')
    print(f'Dobro : {dobro}')
    print(f'Triplo : {triplo}')
    print(f'Quadrado : {quadruplo}')

    contador += 1



