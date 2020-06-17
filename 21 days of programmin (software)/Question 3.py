#Program to find Sum of GP Series

x = int(input("Enter First Number of a G.P Series: = "))
n = int(input("Enter the Total Numbers in the G.P Series: = "))
r = int(input("Enter the Common Ratio = "))

t = 0
val = x
print("\nG.P  Series :", end = " ")
for i in range(n):
    print("%d  " %val, end = " ")
    t = t + val
    val = val * r
print("\n Sum of GP Series = " , t)
