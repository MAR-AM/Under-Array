#N=int(input('enter a nbr : '))
#for i in range (1,N+1):
#  triangle=''
#  for j in range (i):
#     triangle=triangle+str(i)
#  print(str(i)*i)


#N=int(input('enter a nbr : '))
#s=0
#for i in range (0,N+1):
 #   s=i*10**(i-1)
 #   print(s)
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