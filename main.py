def fibonacci_sequence(n):
    fibonacci = [0, 1]
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

def verifica_pertence(n):
    fibonacci = fibonacci_sequence(n)
    if n in fibonacci:
        return f'O número {n} pertence à sequência de Fibonacci.'
    else:
        return f'O número {n} não pertence à sequência de Fibonacci.'

numero = int(input("Digite o número que deseja verificar se pertence à sequência de Fibonacci:"))
print(verifica_pertence(numero))