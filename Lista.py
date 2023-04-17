

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
    

def primeira():
    palavraChave = input("Digite a palavra chave que deseja buscar no texto: ").upper()
    texto = input("Digite o texto em que deseja buscar a palavra chave: ").upper()
    
    quantidadeDeVezes = texto.count(palavraChave)
    primeiraAparicao = texto.find(palavraChave)
    
    print(f"A palavra chave aparece {quantidadeDeVezes} vezes no texto e tem sua primeira aparição na posição {primeiraAparicao + 1}")
    
    
def segunda():
    primeiraPalavra = input("Digite a primeira palavra: ")
    segundaPalavra = input("Digite a segunda palavra que será invertida: ")
    segundaPalavraInvertida = segundaPalavra[::-1]
    
    if(primeiraPalavra == segundaPalavraInvertida):
        print("São palíndromas")
    else:
        print("Não são palíndromas")
        
def terceira():
    caracteres = []
    cadeia = input("Digite a sequência de proteína: ").upper()
    
    for caracter in cadeia:
        caracteres.append(caracter)
        
    response = 1    
    while response != 0:
        response = input("Digite 1 para fazer uma mutação ou 0 para sair: ")
        if(response == "1"):
            posicao = int(input("Digite a posição que deseja mutar: "))
            novoCaracter = input("Digite o novo caracter: ").upper()
            caracteres[posicao - 1] = novoCaracter
        else:
            pass
    print("".join(caracteres))
    
def quarta():
    numeroInicial = int(input("Digite o número inicial: "))
    numeroLimite = int(input("Digite o número limite: "))
    
    quantidades = []
    tempoTotal = 0
    while(numeroInicial <= numeroLimite):
       numeroInicial += numeroInicial * 0.2
       quantidades.append(numeroInicial)
       tempoTotal += 1
    print(f"O número de células após {tempoTotal} horas é de {quantidades[-1]}, e a quantidade de células após cada hora é {quantidades}")
