# 3. LOOP #3


# Skapa ett program där användaren


# Får mata in två tal.
# Skriv sedan till skärmen summan av de två talen.
# Skriv sedan en fråga- Vill du fortsätta(J/N)?.
# Svarar användaren J återupprepas punkt a-c
# Svarar användaren N avbryts programmet

while True:
    n1= float(input ("Ange det första talet :"))
    n2= float(input ("Ange det andra talet :"))
    summa=n1+n2
    print ("summan av de två talen är:",summa)
    fortsätt= input("Vill du forsätt (J/N)?")
    if fortsätt.upper( )!="J":
        break
    print ("sluta")