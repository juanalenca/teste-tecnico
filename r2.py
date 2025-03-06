# Questão 2: Verificar se um número pertence à sequência de Fibonacci
def pertence_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero or numero == 0

num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
if pertence_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")