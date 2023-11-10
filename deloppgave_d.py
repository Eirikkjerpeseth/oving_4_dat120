#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 16:47:43 2023

@author: alfredvik
"""

#Plott antall dager med skiføre for hver skisesong (fra oppgave b) og trend (fra oppgave c) i samme plott, 
#med året skisesongen starter på x-aksen og antall dager med skiføre på y- aksen.
# For å plotte trenden, bruk formelen y = ax+b til å regne ut to punkter, 
#ett for året datasettet starter og ett for året datasettet slutter. 
#Inkluder bare år hvor det er data om snødybde for mesteparten av skisesongen, 
#det må være data for minst 200 dager i hver skisesong.

import csv
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Funksjon for å beregne antall dager med skiføre for en vintersesong
def antall_skiføre_dager(dataset):
    # (din eksisterende kode for antall_skiføre_dager her)
    skisesonger = {}

    for row in dataset:
        try:
            dato = datetime.strptime(row[2], "%d.%m.%Y")
        except ValueError:
            continue

        if dato.month >= 10:
            start_dato = datetime(dato.year, 10, 1)
            slutt_dato = datetime(dato.year + 1, 6, 1)
        elif dato.month >= 6:
            start_dato = datetime(dato.year, 10, 1)
            slutt_dato = datetime(dato.year + 1, 6, 1)
        else:
            start_dato = datetime(dato.year - 1, 10, 1)
            slutt_dato = datetime(dato.year, 6, 1)

        # Initialiserer dictionary. For hver skisesong starter telling 0
        if start_dato not in skisesonger:
            skisesonger[start_dato] = 0

        # Hvis snømengde verdi er - sett den til 0
        snomengde = 0 if row[3] == '-' else int(row[3])

        if snomengde >= 20 and start_dato <= dato <= slutt_dato:
            skisesonger[start_dato] += 1

    return skisesonger
    pass

# Funksjon for å beregne trenden
def trend_datasett(x, y): 
    gjennomsnitt_x = sum(x) / len(x) 
    gjennomsnitt_y = sum(y) / len(y) 

    # Beregner a, stigningstallet
    numerator = sum((x[i] - gjennomsnitt_x) * (y[i] - gjennomsnitt_y) for i in range(len(x)))
    denominator = sum((x[i] - gjennomsnitt_x) ** 2 for i in range(len(x)))

    a = numerator / denominator 

    # beregner skjæringspunktet b, ved å ta gjennomsittav y - a * gjennomsnitt av x 
    b = gjennomsnitt_y - a * gjennomsnitt_x

    return a,b # (din eksisterende kode for trend_datasett her)
    pass

# Les data fra CSV-filen
dataset = []
with open('snoedybder_vaer_en_stasjon_dogn.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    for row in csvreader:
        dataset.append(row)

# Hopper over første rad
header = dataset[0]
dataset = dataset[1:]

# Beregn antall dager med skiføre for hver vintersesong
resultat = antall_skiføre_dager(dataset)

# Opprett lister med x- og y-verdier for trenden
x_koordinat = [start_dato.year for start_dato in resultat.keys()]
y_koordinat = list(resultat.values())

# Bruk funksjonen for å beregne trenden
a, b = trend_datasett(x_koordinat, y_koordinat)

# Skriv ut resultatet
print(f"Trenden for antall dager med skiføre er: verdi = {a:.2f}x + {b:.2f}")

# Plott antall dager med skiføre og trenden
plt.figure()
plt.plot(x_koordinat, y_koordinat, label='Antall dager med skiføre')
plt.plot(x_koordinat, [a * x + b for x in x_koordinat], label=f'Trend: {a:.2f}x + {b:.2f}')

# Visuell forbedring: Legg til aksetitler og en tittel
plt.xlabel('År')
plt.ylabel('Antall dager med skiføre')
plt.title('Antall dager med skiføre og trenden over tid')

# Legg til en figurlegende
plt.legend()

# Vis plottet
plt.show()

