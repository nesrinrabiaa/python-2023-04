
# 3. LOOP #3


# Skapa ett program där användaren


# Får mata in två tal.
# Skriv sedan till skärmen summan av de två talen.
# Skriv sedan en fråga- Vill du fortsätta(J/N)?.
# Svarar användaren J återupprepas punkt a-c
# Svarar användaren N avbryts programmet
import random
while True:
    talet=random.randint(1,6)
    print(f"talet blev {talet }")
    while True:
        svar=input("Vill du kasta en gång till J/N?")

        if svar =="N":
            break
        if svar=="J":
            break
        print ("Ogiltig input")