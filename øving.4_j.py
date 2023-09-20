#Bruk funksjonen fra oppgave e) til å finne ut om temperaturen er stigende eller synkende for
#hvert tidspunkt. Gå gjennom lista som dere får når dere kaller funksjonen fra oppgave e) på temperaturlista. 
#For hvert element skriv ut indeksen og skriv ut «stigende» om 
#differansen er over 0, «synkende» om den er negativ eller «uforandret» om den er 0.

#oppgave e:
#def Differanse_i_liste(liste_1): 
#    differanse =[]
#    for i in range (len(liste_1)-1): 
#        diff = liste_1[i+1]-liste_1[i] 
#        differanse.append(diff) 
#    return differanse 

#resultat = Differanse_i_liste([1,7,5,4,9]) 
#print(resultat) 



def Differanse_i_liste(liste_1):
    differanse = []
    for i in range(len(liste_1) - 1):
        diff = liste_1[i + 1] - liste_1[i]
        differanse.append(diff)
    return differanse

temperaturliste = [20, 22, 24, 21, 19, 25, 23, 23]

differanser = Differanse_i_liste(temperaturliste)

for indeks, diff in enumerate(differanser):
    if diff > 0:
        print(f"Indeks {indeks}: stigende")
    elif diff < 0:
        print(f"Indeks {indeks}: synkende")
    else:
        print(f"Indeks {indeks}: uforandret")
