# 2. LOOP #2

# Skapa ett program där användaren får mata in två tal. Låt sedan programmet
 #skrivt ut alla

# tal som finns mellan dessa två tal på skärmen. Lös detta med en for-loop. 
# Lös den igen med en While-loop.
start=int(input("Mata in det första talet:"))
sluta=int(input("Mata in det andra talet:"))
for i in range (start,sluta +1):
    print(i)
    # Lös den igen med en While-loop.
start=int(input("Mata in det första talet:"))
sluta=int(input("Mata in det andra talet:"))
i=start
while i<=sluta:
    print(i)
    i=i+1
    