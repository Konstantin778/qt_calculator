import sys
from typing import Union, Optional

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase
from ui.design import Ui_MainWindow
from decimal import Decimal
from config import operations, error_zero_div, error_undefined, default_font_size, default_input_font_size


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.entry = self.ui.le_input
        self.temp = self.ui.lbl_temp
        self.input_max_len = self.entry.maxLength()

        QFontDatabase.addApplicationFont("fonts/Pangolin.ttf")

        # setting digits
        self.ui.btn_0.clicked.connect(self.add_digit)
        self.ui.btn_1.clicked.connect(self.add_digit)
        self.ui.btn_2.clicked.connect(self.add_digit)
        self.ui.btn_3.clicked.connect(self.add_digit)
        self.ui.btn_4.clicked.connect(self.add_digit)
        self.ui.btn_5.clicked.connect(self.add_digit)
        self.ui.btn_6.clicked.connect(self.add_digit)
        self.ui.btn_7.clicked.connect(self.add_digit)
        self.ui.btn_8.clicked.connect(self.add_digit)
        self.ui.btn_9.clicked.connect(self.add_digit)

        # actions
        self.ui.btn_c.clicked.connect(self.clear_all)
        self.ui.btn_ce.clicked.connect(self.clear_input)
        self.ui.btn_point.clicked.connect(self.add_comma)
        self.ui.btn_neg.clicked.connect(self.set_negative)
        self.ui.btn_backspace.clicked.connect(self.set_backspace)

        # math
        self.ui.btn_result.clicked.connect(self.calculate)
        self.ui.btn_plus.clicked.connect(self.math_operation)
        self.ui.btn_minus.clicked.connect(self.math_operation)
        self.ui.btn_multipl.clicked.connect(self.math_operation)
        self.ui.btn_division.clicked.connect(self.math_operation)

    def add_digit(self):
        self.remove_error()
        self.clear_temp_if_equality()
        btn = self.sender()

        digit_buttons = ('btn_0', 'btn_1', 'btn_2', 'btn_3', 'btn_4',
                         'btn_5', 'btn_6', 'btn_7', 'btn_8', 'btn_9')

        if btn.objectName() in digit_buttons:
            if self.entry.text() == '0':
                self.entry.setText(btn.text())
            else:
                self.entry.setText(self.entry.text() + btn.text())

        self.adjust_input_font_size()

    def set_negative(self):
        self.clear_temp_if_equality()
        entry = self.entry.text()

        if '-' not in entry:
            if entry != '0':
                entry = '-' + entry
        else:
            entry = entry[1:]

        if len(entry) == self.input_max_len + 1 and '-' in entry:
            self.entry.setMaxLength(self.input_max_len + 1)
        else:
            self.entry.setMaxLength(self.input_max_len)

        self.entry.setText(entry)
        self.adjust_input_font_size()

    def set_backspace(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        entry = self.entry.text()

        if len(entry) != 1:
            if len(entry) == 2 and '-' in entry:
                self.entry.setText('0')
            else:
                self.entry.setText(entry[:-1])
        else:
            self.entry.setText('0')

        self.adjust_input_font_size()

    def clear_all(self):
        self.remove_error()
        self.entry.setText('0')
        self.adjust_input_font_size()
        self.temp.clear()

    def clear_input(self):
        self.remove_error()
        self.clear_temp_if_equality()
        self.entry.setText('0')
        self.adjust_input_font_size()

    def add_comma(self):
        self.clear_temp_if_equality()
        if '.' not in self.entry.text():
            self.entry.setText(self.entry.text() + '.')
            self.adjust_input_font_size()

    def clear_temp_if_equality(self) -> None:
        if self.get_math_sign() == '=':
            self.temp.clear()

    @staticmethod
    def remove_trailing_zeros(num: str):
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n

    def add_temp(self) -> None:
        btn = self.sender()
        entry = self.remove_trailing_zeros(self.entry.text())

        if not self.temp.text() or self.get_math_sign() == '=':
            self.temp.setText(entry + f' {btn.text()} ')
            self.adjust_temp_font_size()
            self.entry.setText('0')
            self.adjust_input_font_size()

    def get_input_num(self) -> Union[int, float]:
        entry = self.entry.text()
        return Decimal(entry) if '.' in entry else int(entry)

    def get_temp_num(self) -> Union[int, float, None]:
        if self.temp.text():
            temp = self.temp.text().split()[0]
            return Decimal(temp) if '.' in temp else int(temp)

    def get_math_sign(self) -> Optional[str]:
        if self.temp.text():
            return self.temp.text().split()[-1]

    def get_input_text_width(self) -> int:
        return self.entry.fontMetrics().boundingRect(self.entry.text()).width()

    def get_temp_text_width(self) -> int:
        return self.temp.fontMetrics().boundingRect(self.temp.text()).width()


    def calculate(self) -> Optional[str]:
        entry = self.entry.text()
        temp = self.temp.text()

        try:
            if temp:
                result = self.remove_trailing_zeros(
                    str(operations[self.get_math_sign()](self.get_temp_num(), self.get_input_num()))
                )
                self.temp.setText(temp + self.remove_trailing_zeros(entry) + ' =')
                self.adjust_temp_font_size()
                self.entry.setText(result)
                self.adjust_input_font_size()
                return result
        except KeyError:
            pass
        except ZeroDivisionError:
            if self.get_temp_num() == 0:
                self.show_error(error_undefined)
            else:
                self.show_error(error_zero_div)

    def math_operation(self) -> None:
        temp = self.temp.text()
        btn = self.sender()

        try:
            if not temp:
                self.add_temp()
            else:
                if self.get_math_sign() != btn.text():
                    if self.get_math_sign() == '=':
                        self.add_temp()
                    else:
                        self.temp.setText(temp[:-2] + f'{btn.text()} ')
                else:
                    self.temp.setText(self.calculate() + f' {btn.text()}')
        except TypeError:
            pass

        self.adjust_temp_font_size()

    def show_error(self, text: str) -> None:
        self.entry.setMaxLength(len(text))
        self.entry.setText(text)
        self.adjust_input_font_size()
        self.disable_buttons(True)

    def remove_error(self) -> None:
        if self.entry.text() in (error_zero_div, error_undefined):
            self.entry.setMaxLength(self.input_max_len)
            self.entry.setText('0')
            self.adjust_input_font_size()
            self.disable_buttons(False)

    def disable_buttons(self, disable: bool) -> None:
        self.ui.btn_result.setDisabled(disable)
        self.ui.btn_plus.setDisabled(disable)
        self.ui.btn_minus.setDisabled(disable)
        self.ui.btn_multipl.setDisabled(disable)
        self.ui.btn_division.setDisabled(disable)
        self.ui.btn_neg.setDisabled(disable)
        self.ui.btn_point.setDisabled(disable)

        colour = 'color: #888;' if disable else 'color: white;'
        self.change_buttons_colour(colour)

    def change_buttons_colour(self, css_colour: str) -> None:
        self.ui.btn_result.setStyleSheet(css_colour)
        self.ui.btn_plus.setStyleSheet(css_colour)
        self.ui.btn_minus.setStyleSheet(css_colour)
        self.ui.btn_multipl.setStyleSheet(css_colour)
        self.ui.btn_division.setStyleSheet(css_colour)
        self.ui.btn_neg.setStyleSheet(css_colour)
        self.ui.btn_point.setStyleSheet(css_colour)

    def adjust_input_font_size(self) -> None:
        font_size = default_input_font_size
        while self.get_input_text_width() > self.entry.width() - 15:
            font_size -= 1
            self.entry.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;')

        font_size = 1
        while self.get_input_text_width() < self.entry.width() - 40:
            font_size += 1

            if font_size > default_input_font_size:
                break

            self.entry.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;')

    def adjust_temp_font_size(self) -> None:
        font_size = default_font_size
        while self.get_temp_text_width() > self.temp.width() - 15:
            font_size -= 1
            self.temp.setStyleSheet('font-size: ' + str(font_size) + 'pt;')

        font_size = 1
        while self.get_temp_text_width() < self.temp.width() - 40:
            font_size += 1

            if font_size > default_font_size:
                break

            self.temp.setStyleSheet('font-size: ' + str(font_size) + 'pt;')

    def resizeEvent(self, event) -> None:
        self.adjust_input_font_size()
        self.adjust_temp_font_size()



app = QApplication(sys.argv)

window = Calculator()
window.show()

sys.exit(app.exec())