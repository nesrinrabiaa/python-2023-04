# 1. IF

# Be användaren att mata in ett tal.

# Kontrollera om talet är större än 10. Meddela

# användaren om talet är större än 10- Talet är större än 10. Om det är mindre än 10

# meddela användaren

# – Talet är mindre än 10
tal = float(input("Vänligen ange ett tal:"))
if tal>10:
    print("Talet är större än 10.")
elif tal<10:
    print ("Talet är mindre än 10.")
else:
    print ("Talet är 10.")    
    