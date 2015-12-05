import random
import os
import sys

def getRandomNumber(original):
    random.seed()
    offset = original * 0.3
    rightOriginal = original

    tempRandom = random.random()
    isPic = tempRandom >= 0.3 and tempRandom <= 0.5
    if isPic:
        offset *= 4
        rightOriginal = original + offset

    return random.uniform(rightOriginal - offset, rightOriginal + offset), isPic

def createMagicData(original, categoryName):
    magicData = []
    positiveData = []

    for item in original:
        magicItem, isPic = getRandomNumber(item)
        magicData.append(magicItem)
        isPositive = magicItem > (item * 1.2)
        positiveData.append(isPositive)
        if isPic:
            rightImageFileName = getImageFileName(categoryName)

    i = 0;
    for item in original:
        magicItem = magicData[i]
        isPositive = positiveData[i]
        print "original = " + str(item) + " magic = " + str(magicItem) + " isPositive = " + str(isPositive)
        i += 1

    print "original = " + str(len(original)) + " magic = " + str(len(magicData)) + " positive = " + str(len(positiveData))
    print "categoryName = " + str(categoryName) + " imageFileName = " + str(rightImageFileName)

    return magicData, rightImageFileName

def getImageFileName(categoryName):
    if categoryName == 'Household appliance stores':
        return "5.png"
    elif categoryName == 'Airlines, Air Carriers':
        return "13.png"
    elif categoryName == 'Electronic Sales':
        return "12.png"
    elif categoryName == "Men's and ladies's clothing":
        return "4.png"
    elif categoryName == 'Eating places,Restaurants':
        return "7.png"
    elif categoryName == 'Medical services':
        return "9.png"
    elif categoryName == 'Furniture,home furnishings':
        return "10.png"
    elif categoryName == 'Cosmetic stores':
        return "16.png"

def test():
    random.seed()

    originalList = []
    i = 0
    while i < 15:
        item = random.randint(0, 1000)
        originalList.append(item)
        i += 1

    createMagicData(originalList, "11")
