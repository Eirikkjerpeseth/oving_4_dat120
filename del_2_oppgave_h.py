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
#%% 



################################################################################################################ 




import statistics

def høyeste_middelvind_og_median(datoliste, middelvindliste):
    data_per_år = {}
    
    for i in range(len(datoliste)):
        print(f"Forsøker å konvertere '{datoliste[i]}' til et heltall.")
        
        år_str = datoliste[i].split(".")[-1]
        if not år_str.isdigit():
            print(f"Ugyldig årformat: '{år_str}', fortsetter til neste iterasjon.")
            continue
        
        år = int(år_str)
        
        # Hopp over verdier som inneholder '-'
        if '-' in middelvindliste[i]:
            continue
        
        try:
            middelvind_verdi = float(middelvindliste[i].replace(',', '.'))
        except ValueError:
            print(f"Ugyldig middelvindformat: '{middelvindliste[i]}', fortsetter til neste iterasjon.")
            continue
        
        if år not in data_per_år:
            data_per_år[år] = []
        
        data_per_år[år].append(middelvind_verdi)
    
    høyeste_middelvind_per_år = {}
    median_middelvind_per_år = {}

    for år, vindverdier in data_per_år.items():
        if len(vindverdier) >= 300:
            høyeste_middelvind_per_år[år] = max(vindverdier)
            median_middelvind_per_år[år] = statistics.median(sorted(vindverdier))
    
    return høyeste_middelvind_per_år, median_middelvind_per_år

import matplotlib.pyplot as plt


# Få resultatene fra funksjonen
høyeste_middelvind, median_middelvind = høyeste_middelvind_og_median(datoliste, hoyestmiddelvind)

# Hent ut data for plotting
år_høyeste = list(høyeste_middelvind.keys())
verdi_høyeste = list(høyeste_middelvind.values())

år_median = list(median_middelvind.keys())
verdi_median = list(median_middelvind.values())

# Plotting
plt.figure(figsize=(12, 6))

# Høyeste middelvind
plt.subplot(1, 2, 1)
plt.plot(år_høyeste, verdi_høyeste, marker='o')
plt.xlabel('År')
plt.ylabel('Høyeste Middelvind (m/s)')
plt.title('Høyeste Middelvind per år')

# Median middelvind
plt.subplot(1, 2, 2)
plt.plot(år_median, verdi_median, marker='o', color='orange')
plt.xlabel('År')
plt.ylabel('Median Middelvind (m/s)')
plt.title('Median Middelvind per år')

plt.tight_layout()
plt.show()
