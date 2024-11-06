# 1.  pole s pěti stringovými hodnotami
pole = ["1", "2", "3", "4", "5"]
print("Základní pole:", pole)

# 2. Přidání vítru pomocí appendu
pole.append("vítr")
print("Po přidání 'vítr':", pole)

# 3. Odstranění druhého prvku pomocí remove
pole.remove("2")
print("Po odstranění druhého prvku:", pole)

# 4. Změna páté hodnoty na slunce
pole[4] = "slunce"
print("Po změně 5. hodnoty na 'slunce':", pole)

# 5. Přidání dvou stringových hodnot pomocí extend
pole.extend(["hvězda", "měsíc"])
print("Po přidání dvou hodnot:", pole)