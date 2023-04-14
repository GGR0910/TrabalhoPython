import matplotlib.pyplot as plt

# Lista vazia para os dados sem tratamento
rawData = []

# Dicionário para armazenar os dados tratados
data = {
    'A': 0,
    'C': 0,
    'T': 0,
    'G': 0
}

# Loop para inserir os dados
while(len(rawData) < 10):
    rawData.append(input("Insira o código genético: "))
    
# Loop para tratar os dados    
for rawItem in rawData:
    # Transforma a string em uma lista de caracteres
    bases = [*rawItem.upper()]
    
    # Loop para contar as bases
    for base in bases:
    
        # Verifica se a base é válida e adiciona ao dicionário
        if base in data:
            data[base] += 1

x = ["A", "C", "T", "G"]
#y recebe os valores do Dicionário
y = [data["A"],data["C"],data["T"],data["G"]]
plt.bar(x,y)
plt.show()