# 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros
# quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário
# a quantidades de latas de tinta a serem compradas e o preço total.

tamanho_m2 = float(input('Informe o tamanho em m² da área a ser pintada: '))

litro = tamanho_m2 / 3

if litro <= 18:
    print('Compre 1(uma) lata de tinta e o preço é R$ 80.00')
elif litro <= 18*2:
    print(f'Compre 2(duas) latas de tinta e o preço é R$ {80.00*2}')
elif litro <= 18*3:
    print(f'Compre 3(três) latas de tinta e o preço é R$ {80.00*3}')
elif litro <= 18*4:
    print(f'Compre 3(três) latas de tinta e o preço é R$ {80.00*4}')





