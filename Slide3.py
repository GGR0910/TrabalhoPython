# import matplotlib.pyplot as plt

def hub():
    questao = float(input("Digite o número da questão que deseja executar: "))
    if(questao == 1):
        primeira()
    elif(questao == 2):
        segunda()
    elif(questao == 3):
       terceira()
    elif(questao == 4):
         quarta()
    elif(questao == 5):
        quinta()
    elif(questao == 6):
        sexta()
    elif(questao == 7):
        setima()
    elif(questao == 8):
        oitava()
    elif(questao == 9):
        nona()
    elif(questao == 10):
        decima()
    elif(questao == 11):
        decimaPrimeira()


def primeira():
    #to do 
    pass    

def segunda():
    total = 0
    
    #loop para imprimir os numeros pares de 0 a 1000 e somando os valores
    #o range(0,1001,2) é o mesmo que range(0,1001) de 2 em 2, pegando só os pares
    for n in range(0,1001,2):
        print(n)
        total += n
            
    print(total) 

def terceira():
    rawData = []
    #loop para inserir os dados
    while len(rawData) < 20:
        rawData.append(input("Digite a sequencia: ").upper())
    
    quantidade = []
    #loop para as sequencias
    for sequencia in rawData:
        quantidadeDaSequencia = 0
        #loop para contar as valinas na sequencia
        for i in sequencia:
            #verifica se a letra é uma valina e se a posição é par
            if(i == "V"):
                quantidadeDaSequencia += 1
        #adiciona a quantidade de valinas na lista
        quantidade.append(quantidadeDaSequencia)
    print(quantidade)
     
     
    #Solução do gpt 
        
    ## Criação das listas vazias para armazenar as sequências e as contagens de valina
    # sequencias = []
    # contagens_valina = []

    # # Loop para ler as 20 sequências de proteína
    # for i in range(20):
    #     sequencia = input("Digite a sequência de proteína: ")
    #     sequencias.append(sequencia)
        
    #     # Contagem das valinas na sequência e armazenamento na lista contagens_valina
    #     contagem = sequencia.count("V")
    #     contagens_valina.append(contagem)

    # # Impressão das contagens de valina para cada sequência
    # for i in range(20):
    #     print(f"A sequência {i+1} tem {contagens_valina[i]} valinas.")
        
    
def quarta():
    rawData = []
    
    #loop para inserir os dados
    while len(rawData) < 20:
        rawData.append(input("Digite a sequencia: ").upper())
        
    quantidade = []
    #loop para as sequencias
    for sequencia in rawData:
        quantidadeNaPalavra = 0
        
        #loop para contar as valinas na sequencia
        for i in sequencia:
            if(i == "V"):
                #verifica se a posição é par
                posicao = sequencia.find("V") + 1
                if(posicao % 2 == 0):
                    #se for par, adiciona 1 a quantidade
                    quantidadeNaPalavra += 1
                    
        #adiciona a quantidade de valinas na lista
        quantidade.append(quantidadeNaPalavra)
    print(quantidade)
    
def quinta():
    #to do 
    pass

def sexta():

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
    # plt.bar(x,y)
    # plt.show()

def setima():
    vetor = []
    #loop para inserir os dados
    while len(vetor) < 20:
        vetor.append(float(input("Digite um número: ")))
    
    maior = 0
    menor = 0
    somaTotal = 0
    #loop para as sequencias
    for n in vetor:
        #verifica se o valor é maior que o padrão ou o maior até o momento
        if(n > maior):
            maior = n
        
        #verifica se o valor é menor que o padrão ou o menor até o momento
        if(n < menor):
            menor = n
        #soma o valor ao total
        somaTotal += n
        
    #calcula a média
    media = somaTotal / len(vetor)
    print("Maior: ", maior)
    print("Menor: ", menor)
    print("Média: ", media)
        
def oitava():
    vetores = {
        "X": [],
        "Y": [],
        "Z": []
    }
    
    #loop para inserir os dados
    for vetor in vetores:
        vetores[vetor].append(float(input(f"Digite o primeiro valor de {vetor}: ")))
        vetores[vetor].append(float(input(f"Digite o segundo valor de {vetor}: ")))
        
        #calcula a força resultante do vetor e adciona na segunda posição da lista
        vetores[vetor].append(vetores[vetor][0] + vetores[vetor][1])
    
    #calcula a força resultante
    forcaResultante = (vetores["X"][2] + vetores["Y"][2] + vetores["Z"][2])
    print(f"Força resultante: {forcaResultante}")
     
def nona():
    seq = input("Digite a sequência de DNA: ")
    lista = []
    
    #loop para inserir os dados
    for i in range(40):
        s = input(f"Digite a sequência {i+1}: ")
        lista.append(s)
        
    distancias = []
    #loop para as sequencias
    for s in lista:
        dist = 0
        
        #loop para contar as distâncias
        for i in s:
            if seq != i:
                dist += 1
            else:
                break
            
        distancias.append(dist)
        
    print("Distâncias:", distancias)

def decima():
    numero = int(input("Digite um número: "))
    valor = 1
    
    #loop para calcular o fatorial
    for n in range(1, numero + 1):
        valor *= n
        
    print(valor)
    
def decimaPrimeira():
    numero = int(input("Digite um número: "))
    valor = 0
    list_of_digits = []
    
    while(numero > 0):
        list_of_digits.append(numero)
        numero -= 1
    
    #loop para calcular o fatorial
    for n in list_of_digits:
        valor += n
    print(valor)