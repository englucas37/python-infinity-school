#Faça um programa em Python que efetue a apresentação do valor da conversão em real (R$) de um valor lido
#em dólar (US$). Para isso, será necessário também ler o valor da cotação do dólar.

cotacao = float(input('Digite a cotação do dólar: '))
dolar = float(input('Digite o valor em dolar: '))
real = cotacao * dolar

print(f'O valor em real é R$ {real}')