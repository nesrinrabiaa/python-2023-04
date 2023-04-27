# 1. LIST #1


# Skapa ett program där användaren får upp fyra frågor om att mata in ett tal. Spara

# alla talen i en lista. Loopa igenom lista och ta fram det tal som är störst. Skriv

# tillbaka resultatet på skärmen för användaren
numbers=[]

for i in range(4):
    number=float(input("Mata in ett tal:"))
    numbers.append(numbers)
    max_number=max(numbers)
    print("Det störta talet är ",max_number)
