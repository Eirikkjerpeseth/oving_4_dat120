# Finn antall penværsdager for hvert år og plott dette. Man kan finne antall penværsdager ved
# å sjekke gjennomsnittlig skydekke. Hver dag med verdi 3 eller lavere er en penværsdag.
# Inkluder bare år hvor det er data om skydekke for mesteparten av året, det må være data for
# minst 300 dager for at et år skal være gyldig.
 


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








def antall_penværsdager(datoer, skydekke):
    antall_dager_per_år = {}
    antall_penværsdager = 0
    maks_penværsdager = 0
    år_med_flest_penværsdager = 0

    for i in range(len(skydekke)):
        skydekke_verdi_str = skydekke[i].replace(',', '.')

        # Hopp over verdier som inneholder '-'
        if '-' in skydekke_verdi_str:
            continue

        try:
            skydekke_verdi = float(skydekke_verdi_str.split('.')[0])
        except ValueError:
            continue  # Hopp over dagen hvis det er en ValueError

        if skydekke_verdi <= 3:
            antall_penværsdager += 1
            if antall_penværsdager > maks_penværsdager:
                maks_penværsdager = antall_penværsdager
                år_med_flest_penværsdager = int(datoer[i].split(".")[-1])
        else:
            # Oppdater antall penværsdager for det gjeldende året
            år = int(datoer[i].split(".")[-1])
            antall_dager_per_år[år] = max(antall_penværsdager, antall_dager_per_år.get(år, 0))
            antall_penværsdager = 0

    return antall_dager_per_år, år_med_flest_penværsdager, maks_penværsdager


antall_dager_per_år, år_med_flest_penværsdager, maks_penværsdager = antall_penværsdager(datoliste,
                                                                                         gjennomsnittskydekke)
for år, antall_dager in antall_dager_per_år.items():
    print(f"Antall penværsdager i år {år}: {antall_dager} dager.")

print(f"\nÅret med flest penværsdager er {år_med_flest_penværsdager} med {maks_penværsdager} dager.")

# Plott resultatene
år = list(antall_dager_per_år.keys())
antall_dager = list(antall_dager_per_år.values())

plt.plot(år, antall_dager, marker='o')
plt.xlabel('År')
plt.ylabel('Antall penværsdager (dager)')
plt.title('Antall penværsdager per år')
plt.show() 

