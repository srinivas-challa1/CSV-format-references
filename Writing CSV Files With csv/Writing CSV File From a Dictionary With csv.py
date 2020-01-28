import csv
with open(r"C:\Users\srini\Documents\employee_file.csv","w") as employee_file:
    fieldnames=["name","dept","birth_month"]
    employee_data=csv.DictWriter(employee_file,fieldnames=fieldnames)
    employee_data.writeheader()
    employee_data.writerow({"name":"srinivas","dept":"AI engineer","birth_month":"01-03-1997"})
