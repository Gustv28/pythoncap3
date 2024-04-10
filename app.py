#lista de frutas vermelhas

frutas_vermelhas = {'1': "morango", '2': "cereja",'3': "framboesa"}
print("Retornando uma lista de frutas")
for valor in frutas_vermelhas.values():
    print(valor)

print("Retornando lista com chave e seus valores")
for chave, valor in frutas_vermelhas.items():
    print(f"{chave}: {valor}")