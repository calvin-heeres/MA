import time 
def vraag1():
    print("\nIn Afghanistan woon je in het noorden, samen met je familie. In de jaren voor de oorlog hadden jullie het goed. Jullie hadden moderne opvattingen, waren vrij om te studeren en werden als vrouw niet beperkt in je rechten. ")
    antwoord = input()
    vraag2()

def vraag2():
    print("\nJullie vrije leven is onder druk komen te staan toen de Taliban steeds meer terrein won. Jullie lopen gevaar: door jullie manier van leven, maar ook omdat jouw broer chirurg en directeur is in het centrale ziekenhuis in het noorden. Hij behandelt veel vredesstrijders onder leiding van verzetsleider Ahmad Shah Massoud. Daardoor heeft hij problemen met de Taliban. Jullie vrezen voor jullie leven. ")
    antwoord = input()
    vraag3()

def vraag3():
    print("\nJe bent twaalf, ineens staan er Talibanleden voor je huis. Drie jaar daarvoor was je moeder overleden. Je vader is in een andere stad aan het werk. Ze komen binnen en vernielen alles. Meubelstukken, apparatuur, maar het ergste van al: de persoonlijke herinneringen aan je moeder. Foto's, geluidsbestanden met jouw moeders stem, video’s: alles wordt kapotgemaakt. De Talibanleden hangen zelfs tapelinten van de video's in de perenboom in de tuin. ")
    antwoord = input()
    vraag4()

def vraag4():
    print("\nNa de inval van de Taliban is bij jullie thuis de situatie dreigender geworden. De Taliban rukten op tot jullie stad. Dag en nacht horen jullie nu schoten. De noordelijke alliantie heeft steeds meer terrein verloren, hierdoor is het voor jullie nu te gevaarlijk. ")
    print("\nA: Je blijft bang binnen \nB: Je gaat nog steeds de straat op ")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag5()
    elif antwoord.lower() == "b":
        vraag6()
    else:
        print("Kies tussen a of b")
        vraag4()

def vraag5():
    print("\nJe gaat het huis niet meer uit. Een paar dagen later komt je broer thuis en vertelt hij dat jullie meteen weg moeten. Tijd om voor te bereiden hebben jullie niet, je zus doet dit dan ook niet en gaat meteen in de auto zitten.. ")
    antwoord = input()
    vraag11()

def vraag6():
    print("\nJe gaat de volgende dag de straat op, kijken of je vriendinnen die je kent ook buiten kunnen komen spelen. Je komt aan bij het huis van je vriendin, je ziet dat het huis leeg is. Er ligt bloed op de vloer en haar hond is verwondt en bloedt. Hij zal de volgende dag waarschijnlijk niet halen.  ")
    print("\nA: Je helpt de hond 1 \nB: Je verlost de hond uit zijn lijden en gaat naar buiten ")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag7()
    elif antwoord.lower() == "b":
        vraag9()
    else:
        print("Kies tussen a of b")
        vraag6()

def vraag7():
    print("\nJe probeert de hond te helpen, je zoekt naar verband dit vindt je in de wc. Je verbindt de wond. De hond haalt het tot de volgende ochtend maar is heel zwak en heeft voedsel en water nodig.  ")
    antwoord = input()
    print("\nA: Je zoekt naar voedsel \nB: Je laat de hond honger lijden en gaat weer naar buiten ")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag8()
    elif antwoord.lower() == "b":
        vraag10()
    else:
        print("Kies tussen a of b")
        vraag7()

def vraag8():
    print("\nJe begint te zoeken naar voedsel voor de hond, binnen zoek je overal. Na 15 minuten zoeken en meubels verplaatst te hebben heb je niks gevonden. Je gaat nu dus naar buiten en gaat daar zoeken naar voedsel. ")
    antwoord = input()
    vraag10()

def vraag9():
    print("\nJe zoekt iets waardoor je de hond een makkelijke dood kan laten begaan, je vindt een wapen in een kastje. Dit wapen was van de vader van je vriendin, je probeert uit te zoeken hoe dit wapen werkt. Je komt erachter na 10 minuten en bent bang om de hond te schieten, je blijft maar twijfelen maar doet dit nu toch. Je huilt maar probeert geen geluid te maken. Na 10 minuten huilen ga je naar buiten. ")
    antwoord = input()
    vraag10()

def vraag10():
    print("\nJe bent nu buiten en loopt een beetje rond, je besluit naar de markt te gaan, hier staan Talibanleden. De Talibanleden schreeuwen naar je en achtervolgen je, ze lossen een paar schoten in de lucht. Je struikelt en de Talibanleden grijpen je, door deze vlucht actie zijn ze boos. Ze trekken een zak over je hoofd en zoeken naar je broer, deze vinden ze. Je wordt wakker in een kamer en ziet je broer voor je, ze laten je toekijken naar hoe ze je broer slaan en jullie vragen stellen over jullie vader die voor de overheid werkt. Jullie geven geen antwoord op deze vragen, hierdoor nemen ze jou naar een andere kamer en wordt je hier verkracht en vermoord. Je broer wordt neergeschoten in de andere kamer. ")
    antwoord = input()
    print("\nEINDE!")
    antwoord = input()
    print("\nWil je dit programma nog een keer overnieuw doen? \na: Ja \nb: Nee")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag1()
    elif antwoord.lower() == "b":
        vraag23()
    else:
        print("Kies a of b")
        vraag10()

def vraag11():
    print("\nJe neemt nog snel wat sieraden van je moeder mee, maar de rest van jouw spullen moet je achterlaten. Je loopt de trap af en gaat naar buiten. ")
    antwoord = input()
    vraag12()

def vraag12():
    print("\nOp het moment dat je naar buiten stapt schrik je. De straat is verlaten, winkels zijn gesloten. De stoep is bezaaid met afval. Ontroostbaar stap je in de auto, je weet dat je jouw huis nooit meer terug zal zien. Je ziet ook tranen bij jouw broer. Het is de eerste keer dat je hem ziet huilen. ")
    antwoord = input()
    vraag13()

def vraag13():
    print("\nDeze eerste vlucht leidt ons naar een stad die nog niet veroverd is door de Taliban. Maar toen het ook daar te gevaarlijk werdt, is vluchten naar het buitenland nu de enige optie geworden. We hebben de keuze gemaakt om naar Pakistan te vluchten en vanuit daar het vliegtuig te pakken.. ")
    antwoord = input()
    vraag14()

def vraag14():
    print("\nJouw vader moet de moeilijkste beslissing uit zijn leven maken door achter te blijven. Hij bezit veel landgoed en huizen en weet dat dat allemaal in de handen van de Taliban zou vallen als hij zou vertrekken. Bovendien is hij te trots om te vluchten: hij houdt van zijn land en landgenoten en zou zich nooit ergens anders thuis kunnen voelen. Je wilt bij je vader blijven maar je broer laat dit niet toe, hij zet je in de auto en doet de deur op slot. De bestuurdersstoel van de auto staat van het slot af, je hebt de mogelijkheid om vanuit de achterstoel naar de voorstoel te gaan en uit de auto te kunnen stappen. Hierdoor kan je achterblijven met je vader, neem je deze mogelijkheid?  ")
    print("\nA: Ja  \nB: Nee ")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag15()
    elif antwoord.lower() == "b":
        vraag17()
    else:
        print("Kies tussen a of b")
        vraag14()

def vraag15():
    print("\nJe klimt op de voorstoel en stapt uit de auto, je verstopt je achter een muur en ziet je vader je broer en zus afscheid nemen. Ze denken allemaal dat je slaapt onder de deken dus beginnen zij weg te rijden richting Pakistan. Je rent richting je vader en omhelst hem, je vader is boos dat je bent achtergebleven tegelijkertijd is hij blij dat je bij hem bent. Toch huilt hij hierom. Je vader neemt de beslissing je richting Turkije te rijden met zijn eigen auto, hij weet dat de rijs 2 dagen duurt en moet langs het tankstation rijden voor benzine. Na een 4 uur komen jullie aan bij het tankstation en tanken jullie de auto plus 3 jerrycans vol met benzine. Jullie zouden het moeten redden naar Turkije vanaf nu.. ")
    antwoord = input()
    vraag16()

def vraag16():
    print("\nNa 11 uur rijden jullie in het westen van Afghanistan, hier rijden er Talibanleden langs jullie. Je duikt onder een deken en verstopt je omdat je bang bent. Wat jullie niet weten is dat er Talibanleden de weg blokkeren 5 minuten verderop, jullie komen aan bij de wegversperring en zij laten jullie er niet langs. Je vader probeert weg te rijden maar zij laten jullie niet weg gaan, je vader draait de auto om en probeert weg te rijden. De Talibanleden worden boos en beginnen op jullie auto te schieten, 1 kogel raakt 1 van de jerrycans die achterin liggen. De jerrycan ontploft en jij bent de enige die deze aanval overleeft. De Talibanleden nemen je mee in hun auto en laten je na 4 jaar met iemand trouwen tegen je wil in. ")
    antwoord = input()
    print("\nEINDE!")
    antwoord = input()
    print("\nWil je dit programma nog een keer overnieuw doen? \na: Ja \nb: Nee")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag1()
    elif antwoord.lower() == "b":
        vraag23()
    else:
        print("Kies a of b")
        vraag16()

def vraag17():
    print("\nJe blijft in de auto zitten en valt in slaap terwijl jullie naar Pakistan rijden. Jullie komen aan bij het vliegveld in Islamabad en moeten kiezen welk land jullie naartoe willen vliegen,  jullie vader heeft jullie genoeg geld gegeven voor 3 vluchten naar een ander land. De 2 eerst volgende vluchten gaan naar Duitsland en Nederland, de 2 landen waar het veilig is en er azcs zijn. Hiermee zal jullie geld wel opkomen en zullen jullie zonder geld in 1 van deze landen zitten. Maar hier zitten jullie tenminste veilig. ")
    print("\nA: Duitsland  \nB: Nederland ")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag18()
    elif antwoord.lower() == "b":
        vraag20()
    else:
        print("Kies tussen a of b")
        vraag17()

def vraag18():
    print("\nJullie nemen de vlucht naar Munchen, Duitsland.  Na ongeveer 7 uur komen jullie aan in Munchen en zoeken jullie hulp bij de overheid. Omdat jij minderjarig bent krijg jij een voogd toegewezen, deze voogd woont 350KM van het azc af waar je broer en zus op de wachtrij staan. Je broer en zouden de mogelijkheid krijgen om naar een azc dichter in de buurt verhuisd te worden, maar de keuze was te lang en het azc zit nu bomvol.. ")
    antwoord = input()
    vraag19()

def vraag19():
    print("\nHet is nu 7 jaar verder en je bent nu 19, je hebt jouw broer en zus in deze 7 jaar niet meer gesproken. Je mist je familie en neemt het besluit je broer en zus op te zoeken in het azc. Na ongeveer 4 uur rijden kom je aan bij het azc, hier vraag je naar de namen van je broer en zus. Je krijgt te horen dat zij uit het azc zijn gehaald en in hun eigen flats zijn gaan wonen. Je vraagt naar het adres van de flats maar dit is persoonlijke informatie en mag niet gegeven worden. 6 maanden vliegen voorbij en je broer en zus zijn ook naar je op zoek geweest, jullie spreken af bij jouw huis. Je broer en zus zie je na 7,5 haar eindelijk weer terug. Je bent super blij en jullie praten alles bij, alleen jullie vader is er niet. ")
    antwoord = input()
    print("\nEINDE!")
    antwoord = input()
    print("\nWil je dit programma nog een keer overnieuw doen? \na: Ja \nb: Nee")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag1()
    elif antwoord.lower() == "b":
        vraag23()
    else:
        print("Kies a of b")
        vraag19()

def vraag20():
    print("\nJullie nemen het vliegtuig naar Nederland, jullie komen aan op vliegveld schiphol en nemen vanaf hier een taxi naar Amsterdam. Hier zoeken jullie hulp bij de overheid, jij krijgt een voogd door je jonge leeftijd. Je broer en zus kunnen opgevangen worden in een azc in Amsterdam. Jouw voogd woont gelukkig in Amsterdam. Jullie houden contact en jullie bezoeken elkaar regelmatig. ")
    antwoord = input()
    vraag21()

def vraag21():
    print("\nHet is nu 10 jaar verder en jij bent goed op je benen gezet door je voogd. Je broer, zus en jij hebben jullie eigen flat waar jullie wonen. Jullie spreken af elke week, jij hebt zelf nu een vriend. Na 8 jaar van de 10 is je vader naar Nederland gevlogen nadat het zelfs voor hem te gevaarlijk in Afghanistan was. Hij is hierna opgevangen bij je zus en daar woont hij nu al 2 jaar. ")
    antwoord = input()
    vraag22()

def vraag22():
    print("De toekomst")
    antwoord = input()
    print("\nHet is nu 21 jaar terug dat je gevlucht bent uit Afghanistan, je hebt nu een gezin. Een man en 2 kinderen van 6 en 8. Het is goedgekomen met jouw familie, zelf werk je nu in de zorg en woon je nu in een huis in Alkmaar. Je denkt na over je toekomst en denkt dat het niet beter dan dit kan, jij en je familie zijn nu veilig en gelukkig en daar gaat het om! ")
    antwoord = input()
    vraag23()

def vraag23():
    print("\nBedankt voor het gebruiken van dit programma!")

vraag1()