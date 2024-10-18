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
#-----------------------------------------------
side = []

for c in range(3):
    c = int(input(f"diga a medida do {c+1}º lado do triângulo: "))
    side.append(c)



if side[0] * side[1] * side[2] == side[0]**3:
    print("este triângulo é equilátero")
elif side[0] == side[1] or side[0] == side[2] or side[1] == side[2]:
    print("este triângulo é isóceles")
else:
    if side[0] > side[1] and side[0] > side[2]:
        if side[1] + side[2] > side[0]:
            print("este triângulo é escaleno")
        else:
            print("não da pra formar um triângulo com essas medidas")
    elif side[1] > side[0] and side[1] > side[2]:
        if side[0] + side[2] > side[1]:
            print("este triângulo é escaleno")
        else:
            print("não da pra formar um triângulo com essas medidas")
    else:
        if side[0] + side[1] > side[2]:
            print("este triângulo é escaleno")
        else:
            print("não da pra formar um triângulo com essas medidas")
#----------------------------------------------------------------------
day = int(input("diga um numero de 1 a 7: "))

match day:
    case 1:
        print("domingo")
    case 2:
        print("lunes")
    case 3:
        print("martes")
    case 4:
        print("miercoles")
    case 5:
        print("jueves")
    case 6:
        print("viernes")
    case 7:
        print("sabado")
    case _:
        print("esse dia ainda não existe")
