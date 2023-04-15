
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
    raio = input("Digite o raio do círculo: ")
    #formula do volume, 4/3 * pi * raio ao cubo
    volume = (4/3) * 3.14 * (float(raio) ** 3)
    print(f"O volume do círculo é: {volume:.2f}")  

def segunda():
    #calcula o preço com desconto
    precoComDisconto = float(24.95 * 0.6)
    quantidade = float(input("Digite a quantidade de livros: "))
    
    #calcula o valor total da entrega com base na quantidade de livros, o preço por livro e o valor base do primeiro
    valorTotalEntrega = 3 + ((quantidade - 1) * 0.75)
    
    #imprime o valor total da compra
    print("valor Total: R$", (precoComDisconto * quantidade) + valorTotalEntrega)
    
def terceira():
    #recebe os dados do usuário
    initialConcentration = float(input("Digite a concentração inicial: "))
    initialVolume = float(input("Digite o volume inicial: "))
    finalVolume = float(input("Digite o volume final: "))
    
    #calcula a concentração final
    finalConcentration = (initialConcentration * initialVolume) / finalVolume
    print(f"A concentração final é: {finalConcentration}")

def quarta():
    #recebe os dados do usuário
    timeOfTravelInMinutes = float(input("Digite o tempo de viagem em minutos: "))
    distanceTraveledInKm = float(input("Digite a distância de viagem em km: "))
    
    #calcula o preço da viagem pela distancia e pelo tempo
    priceForTheDistance = distanceTraveledInKm * 1.4
    princeForTheTime = timeOfTravelInMinutes * 0.26
    
    #imprime o preço da viagem somando com o valor base
    print(f"O preço da viagem é:R${(priceForTheDistance + princeForTheTime) + 2.75}!")
