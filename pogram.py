import random
print ("Välkommen till vårat Sten,Sax,Pase pogram")




gamemode = 0

while gamemode == 0:
    gamemode = 2
    if gamemode == 1:
        print("Du har valt att spela 1v1")



        player1 = input("Sten,Sax,Påse")
        player2 = input("Sten,Sax,Påse")
    elif gamemode == 2:
        print("Du har valt att spela mot pc")
        sax = 1
        sten = 2
        pase = 3
        player1 = input("[1]sax, [2]sten, [3]påse: ")
        while player1 == 1:
            pcchoice = input(random.randint(1, 3))
            if pcchoice == 1:
                print("oavgjort")
            elif pcchoice == 2:
                print("förlust")
            elif pcchoice == 3:
                print("vinst")
            else:
                player1 = 1

        while player1 == 2:
            pcchoice = input(random.randint(1, 3))
            if pcchoice == 1:
                print("förlust")
            elif pcchoice == 2:
                print("oavgjort")
            elif pcchoice == 3:
                print("vinst")
            else:
                player1 = 2

        while player1 == 3:
            pcchoice = input(random.randint(1, 3))
            if pcchoice == 1:
                print("förlust")
            elif pcchoice == 2:
                print("vinst")
            elif pcchoice == 3:
                print("oavgjort")
            else:
                player1 = 1
    else:
        gamemode = 0