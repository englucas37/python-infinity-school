distancia = 0

while True:
    print('1 - Siga em frente')
    print('2 - Vire a esquerda')
    print('3 - Vire a direita')
    print('4 - Parar')
    direcao = input('Digite a direção desejada: ')
    print('')
    if (direcao == '1' or direcao == 'Siga em frente' or direcao == 'siga em frente'):
        distancia = distancia + 100
    elif (direcao == '2' or direcao == 'Vire a esquerda' or direcao == 'vire a esquerda'):
        distancia = distancia + 100
    elif (direcao == '3' or direcao == 'Vire a direita' or direcao == 'vire a direita'):
        distancia = distancia + 100
    elif (direcao == '4' or direcao == 'Parar' or direcao == 'parar'):
        break
    else:
        direcao = input('Entrada inválida. Digite a direção desejada: ')

print(f'A distância percorrida total é {distancia / 1000} km')