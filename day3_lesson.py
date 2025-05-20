num_items = int(input("How many grocery items would you like to add?"))
grocery_lists = []
for i in range(num_items):
    grocery_item = input("Enter grocery item: ")
    grocery_lists.append(grocery_item)
print("Your grocery list is:")
for item in grocery_lists:
    print(f"- {item}")
for item in sorted(grocery_lists):
    print(f"- {item}")