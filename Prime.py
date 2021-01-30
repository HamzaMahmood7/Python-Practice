num = int(input("Enter a number :"))

if num > 1:
    for x in range(2,num):
        if num % x == 0:
            print("Not a prime number")
            break
        else:
            print("Is a prime number")
            break
else:
    print("Is a prime number")