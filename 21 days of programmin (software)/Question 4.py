#Prime number
def primeno():
    a=int(input("Enter the first number = "))
    b=int(input("Enter the second number = "))
    for num in range(a, b):
      for i in range(2, num):
        if num % i == 0:
            break
        else:
            print(num)
            break
primeno()