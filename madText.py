madText1 = ["", "", "", "", ""]
madText2 = ["", "", "", "", ""]
madText3 = ["", "", "", "", ""]
madText4 = ["", "", "", "", ""]
madText5 = ["", "", "", "", ""]
print(type(madText4))


def pirmaisSpeletajs():
    madText1[0] = input("KĀDS?")
    madText5[1] = input("KAS?")
    madText4[2] = input("KUR?")
    madText3[3] = input("KO DARĪJA?")
    madText2[4] = input("KAS SANĀCA")


if __name__ == '__main__':
    print("Šī ir spēle madText")
    speletajs1 = input("Kā sauc pirmo spēlētāju?")
    print(speletajs1 + " Atbildi uz jautājumiem!")
    pirmaisSpeletajs()
    print(madText1)

