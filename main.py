import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PM_calc_design import Ui_PMCalc
import locale


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_PMCalc()
        self.ui.setupUi(self)

        self.ui.calculate_button.clicked.connect(self.calculate)

    def calculate(self):

        # Получаем значения из полей ввода
        development = self.ui.development_value.value()
        analytics = self.ui.analytics_value.value()
        hour_rate = self.ui.hourly_rate_value.value()
        management = self.ui.management_value.value()
        communications = self.ui.communications_value.value()
        testing = self.ui.testing_value.value()
        risks = self.ui.risks_value.value()

        # Выполняем расчет
        total_hours = (development + analytics +
                       ((development + analytics) * management) +
                       ((development + analytics) * communications) +
                       ((development + analytics) * testing) +
                       ((development + analytics) * risks))

        total_sum = total_hours * hour_rate
        total_days = total_hours / 3

        formatted_total_sum = "{:,.2f}".format(total_sum)

        self.ui.total_sum_value.setText(f' {formatted_total_sum}')
        self.ui.total_hours_value.setText(f' {total_hours:.2f}')
        self.ui.total_days_value.setText(f' {total_days:.2f}')



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
