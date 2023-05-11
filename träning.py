# namn =input("my name är ")
# age = input("my age is ")
# print (namn + age )
# # lista=[5, 10, 15, 20, 25]
# namn=" Nesrin "
# namn= namn+"Hollwe"+" "+"heter jag "
# antal= len (namn)
# print(antal)
# print(namn)

# namn=input("Vad heter du?")
# frist=namn[0]
# print(f"vad heter du?")
# namn = input ("vad heter du?")
# antal= len(namn)
# counta=0
# for a in range(0,antal):
#   if namn[a]=="a":
#     counta=counta+1
#     print(f"Du har(counta)a:n")
   
# Minabarn=["osama","mayeh","mira"]
# for barn in Minabarn:
#     Minabarn.append ("barn")
#     print (barn)
#     break
# ålder       18         20
# Location Krogen  Systym
# # promilleHalt < 0.9
# def canIBuyBear( age, Location,promilleHalt):
#     result =True
#     return result
# while True:
#     age=int(input ("Ange ålder:"))
#     Location= input ("Ange var du är S/K")
#     promilleHalt= float(input ("Ange din promille:"))
#     ok= canIBuyBear(age, Location, promilleHalt)
#     if ok==True:
#         print("yes")
#     else:
#         print("no")


# def max_num(num1,num2,num3):
#     if num1>=num2 and num1>=mun3:
#      return num1
#     elif num2>=num1 and num2>=num3 :
#      return num2
#     else:
#        return num3
# print(max_num( 7,9,5))
# print (max(200,150,50))
# def macth_string (str1,str2):
#     if str1!=str2:
#         print("the string do macth")
#     else:
#         print("the sting not macth")    
# macth_string("mohammad","osama")       
# num1= float(input(" Pleas inter the first number:") )
# operator= input("Pleas enter the operator:")
# num2= float(input("Plesa inter the scound number:"))
# if operator== "+":
#     print(num1+num2)
# elif operator=="-":
#     print(num1-num2)
# elif operator=="*" :
#     print(num1*num2)
# elif operator=="/":
#     print(num1/num2)
# else:
#     print("pleas try agien")
# convert_month= {
#     "0": "janunary",
#     "feb":"febraury",
# }
# print(convert_month["0"])
# print (convert_month["feb"])
# i=1
# while i<=10:
      
#       if i == 5:
#           i+=1  
#           break

#       print(i)
    
# print("the loop has ended")  
# for letter in "codezilla":
#     print(letter)


# for loop in "mohammad":
#     print(loop)
# string=["mohammad","nesrin"]    
# # for buddy in buddies:
# #     print (buddy)
# for index in range (len(string)):
#   print((index))
# for x in range(5,30):
#     print(x)
# buddies=["mohammad","nesrin"]
# for buddy in buddies:
#   if buddy =="ahamad":
#     print (buddy," is the winner")
#     break
#   else:
# #     print(buddy,"is not winner")
# numbers=[4,4,6,8,9,8,9,3,2,2,5,5]
# unique_list=[]
# for number in numbers:
#   if number not in unique_list:
#          unique_list.append(number)
#          print(dir(unique_list))

# name="nniittrdd"
# unique_set=set(name)
# print(unique_set)
# unique_lst=list(unique_set)
# unique_lst.reverse()
# print(unique_lst)
# x=["w","b","r"]
# g=["1","3"]
# y=x+g
# print(y)
# def power(base_num,pow_num):
#     result=1
#     for index in range (pow_num):
#         result=result*base_num
#     return result
# print(power(3,4))
# no_list=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]
# # print(no_list[1][2])
# for row in no_list:
# #     print(row)
#   for colum in row:
#        print(colum*colum)
# try:
#    value=int(input("Enter a number"))
#    print(value)
# import pytest
# class person:
#     Name: str
#     streetAdrssress:str=""
#     postaIcode:int= 0
#     City:str=""
#     Age:int=0
#     def SetAge(self,newAge):
#         if newAge>=0 and newAge<=140:
#             self.Age=newAge
#     def MoveTo(self,gatuAdr,postal,city):
#         self.streetAdrssress= gatuAdr
#         self.City=city
#         self.postaIcode=postal

# p = person("Nesrin")
# p.MoveTo
# p.streetAdrssress="testgata123"
# p.City="Teststad"
# # print(f"{p.Name}")
# from dataclasses import dataclass
# @dataclass
# class Course:
#     Name:str
#     Price:float
#     type:str
#     Calories:int
# LunchMuny=[]
# Course1= Course("Pannka",100,"vegtarisk",30)
# Course2=Course("korv",110,"kött",100)
# Course3=Course("Morotssupa",90,"vegtarisk",50)
# LunchMuny.append(Course1)
# LunchMuny.append(Course2)
# LunchMuny.append(Course3)
# print("Dags Lunch")

# for course in LunchMuny:
#     print(f"{course.Name} {course.Price}{course.Calories}")
# import unittest

# def calculateSalary(age, name, hourly_wage, hours_worked):
#     base_salary = hourly_wage * hours_worked
#     bonus = 0
    
#     if 25 <= age < 45:
#         bonus = base_salary * 0.05
#     elif age >= 45:
#         bonus = base_salary * 0.06
        
#     if name == "Stefan":
#         bonus += 220
        
#     return base_salary + bonus

# class TestCalculateSalary(unittest.TestCase):
    
#  def test_base_salary(self):
#         # Testar att baslönen räknas ut korrekt.
#         result = calculateSalary(30, "Nesrin", 100, 8)
#         self.assertEqual(result, 800)
    
# def test_young_bonus(self):
#         # Testar att en ung anställd får rätt bonus.
#         result = calculateSalary(30, "Osama", 100, 8)
#         self.assertEqual(result, 840)
    
# def test_old_bonus(self):
#         # Testar att en äldre anställd får rätt bonus.
#         result = calculateSalary(50, "Jad", 100, 8)
#         self.assertEqual(result, 848)
        
# def test_stefan_bonus(self):
#         # Testar att en anställd med namnet Stefan får rätt bonus.
#         result = calculateSalary(30, "Stefan", 100, 8)
#         self.assertEqual(result, 1020)
     
# if __name__ == '__main__':
# #     unittest.main()
# assert 5*3==15 ," should be 15"
# def test_Case_one():
#     assert 5*10==50 ,"should be 50"
# def test_Case_tow():
#     assert 4*6==24 ,"should be 24"
# if __name__=="_main_":
#     test_Case_one()
#     test_Case_tow()
import unittest
# print("All tests passed")
class MyTestCase (unittest.TestCase):
    def test_one(self):
        self.assertTrue(100>98,"should be Ture")
    def test_tow(self):
        self.assertEqual(40+60,100, "should be 100")
    def test_three_(self):
        self.assertFalse(100>200,"should be 100")
if __name__=="__main__":
    unittest.main()