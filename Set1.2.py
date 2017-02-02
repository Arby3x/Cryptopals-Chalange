def xor(x,y):
    max=0
    min=0
    if x==y:
        print 0
        return None
    if y>x:
        max=y
        min=x
        x=max
        y=min
    res=0
    k=log(x,2)+1
    for n in range(0,k):
        res=res+((2**n)*((((x/(2**n))%2)+((y/(2**n))%2))%2))
        #To learn more about this ^ eqution 
        #Look up https://en.wikipedia.org/wiki/Bitwise_operation in the Xor section
    return hex(res)

def Eq(s1,s2):
    if len(s1) != len(s2):
        print "the hex strings sould be equal length"
        return False
    return True

def log(x, base):
    count = -1
    while x > 0:
        x /= base
        count += 1
        if x == 0:
            return count

a=raw_input()
b=raw_input()
while b!="stop" or a!="stop":
    if Eq(a,b):
        xor(int(a,16),int(b,16))
    a=raw_input()
    b=raw_input()
