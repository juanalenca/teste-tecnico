# Questão 5: Inverter string sem usar reverse
def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

texto = input("Digite uma string para inverter: ")
print("String invertida:", inverter_string(texto))