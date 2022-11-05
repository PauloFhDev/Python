# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu
# peso ideal, utilizando as seguintes fórmulas:
# a) Para homens: (72.7*h) – 58
# b) Para mulheres: (62.1*h) - 44.7

h = float(input('Informe a altura da pessoa: '))
print('\nEscolha o sexo:\n \t"M" ou "m" para sexo Masculino\n \t"F" ou "f" para sexo Feminino')
sexo = str(input("Informe o sexo: "))

if sexo == 'M' or sexo == 'm':
    print(f'Peso ideal = {(72.7 * h) - 58}')
elif sexo == 'F' or sexo =='f': 
    print(f'Peso ideal = {(62.1 * h) - 44.7}')
else:
    print("Opção digitada é invalida")
