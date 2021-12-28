# %%
import math

sutun = 5
satir = 7
sevensegment = []
oneline = [" "]*sutun
# 2d boş liste oluşturrma
for i in range(satir):
    sevensegment.append(oneline.copy())


def printsevensegment():  # seçim sonrası kullanılacak print fonksiyonu
    for i in range(satir):
        for j in range(sutun):
            print(sevensegment[i][j], end=" ")
            if(j == sutun-1):
                print("\n")


def fillA():
    for i in range(satir):
        for j in range(sutun):
            sevensegment[i][j] = "*"
        break


def fillB():
    for i in range(math.ceil(satir/2)):
        for j in range(sutun):
            if j == sutun-1:
                sevensegment[i][j] = "*"


def fillC():
    for i in range(math.floor(satir/2), satir):
        for j in range(sutun):
            if j == sutun-1:
                sevensegment[i][j] = "*"


def fillD():
    for i in range(satir-1, satir):
        for j in range(sutun):
            sevensegment[i][j] = "*"


def fillE():
    for i in range(math.floor(satir/2), satir):
        for j in range(sutun):
            if j == 0:
                sevensegment[i][j] = "*"


def fillF():
    for i in range(math.ceil(satir/2)):
        for j in range(sutun):
            if j == 0:
                sevensegment[i][j] = "*"


def fillG():
    for i in range(math.floor(satir/2), math.floor(satir/2)+1):
        for j in range(sutun):
            sevensegment[i][j] = "*"


funcList = [fillA, fillB, fillC, fillD, fillE, fillF, fillG]

# Olusturulacak sayiyi dictionary bazli bulup cikti almamizi sagliyor
text = ""

inp = int(input("Sayi: "))


def getNum(inp):
    global text

    nums = {
        0: "1111110", 1: "0110000", 2: "1101101", 3: "1111001",
        4: "0110011", 5: "1011011", 6: "1011111", 7: "1110000",
        8: "1111111", 9: "1111011"}

    for i in nums:
        if inp == i:
            text = nums[inp]


getNum(inp)


for index, value in enumerate(text):
    if int(value):
        funcList[index]()


printsevensegment()


# %%
