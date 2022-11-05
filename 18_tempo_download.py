# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de
# um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo
# usando este link (em minutos).

tam_arquivo = float(input('Informe o tamanho do arquivo para download (em MB): '))
vel_link = float(input('Informe a velocidade do link da internet (em Mbps): '))

temp_seg  = tam_arquivo / (vel_link/8)
temp_min = temp_seg/60

print(f'Tempo de download em segundos: {round(temp_seg)} segundos')
print(f'Tempo de download em minutos: {temp_min} minutos')

