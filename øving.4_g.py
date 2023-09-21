# Skriv en funksjon som regner ut hva trenden i et datasett er. Datasettet skal bestå av to
# lister, ei liste med x-koordinater og ei liste med y-koordinater. Elementene på samme indeks
# i de to listene hører sammen. Trenden skal beregnes som to tall a og b, som skal fungere som
# parametere i en lineær formel: verdi = ax + b. Implementer følgende formler, hvor n er til
# men ikke med lengden til lista, xi er i-ende element i lista x, og 𝑥 er gjennomsnittet av alle
# verdiene i lista x. Merk at disse formlene og hvorfor de ser slik ut er pensum i emnet STA100,
# temaet lineær regresjon, minste kvadraters metode 



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

x_koordinat = [2,4,6,8,10]
y_koordinat = [1,3,5,7,9]  

a,b = trend_datasett(x_koordinat , y_koordinat) 
print(f"Trenden i datasettet er: verdi = {a:.2f}x + {b:.2f}")
    
