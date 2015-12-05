import random
import os
import sys

def getRandomNumber(original):
    print original
    random.seed()
    print original * 0.1
    offset = round(original * 0.1)
    print offset
    rightOriginal = original

    tempRandom = random.random()
    isPic = tempRandom >= 0.3 and tempRandom <= 0.5
    if isPic:
        offset *= 4
        rightOriginal = original + offset

    return random.uniform(rightOriginal - offset, rightOriginal + offset)

def createMagicData(original, categoryName):
    magicData = []
    positiveData = []

    for item in original:
        magicItem = getRandomNumber(item)
        magicData.append(magicItem)
        isPositive = magicItem > (item * 1.2)
        positiveData.append(isPositive)

    i = 0;
    for item in original:
        magicItem = magicData[i]
        isPositive = positiveData[i]
        print "original = " + str(item) + " magic = " + str(magicItem) + " isPositive = " + str(isPositive)
        i += 1

    rightImageFileName = getImageFileName(categoryName)

    print "original = " + str(len(original)) + " magic = " + str(len(magicData)) + " positive = " + str(len(positiveData))
    print "categoryName = " + str(categoryName) + " imageFileName = " + str(rightImageFileName)

    return magicData

def getImageFileName(categoryName):
    if categoryName == '1':
        return "1.png"
    elif categoryName == '2':
        return "2.png"
    elif categoryName == '3':
        return "3.png"
    elif categoryName == '4':
        return "4.png"
    elif categoryName == '5':
        return "5.png"
    elif categoryName == '6':
        return "6.png"
    elif categoryName == '7':
        return "7.png"
    elif categoryName == '8':
        return "8.png"

def test():
    random.seed()

    originalList = []
    i = 0
    while i < 15:
        item = random.randint(0, 1000)
        originalList.append(item)
        i += 1

    createMagicData(originalList, "11")
