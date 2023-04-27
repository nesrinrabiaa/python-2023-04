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
# promilleHalt < 0.9
def canIBuyBear( age, Location,promilleHalt):
    result =True
    return result
while True:
    age=int(input ("Ange ålder:"))
    Location= input ("Ange var du är S/K")
    promilleHalt= float(input ("Ange din promille:"))
    ok= canIBuyBear(age, Location, promilleHalt)
    if ok==True:
        print("yes")
    else:
        print("no")


    