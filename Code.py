name = input("What is your name? ")
print("Welcome to the game, " + name + "!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come across a river, you can walk around it or swim across. Type walk to walk around and swim to swim across .").lower()
    if answer == "walk":
        print("You walked for many miles, ran out of food and water, and died.")
    elif answer == "swim":
        print("You swam across the river and were eaten by an alligator.")
    else:
        print("You didn't pick walk or swim! Try again.")

elif answer == "right":
    answer = input("You come across a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()
    if answer == "back":
        print("You go back and were never heard from again.")
    elif answer == "cross":
        print("You crossed the bridge and lived!")
    else:
        print("You didn't pick cross or back! Try again.")

    if answer == "cross":
        answer = input("You see a house and a shed. Which do you go to, house or shed? ").lower()
        if answer == "house":
            print("You go to the house and are eaten by a bear.")
        elif answer == "shed":
            print("You go to the shed and find a boat. You sail away and win the game!")
        else:
            print("You didn't pick house or shed! Try again.")
    elif answer == "back":
        print("You go back and were never heard from again.")   

else:
    print("You didn't pick left or right! Try again.")
