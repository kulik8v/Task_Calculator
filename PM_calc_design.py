# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PM_calc.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_PMCalc(object):
    def setupUi(self, PMCalc):
        if not PMCalc.objectName():
            PMCalc.setObjectName(u"PMCalc")
        PMCalc.setEnabled(True)
        PMCalc.resize(689, 181)
        PMCalc.setStyleSheet(u"background-color:#222831;\n"
"font-family:\"Rubik\";\n"
"color:#EEEEEE\n"
"")
        self.centralwidget = QWidget(PMCalc)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Inputs = QGroupBox(self.centralwidget)
        self.Inputs.setObjectName(u"Inputs")
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(10)
        font.setBold(True)
        self.Inputs.setFont(font)
        self.Inputs.setStyleSheet(u"background-color:#393E46")
        self.gridLayout_2 = QGridLayout(self.Inputs)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.development = QLabel(self.Inputs)
        self.development.setObjectName(u"development")
        font1 = QFont()
        font1.setFamilies([u"Rubik"])
        font1.setPointSize(10)
        self.development.setFont(font1)
        self.development.setStyleSheet(u"background-color:#393E46")

        self.gridLayout_2.addWidget(self.development, 0, 0, 1, 1)

        self.development_value = QDoubleSpinBox(self.Inputs)
        self.development_value.setObjectName(u"development_value")
        self.development_value.setFont(font1)
        self.development_value.setMaximum(10000.000000000000000)

        self.gridLayout_2.addWidget(self.development_value, 0, 1, 1, 1)

        self.analytics = QLabel(self.Inputs)
        self.analytics.setObjectName(u"analytics")
        self.analytics.setFont(font1)
        self.analytics.setStyleSheet(u"background-color:#393E46")

        self.gridLayout_2.addWidget(self.analytics, 1, 0, 1, 1)

        self.analytics_value = QDoubleSpinBox(self.Inputs)
        self.analytics_value.setObjectName(u"analytics_value")
        self.analytics_value.setFont(font1)
        self.analytics_value.setMaximum(10000.000000000000000)

        self.gridLayout_2.addWidget(self.analytics_value, 1, 1, 1, 1)

        self.hourly_rate = QLabel(self.Inputs)
        self.hourly_rate.setObjectName(u"hourly_rate")
        self.hourly_rate.setFont(font1)
        self.hourly_rate.setStyleSheet(u"background-color:#393E46")

        self.gridLayout_2.addWidget(self.hourly_rate, 2, 0, 1, 1)

        self.hourly_rate_value = QDoubleSpinBox(self.Inputs)
        self.hourly_rate_value.setObjectName(u"hourly_rate_value")
        self.hourly_rate_value.setFont(font1)
        self.hourly_rate_value.setMaximum(10000000000000.000000000000000)
        self.hourly_rate_value.setSingleStep(100.000000000000000)
        self.hourly_rate_value.setValue(4800.000000000000000)

        self.gridLayout_2.addWidget(self.hourly_rate_value, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.Inputs, 0, 0, 1, 1)

        self.Add = QGroupBox(self.centralwidget)
        self.Add.setObjectName(u"Add")
        font2 = QFont()
        font2.setFamilies([u"Rubik"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setKerning(False)
        self.Add.setFont(font2)
        self.Add.setStyleSheet(u"background-color:#393E46")
        self.gridLayout = QGridLayout(self.Add)
        self.gridLayout.setObjectName(u"gridLayout")
        self.management = QCheckBox(self.Add)
        self.management.setObjectName(u"management")
        self.management.setEnabled(True)
        self.management.setFont(font1)
        self.management.setToolTipDuration(8)
        self.management.setStyleSheet(u"background-color:#393E46")
        self.management.setChecked(False)
        self.management.setTristate(False)

        self.gridLayout.addWidget(self.management, 0, 0, 1, 1)

        self.management_value = QDoubleSpinBox(self.Add)
        self.management_value.setObjectName(u"management_value")
        self.management_value.setEnabled(False)
        self.management_value.setFont(font1)
        self.management_value.setMaximum(10000.000000000000000)
        self.management_value.setSingleStep(0.050000000000000)
        self.management_value.setValue(0.300000000000000)

        self.gridLayout.addWidget(self.management_value, 0, 1, 1, 1)

        self.communications = QCheckBox(self.Add)
        self.communications.setObjectName(u"communications")
        self.communications.setFont(font1)
        self.communications.setAutoFillBackground(False)
        self.communications.setStyleSheet(u"background-color:#393E46")
        self.communications.setChecked(False)

        self.gridLayout.addWidget(self.communications, 1, 0, 1, 1)

        self.communications_value = QDoubleSpinBox(self.Add)
        self.communications_value.setObjectName(u"communications_value")
        self.communications_value.setEnabled(False)
        self.communications_value.setFont(font1)
        self.communications_value.setMaximum(10000.000000000000000)
        self.communications_value.setSingleStep(0.050000000000000)
        self.communications_value.setValue(0.200000000000000)

        self.gridLayout.addWidget(self.communications_value, 1, 1, 1, 1)

        self.testing = QCheckBox(self.Add)
        self.testing.setObjectName(u"testing")
        self.testing.setFont(font1)
        self.testing.setStyleSheet(u"background-color:#393E46")
        self.testing.setChecked(False)

        self.gridLayout.addWidget(self.testing, 2, 0, 1, 1)

        self.testing_value = QDoubleSpinBox(self.Add)
        self.testing_value.setObjectName(u"testing_value")
        self.testing_value.setEnabled(False)
        self.testing_value.setFont(font1)
        self.testing_value.setMaximum(10000.000000000000000)
        self.testing_value.setSingleStep(0.050000000000000)
        self.testing_value.setValue(0.200000000000000)

        self.gridLayout.addWidget(self.testing_value, 2, 1, 1, 1)

        self.risks = QCheckBox(self.Add)
        self.risks.setObjectName(u"risks")
        self.risks.setFont(font1)
        self.risks.setStyleSheet(u"background-color:#393E46")
        self.risks.setChecked(False)

        self.gridLayout.addWidget(self.risks, 3, 0, 1, 1)

        self.risks_value = QDoubleSpinBox(self.Add)
        self.risks_value.setObjectName(u"risks_value")
        self.risks_value.setEnabled(False)
        self.risks_value.setFont(font1)
        self.risks_value.setMaximum(10000.000000000000000)
        self.risks_value.setSingleStep(0.050000000000000)
        self.risks_value.setValue(0.150000000000000)

        self.gridLayout.addWidget(self.risks_value, 3, 1, 1, 1)


        self.gridLayout_4.addWidget(self.Add, 0, 1, 1, 1)

        self.Result = QGroupBox(self.centralwidget)
        self.Result.setObjectName(u"Result")
        self.Result.setFont(font2)
        self.Result.setStyleSheet(u"background-color:#393E46")
        self.gridLayout_3 = QGridLayout(self.Result)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.total_hours_label = QLabel(self.Result)
        self.total_hours_label.setObjectName(u"total_hours_label")
        self.total_hours_label.setFont(font1)
        self.total_hours_label.setStyleSheet(u"background-color:#393E46")

        self.gridLayout_3.addWidget(self.total_hours_label, 1, 0, 1, 1)

        self.total_sum_label = QLabel(self.Result)
        self.total_sum_label.setObjectName(u"total_sum_label")
        self.total_sum_label.setFont(font1)
        self.total_sum_label.setStyleSheet(u"background-color:#393E46")

        self.gridLayout_3.addWidget(self.total_sum_label, 0, 0, 1, 1)

        self.total_sum_value = QLabel(self.Result)
        self.total_sum_value.setObjectName(u"total_sum_value")
        self.total_sum_value.setFont(font1)
        self.total_sum_value.setStyleSheet(u"background-color:#393E46")

        self.gridLayout_3.addWidget(self.total_sum_value, 0, 1, 1, 1)

        self.total_hours_value = QLabel(self.Result)
        self.total_hours_value.setObjectName(u"total_hours_value")
        self.total_hours_value.setFont(font1)
        self.total_hours_value.setStyleSheet(u"background-color:#393E46")

        self.gridLayout_3.addWidget(self.total_hours_value, 1, 1, 1, 1)

        self.total_days_label = QLabel(self.Result)
        self.total_days_label.setObjectName(u"total_days_label")
        self.total_days_label.setFont(font1)
        self.total_days_label.setStyleSheet(u"background-color:#393E46")

        self.gridLayout_3.addWidget(self.total_days_label, 2, 0, 1, 1)

        self.total_days_value = QLabel(self.Result)
        self.total_days_value.setObjectName(u"total_days_value")
        self.total_days_value.setFont(font1)
        self.total_days_value.setStyleSheet(u"background-color:#393E46")

        self.gridLayout_3.addWidget(self.total_days_value, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.Result, 0, 2, 1, 1)

        self.calculate_button = QPushButton(self.centralwidget)
        self.calculate_button.setObjectName(u"calculate_button")
        self.calculate_button.setFont(font1)
        self.calculate_button.setStyleSheet(u"background-color:#393E46;\n"
"")

        self.gridLayout_4.addWidget(self.calculate_button, 1, 2, 1, 1)

        PMCalc.setCentralWidget(self.centralwidget)

        self.retranslateUi(PMCalc)
        self.management.toggled.connect(self.management_value.setEnabled)
        self.communications.toggled.connect(self.communications_value.setEnabled)
        self.testing.toggled.connect(self.testing_value.setEnabled)
        self.risks.toggled.connect(self.risks_value.setEnabled)

        QMetaObject.connectSlotsByName(PMCalc)
    # setupUi

    def retranslateUi(self, PMCalc):
        PMCalc.setWindowTitle(QCoreApplication.translate("PMCalc", u"Task Calculator", None))
        self.Inputs.setTitle(QCoreApplication.translate("PMCalc", u"Inputs", None))
        self.development.setText(QCoreApplication.translate("PMCalc", u"Development", None))
        self.analytics.setText(QCoreApplication.translate("PMCalc", u"Analytics", None))
        self.hourly_rate.setText(QCoreApplication.translate("PMCalc", u"Hourly Rate", None))
        self.Add.setTitle(QCoreApplication.translate("PMCalc", u"Additions", None))
        self.management.setText(QCoreApplication.translate("PMCalc", u"Management", None))
        self.communications.setText(QCoreApplication.translate("PMCalc", u"Communications", None))
        self.testing.setText(QCoreApplication.translate("PMCalc", u"Testing", None))
        self.risks.setText(QCoreApplication.translate("PMCalc", u"Risks", None))
        self.Result.setTitle(QCoreApplication.translate("PMCalc", u"Result", None))
        self.total_hours_label.setText(QCoreApplication.translate("PMCalc", u"Total Hours:", None))
        self.total_sum_label.setText(QCoreApplication.translate("PMCalc", u"Total Sum:", None))
        self.total_sum_value.setText("")
        self.total_hours_value.setText("")
        self.total_days_label.setText(QCoreApplication.translate("PMCalc", u"Total Days:", None))
        self.total_days_value.setText("")
        self.calculate_button.setText(QCoreApplication.translate("PMCalc", u"Calculate", None))
    # retranslateUi

