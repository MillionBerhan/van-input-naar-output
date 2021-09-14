print("Welkom bij Pizzeria Berhano!")
print("Wat mag het worden?")
small = 1
Medium = 2
Large = 3
size = int(input("press 1 for small, 2 for medium and 3 for large"))
any = int(input("Hoeveel pizza's wilt u?"))
if any <= 5 and size == 1:
    print("u heeft",any,"pizza small besteld, dat wordt dan",3.99 * any)

if any <= 5 and size == 2:
    print("u heeft",any,"pizza medium besteld, dat wordt dan",4.99 * any)

if any <= 5 and size == 3:
    print("u heeft",any,"pizza large besteld, dat wordt dan",5.99 * any)

if any > 5 or size > 3:
    print(" Dat nummer/grootte herkennen wij niet") 
print ("Bedankt voor de bestelling namens Milliono Berhano, wensen wij u een fijne dag toe!")
print ("Heeft u nog vragen neem dan gerust contact op met ons op!")
print ("Contact&Service:")
print ("Klantenservice:085-7078975")
print ("Mail:PizzeriaBerhano71@yahoo.com")
print ("Adres:Mollenburgseweg 82")
print ("4205NB Gorinchem")
print ("Postbus 859")
print ("4200 AW Gorinchem")
print ("De beste pizza's vind je bij Pizzeria Berhano!")