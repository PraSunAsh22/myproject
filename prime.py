num = int(input("Enter given number is prime or not:"))
if num > 1 :
    for i in range(2, num):
        if num % i == 0:
            print("number is not a prime")
            break
    else:
        print("number is prime")
