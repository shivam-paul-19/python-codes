# number breaker, this will break any given number in parts according to te function used

def breaksum():
    '''breaks the number into sum of two numbers'''
    a = int(input("enter the number : "))
    i = 1
    while (i<a):
        r = a - i
        print(f"{i}+{r}={a}")
        i = i + 1

def breakpro():
    '''breaks the number as the product of two numbers'''
    a = int(input("enter the number : "))
    i = 1
    while(i<=a):
        if (a%i == 0):
            print(f"{i},{int(a/i)}")
        i = i + 1

def fac():
    '''breaks the number into product of prime numbers(or simply factorise them)'''
    factors = []
    f = ""
    a = int(input("Enter the number : "))
    i = 2
    while(i<=a):
        if (a%i == 0):
            factors.append(str(i))
            a /= i
        else:
            i += 1
    print(" X ".join(factors))

fac()
breaksum()
breakpro()
