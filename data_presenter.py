open_file = open('CupcakeInvoices.csv')

# Loop through all the data and print each row.
for row in open_file:
    print(row)

# Loop through all the data and print the type of cupcakes purchased.
for row in open_file:
    item = row.split(',')
    print(item[2])

# Loop through all the data and print out the total for each invoice
# (Note: this data is not provided by the csv, you will need to calculate it.
# Also, keep in mind the data from the csv comes back as a string,
# you will need to convert it to a float. Research how to do this.e
for row in open_file:
    item = row.split(',')
    total_sum = int(item[3]) * float(item[4])
    print(total_sum)

# Loop through all the data, and print out the total for all invoices combined.

combined_total = 0

for row in open_file:
    total = row.split(',')
    combined_total = combined_total + (int(total[3]) * float(total[4]))

print(combined_total)
