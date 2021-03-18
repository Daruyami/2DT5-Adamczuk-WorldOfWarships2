players = []
playerNum = 0 # = liczba graczy, podczas tworzenia gracza jego pid jest równe temu, po operacji playerNum++   ...albo po prostu `len(players)
class player:
    def __init__(self, name, pid):
        self.name = name
        self.pid = pid
    # myśle nad przeniesieniem paru z ↓funkcji do środka tego ale nwm    ...zobaczy sie jak zaczne ogarniać gameBoarda

plen = ""
def addPlayer(pname):
    global playerNum
    global plen
    players.append( player(pname, playerNum) )
    playerNum = len(players)
    plen = "f" * playerNum

#def remPlayer(pid):
    # players.pop?

def gameStart(sizex, sizey):
    global plen
    gameBoard = [ [ plen ] * sizey ] * sizex
    print(gameBoard)

#def placeShips(pid, coordString):
    # somethin

#def attack(pid, coordString):
    # somethin

# tutaj pare testów
#addPlayer("Andrzej Duda")
#addPlayer("krowin")
#print(players)
#gameStart(2, 2)
# jako że chce możliwość dołączania do już rozpoczętej gry będe musiał jeszcze dodać żeby ogarniało boarda dla nowo wprowadzonych graczy ale mam już zamysł jak to ma mniej więcej wyglądać
