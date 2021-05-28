# first perform pip install random-word and then run the program

from random_word import RandomWords

print("**************WORD BUILDING**************\n\n")
print("\\\\\\\ HOW TO PLAY ///////\n")
print("1.Give a meaningful word.\n2.The word you are entering should start with the ending letter of the previous word , if not you lose.\n3.The words should not get repeated , if so you get a second chance.\n4.In case you did not follow the Rule 2 in second chance , you lose.")
n=int(input("Enter number of players (min = 2) : "))
while(True):
    if(n<2):
        n=int(input("Re-Enter number of players (min = 2) : "))
    else:
        break
    
players = []
words = []

for player in range(1,n+1):
    players.append(input('Enter player {} name : '.format(player)).lstrip().rstrip().capitalize())
    
playerTurn = 0
randomWord = RandomWords()
words.append(randomWord.get_random_word().lower().lstrip().rstrip())

while (len(players)>1):
    
    lastLetter = words[-1][-1]
    
    print('\n{} its your turn and your word should start with {}'.format(players[playerTurn],lastLetter))

    word = input().lstrip().rstrip().lower()
    
    if word.isdigit() or word[0] != lastLetter:
        print('\n{} you lost...Better luck next time\n'.format(players[playerTurn]))
        players.pop(playerTurn)
        playerTurn+= 1
        if(playerTurn >= len(players)):
            playerTurn=0
            continue
        continue
    
    if(word in words):        
        
        print("\nWord already exists , enter a new word...")
        continue
    
    if(word[0]==lastLetter):
        words.append(word)
        playerTurn+= 1
        if(playerTurn == len(players)):
            playerTurn=0
            continue
    
print('\n{} won the game'.format(players[0]))

print("\n\n!!!!!!! Game over !!!!!!!")
    
    
    