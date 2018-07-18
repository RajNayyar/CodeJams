# Complete the findMinReplacements function below.
def checkIfDistinct(s):
    for i in s:
        if(s.count(i)>1):
            print(i)
            return 0
    return 1
    
def isPalindrome(str):
 
    # Run loop from 0 to len/2 
    for i in range(0, int(len(str)/2)): 
        if str[i] != str[len(str)-i-1]:
            return False
    return True

def findMinReplacements(inputString):
   
    if(inputString==inputString[::-1]):
        return 0
    else:
        if(checkIfDistinct(inputString)==1):
            return len(inputString)-1
    
    i=0;
    j=len(inputString)-1
    appendList = []
    count1=0
    count2=0
    i=0
    j=len(inputString)
    while(i!=len(inputString)):
       
        if(isPalindrome(inputString[i:j])==1):
            count1 = count1
            break
        else:
            print(inputString[i:j])
            count1=count1+1
            i=i+1
    i=0
    while(j!=-1):
        if(isPalindrome(inputString[i:j])==1):
            count2=count2
            break
        else:
            print(inputString[i:j])
            count2=count2+1
            j=j-1
    if(count1==count2):
        
        return count1
    elif(count1<count2):
        return count1
    else:
        return count2
