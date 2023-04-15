
import Slide1, Slide2, Slide3, Slide4


def main():

        lista = float(input("Digite o numero da lista que deseja executar: "))
        if(lista == 1):
            Slide1.hub()
        elif(lista == 2):
            Slide2.hub()
        elif(lista == 3):
            Slide3.hub()
        elif(lista == 4):
            Slide4.hub()
        else:
            print("Lista não encontrada")
   


    
if __name__ == "__main__":
    main()