list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

num_min = list_of_numbers[0]

user_number = int(input("enter any number from 1 to 15 : "))

if user_number < 1:
    print("your number is lower than min")
elif user_number > 1 and user_number < 15:
    print("your number is bigger than min")
elif user_number > 15:
    print("error : pls read signs it says 'enter any number' ")