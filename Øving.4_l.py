def funksjontemp(temperaturer): 
    sum = 0 
    for temperaturer in temperaturer: 
        if temperaturer > 5: 
            vekst = temperaturer - 5 
            sum += vekst 
    return sum 



resultat = funksjontemp([-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18,
21, 26, 21, 31, 15, 4, 1, -2])
print(f"Planten vil vokse {resultat} ved temperaturene i lista") 