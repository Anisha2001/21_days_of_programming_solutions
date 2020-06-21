#Palindrome string or not

def isPalindrome(str): 
    for i in range(0, int(len(str)/2)):  
        if str[i] != str[len(str)-i-1]: 
            return False
    return True
  
string=str(input("Enter a string = "))
ans = isPalindrome(string) 
  
if (ans): 
    print("Yes") 
else: 
    print("No") 
    