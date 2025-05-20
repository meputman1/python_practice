age = int(input("How old are you? "))

if age >+ 21:
    print("You're allowed to drink alocohol in the US!")
else: print("Sorry, not old enough yet.")
score = int(input("Enter your score: "))
if score >=90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

is_tired = input("Are you tired? (yes/no) ")
is_busy = input("Are you busy? (yes/no) ")

if is_tired == "yes" and is_busy == "yes":
    print("You need a break!")
elif is_tired == "yes" or is_busy == "yes":
    print("Maybe take it easy.")
else:
    print("Full speed ahead!")
