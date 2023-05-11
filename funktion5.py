#Skapa en funktion som heter CalculateTaxesOnSalary
# Skapa en funktion som heter CalculateTaxesOnSalary


# Den tar som inparameter ett tal (lönen). 
#  Om Månadslön >= 30000 tar man lön * 0,33

# om Månadslön < 15000 så lön * 0,12

# om Månadslön <30000 så lön * 0,28


# Returnera den beräknade skattesatsen.
def CalculateTaxesOnSalary(lön):
    if lön>=30000:
        skattesats=0.33
    elif lön<15000:
        skattesats=0.12
    else:
        skattesats=0.28
    return skattesats


lön1 = 28000
skattesats1 = CalculateTaxesOnSalary(lön1)
print(skattesats1) 
lön2 = 12000
skattesats2 = CalculateTaxesOnSalary(lön2)
print(skattesats2)
lön3 = 35000
skattesats3 = CalculateTaxesOnSalary(lön3)
print(skattesats3) 