import time
print("Wat denk je dat waar is over mij, beantwoord dit om meer over mij te weten te komen. \n")
time.sleep(3)
answer = input("Beantwoord deze vraag met A,B of C! \nA. Ik kom van vmbo-t \nB. Ik woon in zaanstad \nC. Ik ben goed in talen ")
time.sleep(1)
if answer == "A" : 
    print("Ik kom van Havo 3, hierdoor ben ik ook de jongste uit de klas.")
if answer == "B": 
    print("Dat is goed. Ik woon hier al mn hele leven, en ben 1x verhuisd binnen zaanstad.")
if answer == "C": 
    print("Ik ben zeker niet goed in talen, ik ben alleen goed in Engels maar daar blijft het ook bij. Ik snap andere talen niet en talen snappen mij niet!")
