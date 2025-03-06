# Questão 1: Cálculo da variável SOMA
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K

print("Valor de SOMA:", SOMA)  # Saída esperada: 91



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



# Questão 3: Análise de faturamento diário
import json

def analisar_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)
    
    faturamentos = [dia["valor"] for dia in dados if dia["valor"] > 0]
    
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_mensal = sum(faturamentos) / len(faturamentos)
    dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)
    
    print(f"Menor faturamento: R${menor_faturamento:.2f}")
    print(f"Maior faturamento: R${maior_faturamento:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

# Exemplo de uso
# Salvar um JSON em um arquivo "faturamento.json" e chamar:
# analisar_faturamento("faturamento.json")



# Questão 4: Percentual de faturamento por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_faturamento = sum(faturamento_estados.values())

for estado, valor in faturamento_estados.items():
    percentual = (valor / total_faturamento) * 100
    print(f"{estado}: {percentual:.2f}%")



# Questão 5: Inverter string sem usar reverse
def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

texto = input("Digite uma string para inverter: ")
print("String invertida:", inverter_string(texto))
