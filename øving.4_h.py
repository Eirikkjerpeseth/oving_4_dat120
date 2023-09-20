# Anta du har en plante som krever at temperaturen er +5 grader celsius for å vokse i det hele
# tatt, og så vokser fortere desto varmere det er, lineært med temperatur over 5 grader. Skriv
# en funksjon som regner ut summen av alle tall over 5 i lista. Så i lista [4, 7, 15] blir summen 0
# (for 4) + 2 (for 7) + 10 (for 15). 

def funksjontemp(temperaturer): 
    sum = 0 
    for temperaturer in temperaturer: 
        if temperaturer > 5: 
            vekst = temperaturer - 5 
            sum += vekst 
    return sum 
    if sum <= 0: 
        print("Negativ vekst, planten dør.")
    



resultat = funksjontemp([4,7,15]) 
print(resultat) 

