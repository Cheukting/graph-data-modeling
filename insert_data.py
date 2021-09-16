import csv

from terminusdb_client import WOQLClient
from schema import *

employees = {}
contact_numbers = {}
addresses = {}
managers = {}

with open("Contact.csv") as file:
    csv_file = csv.reader(file)
    next(csv_file)
    for row in csv_file:
        contact_numbers[row[0]] = row[1]
        street = row[2].split(',')[0]
        town = row[2].split(',')[1]
        addresses[row[0]] = Address(street = street, town = town, postcode = row[3])

with open("Employees.csv") as file:
    csv_file = csv.reader(file)
    next(csv_file)
    for row in csv_file:
        team = eval(f"Team.{row[3].lower()}")
        employees[row[0]] = Employee(name = row[1], title = row[2], address=addresses[row[0]], contact_number=contact_numbers[row[0]])
        managers[row[0]] = row[4]

for emp_id, man_id in managers.items():
    if man_id:
        employees[emp_id].manager = employees[man_id]

client = WOQLClient("http://127.0.0.1:6363/")
client.connect(db="demo_workshop")

client.insert_document(list(employees.values()))
