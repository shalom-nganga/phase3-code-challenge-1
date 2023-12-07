def timeConversion():
    timeEntered = input("Input time following this format HH:MM: ")
    hours,min= (int(i) for i in timeEntered.split(":"))
    print("Choose whether AM or PM \n 1: AM \n 2: PM")
    choice=input("Choose either option 1 or 2: ")
    if choice == "1":
        hours +=00
        time=f"{hours:02d}:{min:02d} hrs"
        print(time)
    elif choice == "2":
        hours +=12
        time=f"{hours:02d}:{min:02d} hrs"
        print(time)
timeConversion()