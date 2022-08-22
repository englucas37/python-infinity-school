#Faça um programa em Python que leia dois números reais e calcule as quatro operações básicas entre estes 
#dois números, adição, subtração, multiplicação e divisão. Ao final, o programa deve imprimir os 
#resultados dos cálculos.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

soma = n1 + n2
subtracao = n1 - n2
produto = n1 * n2
divisao = n1 / n2

print(f'A soma é: {soma:.2f}')
print(f'A subtração é: {subtracao:.2f}')
print(f'A multiplicação é: {produto:.2f}')
print(f'A divisão é: {divisao:.2f}')