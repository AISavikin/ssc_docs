from datetime import date
import PySimpleGUI as sg
from gui import get_layout
from utils import Destination, save_road_sheet



class MainWindow:
    current_employee = None
    current_desination = None
    start_date = date.today()

    def __init__(self):
        self.layout = get_layout()
        self.window = sg.Window("Маршрутный лист ЮНЦ", layout=self.layout, element_justification='center')

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

            if event == "-GET_DATE-":
                try:
                    month, day, year = sg.popup_get_date(begin_at_sunday_plus=1)
                    self.start_date = date(year, month, day)
                    self.window["-DATE-"].update(f"{self.start_date: %d %B %y }")
                except:
                    pass

            if event == "Ok":
                employee = self.current_employee
                if employee is None:
                    sg.popup_error("Выберите сотрудника!")
                    continue
                destination = self.current_desination
                if destination is None:
                    sg.popup_error("Выберите пункт назначения!")
                    continue
                objective: str = self.window["-objective-"].get()
                start_day: date = self.start_date
                days: int = self.window["-DAYS-"].get()
                save_road_sheet(employee, destination, objective, start_day, days)


def main():
    win = MainWindow()
    win.show()


if __name__ == '__main__':
    main()
