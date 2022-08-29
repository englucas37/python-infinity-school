print('---------- CALCULADORA ----------')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print('---------------------------------')
print('')
print('---------- OPERADORES -----------')
print('1: SOMA +')
print('2: SUBTRAÇÃO -')
print('3: MULTIPLICAÇÃO *')
print('4: DIVISÃO /')
print('')
operador = str(input('Digite o operador desejado: '))

print('---------------------------------')
print('')
print('---------- RESULTADO ------------')

while True:
    if operador == '+' or operador == '1' or operador == 'soma' or operador == 'Soma' or operador == 'adição' or operador == 'Adição' or operador == 'adicao' or operador == 'Adicao':
        print(f'A soma vale {n1 + n2}')
        break
    elif operador == '-' or operador == '2' or operador == 'subtração' or operador == 'Subtração' or operador == 'subtracao' or operador == 'Subtracao':
        print(f'A subtração vale {n1 - n2}')
        break
    elif operador == '*' or operador == '3' or operador == 'multiplicação' or operador == 'Multiplicação' or operador == 'multiplicacao' or operador == 'Multiplicacao':
        print(f'A multiplicação vale {n1 * n2}')
        break
    elif operador == '/' or operador == '4' or operador == 'divisão' or operador == 'Divisão' or operador == 'divisao' or operador == 'Divisao':
        print(f'A divisão vale {n1 / n2}')
        break
    else:
        print('Operador incorreto. Digite novamente.')
        operador = str(input('Digite o operador desejado: '))
print('---------------------------------')