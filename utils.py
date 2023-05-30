from dataclasses import dataclass
from data_base import Employees, Destinations
from docxtpl import DocxTemplate
from datetime import date, timedelta
import locale

locale.setlocale(locale.LC_TIME, "RU")


@dataclass
class Destination:
    destination: str
    employee: str
    employee_position: str


@dataclass
class Employee:
    name: str
    position: str
    department: str

    def __str__(self):
        return self.name


def save_road_sheet(
        employee: Employee,
        destination: Destination | str,
        objective: str,
        start_day: date,
        days: int):
    tpl = DocxTemplate('tpl.docx')
    end_day = start_day + timedelta(days=days)
    context = {
        "name": employee.name,
        "position": employee.position,
        "department": employee.department,
        "destination": destination.destination,
        "destination_employee": '',
        "destination_employee_position": '',
        "objective": objective,
        "start_day": start_day.day,
        "start_month": f"{start_day: %B}",
        "start_year": start_day.year % 2000,
        "end_day": end_day.day,
        "end_month": f"{end_day: %B}",
        "end_year": end_day.year % 2000,
    }
    if isinstance(destination, Destination):
        context["destination"] = destination.destination,
        context["destination_employee"] = destination.employee,
        context["destination_employee_position"] = destination.employee_position
    else:
        context["destination"] = destination
    tpl.render(context)
    file_name = f"Маршрутный лист {employee.name}.docx"
    tpl.save(file_name)


def str_to_date(str_date: tuple):
    day, month, year = tuple(map(int, str_date))
    return date(year, month, day)


start_day = date.today() + timedelta(days=2)
emp = Employees.get(id=1)
emp = Employee(emp.name, emp.position, emp.department)
dest = Destinations.get(id=1)
objct = "Отбор проб макрозообентоса"
start = "31", "05", "2023"

# save_road_sheet(emp, dest, objct, str_to_date(start), 4)
emps = [Employee(emp.name, emp.position, emp.department) for emp in Employees.select()]

# for emp in Employees.select():
#     emps.append(Employee(emp.name, emp.position, emp.department))
print(emps)
