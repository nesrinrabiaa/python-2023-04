from dataclasses import dataclass

@dataclass
class Course:
    Name: str
    Price: float
    Type: str
    Calories:int

lunchMeny = []

while True:
    # print("1. Lista meny")
    # print("2. Ändra mat")
    # print("3. Lägg till mat")
    # print("4. Exit")
    a = input("Action:")
    # if a == "4":
    #     break
    if  a == "1":
        print("*** DAGENS LUNCH ***")
    for course in lunchMeny:
        print(f"{course.Name}   {course.Price}  {course.Type} {course.Calories}")

    # if a == "2":
    #     print("*** ÄNDRA MATRÄTT ***")
    #     x = 0
    #     for course in lunchMeny:
    #         print(f"{x + 1}:{course.Name}   {course.Price}  {course.Type} {course.Calories}")
    #     x = int(input("Vilken vill du ändra?")) -1           
    #     print(f"{lunchMeny[x].Name}   {lunchMeny[x].Price}  {lunchMeny[x].Type} {lunchMeny[x].Calories}")        
    #     lunchMeny[x].Name = input("Name:")
    #     lunchMeny[x].Price = int(input("Price:"))
    #     lunchMeny[x].Cat = input("Cat:")
    #     lunchMeny[x].Calories = int(input("Calories:"))

    # if a == "3":
    #     print("*** NY MATRÄTT ***")
    #     name = input("Name:")
    #     price = int(input("Price:"))
    #     cat = input("Cat:")
    #     calories = int(input("Calories:"))
    #     course1 = Course(name,price,cat,calories)
    #     lunchMeny.append(course1)