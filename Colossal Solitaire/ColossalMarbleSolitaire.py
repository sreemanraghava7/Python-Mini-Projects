l=[[' ',' ','O','O','O',' ',' '],
   [' ',' ','O','O','O',' ',' '],
   ['O','O','O','O','O','O','O'],
   ['O','O','O',' ','O','O','O'],
   ['O','O','O','O','O','O','O'],
   [' ',' ','O','O','O',' ',' '],
   [' ',' ','O','O','O',' ',' '],]
cols=[0,1,2,3,4,5,6]
points=0
flag=0
exception=[[i,j] for i in [0,1,5,6] for j in [0,1,5,6]]

def board(l,cols):
    print(end='  ')
    for i in cols:
        print(i,end=' ')
    print()
    for count,i in enumerate(l,0):
        print(count,end=' ')
        for j in i:
            print(j,end=' ')
        print(count,end=' ')
        print()
    print(end='  ')
    for i in cols:
        print(i,end=' ')
    print()

def horcheck(l):
  horcount=0
  for i in range(len(l)):
    for j in range(len(l[i])):
      if str(i) in '0156':
        if l[i][j]=='O' and j=='2':
          if l[i][j+1]=='O' and l[i][j+2]==' ':
            horcount+=1
            break
      elif 2<=i<=4 and j<=4 and l[i][j]=='O' and l[i][j+1]=='O' and l[i][j+2]==' ':
        horcount+=1
        break

  for i in range(len(l)):
    for j in reversed(range(len([i]))):
      if str(i) in '0156':
        if l[i][j]=='O' and j=='4':
          if l[i][j-1]=='O' and l[i][j-2]==' ':
            horcount+=1
            break
      elif 2<=i<=4 and j>=2 and l[i][j]=='O' and l[i][j-1]=='O' and l[i][j-2]==' ':
        horcount+=1
        break
  return horcount

def vercheck(l):
  vercount=0
  for i in range(len(l)):
    for j in range(len(l[i])):
      if str(j) in '0156':
        if l[i][j]=='O' and i=='2':
          if l[i+1][j]=='O' and l[i+2][j]==' ':
            vercount+=1
            break
      elif 2<=j<=4 and i<=4 and l[i][j]=='O' and l[i+1][j]=='O' and l[i+2][j]==' ':
        vercount+=1
        break

  for i in reversed(range(len(l))):
    for j in range(len([i])):
      if str(j) in '0156':
        if l[i][j]=='O' and i=='4':
          if l[i-1][j]=='O' and l[i-2][j]==' ':
            vercount+=1
            break
      elif 2<=j<=4 and i>=2 and l[i][j]=='O' and l[i-1][j]=='O' and l[i-2][j]==' ':
        vercount+=1
        break
  return vercount

def welcome():
    print('\nWELCOME TO THE COLOSSAL MARBLE SOLITAIRE\n')
    board(l,cols)
    print('\n')
    game(l,flag,points,exception)

def game(l,flag,points,exceptions):
    
    flag=flag
    points=points
    
    horizontal=horcheck(l)
    vertical=vercheck(l)
    
    while (horizontal+vertical)>=1:
        
        
        
        horizontal=horcheck(l)
        vertical=vercheck(l)
        
        if (horizontal+vertical)<1:
            print('\nNO MORE MOVES POSSIBLE...GAME OVER\n')
            print('\nPOINTS = ',points)
            print()
            return
        else:
            pass
        
        #print('\nhorizontal = ',horizontal)
        #print('\nvertical = ',vertical)
        
        
        
        print('\nENTER THE INITIAL POSITION OF THE MARBLE WHICH YOU WANT TO MOVE : ')
        initialPosition=list(map(int,input().split()))
        ip1=initialPosition[0]
        ip2=initialPosition[1]
        
        print('\nENTER THE DESTINATION POSITION WHERE YOU WANT TO PLACE THE SELECTED MARBLE : ')
        destinationPostion=list(map(int,input().split()))
        dp1=destinationPostion[0]
        dp2=destinationPostion[1]
        
        if (ip1<0 or ip1>=7) or (ip2<0 or ip2>=7) or (dp1<0 or dp1>=7) or (dp2<0 or dp2>=7) or (initialPosition in exception) or (destinationPostion in exception):
            print('\nINVALID POSITIONS...RE-ENTER THE POSITIONS\n')
            flag=1
            break
        else:
            pass
        
        if l[ip1][ip2]==' ':
            print('\nINVALID INITIAL POSITION...ENTER THE VALID POSITIONS\n')
            flag=1
            break
        else:
            pass
        
        if l[dp1][dp2]!=' ':
            print('\nINVALID DESTINATION POSITION...ENTER THE VALID POSITIONS\n')
            flag=1
            break
        else:
            pass
        
        if ip1==dp1:
            if ip2>dp2:
                if  l[dp1][dp2+1]!='O' or abs(ip2-dp2)!=2:
                    print('\nINVALID MOVE...ENTER VALID DESTINATION\n')
                    flag =1
                    break
                else:
                    l[dp1][dp2]='O'
                    l[ip1][ip2]=' '
                    l[dp1][dp2+1]=' '
                    points+=1
            elif ip2<dp2:
                if  l[dp1][dp2-1]!='O' or abs(ip2-dp2)!=2:
                    print('\nINVALID MOVE...ENTER VALID DESTINATION\n')
                    flag =1
                    break
                else:
                    l[dp1][dp2]='O'
                    l[ip1][ip2]=' '
                    l[dp1][dp2-1]=' '
                    points+=1
        
        elif ip2==dp2:
            if ip1>dp1:
                
                if  l[dp1+1][dp2]!='O' or abs(ip1-dp1)!=2:
                    print('\nINVALID MOVE...ENTER VALID DESTINATION\n')
                    flag =1
                    break
                else:
                    l[dp1][dp2]='O'
                    l[ip1][ip2]=' '
                    l[dp1+1][dp2]=' '
                    points+=1
                    
            elif ip1<dp1:
                
                if  l[dp1-1][dp2]!='O' or abs(ip1-dp1)!=2:
                    print('\nINVALID MOVE...ENTER VALID DESTINATION\n')
                    flag =1
                    break
                else:
                    l[dp1][dp2]='O'
                    l[ip1][ip2]=' '
                    l[dp1-1][dp2]=' '
                    points+=1
                    
        print()
        board(l,cols)
        
                    
    if flag==1:
        flag=0
        game(l,flag,points,exception)
        
    else:
        board(l,cols)
        print('\nPOINTS = ',points)
        
welcome()
    








































    