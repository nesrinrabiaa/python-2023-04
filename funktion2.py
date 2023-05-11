# . MOMS


# # # Skapa en metod som räknar ut hur mycket momsen blir på en viss summa.
# #  Summan skall vara en inparameter av typen int.
# # Metoden skall returnera momsvärdet
def calculateVat(amount):
    moms=0.15
    vat_amount= amount*moms
    return vat_amount
amount=2000
vat_amount= calculateVat(amount)
print(f"Moms värdet för {amount} kronaor är{vat_amount} kronor.")



