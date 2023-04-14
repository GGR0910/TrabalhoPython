import os

def main():
    option = ""
    while (option != "3" or option != "4"):
        option = input("Questão 3 ou 4? Ou 0 para sair: ")
        if (option == "3"):
            question3()
        elif (option == "4"):
            question4()
        elif (option == "0"):
            break
        else:
            os.system("cls")
            print("Opção inválida, por favor escolha entre as questões 3 ou 4 ou 0 para sair")


def question3():
    initialConcentration = float(input("Digite a concentração inicial: "))
    initialVolume = float(input("Digite o volume inicial: "))
    finalVolume = float(input("Digite o volume final: "))
    measurementUnit = input("Digite a unidade de medida: ")
    finalConcentration = (initialConcentration * initialVolume) / finalVolume
    print(f"A concentração final é: {finalConcentration} {measurementUnit}")
    print("")


def question4():
    timeOfTravelInMinutes = float(input("Digite o tempo de viagem em minutos: "))
    distanceTraveledInKm = float(input("Digite a distância de viagem em km: "))
    priceForTheDistance = distanceTraveledInKm * 1.4
    princeForTheTime = timeOfTravelInMinutes * 0.26
    print(f"O preço da viagem é:R${priceForTheDistance + princeForTheTime}!")
    print("")


if (__name__) == '__main__':
    main()

