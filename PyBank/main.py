import os
import csv

file = os.path.join("..", "..", "PyBank", "Resources", "budget_data.csv")


with open(file, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    totalMonths = 0 
    netTotal = 0
    totalDates = []
    previousMonthAmount = 0
    netAmountChange = 0
    netAmountChangeL = []
    netAmountAverage = 0
    currentMonth = []
    greatestincInProfits = ["", 0]
    greatestdecInProfits = ["", 9999999999]
    total_list = []

    for row in csvreader:

        total_list.append(int(row[1]))  

        totalDates.append(row[0])

        netTotal = netTotal + int(row[1])

        netAmountChange = int(row[1]) - previousMonthAmount

        previousMonthAmount = int(row[1])

        netAmountChangeL = netAmountChangeL + [netAmountChange]

        currentMonth = currentMonth + [row[0]]

    
    average = sum([item - total_list[index -1] for index, item in enumerate(total_list) if index > 0]) / (len(total_list) -1)
    print(average)
#----------------------------------------------------------------------------------------------------

    if netAmountChange > greatestincInProfits[1]:
            greatestincInProfits[0] = row[0]
            greatestincInProfits[1] = netAmountChange

    if netAmountChange < greatestdecInProfits[1]:
            greatestdecInProfits[0] = row[0]
            greatestdecInProfits[1] = netAmountChange

print(f"Financial Analysis")

print(f"--------------------------------")      

print(f"Total Months: {len(totalDates)}")

print(f"Total:{netTotal}")

print(f"--------------------------------")  

print(f"Average Change: ${round(average,2)}")

print(f"--------------------------------")  

print(f"Greatest Increase in Profits: {greatestdecInProfits}")

print(f"Greatest Decrease in Profits: {greatestdecInProfits}")

#----------------------------------------------------------------------------------------------------

outputfile = "output.txt"
with open(outputfile, "w") as textfile:

    textfile.write(f"Financial Analysis\n")

    textfile.write(f"--------------------------------\n")

    textfile.write(f"Total Months: {len(totalDates)}" +"\n")

    textfile.write(f"Total:{netTotal}" +"\n")

    textfile.write(f"--------------------------------\n")

    textfile.write(f" Average Change: ${round(average,2)}" + "\n")

    textfile.write(f"--------------------------------\n")
    
    textfile.write(f"Greatest Increase in Profits: {greatestincInProfits}" + "\n")

    textfile.write(f"Greatest Decrease in Profits: {greatestdecInProfits}" + "\n")

    textfile.write(f"--------------------------------" + "\n")

with open(outputfile, "r") as textfile:

    print(textfile.read())

