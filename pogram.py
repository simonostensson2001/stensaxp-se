import random
print ("Välkommen till vårat Sten,Sax,Påse pogram")

gamemode = False

while gamemode == False:
    gamemode = input("Välj spelläge [1]1v1 [2]pc: ")
    if gamemode == 1:
        print("Du har valt att spela 1v1")
    elif gamemode == 2:
        print("Du har valt att spela mot pc")
    else:
        gamemode = False
