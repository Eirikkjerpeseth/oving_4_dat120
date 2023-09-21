# Bruk funksjonen fra oppgave g) for å finne trenden i temperaturlista. For å finne trenden
# bruker dere lista «temperaturer_tidspunkter» som x-koordinater og lista «temperaturer»
# som y-koordinater. Skriv ut om trenden er stigende eller synkende. Trenden er stigende hvis
# a er positiv, synkende hvis a er negativ og det er ingen trend hvis a er 0.  

def trend_datasett(x,y): 
    # finner gjennomsnitt av listene sum(n) / lengde(n)
    gjennomsnitt_x = sum(x) / len(x) 
    gjennomsnitt_y = sum(y) / len(y) 

    # Beregner a, stigningstallet
    numerator = sum((x[i] - gjennomsnitt_x) * (y[i] - gjennomsnitt_y) for i in range(len(x)))
    denominator = sum((x[i] - gjennomsnitt_x) ** 2 for i in range(len(x)))

    a = numerator / denominator 

    # beregner skjæringspunktet b, ved å ta gjennomsittav y - a * gjennomsnitt av x 
    b = gjennomsnitt_y - a * gjennomsnitt_x

    return a,b 




y_koordinat = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2] # temperaturer


temperaturer_tidspunkter = list()
for index in range(len(y_koordinat)):
    temperaturer_tidspunkter.append(index) 

x_koordinat = temperaturer_tidspunkter 

# Skriver ut forksjellige setninger ut ifra om trenden er stigende synkende eller = 0 
a,b = trend_datasett(x_koordinat , y_koordinat) 
if a > 0: 
    print(f"Trenden er stigende.") 
if a < 0: 
    print(f"Trenden er synkede.") 
if a == 0: 
    print(f"Trenden = 0.")



# Skriv ut om trenden er stigende eller synkende. Trenden er stigende hvis
# a er positiv, synkende hvis a er negativ og det er ingen trend hvis a er 




#temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]






