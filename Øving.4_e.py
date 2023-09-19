# Skriv en funksjon som tar inn ei liste med tall. For hvert tall i lista unntatt det siste skal
# funksjonen regne ut differansen mellom neste tall i lista og dette tallet. Differansene skal
# legges inn i ei ny liste 

def calculate_differences(lst):
    differences = []
    for i in range(len(lst) - 1):
        diff = lst[i + 1] - lst[i]
        differences.append(diff)
    return differences


