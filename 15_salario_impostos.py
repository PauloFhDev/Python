# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
# no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
# 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos
# dê:
# a) salário bruto.
# b) quanto pagou ao INSS.
# c) quanto pagou ao sindicato.
# d) o salário líquido.
# e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
    # f) + Salário Bruto : R$
    # g) - IR (11%) : R$
    # h) - INSS (8%) : R$
    # i) - Sindicato ( 5%) : R$
    # j) = Salário Liquido : R$
# k) Obs.: Salário Bruto - Descontos = Salário Líquido.

valor_hora = float(input('Quanto você ganha por hora: '))
hora_trabalhada = float(input('Informe o número de horas trabalhadas no mês: '))

salario_bruto = valor_hora * hora_trabalhada
imposto_renda = salario_bruto * 11/100
inss = salario_bruto*8/100
sindicato = salario_bruto*5/100
sal_liquido = salario_bruto - imposto_renda - inss - sindicato

print(f'a) Salário bruto: {salario_bruto}')
print(f'b) Pagou ao INSS: {inss}')
print(f'c) Pagou ao sindicato: {sindicato}')
print(f'd) salário líquido: {sal_liquido}')
print('e) descontos e o salário líquido:')
print(f'\tf) salário Bruto: R${salario_bruto}')
print(f'\tg) IR (11%): R${imposto_renda}')
print(f'\th) INSS (8%): R${inss}')
print(f'\ti) Sindicato (5%): R${sindicato}')
print(f'\tj) salário líquido: R${salario_bruto - imposto_renda - inss - sindicato}')


