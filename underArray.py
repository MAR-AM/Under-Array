def soutable(Table,x,y):
    a = []
    for i in range(x,y):
        a.append(Table[i])
    return a
tab=[]
n=int(input('enter the size of list  : '))
for i in range (n):
   print("enter the number numero",i+1,":")
   m=int(input())
   tab.append(m)
print(tab)
a=int(input('enter the first index :'))
b=int(input('enter the second index :'))
print(soutable(tab,a,b,))
