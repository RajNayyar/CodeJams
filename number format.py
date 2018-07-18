def conversionToHex(n):
  n = int(n)
  sum = ''
  i = 0
  while(n!=0):
    rem = n%16
    
    if(rem>9):
      sum = str(sum)
      sum = sum + alphalist[rem-1]
    else:
      sum = sum + str(pow(10,i)*rem)
    n = int(n/16)
  print("hex is",sum[::-1])
    

def convertToOctal(n):
  n=int(n)
  sum=0
  i=0
  while(n!=0):
    rem=n%8
    sum = sum+(pow(10,i)*rem)
    i=i+1
    n=int(n/8)
  print("octal no is",sum)


def convertToDec(n):

  n = int(n)
  rem=0
  summ=0
  i=0
  while(n!=0):
    rem=int(n%2)
    summ=int(summ+rem*pow(2,i))
    i=i+1
    n=int(n/10)
  return int(summ)

def conversionToBin(n):
  j = 0
  a = 0
  s=''
  n = int(n)
  d = n                        #for conversion from decimal to binary
  while(n!=0):
    rem=int(n)%2
    s=s+str(rem)
    n=int(n/2)
  print("binary is",s[::-1])

def conversionStarts(n,ntype,typelist):
    a = 0
    s = ''
    
    if(ntype=='D'): 
      decno = convertToOctal(n)
      conversionToHex(n)
      conversionToBin(n)
      return n

    elif(ntype=='B'):
     
      decno = convertToDec(n)
      convertToOctal(decno)
      conversionToHex(decno)
      return decno
    
    elif(ntype=='H'):
      print(n)
      s = ''
      alphadict = {'0': '0000', '1': '0001', '2': '0010', '3':'0011', '4':'0100', '5': '0101','6':'0110', '7': '0111', '8':'1000', '9': '1001' , 'A': '1010', 'B': '1011', 'C': '1100', 'D':'1101', 'E': '1110', 'F': '1111'}
      for i in n:
        s=s+alphadict[i]
      print("Working")
      s = int(s)
      print("hex is",s)
      decimalno = convertToDec(s)
      print("dec is ",decimalno)
      convertToOctal(decimalno)
      conversionToBin(decimalno)
      return decimalno
        
    elif(ntype=='O'):
      
      n=int(n)                               #octal to decimal
      rem = 0
      i=0
      decno=0
      while(n>0):
        rem=n%10;
        decno = decno + rem * pow(8,i);
        i=i+1;
        n=int(n/10);
      conversionToBin(decno)                 #octal to binary
      conversionToHex(decno)
      return decno



n = input("enter the no:")
typelist = ['H', 'D', 'B', 'O']
ntype = input("Enter type:")
global alphalist
alphalist = [0,0,0,0,0,0,0,0,0,'A','B','C','D','E','F']
decno = conversionStarts(n,ntype,typelist)
print("its dec is",decno)

 
  