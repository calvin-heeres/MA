while True:
    print("Hello, You!, ik ben Calvin")

    import time
    time.sleep(2)
    print("Wie ben jij?")

    time.sleep(1)
    name = input("je naam:")

    time.sleep(1)
    print("Hello", name) 

    time.sleep(2)
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("De datum en tijd is", current_time)

    time.sleep(2)
    print("wil jij dit programma nog een keer doen?")

    time.sleep(2)
    answer = input("antwoord Y of N: ") 
    if answer == "Y":
        print("")


    time.sleep(1)
    if answer == "N":
        print("Dankjewel voor het gebruiken van dit programma") 
        break
