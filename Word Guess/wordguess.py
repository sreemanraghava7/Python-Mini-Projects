import random

def noOfTurns(word):                                                            # To generate number of chances given to the user to guess the word
    s=set(word)                                                                 # If the uniques letters that should be guessed
    if len(s)>10:                                                               # are greater than 10 then the number of unique letters will be the number of turns
        return len(s)
    else:
        return 10                                                               # else atleast 10 chances are given


def welcome():                                                                  # to display the welcome note and start the game
    print('WELCOME TO WORD GUESS GAME\n')
    print('SELECT THE CATEGORY AND GUESS THE WORD RELATED TO THAT CATEGORY\n')
    wordGuess()
    
def wordGuess():                                                                # game starts here
    print('1. ANIMALS\n2. COUNTRIES\n3. COUNTRY CAPITALS\n4. CURRENCY\n5. LANGUAGES\n6. SPORTS\n7. THINGS\n8. MIXED\n9. EXIT\n')
    print('SELECT ONE CATEGORY\n')
    
    filedict={                                                                  # instead of switch case we can use a dictionary
        1:'animals.txt',
        2:'countries.txt',
        3:'country_capitals.txt',
        4:'currency.txt',
        5:'languages.txt',
        6:'sports.txt',
        7:'things.txt',
        8:'mixed.txt',
        9:'exit',
        10:'p'
        }
    
    ch=int(input())                                                             # to select the category
    
    
    if ch<1 or ch>9:
        print('\nINVALID CHOICE...RE-SELECT THE CATEGORY\n')
        ch=10
        wordGuess()
    
    x=filedict[ch]                                                              # file name according the user choice of category
    
    if x=='exit':                                                               # if the user wants to exit
        print('\nTHANK YOU FOR PLAYING...')
        return
        
    if x=='p':
        print()
        return
    
    with open(x,'r') as f:                                                      # open the file and
        l=[i for i in f]                                                        # store the file contents in a list
    
    y=random.randint(1, len(l))                                                 # to generate random integer so that the word at that position in the list will be the word to be guessed
    
    word=l[y].upper().strip().lstrip().rstrip()                                 # word to be guessed
    answer=[]                                                                   # first it stores blank spaces which represent the missing letters and when the user enters a letter if the letter is present in the word then the respective blank(s) in this answer list will get replaced by the letter
    flag=0                                                                      # to know if the user is winner or he is out of turns
    
    for i in word:                                                              # if the word contains hyphen symbol (-) it will get replaced by space Ex: Tug-of-war will be displayed as Tug of war
        if i=='-':
            word=word.replace('-',' ')
        
    for i in range(len(word)):                                                  # initially to insert blanks in the answer list
        if word[i]==' ':
            answer.append(' ')
        else:
            answer.append('_')
            
    for i in answer:                                                            # print the blanks
        print(i,end=' ')
        
    turns=noOfTurns(word)
    #print(turns)
    #print(word)
    
    for turn in range(1,turns+1):
        temp=''.join(answer)                                                    # joins the elements of the answer list and forms into a string or word
        if temp==word:                                                          # if the letters guessed by the user combinedly is equal to the word that should be guessed then
            flag=1                                                              # sets the flag as 1 denoting that the user won
            break
        
        
        print('\nTURNS LEFT = {}\n'.format((turns-turn+1)))                       # displays the turns left for the user to guess the correct word
        print('GUESS A LETTER\n')
        user=input().upper().strip().lstrip().rstrip()[0]                       # user inputs the letter
        
        for i in range(len(word)):                                          
            if word[i]==user:                                                   # if any of the letter in the word equals the letter entered by the user then
                answer[i]=user                                                  # replace the respective position of the letter ( in word ) in the answer list with the letter
                
        print()
        print(' '.join(answer))                                                 # displays the answer list 
        
        
    if flag==0:
        print('\nYOUR TURNS ARE OVER...\n\nTHE WORD IS {}\n\nBETTER LUCK NEXT TIME\n'.format(word))
        return
    elif flag==1:
        print('\nYOU GUESSED IT RIGHT. CONGRATULATIONS BUDDY !!!\n')
        print('\nWANNA PLAY ONE MORE ? Y/N\n')
        yesno=input().lower().strip().lstrip().rstrip()[0]                      # to know whether the user wants to play again or not
        if yesno=='y':                                                          # if yes then
            wordGuess()                                                         # the game starts again 
        elif yesno=='n':                                                        # if no
            print('\nTHANK YOU FOR PLAYING...\n')                                                       
            return                                                              # exits the game
    
welcome()