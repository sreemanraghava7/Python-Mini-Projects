import itertools
def originalMatrix(a):								                              	
  print()
  for i in range(1,len(a)+1):
    if a[i-1]=='X':
      print('\033[1;34;47m X \033[0;0m',end='')
    elif a[i-1]=='O':
      print('\033[1;31;47m O \033[0;0m',end='')
    elif a[i-1] in '123456789':
      print('\033[1;30;47m {} \033[0;0m'.format(i),end='')
    if i%3==0:
      print()

def result(sublists,possibleSolutions):						                       	
  res=0
  for i in sublists:
    if i in possibleSolutions:
      res=1
      return res
      break
    else:
      continue


matrix='123456789'
possibleSolutions=[[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]
p1=[]                                                                           	
p2=[]                                                                           	
fp1=[]                                                                         	 	
fp2=[]										                                    	
print('\nTIC - TAC - TOE')                                                      	
originalMatrix(matrix)
i=1
while(i<len(matrix)+1):
  if i%2==0:
    print('\nPLAYER 2 TURN : ')
  else:
    print('\nPLAYER 1 TURN : ')
  position=int(input())
  if i%2!=0 and str(position) in list(matrix):      
    p1.append(position)                                                         	
    matrix=matrix.replace(str(position),'X')                                    	
    originalMatrix(matrix)

    i+=1

    if len(p1)>=3:                                                              	
      for comb in itertools.combinations(p1, 3):                                	
        fp1.append(sorted(list(comb)))
      t=result(fp1,possibleSolutions)
      if t==1:
        print('\nPLAYER 1 WON THE MATCH')
        tie=0
        break
    else:
      tie=1
      continue
  elif i%2==0 and str(position) in list(matrix):
    p2.append(position)                                                         	
    matrix=matrix.replace(str(position),'O')                                    
    originalMatrix(matrix)
      
    i+=1
                                                    
    if len(p1)>=3:                                                              
      for comb in itertools.combinations(p2, 3):                                
        fp2.append(sorted(list(comb)))
      t=result(fp2,possibleSolutions)
      if t==1:
        print('\nPLAYER 2 WON THE MATCH')
        tie=0
        break
    else:
      tie=1
      continue
  else:
    print('\nPOSITION NOT FOUND...RE ENTER THE POSITION\n')
    originalMatrix(matrix)
if tie==1:
  print('\nMATCH TIED')


