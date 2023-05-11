# Övning 2
# Skapa en klass, Person. Vi ska hålla reda på personens
# Födelsedatum
# Namn
# GatuAdress
# PostNummer
# Postort
# Överkurs: Skapa en constructor! En person har alltid ett födelsedatum eller hur!
# Allt det andra behöver den inte ha...kan sättas senare "i livet"

# Gör properties - get?? Vilka funktioner:
# Namnge
# BytAdress
# Skapar du upp två personer. Du och en kompis. Sätt addresser för er två. Skriv kod så att den ena flyttar in hos den andra!

  
def __init__(self, födelsedatum,namn,GatuAdress,postNummer,Postort):
        self.födelsedatum = födelsedatum
        self._namn = None
        self._adress = None
        self._GatuAdress=GatuAdress
        self._postNummer=postNummer
        self._postort=Postort
class Person:
    def __init__(self, birthdate, name=None):
        self.birthdate = birthdate
        self.name = name
        self.address = None
        self.postal_code = None
        self.city = None
        
    def __str__(self):
        return f"{self.name} ({self.birthdate}), {self.address}, {self.postal_code} {self.city}"

    def rename(self, new_name):
        self.name = new_name
    
    def change_address(self, new_address, new_postal_code, new_city):
        self.address = new_address
        self.postal_code = new_postal_code
        self.city = new_city
# För att skapa två personer och sätta adresser för dem kan 
# vi göra så här:
person1 = Person("1988-01-01", "Nesrin")
person1.change_address("Storgatan 1", "12345", "Tranås")

person2 = Person("1995-07-15", "Osama")
person2.change_address("Ågatan 2", "54321", "Sommen")
# För att flytta in person2 hos person1 kan vi använda change_address-metoden 
# för person2:
person2.change_address(person1.address, person1.postal_code,
person1.city)
print(person1)
print(person2)

