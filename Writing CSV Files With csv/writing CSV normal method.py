import csv
with open(r"C:\Users\srini\Documents\employees_birthday.txt","w") as employee_data:
    employee_file=csv.writer(employee_data,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL,escapechar="\n")
    employee_file.writerow(['name','address','date_joined'])
    employee_file.writerow(['john smith','1132 Anywhere Lane Hoboken NJ ', '07030','Jan 4'])
