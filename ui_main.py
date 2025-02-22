# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(542, 237)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(167, 80, 151, 23))
        self.spinBox.setMaximum(999)
        self.spinBox.setValue(30)
        self.spinBox_2 = QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(167, 110, 151, 23))
        self.spinBox_2.setMaximum(999)
        self.spinBox_2.setValue(20)
        self.spinBox_3 = QSpinBox(self.centralwidget)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(167, 140, 151, 23))
        self.spinBox_3.setMaximum(999)
        self.spinBox_3.setValue(50)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 20, 401, 21))
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(490, 20, 25, 23))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 58, 17))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 191, 17))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 110, 191, 17))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 140, 191, 17))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 170, 191, 17))
        self.spinBox_4 = QSpinBox(self.centralwidget)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setGeometry(QRect(167, 170, 151, 23))
        self.spinBox_4.setMaximum(9999)
        self.spinBox_4.setValue(100)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(370, 130, 111, 61))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"midi\u8def\u5f84", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6700\u4f4e\u54cd\u5ea6", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6700\u4f4e\u6301\u7eed\u65f6\u95f4", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7436\u97f3\u6574\u5408", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u7eed\u6d88\u9664", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5427\uff01", None))
    # retranslateUi

