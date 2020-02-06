def add(num1,num2):
    return num1+num2

def isleapyear(year):
    if (year%400==0) or (year%4==0 and year%100!=0):
        print("leap")
    else:
        print("not a leap")
        
def isprime(v):
    count=0
    for i in range(1,v+1):
        if v%i==0:
            count+=1
    if count==2:
        print(v,"prime")
    else:
        print(v,"not prime")
    
def alleven(lb,up):
    for i in range(lb,up+1):
        if i%2==0:
            print(i)

def allodd(lb,up):
    for i in range(lb,up+1):
        if i%2==1:
            print(i)

def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f