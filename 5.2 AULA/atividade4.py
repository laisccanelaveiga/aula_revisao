
for aluno in range(10):
    print(f'Aluno {aluno + 1}')
    
    soma = 0
    for nota in range (4):
        valor_nota = float(input(f"Insira a nota {nota + 1} do aluno: "))
        soma += valor_nota
    
    media = soma / 4
    print(f'\nA média do aluno {aluno + 1} é {media:.2f}\n')

