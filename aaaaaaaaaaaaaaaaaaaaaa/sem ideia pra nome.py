number = int(input("digite qualquer número não negativo: "))
#-------------------------------
while number < 1:

    number = int(input("digite qualquer número não negativo: "))

#-------------------------------
print("\n\n")
for c in range(1,number+1):

    print("o dobro de ",c," é ",c*2)