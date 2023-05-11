# Skapa automatiska enhetstester för CanIBuyBeer
# - ta din egen eller
# ålder      18      20
# location Krogen Systemet
# promilleHalt < 1.0
def canIBuyBeer(age,location,promilleHalt):
    if promilleHalt > 1.0:
        return False
    if location == "S" and age < 19:
        return False
    if location == "K" and age < 18:
        return False
    return True