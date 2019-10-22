import random
import time # Används vid olika moment, Delay
print ("Välkommen till vårat Sten, Sax, Påse spel")
PcScore = 0
Player1Score = 0
Player2Score = 0

menu = 0
gamemode = 0

while menu == 0:
    gamemode = int(input("[1]Spela mot en kompis [2]Spela mot dator: "))
    if gamemode == 1:
        print("Du har valt att spela 1v1")



        player1 = input("[1]sax, [2]sten, [3]påse: ")
        player2 = input("[1]sax, [2]sten, [3]påse: ")
    elif gamemode == 2:
        print("Du har valt att spela mot pc")
        sax = 1
        sten = 2
        pase = 3
        player1 = int(input("[1]sax, [2]sten, [3]påse: "))
        pcchoice = int(random.randint(1, 3))
        while player1 == 1:
            if pcchoice == 1:
                print("Du spelade sax")
                time.sleep(1)
                print("Datorn spelade sax")
                time.sleep(1)
                print("oavgjort")
                print("Spelare", Player1Score, "-", PcScore, "Dator",)
                player1 = 0
            elif pcchoice == 2:
                print("Du spelade sax")
                time.sleep(1)
                print("Datorn spelade sten")
                time.sleep(1)
                print("förlust")
                PcScore = PcScore + 1
                print("Spelare", Player1Score, "-", PcScore, "Dator",)
                player1 = 0
            elif pcchoice == 3:
                print("Du spelade sax")
                time.sleep(1)
                print("Datorn spelade påse")
                time.sleep(1)
                print("vinst")
                Player1Score = Player1Score + 1
                print("Spelare", Player1Score, "-", PcScore, "Dator",)
                player1 = 0
            else:
                player1 = 0

        while player1 == 2:
            if pcchoice == 1:
                print("Du spelade sten")
                time.sleep(1)
                print("datorn spelade sax")
                time.sleep(1)
                print("vinst")
                Player1Score = Player1Score + 1
                print("Spelare", Player1Score, "-", PcScore, "Dator",)
                player1 = 0
            elif pcchoice == 2:
                print("Du spelade sten")
                time.sleep(1)
                print("Datorn spelade sten")
                time.sleep(1)
                print("oavgjort")
                print("Spelare", Player1Score, "-", PcScore, "Dator",)
                player1 = 0
            elif pcchoice == 3:
                print("Du spelade sten")
                time.sleep(1)
                print("Datorn spelade påse")
                time.sleep(1)
                print("förlust")
                PcScore = PcScore + 1
                print("Spelare", Player1Score, "-", PcScore, "Dator",)
                player1 = 0
            else:
                player1 = 0

        while player1 == 3:
            if pcchoice == 1:
                print("Du spelade påse")
                time.sleep(1)
                print("Datorn spelade sax")
                time.sleep(1)
                print("förlust")
                PcScore = PcScore + 1
                print("Spelare", Player1Score, "-", PcScore, "Dator",)
                player1 = 0
            elif pcchoice == 2:
                print("Du spelade påse")
                time.sleep(1)
                print("Datorn spelade sten")
                time.sleep(1)
                print("vinst")
                Player1Score = Player1Score + 1
                print("Spelare", Player1Score, "-", PcScore, "Dator",)
                player1 = 0
            elif pcchoice == 3:
                print("Du spelade påse")
                time.sleep(1)
                print("Datorn spelade påse")
                time.sleep(1)
                print("oavgjort")
                print("Spelare", Player1Score, "-", PcScore, "Dator",)
                player1 = 0
            else:
                player1 = 0
        else:
            time.sleep(1)
            if PcScore == 2:
                print("Datorn vann")
                Player1Score = 0
                PcScore = 0
                menu = 0
            elif Player1Score == 2:
                print("Du vann")
                Player1Score = 0
                PcScore = 0
                menu = 0
            else:
                print("Spela igen!")
                time.sleep(1)
                gamemode = 2