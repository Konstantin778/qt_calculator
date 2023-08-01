# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QShortcut)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import ui.files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 500)
        MainWindow.setMinimumSize(QSize(300, 500))
        icon = QIcon()
        icon.addFile(u":/icons/icons/calculate.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #121212;\n"
"	font-family: Pangolin;\n"
"	font-size: 16pt;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #670;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #660;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_temp = QLabel(self.centralwidget)
        self.lbl_temp.setObjectName(u"lbl_temp")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy)
        self.lbl_temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lbl_temp)

        self.le_input = QLineEdit(self.centralwidget)
        self.le_input.setObjectName(u"le_input")
        self.le_input.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_input.sizePolicy().hasHeightForWidth())
        self.le_input.setSizePolicy(sizePolicy1)
        self.le_input.setStyleSheet(u"font-size: 40pt;\n"
"border: none;")
        self.le_input.setMaxLength(16)
        self.le_input.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.le_input.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_input)

        self.layout_buttons = QGridLayout()
        self.layout_buttons.setObjectName(u"layout_buttons")

        self.btn_neg = QPushButton(self.centralwidget)
        self.btn_neg.setObjectName(u"btn_neg")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_neg.sizePolicy().hasHeightForWidth())
        self.btn_neg.setSizePolicy(sizePolicy2)
        self.btn_neg.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_neg, 4, 0, 1, 1)

        self.btn_ce = QPushButton(self.centralwidget)
        self.btn_ce.setObjectName(u"btn_ce")
        sizePolicy2.setHeightForWidth(self.btn_ce.sizePolicy().hasHeightForWidth())
        self.btn_ce.setSizePolicy(sizePolicy2)
        self.btn_ce.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_ce, 0, 1, 1, 1)


        self.btn_backspace = QPushButton(self.centralwidget)
        self.btn_backspace.setObjectName(u"btn_backspace")
        sizePolicy2.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy2)
        self.btn_backspace.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/backspace.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_backspace.setIcon(icon1)
        self.btn_backspace.setIconSize(QSize(24, 24))

        self.layout_buttons.addWidget(self.btn_backspace, 0, 2, 1, 1)

        self.btn_c = QPushButton(self.centralwidget)
        self.btn_c.setObjectName(u"btn_c")
        sizePolicy2.setHeightForWidth(self.btn_c.sizePolicy().hasHeightForWidth())
        self.btn_c.setSizePolicy(sizePolicy2)
        self.btn_c.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_c, 0, 0, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy2.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy2)
        self.btn_0.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_0, 4, 1, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy2.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy2)
        self.btn_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy2.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy2)
        self.btn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy2.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy2)
        self.btn_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy2.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy2)
        self.btn_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy2.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy2)
        self.btn_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy2.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy2)
        self.btn_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy2.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy2)
        self.btn_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy2.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy2)
        self.btn_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy2.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy2)
        self.btn_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_division = QPushButton(self.centralwidget)
        self.btn_division.setObjectName(u"btn_division")
        sizePolicy2.setHeightForWidth(self.btn_division.sizePolicy().hasHeightForWidth())
        self.btn_division.setSizePolicy(sizePolicy2)
        self.btn_division.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_division, 0, 3, 1, 1)

        self.btn_multipl = QPushButton(self.centralwidget)
        self.btn_multipl.setObjectName(u"btn_multipl")
        sizePolicy2.setHeightForWidth(self.btn_multipl.sizePolicy().hasHeightForWidth())
        self.btn_multipl.setSizePolicy(sizePolicy2)
        self.btn_multipl.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_multipl, 1, 3, 1, 1)

        self.btn_minus = QPushButton(self.centralwidget)
        self.btn_minus.setObjectName(u"btn_minus")
        sizePolicy2.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy2)
        self.btn_minus.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_minus, 2, 3, 1, 1)

        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setObjectName(u"btn_plus")
        sizePolicy2.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy2)
        self.btn_plus.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_plus, 3, 3, 1, 1)

        self.btn_point = QPushButton(self.centralwidget)
        self.btn_point.setObjectName(u"btn_point")
        sizePolicy2.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy2)
        self.btn_point.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_point, 4, 2, 1, 1)

        self.btn_result = QPushButton(self.centralwidget)
        self.btn_result.setObjectName(u"btn_result")
        sizePolicy2.setHeightForWidth(self.btn_result.sizePolicy().hasHeightForWidth())
        self.btn_result.setSizePolicy(sizePolicy2)
        self.btn_result.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_result, 4, 3, 1, 1)


        self.verticalLayout.addLayout(self.layout_buttons)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.lbl_temp.setText("")
        self.le_input.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btn_neg.setText(QCoreApplication.translate("MainWindow", u"+/\u2212", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.btn_ce.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0415", None))
#if QT_CONFIG(shortcut)
        self.btn_ce.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_backspace.setText("")
#if QT_CONFIG(shortcut)
        self.btn_backspace.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.btn_c.setText(QCoreApplication.translate("MainWindow", u"\u0421", None))
#if QT_CONFIG(shortcut)
        self.btn_c.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_division.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.btn_division.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_multipl.setText(QCoreApplication.translate("MainWindow", u"*", None))
#if QT_CONFIG(shortcut)
        self.btn_multipl.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.btn_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.btn_minus.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btn_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.btn_plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btn_point.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)

        for sc in (',', '.'):
            QShortcut(sc, self.btn_point).activated.connect(self.btn_point.animateClick)

#endif // QT_CONFIG(shortcut)
        self.btn_result.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)

        for sc in ('=', 'Enter', 'Return'):
            QShortcut(sc, self.btn_result).activated.connect(self.btn_result.animateClick)

#endif // QT_CONFIG(shortcut)
    # retranslateUi

