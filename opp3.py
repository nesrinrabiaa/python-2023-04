# Övning 3

# Skapa en klass ChristmasPresent. Den ska ha Name och ett Price 
 #(vad den kostar)
class ChristmasPresent:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Person:
    def __init__(self, name):
        self.name = name
        self.presents = []
        
    def add_present(self, present):
        self.presents.append(present)
        
    def total_present_cost(self):
        return sum(present.price for present in self.presents)


# Skapa en klass Person. Den ska ha Name och en lista med julklappar.
# Gör också så att det går att lägga till julklappar, 
#och räkna fram totalen (vad alla personens julklappar kostar)
person1 = Person("Nesrin")
present1 = ChristmasPresent("cup", 150)
present2 = ChristmasPresent("Kläder", 500)
person1.add_present(present1)
person1.add_present(present2)

person2 = Person("Osama")
present3 = ChristmasPresent("Leksak", 200)
person2.add_present(present3)

person3 = Person("Marieh")
present4 = ChristmasPresent("Smycken", 1000)
present5 = ChristmasPresent("Choklad", 50)
person3.add_present(present4)
person3.add_present(present5)


# Skapa nu tre personer. Skapa några julklappar för varje person
# och skriv en loop som går igenom alla personer,
for person in [person1, person2, person3]:
    print(f"{person.name} har fått julklappar som totalt kostar {person.total_present_cost()} kr.")

# skriver ut dess namn och vad dess julklappar kostar. 


