import PySimpleGUI as sg
from utils import get_employees
from datetime import date



def date_frame():
    return [
        [sg.Input(readonly=True, size=20, k="-DATE-", default_text=f"{date.today(): %d %B %Y}"),
         sg.Button("Выбрать", k="-GET_DATE-"),
         sg.Text("кол-во\nдней"),
         sg.Spin(values=list(range(1, 30)), size=4, readonly=True, k="-DAYS-")]
    ]


def employee_frame():
    return [
        [sg.Combo(values=[emp for emp in get_employees()],
                  expand_x=True, key="-employees-",
                  enable_events=True),
         sg.Button("+")],
        [sg.Text("Цель\nкомандировки"), sg.Input(size=30, k="-objective-")]
    ]


def destination_frame():
    return [
        [sg.Input(tooltip="Куда командируется", key="-destination-")],
        [sg.Button("Панов"), sg.Button("Денеб")]
    ]


def get_layout():
    return [
        [sg.Frame("Начало экспедиции", layout=date_frame())],
        [sg.Frame("Сотрудник", layout=employee_frame(), expand_x=True)],
        [sg.Frame('Место назначения', layout=destination_frame(), expand_x=True)],
        [sg.Button("Сохранить маршрутный лист", expand_x=True, k="Ok")]

    ]


def main():
   pass


if __name__ == '__main__':
    main()
