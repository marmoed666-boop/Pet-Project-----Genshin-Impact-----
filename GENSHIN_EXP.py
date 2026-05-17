class character():
    def __init__(self, name, element, weapon_type):
        self.name = str(name)
        self.element = str(element)
        self.weapon_type = str(weapon_type)
    def battle(self):
        return f"{self.name} Attack with {self.element} {self.weapon_type}"
Kadzuha = character("Kadzuha", "Anemo", "light_sword")
Raiden = character("Raiden", "Electro", "Polearm")

print("<----Genshin Impact---->")
print(" <Enter Play to start game:> ")
start = input("")
while start == "Play":
    print("<----Choose character---->")
    print("Character gallery: \n"
          "Kadzuha " "Raiden")
    hero = str(input("Choose character: "))
    if hero == "Kadzuha":
        print("<Kadzuha selected>")
        a = input("write attack to battle: ")
        if a ==  "attack":
            print(Kadzuha.battle())
    elif hero == "Raiden":
        print("<Raiden selected>")
        a = input("write attack to battle: ")
        if a == "attack":
            print(Raiden.battle())
    else:
        break

