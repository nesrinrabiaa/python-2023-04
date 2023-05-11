# om man handlat för  minst 1000 kr får man 100kr i rabatt
# om man är medlem i kundklubb får man 2% rabatt
# om man handlat för minst 5000 kr man 1% rabatt på priset över 5000
# vi ska skriva en calculateDiscountedPrice(totalPrice) som implementerar dessa regler
# om vi inte är medlem och betal 200 kr->200
def calculateDiscountedPrice(totalPrice, isMember):
    rabatt = 0
    if totalPrice >= 5000:
        rabatt = rabatt + (totalPrice * 0.01)
    if isMember:
        rabatt = rabatt + (totalPrice * 0.02)
    if totalPrice > 1000:
        rabatt = rabatt + 1000
    return totalPrice - rabatt
# while True:
#     price=float(input("price"))
#     if input("medlen 1/N")=="J":
#         isMember=True
#         newprice=
#         price(f"Nytt price:(newprice)")