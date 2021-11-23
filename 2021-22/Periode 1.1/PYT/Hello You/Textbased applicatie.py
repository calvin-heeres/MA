while True:
    import time 

    print("Je wordt wakker in je huis, je ligt op bed. Bommen exploderen om je heen, je paniekt en weet niet wat je moet doen.")
    time.sleep(2)
    answer1 = input("Wat moet je doen? \nA. Rustig blijven en opstaan \nB. In paniek blijven en schreeuwen \nC. Doorslapen \n ")
    time.sleep(1)
    if answer1 == "A" or answer1 == "a": 
        print("\nJe stapt uit je bed, het is donker in je kamer.")
        ans2 = input("wat is je volgende stap? \nA. Het licht aanzetten \nB. De deur zoeken \nC. Een random richting lopen \n ")
        if ans2 == "A" or answer1 == "a": 
            print("")

    if answer1 == "B" or answer1 == "b": 
        print("\nJe begint te schreeuwen, \nje buurman hoort je en stormt je kamer binnen. \nHij kalmeert je, dit duurt een halfuur \nNa dit halfuur proberen jullie een plan te bedenken. \nER VALT EEN BOM OP JE HUIS! \nJe overleeft de bom niet, je buurman wel... \n ")
    
    if answer1 == "C" or answer1 == "c": 
        print("Ik ben zeker niet goed in talen, ik ben alleen goed in Engels maar daar blijft het ook bij. Ik snap andere talen niet en talen snappen mij niet!")

    print("wil jij dit programma nog een keer doen?")

    answer2 = input("antwoord Y of N: ") 
    if answer2 == "Y" or answer2 == "y":
        print("")

    if answer2 == "N" or answer2 == "n":
        print("Dankjewel voor het gebruiken van dit programma") 
        break

    