from openpxyl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B2"] = "world!"

workbook.save(filename="hello_world.xlsx")