#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 12:23:14 2023

@author: alfredvik
"""

#Beregn veksten for den tenkte planten for hvert år i datasettet med bruk av funksjonen fra del 1 oppgave h). 
#Plott dette for hvert år i datasettet. 
#Inkluder bare år hvor det er temperaturdata for mesteparten av året, det må være data for minst 300 dager for at et år skal være gyldig.
# Dette vil kreve at dere lager separate lister for hvert år som kan brukes som parameter til funksjonen fra del 1 oppgave h)

#OPG H DEL 1
# Anta du har en plante som krever at temperaturen er +5 grader celsius for å vokse i det hele
# tatt, og så vokser fortere desto varmere det er, lineært med temperatur over 5 grader. Skriv
# en funksjon som regner ut summen av alle tall over 5 i lista. Så i lista [4, 7, 15] blir summen 0
# (for 4) + 2 (for 7) + 10 (for 15). 


import matplotlib.pyplot as plt



navnliste = []
stasjonIDliste = []
datoliste = []
snodybdeliste = []
nedborliste = []
middeltemp = []
gjennomsnittskydekke = []
hoyestmiddelvind = []

temperaturliste = []

# Definer funksjonen for å beregne vekst
def funksjontemp(temperaturer):
    sum_vekst = 0
    for temperatur in temperaturer:
        if temperatur > 5:
            vekst = temperatur - 5
            sum_vekst += vekst
    return sum_vekst







def jabba():
    with open("snoedybder_vaer_en_stasjon_dogn.csv","r",encoding="UTF8") as fila:
        first_line = fila.readline()
        for linje in fila:
            ordene = linje.split(";")
            navnliste.append(ordene[0])
            stasjonIDliste.append(ordene[1])
            datoliste.append(ordene[2])
            try:
                snodybdeliste.append(int(ordene[3]))
            except ValueError:
                snodybdeliste.append(0)  
            nedborliste.append(ordene[4])
            try:
                middeltemp.append(int(ordene[5]))
            except ValueError:
                middeltemp.append(0)
            gjennomsnittskydekke.append(ordene[6])
            hoyestmiddelvind.append(ordene[7])

jabba()



def separate_lister(temperatur_data, dato_liste, min_antall_dager):
    årsvis_data = {}  # Et tomt dictionary for å holde separate lister for hvert år

    for dato, temperatur in zip(dato_liste, temperatur_data):
        år = dato.split(".")[-1]  # Hent ut årstallet fra datoen

        if år not in årsvis_data:
            årsvis_data[år] = []

        årsvis_data[år].append(temperatur)

    # Filtrer ut lister med færre enn min_antall_dager dager med data
    for år in list(årsvis_data.keys()):
        if len(årsvis_data[år]) < min_antall_dager:
            del årsvis_data[år]

    return årsvis_data


min_antall_dager = 300

jabba()

# Opprett separate lister for hvert år
årsvis_temperaturdata = separate_lister(middeltemp, datoliste, min_antall_dager)





vekst_resultater = {}

# Gå gjennom hvert år i årsvis_temperaturdata og beregn vekst for hvert år
for år, temperaturliste in årsvis_temperaturdata.items():
    # Bruk funksjontemp til å beregne vekst for dette året
    vekst = funksjontemp(temperaturliste)
    
    # Lagre resultatet i vekst_resultater-dictionary med året som nøkkel
    vekst_resultater[år] = vekst

# Skriv ut veksten for hvert år
for år, vekst in vekst_resultater.items():
    print(f"Vekst for år {år}: {vekst}")




 #Innstillinger for plott
 
plt.figure()
år_liste = list(vekst_resultater.keys())
vekst_liste = list(vekst_resultater.values())     
     
plt.plot(år_liste, vekst_liste, marker='o')
     
     #Overskrifter
plt.xlabel('År')
plt.ylabel('Plantevekst')
plt.title('Plantens vekst over årene')
plt.grid(True)


#justering av utforming
plt.xticks(rotation='vertical')
plt.tight_layout()
     
plt.show()
 
 
 