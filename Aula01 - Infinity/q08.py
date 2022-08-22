#Faça um programa em Python que leia três números reais e calcule a média aritmética destes números. 
#Ao final, o programa deve imprimir o resultado do cálculo.

n1 = float(input('Digite o primeiro número real: '))
n2 = float(input('Digite o segundo número real: '))
n3 = float(input('Digite o terceiro número real: '))

media = (n1 + n2 + n3) / 3

print(f'A média é: {media:.2f}')