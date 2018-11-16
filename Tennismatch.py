# Det här är ett program som simulerar en tennismatch.
# Användaren får välja ut två spelare som tävlar mot
# varandra, en slumpmässigt vald spelare vinner.
# Programmet lagrar spelarna i en fil med namnet
# "players.txt" mellan körningarna.
 
from random import*
 
class Player:
   
    def __init__(self, name, odds, won, played, percentage):
        self.name = name
        self.odds = odds
        self.won = won
        self.played = played
        self.percentage = percentage
        
    def parseLine(line):
        (name, odds, won, played, percentage) = line.split(",")
        return Player(name, float(odds), int(won), int(played), int(percentage))


    def printPlayersInformation(player_list):
        print("%12s %12s %12s %12s %12s %12s\n" % ("Placering", "Spelare", "Odds", "Vunna", "Spelade", "Procent")) 
        i = 1
        for player in player_list:
            print("%12s %12s %12s %12s %12s %12s\n" % (i, player.name, player.odds, player.won, player.played, player.percentage))
            i += 1

    def __repr__(self):
        list_info = (self.name, self.odds, self.won, self.played, self.percentage)
        string_list = map(str, list_info)
        return ",".join(string_list)

class Game:

    def __init__(self, filename = "players.txt"):
         player_list = []
         self.player_list = player_list
         self.filename = filename
         file = open(filename, "r")
         for line in file:
            player_list.append(Player.parseLine(line))
         file.close()

    def save(self, filename = "players.txt"):
        file = open(filename, "w")
        for player in self.player_list:
            file.write(str(player))
            file.write("\n")
        file.close()
  
    def playMatch(self):
        player = 2 * [None]
        for i in range(0,2):
            while True:
                try:
                    player[i] = int(input("Välj en spelare till matchen. Skriv in spelarens placering i listan.\n"))
                    
                    if player[0] == player[1]:
                        print("Välj två olika spelare.\n")
                        continue
                    if player[i] > 5:
                        print("För stort tal. Skriv in ett nummer mellan 1 och 5.\n")
                        continue
                    if player[i] < 1:
                        print("För litet tal. Skriv in ett nummer mellan 1 och 5.\n")
                        continue
                                            
                except ValueError:
                    print("Skriv in ett nummer mellan 1 och 5.\n")
                    continue
                
                break
        i += 1
            
        print("Låt matchen börja!\n")

        for i in range(0,2):
            player[i] = self.player_list[player[i]-1]
            player[i].played = player[i].played + 1
            i += 1
        
        win = random()

        if win < (player[0].odds / (player[0].odds + player[1].odds)):
            print("Grattis, spelare " + player[0].name + " vann!\n")
            player[0].won = player[0].won + 1
            
        else:
            print("Grattis, spelare " + player[1].name + " vann!\n")
            player[1].won = player[1].won + 1

        for i in range(0,2):
            player[i].percentage = int(round(100 * float(player[i].won)/float(player[i].played)))
            i += 1
        
        print("Matchen är över, tack för att ni spelade.\n")

        self.player_list.sort(key = lambda player: player.percentage, reverse = True)
        Player.printPlayersInformation(self.player_list)

def printMenu():
    print("L Lista alla spelare.\nS Spela en match.\nA Avsluta programmet.\n")

def choose():
    printMenu()
    choice = input("Vad vill du göra? Skriv in vald bokstav.\n")
    return choice[0].upper()

def listPlayers(game):
    my_players = game.player_list
    Player.printPlayersInformation(my_players)
    
def playMatchListInformation(game):
    game.playMatch()
    game.save()
 
print("Välkommen till århundradets tennismatch!\nHär väljer du två antagonister ifrån en lista som får tävla mot varandra.\n")

game = Game()
 
choice = choose()
while choice != "A":
    if choice == "L":
        listPlayers(game)
    if choice == "S":
        playMatchListInformation(game)
    choice = choose()
 
 
print("Välkommen åter")
 
game.save()
