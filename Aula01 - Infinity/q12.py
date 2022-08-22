"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para 
o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: 
* salário bruto. 
a. quanto pagou ao INSS. 
b. quanto pagou ao sindicato. 
c. o salário líquido. 
d. calcule os descontos e o salário líquido, conforme a tabela abaixo: 
e. + Salário Bruto : R$ 
f. - IR (11%) : R$ 
g. - INSS (8%) : R$
h. - Sindicato ( 5%) : R$ = Salário Liquido : R$ 
"""

valor_hora = float(input('Digite o valor da hora: '))
horas = int(input('Digite a quantidade de horas trabalhadas: '))
salario_bruto = valor_hora * horas

desconto_IR = 11 * salario_bruto / 100
desconto_INSS = 8 * salario_bruto / 100
desconto_sindicato = 5 * salario_bruto / 100
desconto_total = desconto_IR + desconto_INSS + desconto_sindicato
salario_liquido = salario_bruto - desconto_total

print(f'Salário bruto: R$ {salario_bruto:.2f}')
print(f'(-) IR (11%): R$ {desconto_IR:.2f}')
print(f'(-) INSS (8%): R$ {desconto_INSS:.2f}')
print(f'(-) Sindicato (5%): R$ {desconto_sindicato:.2f}')
print(f'Total de descontos: R$ {desconto_total:.2f}')
print(f'Salário líquido: R$ {salario_liquido:.2f}')