T=list(input('')) 
C=0
P=0
while P<len(T):
    if T[P]=='+':
            C=C+1
    elif T[P]=='-':
            C=C-1
    elif T[P]==')':
        if C!=0:
            while T[P]!='(':
                P=P-1
    elif T[P]=='$':
        print(chr(C))

    P+=1
