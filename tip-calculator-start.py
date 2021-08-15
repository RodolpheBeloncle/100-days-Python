print("Welcome to the tip Calculator")

bill = input("What was the total bill ?: ")

billStringToFloat = float(bill)

#--------------------------------

amountOfTips = input("What percentage of tips would you like to give ? 10 ,12 or 15 : ")

amountOfTipsStringToFloat = int(amountOfTips)

#--------------------------------

numberOfPeople = input("How Many People to split the bill ? : ")

numberOfPeopleStringToInt = int(numberOfPeople)

#--------------------------------

def splitBillWithTips(totalBill,tips,nbPeople):

peopleToSplit = totalBill / nbPeople

percentageTip = tips

totalToPay = round((peopleToSplit * (percentageTip/100)) + peopleToSplit,2)

print(F"Each Person should pay {totalToPay}")

#--------------------------------

splitBillWithTips(billStringToFloat,amountOfTipsStringToFloat,numberOfPeopleStringToInt)
