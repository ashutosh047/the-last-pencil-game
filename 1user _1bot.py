import sys
import random
#john one move
def john_move(n):
    m=input()
    while True:
        try:
            m=int(m)
            if m not in ([1,2,3]):
                print("Possible values: '1', '2' or '3'")
            elif(m>n):
                print('Too many pencils were taken')
            elif m in ([1,2,3]):
                n=n-m
                for i in range(n):
                    print('|',end="")
                print()
                return n
            else:
                print("Possible values: '1', '2' or '3'")
                    
        except Exception:
            print("Possible values: '1', '2' or '3'")
        m=input()
#jack one move
def jack_move(n):
    f=check(n)
    if(f):
        #winning move
        if(n%4)==0:
            m=3
        elif(n%4)==3:
            m=2
        elif(n%4)==2:
            m=1
    else:
        #random move
        if(n==1):
            m=1
        else:    
            m=random.randint(1,3)
    print(m)
    while True:
        try:
            m=int(m)
            if m not in ([1,2,3]):
                print("Possible values: '1', '2' or '3'")
            elif(m>n):
                print('Too many pencils were taken')
            elif m in ([1,2,3]):
                n=n-m
                for i in range(n):
                    print('|',end="")
                print()
                return n
            else:
                print("Possible values: '1', '2' or '3'")
                    
        except Exception:
            print("Possible values: '1', '2' or '3'")
        #m=input()
#check winning position
def check(n):
    if((n-1)%4)==0:
        #losing position
        return False
    else:
        #winning position
        return True
#main program
turn=-1
n=input('How many pencils would you like to use:')
while True:
    try:
        n=int(n)
        if(n==0):
            print('The number of pencils should be positive')
        elif(n<0):
            print('The number of pencils should be numeric')
        else:
            break    
    except Exception:
        print('The number of pencils should be numeric')
    n=input()
x=input('Who will be the first (John, Jack):')
while True:
    if x not in (['John','Jack']):
        print("Choose between 'John' and 'Jack'")
    else:
        break
    x=input()
for i in range(n):
    print('|',end="")
print()
#main program
l=['John','Jack']
if(x=='John'):
    turn=0
elif(x=='Jack'):
    turn=1
print(x+"'s turn!")
while(n>0):
    if(n==0):
        break
    else:
        if(turn==0):
            n=john_move(n)
            if(n==0):
                turn=(turn+1)%2
                print(l[turn]+" won!")
                sys.exit()
            else:
                turn=(turn+1)%2
                print(l[turn]+"'s turn!")
        elif(turn==1):
            n=jack_move(n)
            if(n==0):
                turn=(turn+1)%2
                print(l[turn]+" won!")
                sys.exit()
            else:
                turn=(turn+1)%2
                print(l[turn]+"'s turn!")
