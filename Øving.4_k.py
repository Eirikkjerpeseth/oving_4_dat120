# Bruk funksjonen fra oppgave g) for å finne trenden i temperaturlista. For å finne trenden
# bruker dere lista «temperaturer_tidspunkter» som x-koordinater og lista «temperaturer»
# som y-koordinater. Skriv ut om trenden er stigende eller synkende. Trenden er stigende hvis
# a er positiv, synkende hvis a er negativ og det er ingen trend hvis a er 0.  


temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]

dogn_nedbor = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]

temperaturer_tidspunkter = list()

for index in range(len(temperaturer)): 
    
temperaturer_tidspunkter.append(index) 
