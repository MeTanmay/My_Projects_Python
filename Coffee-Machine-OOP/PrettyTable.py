from turtle import left
from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Name",["Tanmay", "Magnus", "Fabiano", "Hans"])
table.add_column("Rating",[1500, 2865, 2799, 2700])
table.add_column("World Championship Titles",[0, 5, 0, "cheat"])
table.align="c"
table.header=True
print(table)

# table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# table.add_row(["Adelaide", 1295, 1158259, 600.5])
# table.add_row(["Brisbane", 5905, 1857594, 1146.4])
# table.add_row(["Darwin", 112, 120900, 1714.7])
# table.add_row(["Hobart", 1357, 205556, 619.5])
# table.add_row(["Sydney", 2058, 4336374, 1214.8])
# table.add_row(["Melbourne", 1566, 3806092, 646.9])
# table.add_row(["Perth", 5386, 1554769, 869.4])

# print(table)