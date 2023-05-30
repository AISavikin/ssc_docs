import PySimpleGUI as sg
from data_base import *
from utils import *


class MainWindow:
    current_employee = None
    current_desination = None
    current_date = date.today()

    def __init__(self):
        self.employees = sorted([Employee(emp.name, emp.position, emp.department) for emp in Employees.select()],
                                key=lambda x: x.name)
        self.get_layout()
        self.window = sg.Window("Title", layout=self.layout, element_justification='center')

    def get_layout(self):
        date_frame = [
            [sg.Text("Число"),
             sg.Combo(values=[i for i in range(1, 32)], default_value=self.current_date.day, readonly=True, k="day"),
             sg.Text("Месяц"),
             sg.Combo(values=[i for i in range(1, 13)], default_value=self.current_date.month, readonly=True,
                      k="month"),
             sg.Text("Год"),
             sg.Combo(values=[i for i in range(2023, 2027)], default_value=self.current_date.year, readonly=True,
                      k="year")]
        ]
        employee_frame = [
            [sg.Combo(values=[emp for emp in self.employees],
                      expand_x=True, key="-employees-",
                      enable_events=True),
             sg.Button("+")],
            [sg.Text("Цель командировки"), sg.Input()]
        ]
        destination_frame = [
            [sg.Input(tooltip="Куда командируется", size=30, key="-destination-")],
            [sg.Button("Панов"), sg.Button("Денеб")]
        ]

        layout = [
            [sg.Frame("Начало экспедиции", layout=date_frame)],
            [sg.Frame("Сотрудник", layout=employee_frame)],
            [sg.Frame('Место назначения', layout=destination_frame, expand_x=True), sg.Text("кол-во\nдней"),
             sg.Spin(values=list(range(1, 30)), size=4, readonly=True)],
            [sg.Button("Ok")]

        ]
        self.layout = layout

    def show(self):
        while True:
            event, value = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == "+":
                sg.Popup("Функция добавления сотрудника не дописана!")
                # self.employees.append(Employee("qwe", 'qwe', '123'))
            if event == '-employees-':
                self.current_employee = self.window['-employees-'].get()

            if event == 'Панов':
                self.current_desination = Destination('НИС "Профессор Панов"', 'Пожидаев Вячеслав Иванович', 'Капитан')
                self.window["-destination-"].update(self.current_desination.destination)

            if event == 'Денеб':
                self.current_desination = Destination('ПТР "Денеб"', 'Ткаченко Владимир Иванович', 'Капитан')
                self.window["-destination-"].update(self.current_desination.destination)

            if event == "Ok":
                self.save()
                res = self.window["-employees-"].get()

    def update(self):
        self.window["-employees-"].update(values=[emp.name for emp in self.employees])

    def save(self):
        if not self.current_employee:
            sg.PopupError("Выберите сотрудника!")
            return
        date =


def main():
    win = MainWindow()
    win.show()


if __name__ == '__main__':
    main()
