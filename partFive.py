# used .lower() to instantly lowercase any input so if someone was to enter an uppercase, it would still work
day = input("What day is it today? ").lower()

# distinguishing weekend days from weekdays
if (day=="saturday"
   or day=="sunday"):
   print("It's the weekend!")
elif (day=="monday"
   or day=="tuesday"
   or day=="wednesday"
   or day=="thursday"
   or day=="friday"):
   print("It's a weekday.")
# handling any invalid inputs
else:
   print("Invalid input. Please enter a day of the week.")