# MODELL 1.0: Bara hitta närmsta fabrik och multiplicera med efterfrågan 

#Exempelavstånd: 

avstånd = [[2, 3, 5],       # Grossist 0 till Fabrik 1, 2, 3
           [1, 3, 2],       # Grossist 1 till Fabrik 1, 2, 3
           [1, 2, 2], 
           [2, 4, 5],       # ... 
           [4, 9, 10], 
           [2, 3, 5], 
           [4, 4, 1], 
           [3, 1, 3]]       # Grossist 7 till Fabrik 1, 2, 3


efterfrågan = [1, 2, 4, 5, 6, 1, 2, 5]  # Antal containrar varje grossist efterfrågar / vecka (?) 
produktionsförmåga = [100, 150, 20]          # Antal containrar varje fabrik producerar / vecka 

def avstånd_närmsta(grossist):
    return min(avstånd[grossist]) 

def total_körsträcka(grossist): 
    return avstånd_närmsta(grossist) * efterfrågan[grossist]

def lista_körsträckor():
    körsträckor = [] 
    for g in range(8):
        körsträckor.append(total_körsträcka(g))
    return körsträckor

print(lista_körsträckor())