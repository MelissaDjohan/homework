# import
import os
import csv
#to read csv
budget_csv_path = os.path.join('Resources', 'budget_data.csv')
with open(budget_csv_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
    #variables
    month_count = 0
    total = 0 
    start_val = 0
    difference = 0
    max_diff = 0
    min_diff = 0
    #loop to find difference
    for i in csv_reader:
        month = i[0]
        amount = i[1]
        iamount = int(amount)
        difference = iamount - start_val
        #for greatest increase in profits
        if max_diff < difference:
            max_diff = difference
            max_date = month
        #for greatest decrease in profits
        if min_diff > difference:
            min_diff = difference
            min_date = month
        start_val = iamount
        #for total months
        month_count = month_count + 1
        total += int(amount)

    #FINANCIAL ANALYSIS RESULTS
    print("Financial Analysis")
    print("---------------------------")
    print(f'Total Months : {month_count}')
    print(f'Total: ${total}')
    print(f'Greatest Increase in Profits: {max_date} ($ {max_diff})')
    print(f'Greatest Decrease in Profits: {min_date} ($ {min_diff})')

    #print to .txt file
    import sys
    sys.stdout = open('FinancialAnalysis.txt', 'w')
    print("Financial Analysis")
    print("---------------------------")
    print(f'Total Months : {month_count}')
    print(f'Total: ${total}')
    print(f'Greatest Increase in Profits: {max_date} ($ {max_diff})')
    print(f'Greatest Decrease in Profits: {min_date} ($ {min_diff})')
    sys.stdout.close()