
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


def primeira():
    cadeia = input("Digite a cadeia: ")
    cadeiaRelativa = ""
    for pepitideo in cadeia:
        if pepitideo == "A":
            cadeiaRelativa += "T"
        elif pepitideo == "T":
            cadeiaRelativa += "A"
        elif pepitideo == "C":
            cadeiaRelativa += "G"
        elif pepitideo == "G":
            cadeiaRelativa += "C"
    print(cadeiaRelativa)
    
def segunda():
    primeiraCadeia = input("Digite a primeira cadeia: ")
    segundaCadeira = input("Digite a segunda cadeia: ")
    
    numeroDeDIferencas = 0
    tamanhoPrimeiraCadeia = len(primeiraCadeia)
    index = 0
    
    while index < tamanhoPrimeiraCadeia:
        if primeiraCadeia[index] != segundaCadeira[index]:
            numeroDeDIferencas += 1
        index += 1
    print(numeroDeDIferencas)
    
def terceira():
    palavraChave = input("Digite a palavra chave: ").upper()
    texto = input("Digite o texto: ").upper()
    
    listaDePalavras = texto.split()
    totalDeRepeticoes = 0
    
    for palavra in listaDePalavras:
        totalDeRepeticoes += palavra.count(palavraChave)
        
    print(totalDeRepeticoes)
    
def quarta():
    primeiraPalavra = input("Digite a primeira palavra: ")
    segundaPalavra = input("Digite a segunda palavra: ")
    primeiraPalavraInvertida = primeiraPalavra[::-1]
    segundaPalavraInvertida = segundaPalavra[::-1]
    
    if(primeiraPalavra == segundaPalavraInvertida
       or segundaPalavra == primeiraPalavraInvertida
       or segundaPalavraInvertida == primeiraPalavraInvertida):
        print("São palíndromos")
    else:
        print("Não são palíndromos")

def quinta():
    data = {}
    
    while len(data) < 4:
        nome = input("Digite o nome do produto: ")
        data[nome] = []
    
    for nome in data:
        data[nome].append(int(input(f"Digite a % de aminoácidos de {nome}: ")))
        data[nome].append(int(input(f"Digite a % de Leucina de {nome}: ")))
        data[nome].append(int(input(f"Digite a % de Lisina de {nome}: ")))
        
    selecionado = ""
    menorLeucina = 100
    for nome in data:
        if(data[nome][1] < menorLeucina):
            menorLeucina = data[nome][1]
            selecionado = nome
    print("O produto com menor teor de Leucina é a:", selecionado)

def sexta():
    pass

def setima():
    data = {}
    while len(data) < 10:
        nome = input("Digite o nome da pessoa: ")
        idade = int(input("Digite a idade da pessoa: "))
        data[nome] = idade
    
    maiorIdade = 0
    maiorNome = ""
    for pessoa in data:
        if(data[pessoa] > maiorIdade):
            maiorIdade = data[pessoa]
            maiorNome = pessoa
    print("A pessoa mais velha é:", maiorNome, "com", maiorIdade, "anos")
    
