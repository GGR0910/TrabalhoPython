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
    
    
def primeira():
    caractere = input("Digite o caractere: ").upper()
    
    #verifica qual o caractere em maiusculo e imprime a mensagem correspondente
    if(caractere == "A"):
        print("Essa é uma adenina")
    elif(caractere == "C"):
        print("Essa é uma citosina")
    elif(caractere == "G"):
        print("Essa é uma guanina")
    elif(caractere == "T"):
        print("Essa é uma timina")
    else:
        print("Não é um nucleotídeo")
        
def segunda():
    quantidadePares = int(input("Digite a quantidade de pares: "))
    
    #verifica o intervalo que se encontra e imprime a mensagem correspondente
    if(quantidadePares < 10000):
        print("O melhor tipo de vetor é o Plasmídeo")
    elif(10000 < quantidadePares < 20000):
        print("O melhor tipo de vetor é o Bacteriofago")
    elif(20000 < quantidadePares < 40000):
        print("O melhor tipo de vetor é o Cosmídeos")
    elif(40000 < quantidadePares < 300000):
        print("O melhor tipo de vetor é o BACs")
    elif(300000 < quantidadePares < 1000000):
        print("O melhor tipo de vetor é o YACs")
    else:
        print("Não é um nucleotídeo")

def terceira():
    quantidadeDeMinutos = float(input("Digite a quantidade de minutos: "))
    
    #verifica o intervalo que se encontra e imprime a mensagem 
    # correspondente calculando o valor da conta pela quantidade de minutos
    if(quantidadeDeMinutos < 200):
        print("O valor da conta é: R$", 0.21 * quantidadeDeMinutos)
    elif(200 < quantidadeDeMinutos < 400):
        print("O valor da conta é: R$", 0.18 * quantidadeDeMinutos)
    elif(400 < quantidadeDeMinutos):
        print("O valor da conta é: R$", 0.15 * quantidadeDeMinutos)
        
def quarta():
    numero = int(input("Digite um número: "))
    
    #Verifica se o número é negativo, positivo ou nulo/zero
    if(numero < 0):
        print("O número é negativo")
    elif(numero > 0):
        print("O número é positivo")
    elif(numero == 0):
        print("O número é nulo/zero")
        
def quinta():
    primeiroNumero = float(input("Digite o primeiro número: "))
    segundoNumero = float(input("Digite o segundo número: "))
    
    #Verifica se o primeiro número é maior, menor ou igual ao segundo número
    if(primeiroNumero == segundoNumero):
        print("Os números são iguais")
    elif(primeiroNumero > segundoNumero):
        print("O primeiro número é maior que o segundo")
    elif(primeiroNumero < segundoNumero):
        print("O segundo número é maior que o primeiro")

def sexta():
    massa = float(input("Digite a massa do paciente: "))
    altura = float(input("Digite a altura do paciente: "))
    
    #Calcula o IMC e verifica o intervalo que se encontra e imprime a mensagem correspondente
    IMC = massa / (altura ** 2)
    
    #Verifica o resultado do IMC e imprime a mensagem correspondente
    if(IMC < 18):
        print("Abaixo do peso")
    elif(18 < IMC < 25):
        print("Peso normal")
    elif(25 < IMC < 30):
        print("Sobrepeso")
    elif(30 < IMC < 35):
        print("Obesidade grau 1")
    elif(35 < IMC < 40):
        print("Obesidade grau 2")
    elif(IMC > 40):
        print("Obesidade grau 3")