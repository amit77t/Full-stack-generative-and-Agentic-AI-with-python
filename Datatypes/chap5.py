age = 18

if age >= 18:
    print("you are eligible to vote")

else:
    print("you can not vote ")


cup_size = input("Enter cup size: ").lower()

if cup_size == "small":
    price = 10

elif cup_size == "medium":
    price = 20

elif cup_size == "large":
    price = 30

else:
    price = None
    print("Unknown cup size!")

if price is not None:
    print(f"Your chai price is ₹{price}")