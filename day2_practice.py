age = int(input("How old are you? "))

if age <= 13:
    print("Child")
elif age >= 14 and age <= 19:
    print("Teen")
elif age >= 20 and age<= 64:
    print("Adult")
else: 
    print("Senior")
