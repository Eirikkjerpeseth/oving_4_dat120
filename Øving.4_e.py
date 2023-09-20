# Skriv en funksjon som tar inn ei liste med tall. For hvert tall i lista unntatt det siste skal
# funksjonen regne ut differansen mellom neste tall i lista og dette tallet. Differansene skal
# legges inn i ei ny liste 



def Differanse_i_liste(liste_1): 
    differanse = 0 
    for n in range (len(liste_1)-1): 
        diff = liste_1[i +1]-liste_1[i] 
        differanse.append(diff) 
    return differanse 

resultat = Differanse_i_liste([1,7,5,4,9]) 
print(resultat) 
