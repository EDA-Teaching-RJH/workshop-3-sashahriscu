score = int(input("Input mark to obtain grade "))

# setting boundaries and handling invalid input
if score < 0 or score > 100:
    print("Invalid value, please enter a numerical score between 1 and 100")
# print corresponding letter grade
elif score >=90 and score <=100:
    print("Grade A")
elif score >=80 and score <=89:
    print("Grade B")
elif score >=70 and score <=79:
    print("Grade C")
elif score >=60 and score <=69:
    print("Grade D")
else:
    print("Grade F")
