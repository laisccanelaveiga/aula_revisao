# Uma escola deseja desenvolver um sistema para calcular a média final de seus alunos. 
# Crie um programa que realize o cadastro de 10 alunos, recebendo 4 notas para cada um. 
# O sistema deverá calcular a média final de cada aluno a partir das notas informadas e,
# ao final de cada cadastro, exibir a média obtida com duas casas decimais. 

alunos = 0
medias = 0
contador = 1

while alunos < 10:
    print("\nInsira as notas abaixo: ")
    not1 = float(input("Insira a primeira nota: "))
    not2 = float(input("Insira a segunda nota: "))
    not3 = float(input("Insira a terceira nota: "))
    not4 = float(input("Insira a quarta nota: "))
    media = (not1 + not2 + not3 + not4) / 4
    print(f'Média aluno {contador}: {media}')

    alunos += 1
    contador += 1
    medias += media


media_final = medias / 10
print(f'\nA média de todos os alunos é {media_final}\n')
    