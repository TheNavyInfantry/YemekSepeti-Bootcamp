import string
# %%

# Q1
userInp = input("Type: ")


def getLength(inp):
    print(len(str(inp)))


getLength(userInp)
# %%

# Q2
userInp = input("Type: ")


def firstLast(inp):
    print(f"{inp[0]} {inp[-1]}")


firstLast(userInp)
# %%

# Q3
textInp = input("Text: ")
old, new = input("Old and New").split(" ")


def change(text, old, new):
    print(text.replace(old, new))  # string.replace(oldvalue, newvalue, count)


change(textInp, old, new)

# %%

# Q4
userInp = str(input("Type: "))


def isPalindrome(inp):
    if inp == inp[::-1]:
        return True
    else:
        return False


print(isPalindrome(userInp))
# %%

# Q5

userInp = input("Type: ")


def lastTwo(inp):
    splitLast = inp[:(len(inp)-2)]  # uzunlugun 2 eksigini index den aldik
    getLast1 = inp[len(inp)-1] * 4
    getLast2 = inp[len(inp)-2] * 4

    print("".join([splitLast, getLast1, getLast2]))


lastTwo(userInp)


# %%

# Q6

listFive = [1, "a", 3, "b", 5]


def changeTwo(liste):
    liste[1] = 100
    print(liste)


changeTwo(listFive)

# %%

# Q7

liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

liste3_1 = liste1.copy()

liste1.append(liste2)
print(liste1)

liste3_1.extend(liste2)
print(liste3_1)

liste3_1 + liste2
print(liste3_1)


# %%

# Q8

listThree = ["a", 2, "b"]


def insertFirst(liste):
    liste.insert(0, "elma")
    print(liste)


insertFirst(listThree)
# %%

# Q9

liste = [1, 2, 3, 4, 5, 6, 7, 1, 3, 3, 3, 2, 2, 1, 23]


def justThree(liste):

    check = True  # listedeki ilk gelen 3 rakami icin kontrol anahtari

    for i in liste:
        if check:
            if i == 3:
                check = False
                liste.remove(3)

    print(liste)


justThree(liste)
# %%

# Q10

liste1 = ["1", 1, 2, "3"]


def listCopy(list):
    liste2Copy = liste1.copy()
    liste2Copy.insert(len(liste2Copy), 250)

    print(f"{liste1}\n{liste2Copy}")


listCopy(liste1)
# %%

# Q11

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

# merged = dict1 | dict2 | dict3 # Python 3.9.0+ Only
merged = {**dict1, **dict2, **dict3}
print(merged)


# %%

# Q12

sozluk = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

removeItem = sozluk.popitem()

print(removeItem)
# %%

# Q13

dict1 = {1: 10, 2: 20}
dict1[3] = 30

print(dict1)

# %%

# Q14
liste = [1, 2, 3, 4, 5]

dictA = {}
dictB = {}

for key in liste:
    dictA[key] = 0

print(dictA)

for key in dictA:
    dictB[key] = (key*10)

print(dictB)
# %%

# Q15

sozluk = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

sozluk.setdefault(6, 60)

print(sozluk)
# %%

# Q16

"""
Diger dosyada bulunuyor.
"""
# %%

# Q17

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

sortedNum = {i: sorted(num[i]) for i in num.keys()}  # dict comprehension

print(sortedNum)

# %%

# Q18
sozluk = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}

keyList = [newVal.replace(" ", "") for newVal in sozluk.keys()]

print(dict(zip(keyList, list(sozluk.values()))))


# %%

# Q19

liste1 = [1, 2, 3]
liste2 = [4, 5, 6, 7, 8]

liste3 = []

liste3.extend(liste1)
liste3.extend(liste2)

print(liste3)
# %%

# Q20

liste = [1, 2, 3, 4, 5, 6]
del liste[0]
print(liste)


# %%

# Q21

liste = ["elma", "armut", "çilek"]
liste.append(3)
print(liste)

# %%

# Q22


def getThreeMax(list):
    list.sort(reverse=True)  # Descending yapiyor
    return list[:3]


print(getThreeMax([1, 3, 10, 1, 9, 5, 7, 1, 11, 2]))


# %%

# Q23


userInp = input("Type: ")


def upperLower(text):

    upper = []
    lower = []

    for i in text:
        if i in string.ascii_lowercase:
            lower.append(i)
        elif i in string.ascii_uppercase:
            upper.append(i)

    print(f"Upper: {upper}\nLower: {lower}")


upperLower(userInp)
# %%

# Q24
key = True

inpList = []

# Usera 10 tane input girmesini istiyoruz
# sonra da tek cift kontrolune yolluyoruz
while key:
    userInp = int(input("Type: "))

    inpList.append(userInp)

    if len(inpList) == 10:
        key = False


def oddOrEven(list):

    print("Odd: ", [x for x in list if x % 2 != 0],
          "Even: ", [x for x in list if x % 2 == 0])


oddOrEven(inpList)
