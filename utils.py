from dataclasses import dataclass
import sqlite3
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


def get_employees():
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    # запрос на выборку всех данных из таблицы Employee
    cursor.execute('SELECT name, position, department FROM employees')
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return sorted([Employee(emp[0], emp[1], emp[2]) for emp in data],
                  key=lambda x: x.name)



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
        context["destination"] = destination.destination
        context["destination_employee"] = destination.employee
        context["destination_employee_position"] = destination.employee_position
    else:
        context["destination"] = destination
    print(context)
    tpl.render(context)
    file_name = f"Командировки/Маршрутный лист {employee.name}.docx"
    tpl.save(file_name)

