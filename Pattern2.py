n=int(input("enter any number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if( i == 1 or i == n or j == 1 or j == n or  i == j-1 or i+j==n+1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()