number = int(input("secret number : "))
guess = int(input("guess number from 1 to 10 : "))
while guess != number:
    print("WRONG!, TRY AGAIN!")
else: print("correct!")
