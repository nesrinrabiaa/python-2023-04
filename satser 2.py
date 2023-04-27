# 2. IF #2

# Be användaren att mata in hur många paket mjölk som finns kvar. Är det mindre än

# 10 skriv- Beställ 30 paket. Är det mellan 10 och 20 skriv- Beställ 20 paket. Annars

# skriv-Du behöver inte beställa någon mjölk.
paket = inte (input("mata in hur många paket mjölk som finns kvar"))
if paket < 10 :
    print("Beställ 30 paket")
elif paket > 10-20:
 print("Beställ 20 paket")
else:
print("Du behöver inte beställa någon mjölk")  
