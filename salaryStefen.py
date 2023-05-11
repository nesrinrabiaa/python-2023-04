# a)  med TDD utvecklar du  calculateSalary(...)
# Denna funktion tar den anställdes ålder, namn,
 #timlön och antal timmar som den jobbat
# Regler för att räkna lön
# - lönen blir antal timmar *  timlönen
# - om man är mellan 25 och 45 år får man 5% bonus
# - om man är över 45 får man 6% bonus
# -om man heter Stefan får man 220 kr bonus

# Se till att enhetstester är så täckande som möjligt
#  name :str
#  age:int =0
#  hourly_wage:float
#  hours_worked:float
# class Emplyoo:



def calculateSalary(name, age, hourlyWage, hoursWorked):
    baseSalary = hourlyWage * hoursWorked
    bonus = 0
    if age >= 25 and age <= 45:
        bonus = baseSalary * 0.05
    elif age > 45:
        bonus = baseSalary * 0.06
    if name == 'Stefan':
        bonus += 220
    return baseSalary + bonus

    



