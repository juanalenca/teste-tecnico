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