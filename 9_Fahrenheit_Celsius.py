# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a
    # temperatura em graus Celsius.
    # a) C = 5 * ((F-32) / 9).
    
Fahrenheit = float(input('Informe a temperatura em graus Fahrenheit: '))
print(f'Essa temperatura em graus Celsius = {round((Fahrenheit-32)/1.8, 3)}°C')