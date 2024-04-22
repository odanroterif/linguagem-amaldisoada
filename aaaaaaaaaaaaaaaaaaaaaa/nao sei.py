price_unit = float(input("Preço do produto: "))
number = float(input("\nquantidade levada: "))
code_piece = input("\ncodigo da peça comprada: ")
idtrader = input("\nID do vendedor: ")

bonus = (price_unit*number)*0.05

print("\n\nComissão: ",bonus)