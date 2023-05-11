# a) Bankomaten
# Skapa en klass Bankomat. Den ska ha en dictionary med konton (kontonummer mappat till  saldo)

# Skriv med TDD tester för att
# ta ut pengar
# sätta in pengar
# osv osv

# Vilka fel kan uppstå?

# För varje test se till att Bankomaten fungerar enligt spec

# b) Bankomaten 2
# Account ska nu vara en egen klass. Med kontonummer, saldo, och Lista med Transactions-
# Dvs varje gång man gör nåt ska det skapas en Transaction
# (uttag/insättning, datum, belopp, nytt saldo)


      
import datetime

class Transaktion:
    def __init__(self, typ, datum, belopp, saldo):
        self.typ = typ
        self.datum = datum
        self.belopp = belopp
        self.saldo = saldo

class Account:
    def __init__(self, kontonummer, saldo):
        self.kontonummer = kontonummer
        self.saldo = saldo
        self.transaktioner = []

    def sätt_in(self, belopp):
        if belopp <= 0:
            raise ValueError("Beloppet måste vara positivt.")
        self.saldo += belopp
        self.transaktioner.append(Transaktion('insättning', datetime.datetime.now(), belopp, self.saldo))

    def ta_ut(self, belopp):
        if belopp <= 0:
            raise ValueError("Beloppet måste vara positivt.")
        if belopp > self.saldo:
            raise ValueError("Otillräckligt saldo.")
        self.saldo -= belopp
        self.transaktioner.append(Transaktion('uttag', datetime.datetime.now(), belopp, self.saldo))

class Bankomat:
    def __init__(self):
        self.konton = {}

    def skapa_konto(self, kontonummer, saldo):
        if kontonummer in self.konton:
            raise ValueError("Kontot finns redan.")
        self.konton[kontonummer] = Account(kontonummer, saldo)

    def ta_bort_konto(self, kontonummer):
        if kontonummer not in self.konton:
            raise ValueError("Kontot finns inte.")
        del self.konton[kontonummer]

    def saldo(self, kontonummer):
        if kontonummer not in self.konton:
            raise ValueError("Kontot finns inte.")
        return self.konton[kontonummer].saldo

    def sätt_in(self, kontonummer, belopp):
        if kontonummer not in self.konton:
            raise ValueError("Kontot finns inte.")
        self.konton[kontonummer].sätt_in(belopp)

    def ta_ut(self, kontonummer, belopp):
        if kontonummer not in self.konton:
            raise ValueError("Kontot finns inte.")
        self.konton[kontonummer].ta_ut(belopp)