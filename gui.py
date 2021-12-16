# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginnqaCjU.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


# import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(605, 315)
        MainWindow.setMinimumSize(QSize(605, 315))
        MainWindow.setMaximumSize(QSize(605, 315))
        MainWindow.setStyleSheet(u"background-color:")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(605, 315))
        self.centralwidget.setMaximumSize(QSize(605, 315))
        self.centralwidget.setStyleSheet(u"background-color: rgba(39, 37, 37, 240)")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 605, 315))
        self.groupBox.setMinimumSize(QSize(605, 315))
        self.groupBox.setMaximumSize(QSize(605, 315))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(530, 10, 64, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.b_minimize = QPushButton(self.layoutWidget)
        self.b_minimize.setObjectName(u"b_minimize")
        self.b_minimize.setMinimumSize(QSize(30, 20))
        self.b_minimize.setMaximumSize(QSize(30, 20))
        self.b_minimize.setStyleSheet(u"background-color:#203534")
        icon = QIcon()
        icon.addFile(u":/minimize/Minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.b_minimize.setIcon(icon)
        self.b_minimize.setIconSize(QSize(16, 16))
        self.b_minimize.setFlat(True)

        self.horizontalLayout.addWidget(self.b_minimize)

        self.b_close = QPushButton(self.layoutWidget)
        self.b_close.setObjectName(u"b_close")
        self.b_close.setMinimumSize(QSize(30, 20))
        self.b_close.setMaximumSize(QSize(30, 20))
        self.b_close.setStyleSheet(u"QPushButton{\n"
                                   "	border: 0px solid green ;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "	background-color:rgba(255, 0, 0, 180)\n"
                                   "}\n"
                                   "QPushButton:pressed{\n"
                                   "	background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1 stop: 0 rgba(255, 0, 0, 180), stop: 1 rgba(255, 0, 0, 140));\n"
                                   "}\n"
                                   "")
        icon1 = QIcon()
        icon1.addFile(u":/close/Close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.b_close.setIcon(icon1)
        self.b_close.setFlat(True)

        self.horizontalLayout.addWidget(self.b_close)

        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 30, 120, 80))
        self.frame.setLayoutDirection(Qt.RightToLeft)
        self.frame.setStyleSheet(u"image: url(:/logo/Logo.svg);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.n_newUser = QPushButton(self.groupBox)
        self.n_newUser.setObjectName(u"n_newUser")
        self.n_newUser.setGeometry(QRect(440, 220, 140, 40))
        self.n_newUser.setMinimumSize(QSize(80, 40))
        self.n_newUser.setMaximumSize(QSize(140, 40))
        font = QFont()
        font.setPointSize(14)
        self.n_newUser.setFont(font)
        self.n_newUser.setStyleSheet(u"QPushButton{\n"
                                     "	border:2px solid #0C8040;\n"
                                     "	border-radius: 15px;\n"
                                     "	color: #72AE74\n"
                                     "}QPushButton:hover{\n"
                                     "	border: 2px solid	#72AE74;\n"
                                     "	color: #72AE74 ;\n"
                                     "}QPushButton:pressed{\n"
                                     "	background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1 stop: 0 rgba(56, "
                                     "102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n "
                                     "}\n"
                                     "")
        icon2 = QIcon()
        icon2.addFile(u":/add/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.n_newUser.setIcon(icon2)
        self.n_newUser.setIconSize(QSize(20, 20))
        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(40, 140, 549, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tb_mkey = QLineEdit(self.horizontalLayoutWidget)
        self.tb_mkey.setObjectName(u"tb_mkey")
        self.tb_mkey.setMinimumSize(QSize(451, 40))
        self.tb_mkey.setMaximumSize(QSize(451, 40))
        font1 = QFont()
        font1.setPointSize(18)
        self.tb_mkey.setFont(font1)
        self.tb_mkey.setStyleSheet(u"QLineEdit{\n"
                                   "	border-top:2px solid #0C8040;\n"
                                   "	border-bottom:2px solid #0C8040;\n"
                                   "	border-left:2px solid #0C8040;\n"
                                   "	border-top-left-radius: 15px;\n"
                                   "	border-bottom-left-radius: 15px;\n"
                                   "	color: #72AE74\n"
                                   "}QLineEdit:hover{\n"
                                   "	border: 2px solid	#72AE74;\n"
                                   "	color: #72AE74 ;\n"
                                   "}")
        self.tb_mkey.setEchoMode(QLineEdit.Password)
        self.tb_mkey.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.tb_mkey.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.tb_mkey)

        self.b_pwToggle = QPushButton(self.horizontalLayoutWidget)
        self.b_pwToggle.setObjectName(u"b_pwToggle")
        self.b_pwToggle.setMinimumSize(QSize(48, 40))
        self.b_pwToggle.setMaximumSize(QSize(48, 40))
        self.b_pwToggle.setStyleSheet(u"QPushButton{\n"
                                      "	border-top:2px solid #0C8040;\n"
                                      "	border-bottom:2px solid #0C8040;\n"
                                      "	border-left:2px solid #0C8040;\n"
                                      "	color: #72AE74;\n"
                                      "	icon:url(:/hidden/Hidden.svg)\n"
                                      "}QPushButton:hover{\n"
                                      "	border: 2px solid	#72AE74;\n"
                                      "	color: #72AE74 ;\n"
                                      "}QPushButton:checked{\n"
                                      "	background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1 stop: 0 rgba(56, "
                                      "102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n "
                                      "	icon:url(:/plain/plain.svg);\n"
                                      "}")
        icon3 = QIcon()
        icon3.addFile(u":/hidden/Hidden.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.b_pwToggle.setIcon(icon3)
        self.b_pwToggle.setIconSize(QSize(36, 36))
        self.b_pwToggle.setCheckable(True)
        self.b_pwToggle.setChecked(False)

        self.horizontalLayout_3.addWidget(self.b_pwToggle)

        self.b_login = QPushButton(self.horizontalLayoutWidget)
        self.b_login.setObjectName(u"b_login")
        self.b_login.setMinimumSize(QSize(48, 40))
        self.b_login.setMaximumSize(QSize(48, 40))
        self.b_login.setStyleSheet(u"QPushButton{\n"
                                   "	border:2px solid #0C8040;\n"
                                   "	border-top-right-radius: 15px;\n"
                                   "	border-bottom-right-radius: 15px;\n"
                                   "	color: #72AE74\n"
                                   "}QPushButton:hover{\n"
                                   "	border: 2px solid	#72AE74;\n"
                                   "	color: #72AE74 ;\n"
                                   "}QPushButton:pressed{\n"
                                   "	background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1 stop: 0 rgba(56, "
                                   "102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n "
                                   "}\n"
                                   "")
        icon4 = QIcon()
        icon4.addFile(u":/select/Select.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.b_login.setIcon(icon4)
        self.b_login.setIconSize(QSize(36, 36))

        self.horizontalLayout_3.addWidget(self.b_login)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.b_close.clicked.connect(MainWindow.close)
        self.b_minimize.clicked.connect(MainWindow.showMinimized)
        self.b_pwToggle.clicked.connect(self.toggle_pass_handler)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.b_minimize.setText("")
        self.b_close.setText("")
        # if QT_CONFIG(tooltip)
        self.n_newUser.setToolTip(QCoreApplication.translate("MainWindow", u"Create a New user", None))
        # endif // QT_CONFIG(tooltip)
        self.n_newUser.setText(QCoreApplication.translate("MainWindow", u"   New User", None))
        self.tb_mkey.setInputMask("")
        self.tb_mkey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter the Master Key", None))
        # if QT_CONFIG(tooltip)
        self.b_pwToggle.setToolTip(QCoreApplication.translate("MainWindow", u"Toggle visibility", None))
        # endif // QT_CONFIG(tooltip)
        self.b_pwToggle.setText("")
        self.b_login.setText("")
        # if QT_CONFIG(shortcut)
        self.b_login.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))

    def toggle_pass_handler(self):
        if self.b_pwToggle.isChecked():
            self.tb_mkey.setEchoMode(QLineEdit.Normal)
        else:
            self.tb_mkey.setEchoMode(QLineEdit.Password)
# endif // QT_CONFIG(shortcut)
# retranslateUi


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())
