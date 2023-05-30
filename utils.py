from dataclasses import dataclass

from docxtpl import DocxTemplate
from datetime import date, timedelta
import locale

locale.setlocale(locale.LC_TIME, "RU")


# tpl = DocxTemplate('tpl.docx')
# context = {
#     "name": "Савикин Андрей Игоревич",
#     "position": "м.н.с.",
#     "destination": 'НИС "Профессор Панов"',
#     "objective": "Отбор проб макрозообентоса",
#     "start_day": "31",
#     "start_month": "мая",
#     "start_year": "23",
#     "end_day": "4",
#     "end_month": "июня",
#     "end_year": "23",
# }
# tpl.render(context)
# file_name = "Маршрутный лист.docx"
# tpl.save(file_name)
#
@dataclass
class Destination:
    destination: str = 'НИС "Профессор Панов"'
    employee: str = "Иванов Иван Иванович"
    employee_position: str = "Капитан"


@dataclass
class Employee:
    name: str
    position: str
    department: str


def save_road_sheet(
        employee: Employee,
        destination: Destination,
        objective: str,
        start_day: date,
        days: int | Destination):

    tpl = DocxTemplate('tpl.docx')
    end_day = start_day + timedelta(days=days)
    context = {
        "name": employee.name,
        "position": employee.position,
        "department": employee.department,
        "destination": destination.destination,
        "destination_employee": destination.employee,
        "destination_employee_position": destination.employee_position,
        "objective": objective,
        "start_day": start_day.day,
        "start_month": f"{start_day: %B}",
        "start_year": start_day.year % 2000,
        "end_day": end_day.day,
        "end_month": f"{end_day: %B}",
        "end_year": end_day.year % 2000,
    }
    file_name = "Маршрутный лист.docx"
    tpl.save(file_name)



objective = "Отбор проб макрозообентоса"
start_day = date.today() + timedelta(days=2)

# save_road_sheet(name, position, destination, objective, start_day, 4)
