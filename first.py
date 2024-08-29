n = int(input("enter the no. ="))
num = 11
if n==1:
    print("the no. is not prime")

if n > 1:
    for i in range (2,num):
        if num % i == 0:
            print("the no. is not prime")
            break
    else:
        print("the no. is prime")
