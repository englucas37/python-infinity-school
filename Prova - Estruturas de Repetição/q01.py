numero_inicial = int(input('Digite o número inicial: '))
numero_final = int(input('Digite o número final: '))
primos = []

def ehPrimo(numero):
    divisores = 0
    for i in range (1, numero+1):
        if (numero % i == 0):
            divisores += 1
    
    if divisores == 2:
        primos.append(numero)

for i in range(numero_inicial, numero_final):
    ehPrimo(i)

print(f'Os números primos entre {numero_inicial} e {numero_final} são {primos}')