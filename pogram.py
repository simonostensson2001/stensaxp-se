import random
import time # Används vid olika moment, Delay
print ("Välkommen till vårat Sten,Sax,Pase pogram")




gamemode = 0

while gamemode == 0:
    gamemode = int(input("[1]Spela mot en kompis [2]Spela mot dator"))
    if gamemode == 1:
        print("Du har valt att spela 1v1")



        player1 = input("Sten,Sax,Påse")
        player2 = input("Sten,Sax,Påse")
    elif gamemode == 2:
        print("Du har valt att spela mot pc")
        sax = 1
        sten = 2
        pase = 3
        player1 = int(input("[1]sax, [2]sten, [3]påse: "))
        pcchoice = int(random.randint(1, 3))
        while player1 == 1:
            if pcchoice == 1:
                print("oavgjort")
                player1 = 0
            elif pcchoice == 2:
                print("förlust")
                player1 = 0
            elif pcchoice == 3:
                print("vinst")
                player1 = 0
            else:
                player1 = 0

        while player1 == 2:
            if pcchoice == 1:
                print("förlust")
                player1 = 0
            elif pcchoice == 2:
                print("oavgjort")
                player1 = 0
            elif pcchoice == 3:
                print("vinst")
                player1 = 0
            else:
                player1 = 0

        while player1 == 3:
            if pcchoice == 1:
                print("förlust")
                player1 = 0
            elif pcchoice == 2:
                print("vinst")
                player1 = 0
            elif pcchoice == 3:
                print("oavgjort")
                player1 = 0
            else:
                player1 = 0
        else:
            time.sleep(1)
            print("Spela igen!")
            time.sleep(1)
            gamemode = 0