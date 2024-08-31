age = int(input("enter your age:"))
if age >= 0 and age <= 10:
    print("discount 20$")
elif age >= 11 and age <= 15:
    print("discount 15$")
elif age >= 16 and age <= 18:
    print("discount 5$")
elif age > 18:
    print("discount 0$")
print("proceed to payment")