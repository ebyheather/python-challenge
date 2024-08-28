#Import budget_data CSV file
import os
import csv

#Open the file path
csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    #Skip the header row
    header = next(csvreader)

    #Store months from first column
    unique_months = []
    profits_losses = []
    
    #Iterate through the rows
    for row in csvreader:
        unique_months.append(row[0])
        profits_losses.append(int(row[1]))
        

#Count unique values in month_data
unique_count = len(unique_months)

#Sum of total gains/losses
total_sum = sum(profits_losses)

#Print Financial Analysis and totals
print("""Financial Analysis
---------------------------""")
print(f'Total Months: {unique_count}')
print(f'Total: ${total_sum}')

#Find the difference in gains per row
difference_gains = []

for i in range(len(profits_losses)-1):
    difference = profits_losses[i+1] - profits_losses[i]
    difference_gains.append(difference)

#Find the average difference
difference_average = round(sum(difference_gains)/len(difference_gains),2)
print(f'Average Change: ${difference_average}')

#Find the max gain and max loss
max_gain = max(difference_gains)
gain_index = difference_gains.index(max_gain)+1
gain_month = unique_months[gain_index]

max_loss = min(difference_gains)
loss_index = difference_gains.index(max_loss)+1
loss_month = unique_months[loss_index]

print(f'Greatest Increase in Profits: {gain_month} (${max_gain})')
print(f'Greatest Decrease in Profits: {loss_month} (${max_loss})')

#Write to CSV file
output_path = os.path.join('analysis','results.csv')

with open(output_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(["Financial Analysis"])
    writer.writerow(["---------------------------"])
    
    # Write the analysis results
    writer.writerow(['Total Months', f'{unique_count}'])
    writer.writerow(['Total', f'${total_sum}'])
    writer.writerow(['Average Change', f'${difference_average}'])
    writer.writerow(['Greatest Increase in Profits', f'{gain_month} (${max_gain})'])
    writer.writerow(['Greatest Decrease in Profits', f'{loss_month} (${max_loss})'])

print(f"Results written to {output_path}")
