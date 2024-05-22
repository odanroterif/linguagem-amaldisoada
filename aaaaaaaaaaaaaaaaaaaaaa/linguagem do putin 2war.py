numbers = [22,44,-33,21,-12,11,23,37,-36,-46,45,-41]
positive = [] 
negative = []

for c in numbers:

    if(c < 0):
        negative.append(c)
    else:
        positive.append(c)


print("positivo vector: ",positive)
print("negativo vector: ",negative)
        