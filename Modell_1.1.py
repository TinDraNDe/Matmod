# MODELL 1.1: Lägg till begränsad produktionsförmåga

import itertools        #för lite kombinatorik 

#Exempelavstånd: 

avstånd = [[1, 1, 1],       # Grossist 0 till Fabrik 1, 2, 3
           [1, 3, 2],       # Grossist 1 till Fabrik 1, 2, 3
           [1, 2, 2], 
           [2, 4, 5],       # ... 
           [4, 9, 1], 
           [2, 3, 5], 
           [4, 4, 1], 
           [3, 1, 3]]       # Grossist 7 till Fabrik 1, 2, 3


efterfrågan = [1, 2, 4, 5, 6, 1, 2, 5]  # Antal containrar varje grossist efterfrågar / tidsenhet
produktionsförmåga = [20, 150, 20]          # Antal containrar varje fabrik producerar / tidsenhet 

alla_miljöfaktorer = [] 
for grossist in range(8):
    row = []
    for f in avstånd[grossist]:
        row.append(f * efterfrågan[grossist])       # Produkten av efterfrågan och körsträcka för varje fabrik/grossist läggs till i en lista
    alla_miljöfaktorer.append(sorted(row))
    

indexes = [0, 1, 2] #Fabrik 0, 1, 2
matchningar = list(itertools.product(indexes, indexes, indexes, indexes, indexes, indexes, indexes, indexes)) # skapar en lååång lista av tupler (3^8 lång)

möjliga_summor = []

for combos in matchningar:
    colsum = 0                              #Summa av kolumnen av kombinationer av miljöfaktorer
    f_sum = [0, 0, 0]                       #Summa efterfrågan för varje fabrik
    for index in range(8):
        colsum += alla_miljöfaktorer[index][combos[index]]
        f_sum[combos[index]] += efterfrågan[index]
    if f_sum[0] <= produktionsförmåga[0] and f_sum[1] <= produktionsförmåga[1] and f_sum[2] <= produktionsförmåga[2]: #Kolla så efterfrågan inte är för hög
        möjliga_summor.append(colsum)
    else:
        möjliga_summor.append(10000000000) #Läggs till om ej OK. Behåller index för värdet. 
        
minsta = min(möjliga_summor)                #Minsta hittade värdet

alla_minsta = []

for i in range(len(möjliga_summor)):        #Hittar alla matchningar med minsta värdet 
    if möjliga_summor[i] == minsta:
        alla_minsta.append(i)

motsvarande_fabriker = []                   #Beskriver  vilka val som görs för att få det minsta värdet 

for x in alla_minsta: 
    motsvarande_fabriker.append(matchningar[x])         

#print(möjliga)             #LÅÅÅNG lista av alla möjliga sammanlagda körsträckor                 
#print(minsta)
#print(alla_minsta)
print(motsvarande_fabriker) #Bästa valen!





