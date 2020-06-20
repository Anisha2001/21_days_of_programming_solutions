#Frequency calculation

def freq_cal(x):
    freq = dict()   
    while(x):       
        dig = x%10    
        if (dig in freq):    
            freq[dig] = (freq[dig] + 1) 
        else:
            freq[dig] = 1    
        x = int(x/10)
    print(freq)
x=int(input("Enter a number= "))   
freq_cal(x)