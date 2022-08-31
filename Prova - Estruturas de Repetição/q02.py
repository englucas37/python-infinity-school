vazamentos = int(input('Digite a quantidade de vazamentos: '))
agua_desperdicada = 0
for i in range(1, vazamentos + 1):
    agua_por_hora = float(input('Digite a quantidade vazada por hora (em litros): '))
    quantidade_horas = int(input('Digite a quantidade de horas que o vazamento ficou aberto: '))
    agua_desperdicada = agua_desperdicada + agua_por_hora * quantidade_horas

print(f'A quantidade de água despediçada foi de {agua_desperdicada} litros')