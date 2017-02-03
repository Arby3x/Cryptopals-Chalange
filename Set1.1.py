#function takes a hex string and converts it to base64 string
#return nothing
def HexToBase64(s):
    #The base64 table
    b64table = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/",)
    list = []
    #for computing binary for an array of 0s and 1s
    power = (5,4,3,2,1,0)
    #converting the hex string to a binary array
    while s != 1:
        list.append(s % 2)
        s = s / 2
        if s == 1:
            list.append(1)
    #adds 0 to the end of the array,if the bin array length is odd(so somthing like this won't happen: 0b111,insted:0b0111 )
    if(len(list) % 2 != 0):
        list.append(0)
    #reversing the array after breaking down the intger
    list2=list[::-1]
    msglen = len(list2)
    #checks if the number of bytes divisible by 3,if not adding the amount of
    #bytes missing
    i = len(list2)#*
    k = 6 - (i % 6)#*
    if k != 6:#*
        while k > 0:
            list2.append(0)
            k-=1
    #dividing the bin number into an 6 bits octats array
    i = len(list2)
    k = 6
    list = []
    for x in range(0,i,6):
        list.append(list2[x:k])
        k+=6
    #converting the 6 bits octats into an index array
    list2 = []
    sum = 0
    string = ""
    for x in range(0,len(list)):
        k = list[x]
        for y in range(0,6):
            sum = sum + k[y] * (2 ** power[y])
        list2.append(sum)
        sum = 0
    #checking if padding is needed
    for x in range(0,len(list2)):
        string = string + b64table[list2[x]]
    if len(list2) % 4 == 3:
        string = string + "="
    elif len(list2) % 4 == 2:
        string = string + "=="
    else:
        string = string
    print string
    return None
#if ascii char detected,convert to hex
def ErrorToHex(s):
    return s.encode("hex")
b = raw_input("Enter you hex string / Ascii string(or stop)")
#""MAIN""#
while(b != "stop"):
    try :
        if len(b)%2!=0:
            temp=b[:len(b)-1]
            temp=temp+"0"+b[len(b)-1:]
            b=temp
        b = int(b,16)
        HexToBase64(b)
    except ValueError :
         b = ErrorToHex(b)
         b = int(b,16)
         HexToBase64(b)
    b = raw_input()
##############################
#originally i planned it to convert only hex to base64,but i thought that i can add ascii also
#and then it broke
#Working on fixing the following those problems:
#[FIXED]cant convert properly odd len hex strings
#What dose work:
#assci to base64
#even len hex strings
#Side Note:every string that can do int(string,16)
#will be converted as hex to base64,and not as ascii to base64
