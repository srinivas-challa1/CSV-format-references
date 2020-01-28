import csv
with open(r"C:\Users\srini\Documents\employees_birthday.txt","r") as csv_file:
    csv_reader=csv.DictReader(csv_file,delimiter=",")
    line_count=0
    for row in csv_reader:
        if line_count==0:
            print(f'column names are {",".join(row)}')
            line_count+=1
        print(f'{row["name"]} works in {row["department"]} department ,and was born in {row["birthday month"] }')
        line_count+=1
    print(f'{line_count} lines processed')
