import random
print ("Välkommen till vårat Sten,Sax,Pase pogram")




gamemode = 0

while gamemode == 0:
    gamemode = 2
    if gamemode == 1:
        print("Du har valt att spela 1v1")



        player1 = input("Sten,Sax,Pase")
        player2 = input("Sten,Sax,Pase")
    elif gamemode == 2:
        print("Du har valt att spela mot pc")
        sax = 1
        sten = 2
        pase = 3
        player1 = input("[1]sax, [2]sten, [3]pase")
        while player1 == 1:
            pcchoice = input(random.randint(1, 3))
            if pcchoice == 1:
                print("oavgjort")
            elif pcchoice == 2:
                print("forlust")
            elif pcchoice == 3:
                print("vinst")
            else:
                player1 = 1


    else:
        gamemode = 0