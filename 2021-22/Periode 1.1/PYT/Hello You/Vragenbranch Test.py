while True:
    import sys
    import time
    import os
    print("Hello, You!, ik ben Calvin")
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

    print("Wat denk je dat waar is over mij, beantwoord dit om meer over mij te weten te komen. \n")
    time.sleep(3)
    answer1 = input("Beantwoord deze vraag met A,B of C! \nA. Ik kom van vmbo-t \nB. Ik woon in zaanstad \nC. Ik ben goed in talen ")
    time.sleep(1)
    if answer1 == "B" or answer1 == "b":
        print("Dat is goed. Ik woon hier al mn hele leven, en ben 1x verhuisd binnen zaanstad.")
    if answer1 == "A" or answer1 == "a": 
        print("Ik kom van Havo 3, hierdoor ben ik ook de jongste uit de klas.")   
    if answer1 == "C" or answer1 == "c": 
        print("Ik ben zeker niet goed in talen, ik ben alleen goed in Engels maar daar blijft het ook bij. Ik snap andere talen niet en talen snappen mij niet!")
        

 

    print("wil jij dit programma nog een keer doen?")

    answer0 = input("antwoord Y of N: ") 
    if answer0 == "Y" or answer0 == "y":
        os.system('cls')
        print("")


    if answer0 == "N" or answer0 == "n":
        print("Dankjewel voor het gebruiken van dit programma")
        os.system('cls')
        break