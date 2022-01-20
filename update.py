import trelloParsers

f = open('keys.dat')
KEY = str(f.readline()).strip()
TOKEN = str(f.readline()).strip()
BOARD = str(f.readline()).strip()
f.close()
url = 'https://api.trello.com/1/boards/'+BOARD+'/lists?cards=open&key='+KEY+'&token='+TOKEN
cards = trelloParsers.getCardsFromURL(url)
lista = cards.get("Do zrobienia")

file = open("log.txt", "w")
for x in lista:
	file.writelines(x)
	file.write("\n")
file.close()

file = open("log.txt", "r")
readlist = list()
for x in range(5):
	readlist.append(file.readline().strip())
file.close()

print (lista)
print (readlist)
