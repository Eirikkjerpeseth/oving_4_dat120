

import matplotlib.pyplot as plt

# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 08:30:27 2023

@author: simon olsen
"""
navnliste = []
stasjonIDliste = []
datoliste = []
snodybdeliste = []
nedborliste = []
middeltemp = []
gjennomsnittskydekke = []
hoyestmiddelvind = []


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
            middeltemp.append(ordene[5])
            gjennomsnittskydekke.append(ordene[6])
            hoyestmiddelvind.append(ordene[7])
jabba() 




datoer = datoliste
nedbør = nedborliste


def finn_lengste_periode_med_null_nedbør(datoer, nedbør):
    nåværende_periode = 0
    lengste_periode = 0
    start_indeks = 0
    lengste_start_indeks = 0
    år_med_lengste_periode = 0

    for i in range(len(nedbør)):
        if nedbør[i] == '0':
            nåværende_periode += 1
            if nåværende_periode == 1:
                start_indeks = i
            if nåværende_periode > lengste_periode:
                lengste_periode = nåværende_periode
                lengste_start_indeks = start_indeks
                år_med_lengste_periode = int(datoer[i].split(".")[-1])
        else:
            nåværende_periode = 0

    return lengste_periode, år_med_lengste_periode

# Eksempel bruk:

antall_dager, år_med_lengste_periode = finn_lengste_periode_med_null_nedbør(datoer, nedbør)
print(f"Lengste periode med 0 nedbør: {antall_dager} dager, år: {år_med_lengste_periode}")


################################ 


import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def lengste_tørke_per_år(nedbørsliste, datoliste, start_år, slutt_år):
    år_og_maks_lengde = {}

    for år in range(start_år, slutt_år + 1):
        # Sjekk om det er nok data for å gjøre året gyldig
        antall_dager = sum(1 for dato in datoliste if dato and datetime.strptime(dato, "%d.%m.%Y").year == år)
        
        if antall_dager >= 300:
            lengde = 0
            maks_lengde = 0

            for tall, dato_str in zip(nedbørsliste, datoliste):
                if dato_str and datetime.strptime(dato_str, "%d.%m.%Y").year == år:
                    if tall == '0':
                        lengde += 1
                        maks_lengde = max(maks_lengde, lengde)
                    elif tall != '0':
                        lengde = 0

            år_og_maks_lengde[år] = maks_lengde

    return år_og_maks_lengde

# Eksempel på bruk:


start_år = 1980
slutt_år = 2023

resultater = lengste_tørke_per_år(nedborliste, datoliste, start_år, slutt_år)






# Plott resultatene
år = list(resultater.keys())
maks_lengde = list(resultater.values())

plt.plot(år, maks_lengde, marker='o')
plt.xlabel('År')
plt.ylabel('Maks Tørkeperiode (dager)')
plt.title('Maks Tørkeperiode per År')
plt.show()
