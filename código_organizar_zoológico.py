girafas = int(input("Quantas girafas você tem no zoológico? "))
elefantes = int(input("Quantos elefantes você tem no zoológico? "))
macacos = int(input("Quantos macacos você tem no zoológico? "))
zebras = int(input("Quantas zebras você tem no zoológico? "))
cobras = int(input("Quantas cobras você tem no zoológico? "))
print("Quantidade de animais no zoológico:")
if girafas == 0:
    print("Não tem girafas.")
else:
    print(f"Girafas: {girafas}")
if elefantes == 0:
    print("Não tem elefantes.")
else:
    print(f"Elefantes: {elefantes}")
if macacos == 0:
    print("Não tem macacos.")
else:
    print(f"Macacos: {macacos}")
if zebras == 0:
    print("Não tem zebras.")
else:
    print(f"Zebras: {zebras}")
if cobras == 0:
    print("Não tem cobras.")
else:
    print(f"Cobras: {cobras}")
###total_animais = girafas + elefantes + macacos + zebras + cobras
###print(f"\nTotal de animais no zoológico: {total_animais}")