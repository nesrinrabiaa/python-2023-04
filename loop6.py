# 6. LOOP #7 (Överkurs)


# Rolling the dice


# Kasta två tärningar” och visa resultatet enligt skärmdump ända tills man INTE svarar ”y” eller ”yes” på frågan om igen
import random
while True:
    roll1= random.randint(1,6)
    roll2=random.randint(1,6)
    print("Reslutat:",roll1,roll2)
    
    svar =input("om svar J/N :")
    if svar ("J/N"):
     print(f"Reslutat:" ,{roll1,roll2})
     

