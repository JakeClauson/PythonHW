import os
import csv
#create variables for what im going to display/change
months = 0
gross = 0
monthlist = []
profitlist = []
changelist = []

#C:\Users\Office 1\Desktop\PythonStuff\UofA-PHX-DATA-PT-11-2019-U-C-master\03-Python\Homework\Instructions

# create a path to the file
csvpath = os.path.join('..','Resources', 'budget_data.csv')
# Open the CSV
with open(csvpath, newline='', encoding="utf8") as datafile:
    csvreader = csv.reader(datafile, delimiter=',')
    # skip header
    csvheader = next(csvreader)
    
    #loop through data
    for row in csvreader:
        months = months + 1
        profit = int(row[1])
        profitlist.append(profit)
        monthlist.append(row[0])
        gross += profit

# formula for change starting at the 2nd row      
        if months > 1:
            change = float(row[1]) - profitlist[len(profitlist)-2]
            changelist.append(change)

#function for total of the change / how many changes 
        def average(numbers):
            total = 0.0
            all_change = len(changelist)
            for change in changelist:
                    total += change
            return total / all_change

#pulling the max amount and min amount of change
greatest_increase = max(changelist)
greatest_decrease = min(changelist)

# print data
print("Financial Analysis")
print("------------------------")
print(f"Total Months: " + str(months)) 
print("Total: $" + str(gross))
print("Average Change: " + (str(round(average(changelist), 2))))
print("Greatest Increase in Profits: (" + str(round(greatest_increase)) + ")")
print("Greatest Decrease in Profits: (" + str(round(greatest_decrease)) + ")") 

# Specify the file to write to
output_path = os.path.join("PyBank.txt")
with open(output_path, "w", newline="") as f:
    #inatalize writer
    #f.writeiter(csvfile, delimiter=',')

#write to new text file
    f.write("Financial Analysis\n")
    f.write("------------------------\n")
    f.write(f"Total Months: " + str(months) + "\n")
    f.write(f"Total: $" + str(gross) + "\n")
    f.write(f"Average Change: " + (str(round(average(changelist), 2)) + "\n"))
    f.write(f"Greatest Increase in Profits: (" + str(round(greatest_increase)) + ")\n")
    f.write(f"Greatest Decrease in Profits: (" + str(round(greatest_decrease)) + ")\n") 


