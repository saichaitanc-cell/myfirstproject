items = []
while True:
    choice = input("\na-Add  r-Remove  s-Show  q-Quit\nChoose: ")
    if choice == "q":
        print("Goodbye!")
        break
    elif choice == "a":
        while True:
            item =input("Item to add (or 'done' to finish): ")
            if item.lower() in ("checkout","done"):
                print("Items added in cart")
                break
            if item in items:
                print(f"{item} is already in the list")
            items.append(item)
            print(f"Added:{item}")
    elif choice == "s":
       if len(items)==0:
         print("List is empty")
       else:
         items.sort()
         number =1
         for item in sorted(set(items)):
            count = items.count(item)
            if count > 1:
                print(f"{number}.{item}({count})")
            else:
                print(f"{number}. {item}")
            number +=1
    elif choice == "r":
        rem = input("Item to remove: ")
        if rem in items:
            items.remove(rem)
            print(f"removed {rem}")
        else:
            print(f"{rem} is not in the list")
    else:
        print("Invalid choice")