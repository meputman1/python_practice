age = int(input("How old are you? "))
is_student = input("Are you a student? (yes/no) ").lower()
if age < 5:
    print("Free")
elif 5 <= age <= 17:
    print("$8")
elif 18 <= age <= 64 and is_student == "no":
    print("$12")
elif 18 <= age <= 64 and is_student == "yes":
    print("$10")
else:
    print("$6")