print("Welcome to the ultimate love calculator")
name1 = input("What is your name? \n ")
name2 = input("What is their name? \n ")

combined_names = name1 + name2
lower_case_string = combined_names.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

true_love = int(str(true) + str(love))

if (true_love < 10) or (true_love > 90):
    print(f"your love score is {true_love}, you go like coke and mentos.")
elif (true_love >= 40) and (true_love <= 50):
    print(f"your love score is {true_love}, you go together.")
else:
    print(f"Your love score is {true_love}")

