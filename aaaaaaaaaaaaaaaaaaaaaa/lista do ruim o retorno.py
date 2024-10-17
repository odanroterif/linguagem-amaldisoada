number = int(input("diga um numero: "))

if number % 2 == 0:
    print("par")
else:
    print("impar")
#------------------------------------
number = int(input("diga um numero: "))
number_two =  int(input("diga outro numero: "))

if number > number_two:
    print(number,"é maior que",number_two)
elif number_two > number:
    print(number_two, "é maior que",number)
else:
    print("os 2 são iguais")
#-------------------------------------
notes = []


for c in range(2):
    c = float(input("digite a nota: "))
    notes.append(c)





if (notes[0]*notes[1])/2 >=6:
    print("\n\n\naprovado")
    
elif ((notes[0]*notes[1])/2 < 6) and ((notes[0]*notes[1])/2 >= 5.5):
    
    print("\n\n\nrecuperação")
    
else:
    
    print("\n\n\nreprovado")
  #-----------------------------------------------
  age = int(input("diga sua idade: "))


if age < 18:
    print("\n\n\nmenor de idade")

elif (age >= 18) and (age < 60):

    print("\n\n\nadulto")

else:

    print("\n\n\nidoso")
  #----------------------------------------
  notes = []

for c in range(2):
    c = float(input("digite a nota: "))
    notes.append(c)

if (notes[0] * notes[1]) / 2 >= 7:
    print("\n\n\naprovado")

elif (notes[0] * notes[1]) / 2 <= 4:

    print("\n\n\nreprovado")

else:

    print("\n\n\nrecuperação")
