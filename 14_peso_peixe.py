# 14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o
# rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
# estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa
# de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
# variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de
# quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados
# do programa com as mensagens adequadas.

peso_estabelecido = 50
multa_por_kg = 4.00

peso_pesca = float(input('Informe o valor do peso pescado(em kg):'))

if peso_pesca > 50:
    excesso = peso_pesca - peso_estabelecido
    multa = excesso * multa_por_kg
    print(f'João pescou {excesso}kg além do permitido e vai pagar multa de R$ {multa} reais.')
else:
    print(f'joão pescou {peso_pesca} kg, peso permitido pelo regulamento')