#Finding Runners up 

import array as arr
arr_num = arr.array('i',[])
n=int(input("Enter no. of scores: "))
for x in range(0,n):
    a=int(input("Enter score : "))
    arr_num.append(a)
    
print("SCORES: "+str(arr_num))

for i in range(0, len(arr_num)):    
    for j in range(i+1, len(arr_num)):    
        if(arr_num[i] > arr_num[j]):    
            t = arr_num[i]   
            arr_num[i] = arr_num[j]   
            arr_num[j] = t    
     
print()
print("The runners up score is: ");    
print(arr_num[-2])