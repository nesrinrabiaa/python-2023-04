# Skapa en metod som du döper till HittaLangstaOrdet. 
# Metoden skall ta som inparameter en array med strängar.
# Metoden skall loopa igenom arrayen och returnera det längsta ordet.
def HittaLangstaOrdet(arr):
    langste_ord= ""
    for ord in arr:
        if len(ord)>len (langste_ord):
            langste_ord = ord
    return langste_ord

ord_arr=[ "Osama","Mohammad","Nesrin"]
langste_ord = HittaLangstaOrdet(ord_arr)
print(langste_ord)

