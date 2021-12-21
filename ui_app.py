import sys
import icons.rc_icons
from PyQt6 import QtCore, QtGui, QtWidgets


class ButtonWidgetRow(QtWidgets.QPushButton):
    def __init__(self, rowid, parent=None):
        super(QtWidgets.QPushButton, self).__init__(parent=None)
        self.rowID = rowid
        self.setMinimumSize(69, 69)
        self.setMaximumSize(69, 69)
        self.setStyleSheet("QPushButton{\n"
                           "    color: #72AE74\n"
                           "    text-align: center;\n"
                           "    background-color:rgba(0,0,0,0);\n"
                           "}QPushButton:hover{\n"
                           "    color: rgba(170, 255, 127,255);\n"
                           "}QPushButton:pressed{\n"
                           "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                           "}")
        self.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/select/Select.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(40, 40))


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(999, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(999, 600))
        MainWindow.setMaximumSize(QtCore.QSize(999, 600))
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/Logo.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgba(39, 37, 37, 240)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(605, 315))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(997, 598))
        self.stackedWidget.setMaximumSize(QtCore.QSize(997, 598))
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.splash_login = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splash_login.sizePolicy().hasHeightForWidth())
        self.splash_login.setSizePolicy(sizePolicy)
        self.splash_login.setObjectName("splash_login")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.splash_login)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.frame1 = QtWidgets.QFrame(self.splash_login)
        self.frame1.setMinimumSize(QtCore.QSize(605, 315))
        self.frame1.setMaximumSize(QtCore.QSize(605, 315))
        self.frame1.setObjectName("frame1")
        self.gridLayout = QtWidgets.QGridLayout(self.frame1)
        self.gridLayout.setContentsMargins(0, 0, 0, 60)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame1)
        self.frame_2.setMinimumSize(QtCore.QSize(120, 80))
        self.frame_2.setMaximumSize(QtCore.QSize(120, 80))
        self.frame_2.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.frame_2.setStyleSheet("image: url(:/logo/Logo.svg);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(220, -1, 0, 60)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.b_minimize = QtWidgets.QPushButton(self.frame1)
        self.b_minimize.setMinimumSize(QtCore.QSize(30, 20))
        self.b_minimize.setMaximumSize(QtCore.QSize(40, 25))
        self.b_minimize.setStyleSheet("background-color:#203534")
        self.b_minimize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/minimize/Minimize.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.b_minimize.setIcon(icon1)
        self.b_minimize.setIconSize(QtCore.QSize(16, 16))
        self.b_minimize.setFlat(True)
        self.b_minimize.setObjectName("b_minimize")
        self.horizontalLayout_2.addWidget(self.b_minimize)
        self.b_close = QtWidgets.QPushButton(self.frame1)
        self.b_close.setMinimumSize(QtCore.QSize(30, 20))
        self.b_close.setMaximumSize(QtCore.QSize(40, 25))
        self.b_close.setStyleSheet("QPushButton{\n"
                                   "    border: 0px solid green ;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "    background-color:rgba(255, 0, 0, 180)\n"
                                   "}\n"
                                   "QPushButton:pressed{\n"
                                   "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1 stop: 0 rgba(255, 0, 0, 180), stop: 1 rgba(255, 0, 0, 140));\n"
                                   "}\n"
                                   "")
        self.b_close.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/close/Close.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.b_close.setIcon(icon2)
        self.b_close.setFlat(True)
        self.b_close.setObjectName("b_close")
        self.horizontalLayout_2.addWidget(self.b_close)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(18, 20, 18, 30)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tb_username = QtWidgets.QLineEdit(self.frame1)
        self.tb_username.setMinimumSize(QtCore.QSize(451, 40))
        self.tb_username.setMaximumSize(QtCore.QSize(600, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tb_username.setFont(font)
        self.tb_username.setStyleSheet("QLineEdit{\n"
                                       "    border:2px solid #0C8040;\n"
                                       "    border-radius: 15px;\n"
                                       "    color: #72AE74\n"
                                       "}QLineEdit:hover{\n"
                                       "    border: 2px solid    #72AE74;\n"
                                       "    color: #72AE74 ;\n"
                                       "}")
        self.tb_username.setInputMask("")
        self.tb_username.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.tb_username.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.tb_username.setClearButtonEnabled(True)
        self.tb_username.setObjectName("tb_username")
        self.verticalLayout_3.addWidget(self.tb_username)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tb_mkey = QtWidgets.QLineEdit(self.frame1)
        self.tb_mkey.setMinimumSize(QtCore.QSize(451, 40))
        self.tb_mkey.setMaximumSize(QtCore.QSize(500, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tb_mkey.setFont(font)
        self.tb_mkey.setStyleSheet("QLineEdit{\n"
                                   "    border-top:2px solid #0C8040;\n"
                                   "    border-bottom:2px solid #0C8040;\n"
                                   "    border-left:2px solid #0C8040;\n"
                                   "    border-top-left-radius: 15px;\n"
                                   "    border-bottom-left-radius: 15px;\n"
                                   "    color: #72AE74\n"
                                   "}QLineEdit:hover{\n"
                                   "    border: 2px solid    #72AE74;\n"
                                   "    color: #72AE74 ;\n"
                                   "}")
        self.tb_mkey.setInputMask("")
        self.tb_mkey.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.tb_mkey.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.tb_mkey.setClearButtonEnabled(True)
        self.tb_mkey.setObjectName("tb_mkey")
        self.horizontalLayout_3.addWidget(self.tb_mkey)
        self.b_pwToggle = QtWidgets.QPushButton(self.frame1)
        self.b_pwToggle.setMinimumSize(QtCore.QSize(48, 40))
        self.b_pwToggle.setMaximumSize(QtCore.QSize(48, 40))
        self.b_pwToggle.setStyleSheet("QPushButton{\n"
                                      "    border-top:2px solid #0C8040;\n"
                                      "    border-bottom:2px solid #0C8040;\n"
                                      "    border-left:2px solid #0C8040;\n"
                                      "    color: #72AE74;\n"
                                      "    icon:url(:/hidden/Hidden.svg)\n"
                                      "}QPushButton:hover{\n"
                                      "    border: 2px solid    #72AE74;\n"
                                      "    color: #72AE74 ;\n"
                                      "}QPushButton:checked{\n"
                                      "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1 stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                      "    icon:url(:/plain/plain.svg);\n"
                                      "}")
        self.b_pwToggle.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/hidden/Hidden.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.b_pwToggle.setIcon(icon3)
        self.b_pwToggle.setIconSize(QtCore.QSize(36, 36))
        self.b_pwToggle.setCheckable(True)
        self.b_pwToggle.setChecked(False)
        self.b_pwToggle.setObjectName("b_pwToggle")
        self.horizontalLayout_3.addWidget(self.b_pwToggle)
        self.b_login = QtWidgets.QPushButton(self.frame1)
        self.b_login.setMinimumSize(QtCore.QSize(48, 40))
        self.b_login.setMaximumSize(QtCore.QSize(48, 40))
        self.b_login.setStyleSheet("QPushButton{\n"
                                   "    border:2px solid #0C8040;\n"
                                   "    border-top-right-radius: 15px;\n"
                                   "    border-bottom-right-radius: 15px;\n"
                                   "    color: #72AE74\n"
                                   "}QPushButton:hover{\n"
                                   "    border: 2px solid    #72AE74;\n"
                                   "    color: #72AE74 ;\n"
                                   "}QPushButton:pressed{\n"
                                   "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1 stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                   "}\n"
                                   "")
        self.b_login.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/select/Select.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.b_login.setIcon(icon4)
        self.b_login.setIconSize(QtCore.QSize(36, 36))
        self.b_login.setObjectName("b_login")
        self.horizontalLayout_3.addWidget(self.b_login)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.l_info = QtWidgets.QLabel(self.frame1)
        self.l_info.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_info.setFont(font)
        self.l_info.setStyleSheet("    color: #72AE74\n"
                                  "")
        self.l_info.setObjectName("l_info")
        self.horizontalLayout_4.addWidget(self.l_info)
        self.n_newUser = QtWidgets.QPushButton(self.frame1)
        self.n_newUser.setMinimumSize(QtCore.QSize(80, 40))
        self.n_newUser.setMaximumSize(QtCore.QSize(140, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.n_newUser.setFont(font)
        self.n_newUser.setStyleSheet("QPushButton{\n"
                                     "    border:2px solid #0C8040;\n"
                                     "    border-radius: 15px;\n"
                                     "    color: #72AE74\n"
                                     "}QPushButton:hover{\n"
                                     "    border: 2px solid    #72AE74;\n"
                                     "    color: #72AE74 ;\n"
                                     "}QPushButton:pressed{\n"
                                     "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1 stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                     "}\n"
                                     "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/add/add.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.n_newUser.setIcon(icon5)
        self.n_newUser.setIconSize(QtCore.QSize(20, 20))
        self.n_newUser.setObjectName("n_newUser")
        self.horizontalLayout_4.addWidget(self.n_newUser)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 2, 2)
        self.horizontalLayout_16.addWidget(self.frame1)
        self.stackedWidget.addWidget(self.splash_login)
        self.splashnewuser = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splashnewuser.sizePolicy().hasHeightForWidth())
        self.splashnewuser.setSizePolicy(sizePolicy)
        self.splashnewuser.setObjectName("splashnewuser")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.splashnewuser)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.splashnewuser)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QtCore.QSize(605, 400))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setMinimumSize(QtCore.QSize(120, 80))
        self.frame_4.setMaximumSize(QtCore.QSize(120, 80))
        self.frame_4.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.frame_4.setStyleSheet("image: url(:/logo/Logo.svg);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2.addWidget(self.frame_4, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(18, -1, 18, 60)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tb_username_2 = QtWidgets.QLineEdit(self.frame_3)
        self.tb_username_2.setMinimumSize(QtCore.QSize(451, 40))
        self.tb_username_2.setMaximumSize(QtCore.QSize(600, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tb_username_2.setFont(font)
        self.tb_username_2.setStyleSheet("QLineEdit{\n"
                                         "    border:2px solid #0C8040;\n"
                                         "    border-radius: 15px;\n"
                                         "    color: #72AE74\n"
                                         "}QLineEdit:hover{\n"
                                         "    border: 2px solid    #72AE74;\n"
                                         "    color: #72AE74 ;\n"
                                         "}")
        self.tb_username_2.setInputMask("")
        self.tb_username_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.tb_username_2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.tb_username_2.setClearButtonEnabled(True)
        self.tb_username_2.setObjectName("tb_username_2")
        self.verticalLayout_4.addWidget(self.tb_username_2)
        self.tb_email = QtWidgets.QLineEdit(self.frame_3)
        self.tb_email.setMinimumSize(QtCore.QSize(500, 40))
        self.tb_email.setMaximumSize(QtCore.QSize(600, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tb_email.setFont(font)
        self.tb_email.setStyleSheet("QLineEdit{\n"
                                    "    border:2px solid #0C8040;\n"
                                    "    border-radius: 15px;\n"
                                    "    color: #72AE74\n"
                                    "}QLineEdit:hover{\n"
                                    "    border: 2px solid    #72AE74;\n"
                                    "    color: #72AE74 ;\n"
                                    "}")
        self.tb_email.setInputMask("")
        self.tb_email.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.tb_email.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.tb_email.setClearButtonEnabled(True)
        self.tb_email.setObjectName("tb_email")
        self.verticalLayout_4.addWidget(self.tb_email)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tb_mkey_2 = QtWidgets.QLineEdit(self.frame_3)
        self.tb_mkey_2.setMinimumSize(QtCore.QSize(450, 40))
        self.tb_mkey_2.setMaximumSize(QtCore.QSize(600, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tb_mkey_2.setFont(font)
        self.tb_mkey_2.setStyleSheet("QLineEdit{\n"
                                     "    border-top:2px solid #0C8040;\n"
                                     "    border-bottom:2px solid #0C8040;\n"
                                     "    border-left:2px solid #0C8040;\n"
                                     "    border-top-left-radius: 15px;\n"
                                     "    border-bottom-left-radius: 15px;\n"
                                     "    color: #72AE74\n"
                                     "}QLineEdit:hover{\n"
                                     "    border: 2px solid    #72AE74;\n"
                                     "    color: #72AE74 ;\n"
                                     "}")
        self.tb_mkey_2.setInputMask("")
        self.tb_mkey_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.tb_mkey_2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.tb_mkey_2.setClearButtonEnabled(True)
        self.tb_mkey_2.setObjectName("tb_mkey_2")
        self.horizontalLayout_7.addWidget(self.tb_mkey_2)
        self.b_pwToggle_2 = QtWidgets.QPushButton(self.frame_3)
        self.b_pwToggle_2.setMinimumSize(QtCore.QSize(48, 40))
        self.b_pwToggle_2.setMaximumSize(QtCore.QSize(48, 40))
        self.b_pwToggle_2.setStyleSheet("QPushButton{\n"
                                        "    border:2px solid #0C8040;\n"
                                        "    border-top-right-radius: 15px;\n"
                                        "    border-bottom-right-radius: 15px;\n"
                                        "    color: #72AE74;\n"
                                        "    icon:url(:/hidden/Hidden.svg)\n"
                                        "}QPushButton:hover{\n"
                                        "    border: 2px solid    #72AE74;\n"
                                        "    color: #72AE74 ;\n"
                                        "}QPushButton:checked{\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1 stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                        "    icon:url(:/plain/plain.svg);\n"
                                        "}")
        self.b_pwToggle_2.setText("")
        self.b_pwToggle_2.setIcon(icon3)
        self.b_pwToggle_2.setIconSize(QtCore.QSize(36, 36))
        self.b_pwToggle_2.setCheckable(True)
        self.b_pwToggle_2.setChecked(False)
        self.b_pwToggle_2.setObjectName("b_pwToggle_2")
        self.horizontalLayout_7.addWidget(self.b_pwToggle_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.l_info_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_info_2.setFont(font)
        self.l_info_2.setStyleSheet("    color: #72AE74\n"
                                    "")
        self.l_info_2.setObjectName("l_info_2")
        self.horizontalLayout_9.addWidget(self.l_info_2)
        self.n_newUser_2 = QtWidgets.QPushButton(self.frame_3)
        self.n_newUser_2.setMinimumSize(QtCore.QSize(80, 40))
        self.n_newUser_2.setMaximumSize(QtCore.QSize(140, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.n_newUser_2.setFont(font)
        self.n_newUser_2.setStyleSheet("QPushButton{\n"
                                       "    border:2px solid #0C8040;\n"
                                       "    border-radius: 15px;\n"
                                       "    color: #72AE74\n"
                                       "}QPushButton:hover{\n"
                                       "    border: 2px solid    #72AE74;\n"
                                       "    color: #72AE74 ;\n"
                                       "}QPushButton:pressed{\n"
                                       "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1 stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                       "}\n"
                                       "")
        self.n_newUser_2.setIcon(icon5)
        self.n_newUser_2.setIconSize(QtCore.QSize(20, 20))
        self.n_newUser_2.setObjectName("n_newUser_2")
        self.horizontalLayout_9.addWidget(self.n_newUser_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 1, 0, 1, 2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(220, -1, -1, 60)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.b_minimize_2 = QtWidgets.QPushButton(self.frame_3)
        self.b_minimize_2.setMinimumSize(QtCore.QSize(30, 20))
        self.b_minimize_2.setMaximumSize(QtCore.QSize(40, 25))
        self.b_minimize_2.setStyleSheet("background-color:#203534")
        self.b_minimize_2.setText("")
        self.b_minimize_2.setIcon(icon1)
        self.b_minimize_2.setIconSize(QtCore.QSize(16, 16))
        self.b_minimize_2.setFlat(True)
        self.b_minimize_2.setObjectName("b_minimize_2")
        self.horizontalLayout_6.addWidget(self.b_minimize_2)
        self.b_close_2 = QtWidgets.QPushButton(self.frame_3)
        self.b_close_2.setMinimumSize(QtCore.QSize(30, 20))
        self.b_close_2.setMaximumSize(QtCore.QSize(40, 25))
        self.b_close_2.setStyleSheet("QPushButton{\n"
                                     "    border: 0px solid green ;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "    background-color:rgba(255, 0, 0, 180)\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1 stop: 0 rgba(255, 0, 0, 180), stop: 1 rgba(255, 0, 0, 140));\n"
                                     "}\n"
                                     "")
        self.b_close_2.setText("")
        self.b_close_2.setIcon(icon2)
        self.b_close_2.setFlat(True)
        self.b_close_2.setObjectName("b_close_2")
        self.horizontalLayout_6.addWidget(self.b_close_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)
        self.horizontalLayout_5.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.splashnewuser)
        self.mainpage = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainpage.sizePolicy().hasHeightForWidth())
        self.mainpage.setSizePolicy(sizePolicy)
        self.mainpage.setMinimumSize(QtCore.QSize(905, 600))
        self.mainpage.setMaximumSize(QtCore.QSize(1000, 600))
        self.mainpage.setObjectName("mainpage")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainpage)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainpage_frame = QtWidgets.QFrame(self.mainpage)
        self.mainpage_frame.setMinimumSize(QtCore.QSize(1000, 600))
        self.mainpage_frame.setMaximumSize(QtCore.QSize(1000, 600))
        self.mainpage_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.mainpage_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.mainpage_frame.setObjectName("mainpage_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.mainpage_frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.sidebar = QtWidgets.QFrame(self.mainpage_frame)
        self.sidebar.setMinimumSize(QtCore.QSize(250, 596))
        self.sidebar.setMaximumSize(QtCore.QSize(450, 16777215))
        self.sidebar.setStyleSheet("background-color:rgba(32, 53, 52, 220);\n"
                                   "border: 1px solid rgb(32, 53, 52);\n"
                                   "border-top-right-radius: 10px;\n"
                                   "border-bottom-right-radius: 10px;")
        self.sidebar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.sidebar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.sidebar.setObjectName("sidebar")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.sidebar)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 60)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.b_info = QtWidgets.QPushButton(self.sidebar)
        self.b_info.setMaximumSize(QtCore.QSize(150, 100))
        self.b_info.setStyleSheet("QPushButton{\n"
                                  "    border: 0px solid green ;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "    border-bottom: 2px solid rgba(0, 255, 0, 10);\n"
                                  "}\n"
                                  "QPushButton:pressed{\n"
                                  "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                  "}\n"
                                  "")
        self.b_info.setText("")
        self.b_info.setIcon(icon)
        self.b_info.setIconSize(QtCore.QSize(100, 100))
        self.b_info.setFlat(True)
        self.b_info.setObjectName("b_info")
        self.verticalLayout_6.addWidget(self.b_info)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 80)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.tb_search = QtWidgets.QPlainTextEdit(self.sidebar)
        self.tb_search.setMinimumSize(QtCore.QSize(220, 0))
        self.tb_search.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tb_search.setFont(font)
        self.tb_search.setStyleSheet("QPlainTextEdit{\n"
                                     "    border-top:2px solid #0C8040;\n"
                                     "    border-bottom:2px solid #0C8040;\n"
                                     "    border-left:2px solid #0C8040;\n"
                                     "    border-top-left-radius: 15px;\n"
                                     "    border-bottom-left-radius: 15px;\n"
                                     "    color: #72AE74\n"
                                     "}\n"
                                     "\n"
                                     "QPlainTextEdit:hover{\n"
                                     "    color:rgb(0, 0, 0);\n"
                                     "    border-color: black;\n"
                                     "}\n"
                                     "")
        self.tb_search.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tb_search.setObjectName("tb_search")
        self.horizontalLayout_11.addWidget(self.tb_search)
        self.b_search = QtWidgets.QPushButton(self.sidebar)
        self.b_search.setStyleSheet("QPushButton{\n"
                                    "    border:2px solid #0C8040;\n"
                                    "    border-top-right-radius: 15px;\n"
                                    "    border-bottom-right-radius: 15px;\n"
                                    "    color: #72AE74\n"
                                    "}QPushButton:hover{\n"
                                    "    color: rgba(170, 255, 127,255);\n"
                                    "}QPushButton:pressed{\n"
                                    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                    "}")
        self.b_search.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/search/Search.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.b_search.setIcon(icon6)
        self.b_search.setIconSize(QtCore.QSize(40, 36))
        self.b_search.setObjectName("b_search")
        self.horizontalLayout_11.addWidget(self.b_search)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.b_allItems = QtWidgets.QPushButton(self.sidebar)
        self.b_allItems.setMaximumSize(QtCore.QSize(269, 48))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.b_allItems.setFont(font)
        self.b_allItems.setMouseTracking(True)
        self.b_allItems.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.b_allItems.setAutoFillBackground(False)
        self.b_allItems.setStyleSheet("QPushButton{\n"
                                      "    border: 0px solid green ;\n"
                                      "    color: rgba(170, 255, 127,190);\n"
                                      "}QPushButton:hover{\n"
                                      "    border-bottom: 2px solid rgba(0, 255, 0, 10);\n"
                                      "    color: rgba(170, 255, 127,255);\n"
                                      "}QPushButton:pressed{\n"
                                      "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,                                     stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                      "}\n"
                                      "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/hamburger/Hamburger.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.b_allItems.setIcon(icon7)
        self.b_allItems.setIconSize(QtCore.QSize(40, 40))
        self.b_allItems.setFlat(True)
        self.b_allItems.setObjectName("b_allItems")
        self.verticalLayout_6.addWidget(self.b_allItems, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.b_addNew = QtWidgets.QPushButton(self.sidebar)
        self.b_addNew.setMaximumSize(QtCore.QSize(269, 48))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.b_addNew.setFont(font)
        self.b_addNew.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.b_addNew.setAutoFillBackground(False)
        self.b_addNew.setStyleSheet("QPushButton{\n"
                                    "    border: 0px solid green ;\n"
                                    "    color: rgba(170, 255, 127,190);\n"
                                    "}QPushButton:hover{\n"
                                    "    border-bottom: 2px solid rgba(0, 255, 0, 10);\n"
                                    "    color: rgba(170, 255, 127,255);\n"
                                    "}QPushButton:pressed{\n"
                                    "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,                                     stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                    "}\n"
                                    "")
        self.b_addNew.setIcon(icon5)
        self.b_addNew.setIconSize(QtCore.QSize(40, 40))
        self.b_addNew.setFlat(True)
        self.b_addNew.setObjectName("b_addNew")
        self.verticalLayout_6.addWidget(self.b_addNew, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.b_sync = QtWidgets.QPushButton(self.sidebar)
        self.b_sync.setMaximumSize(QtCore.QSize(269, 48))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.b_sync.setFont(font)
        self.b_sync.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.b_sync.setAutoFillBackground(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/sync/Sync.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.b_sync.setIcon(icon8)
        self.b_sync.setIconSize(QtCore.QSize(40, 40))
        self.b_sync.setFlat(True)
        self.b_sync.setObjectName("b_sync")
        self.verticalLayout_6.addWidget(self.b_sync, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.b_bandr = QtWidgets.QPushButton(self.sidebar)
        self.b_bandr.setMaximumSize(QtCore.QSize(269, 48))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.b_bandr.setFont(font)
        self.b_bandr.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.b_bandr.setAutoFillBackground(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/bandr/Backup And restore.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.b_bandr.setIcon(icon9)
        self.b_bandr.setIconSize(QtCore.QSize(40, 40))
        self.b_bandr.setFlat(True)
        self.b_bandr.setObjectName("b_bandr")
        self.verticalLayout_6.addWidget(self.b_bandr, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.b_generatenew = QtWidgets.QPushButton(self.sidebar)
        self.b_generatenew.setMaximumSize(QtCore.QSize(269, 48))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.b_generatenew.setFont(font)
        self.b_generatenew.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.b_generatenew.setAutoFillBackground(False)
        self.b_generatenew.setStyleSheet("QPushButton{\n"
                                         "    border: 0px solid green ;\n"
                                         "    color: rgba(170, 255, 127,190);\n"
                                         "}QPushButton:hover{\n"
                                         "    border-bottom: 2px solid rgba(0, 255, 0, 10);\n"
                                         "    color: rgba(170, 255, 127,255);\n"
                                         "}QPushButton:pressed{\n"
                                         "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,                                     stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                         "}\n"
                                         "")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/generate/Generate.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.b_generatenew.setIcon(icon10)
        self.b_generatenew.setIconSize(QtCore.QSize(40, 40))
        self.b_generatenew.setFlat(True)
        self.b_generatenew.setObjectName("b_generatenew")
        self.verticalLayout_6.addWidget(self.b_generatenew, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_12.addLayout(self.verticalLayout_6)
        self.horizontalLayout_8.addWidget(self.sidebar)
        self.mainbox = QtWidgets.QVBoxLayout()
        self.mainbox.setObjectName("mainbox")
        self.topframe = QtWidgets.QFrame(self.mainpage_frame)
        self.topframe.setMinimumSize(QtCore.QSize(744, 100))
        self.topframe.setMaximumSize(QtCore.QSize(744, 100))
        self.topframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.topframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.topframe.setObjectName("topframe")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.topframe)
        self.horizontalLayout_14.setContentsMargins(670, 0, 0, 60)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(1)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.b_minimize_3 = QtWidgets.QPushButton(self.topframe)
        self.b_minimize_3.setMinimumSize(QtCore.QSize(30, 20))
        self.b_minimize_3.setMaximumSize(QtCore.QSize(40, 25))
        self.b_minimize_3.setStyleSheet("background-color:#203534")
        self.b_minimize_3.setText("")
        self.b_minimize_3.setIcon(icon1)
        self.b_minimize_3.setIconSize(QtCore.QSize(16, 16))
        self.b_minimize_3.setFlat(True)
        self.b_minimize_3.setObjectName("b_minimize_3")
        self.horizontalLayout_13.addWidget(self.b_minimize_3)
        self.b_close_3 = QtWidgets.QPushButton(self.topframe)
        self.b_close_3.setMinimumSize(QtCore.QSize(30, 20))
        self.b_close_3.setMaximumSize(QtCore.QSize(40, 25))
        self.b_close_3.setStyleSheet("QPushButton{\n"
                                     "    border: 0px solid green ;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "    background-color:rgba(255, 0, 0, 180)\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1 stop: 0 rgba(255, 0, 0, 180), stop: 1 rgba(255, 0, 0, 140));\n"
                                     "}\n"
                                     "")
        self.b_close_3.setText("")
        self.b_close_3.setIcon(icon2)
        self.b_close_3.setFlat(True)
        self.b_close_3.setObjectName("b_close_3")
        self.horizontalLayout_13.addWidget(self.b_close_3)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_13)
        self.mainbox.addWidget(self.topframe)
        self.maininfo = QtWidgets.QFrame(self.mainpage_frame)
        self.maininfo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.maininfo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.maininfo.setObjectName("maininfo")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.maininfo)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.stackedWidget_main = QtWidgets.QStackedWidget(self.maininfo)
        self.stackedWidget_main.setMinimumSize(QtCore.QSize(742, 486))
        self.stackedWidget_main.setMaximumSize(QtCore.QSize(742, 486))
        self.stackedWidget_main.setStyleSheet("border-radius: 10px")
        self.stackedWidget_main.setObjectName("stackedWidget_main")
        self.all_items = QtWidgets.QWidget()
        self.all_items.setObjectName("all_items")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.all_items)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.scrollArea = QtWidgets.QScrollArea(self.all_items)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 722, 466))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setMinimumSize(QtCore.QSize(704, 448))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableView{\n"
                                       "    background-color: rgb(37, 37, 37);\n"
                                       "    alternate-background-color: rgb(37, 42, 37);\n"
                                       "    selection-background-color: rgba(170, 255, 127,30);\n"
                                       "    grid-line:2px solid  rgb(114, 174, 116);\n"
                                       "    color:rgb(114, 174, 116);\n"
                                       "}QHeaderView::section{\n"
                                       "    background-color:rgb(39, 37, 37);\n"
                                       "    border-style:none;\n"
                                       "    border-bottom:1px solid rgb(114, 174, 116);\n"
                                       "}QTableView::item{\n"
                                       "    border-bottom:1px solid rgb(114, 174, 116);\n"
                                       "} QScrollBar:vertical {\n"
                                       "    margin: 22px 0 22px 0;\n"
                                       "    border: 1px solid rgb(114, 174, 116);\n"
                                       "    border-radius:6px;\n"
                                       "    background: rgba(56, 102, 84, 140);\n"
                                       "    width: 16px;\n"
                                       "}QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                       "    background: none;\n"
                                       "} QScrollBar::handle:vertical {\n"
                                       "    background:#72ae74;\n"
                                       "    border: 1px solid #72ae74;\n"
                                       "    border-radius:6px;\n"
                                       "    min-height: 10px;\n"
                                       "    max-height:10px;\n"
                                       "}QScrollBar::add-line:vertical {\n"
                                       "    width: 0px;\n"
                                       "    height: 0px;\n"
                                       "}QScrollBar::sub-line:vertical {\n"
                                       "    width: 0px;\n"
                                       "    height: 0px;\n"
                                       "}QHeaderView::down-arrow {\n"
                                       "    color:lime;\n"
                                       "    subcontrol-position: center right;\n"
                                       "    image:url(:/downarrow/down_arrow.svg);\n"
                                       "    width: 15px;\n"
                                       "    height:15px;\n"
                                       "}QHeaderView::up-arrow {\n"
                                       "    color:lime;\n"
                                       "    subcontrol-position: center right;\n"
                                       "    image:url(:/uparrow/up_arrow.svg);\n"
                                       "    width: 15px;\n"
                                       "    height:15px;\n}"
                                       "")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.DashDotLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        self.tableWidget.setColumnWidth(0, 340)
        self.tableWidget.setColumnWidth(1, 300)
        self.tableWidget.setColumnWidth(2, 70)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(114, 174, 116, 190))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(114, 174, 116, 190))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(300)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(120)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(70)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(70)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_17.addWidget(self.tableWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_14.addWidget(self.scrollArea)
        self.verticalLayout_15.addLayout(self.verticalLayout_14)
        self.stackedWidget_main.addWidget(self.all_items)
        self.add_new = QtWidgets.QWidget()
        self.add_new.setObjectName("add_new")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.add_new)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, 100, -1, 100)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.add_new)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: 2 px solid rgb(56, 102, 84);\n"
                                   "border-bottom: 2 px solid rgb(56, 102, 84);\n"
                                   "color: rgba(170, 255, 127,190);\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.tb_add_new_title = QtWidgets.QPlainTextEdit(self.add_new)
        self.tb_add_new_title.setMinimumSize(QtCore.QSize(0, 40))
        self.tb_add_new_title.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tb_add_new_title.setFont(font)
        self.tb_add_new_title.setStyleSheet("QPlainTextEdit{\n"
                                            "    border-top:2px solid #0C8040;\n"
                                            "    border-bottom:2px solid #0C8040;\n"
                                            "    border-left:2px solid #0C8040;\n"
                                            "    border-right:2px solid #0C8040;\n"
                                            "    border-top-left-radius: 15px;\n"
                                            "    border-bottom-left-radius: 15px;\n"
                                            "    border-top-right-radius: 15px;\n"
                                            "    border-bottom-right-radius: 15px;\n"
                                            "    color: #72AE74\n"
                                            "}\n"
                                            "\n"
                                            "QPlainTextEdit:hover{\n"
                                            "    color:rgb(0, 0, 0);\n"
                                            "    border-color: black;\n"
                                            "}\n"
                                            "")
        self.tb_add_new_title.setTabChangesFocus(True)
        self.tb_add_new_title.setObjectName("tb_add_new_title")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tb_add_new_title)
        self.url = QtWidgets.QLabel(self.add_new)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.url.setFont(font)
        self.url.setStyleSheet("border: 2 px solid rgb(56, 102, 84);\n"
                               "border-bottom: 2 px solid rgb(56, 102, 84);\n"
                               "color: rgba(170, 255, 127,190);\n"
                               "")
        self.url.setObjectName("url")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.url)
        self.tb_add_new_url = QtWidgets.QPlainTextEdit(self.add_new)
        self.tb_add_new_url.setMinimumSize(QtCore.QSize(0, 40))
        self.tb_add_new_url.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tb_add_new_url.setFont(font)
        self.tb_add_new_url.setStyleSheet("QPlainTextEdit{\n"
                                          "    border-top:2px solid #0C8040;\n"
                                          "    border-bottom:2px solid #0C8040;\n"
                                          "    border-left:2px solid #0C8040;\n"
                                          "    border-right:2px solid #0C8040;\n"
                                          "    border-top-left-radius: 15px;\n"
                                          "    border-bottom-left-radius: 15px;\n"
                                          "    border-top-right-radius: 15px;\n"
                                          "    border-bottom-right-radius: 15px;\n"
                                          "    color: #72AE74\n"
                                          "}\n"
                                          "\n"
                                          "QPlainTextEdit:hover{\n"
                                          "    color:rgb(0, 0, 0);\n"
                                          "    border-color: black;\n"
                                          "}\n"
                                          "")
        self.tb_add_new_url.setTabChangesFocus(True)
        self.tb_add_new_url.setObjectName("tb_add_new_url")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tb_add_new_url)
        self.username = QtWidgets.QLabel(self.add_new)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.username.setFont(font)
        self.username.setStyleSheet("border: 2 px solid rgb(56, 102, 84);\n"
                                    "border-bottom: 2 px solid rgb(56, 102, 84);\n"
                                    "color: rgba(170, 255, 127,190);\n"
                                    "")
        self.username.setObjectName("username")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.username)
        self.tb_add_new_uname = QtWidgets.QPlainTextEdit(self.add_new)
        self.tb_add_new_uname.setMinimumSize(QtCore.QSize(0, 40))
        self.tb_add_new_uname.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tb_add_new_uname.setFont(font)
        self.tb_add_new_uname.setStyleSheet("QPlainTextEdit{\n"
                                            "    border-top:2px solid #0C8040;\n"
                                            "    border-bottom:2px solid #0C8040;\n"
                                            "    border-left:2px solid #0C8040;\n"
                                            "    border-right:2px solid #0C8040;\n"
                                            "    border-top-left-radius: 15px;\n"
                                            "    border-bottom-left-radius: 15px;\n"
                                            "    border-top-right-radius: 15px;\n"
                                            "    border-bottom-right-radius: 15px;\n"
                                            "    color: #72AE74\n"
                                            "}\n"
                                            "\n"
                                            "QPlainTextEdit:hover{\n"
                                            "    color:rgb(0, 0, 0);\n"
                                            "    border-color: black;\n"
                                            "}\n"
                                            "")
        self.tb_add_new_uname.setTabChangesFocus(True)
        self.tb_add_new_uname.setObjectName("tb_add_new_uname")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tb_add_new_uname)
        self.label_14 = QtWidgets.QLabel(self.add_new)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("border: 2 px solid rgb(56, 102, 84);\n"
                                    "border-bottom: 2 px solid rgb(56, 102, 84);\n"
                                    "color: rgba(170, 255, 127,190);\n"
                                    "")
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_14)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.tb_mkey_3 = QtWidgets.QLineEdit(self.add_new)
        self.tb_mkey_3.setMinimumSize(QtCore.QSize(520, 40))
        self.tb_mkey_3.setMaximumSize(QtCore.QSize(530, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tb_mkey_3.setFont(font)
        self.tb_mkey_3.setStyleSheet("QLineEdit{\n"
                                     "    border:2px solid #0C8040;\n"
                                     "    border-top-left-radius: 15px;\n"
                                     "    border-bottom-left-radius: 15px;\n"
                                     "    color: #72AE74\n"
                                     "}\n"
                                     "\n"
                                     "QLineEdit:hover{\n"
                                     "    color:rgb(0, 0, 0);\n"
                                     "    border-color: black;\n"
                                     "}\n"
                                     "")
        self.tb_mkey_3.setText("")
        self.tb_mkey_3.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.tb_mkey_3.setObjectName("tb_mkey_3")
        self.horizontalLayout_22.addWidget(self.tb_mkey_3)
        self.b_pwToggle_3 = QtWidgets.QPushButton(self.add_new)
        self.b_pwToggle_3.setMinimumSize(QtCore.QSize(40, 40))
        self.b_pwToggle_3.setStyleSheet("QPushButton{\n"
                                        "    border:2px solid #0C8040;\n"
                                        "    border-top-right-radius: 15px;\n"
                                        "    border-bottom-right-radius: 15px;\n"
                                        "    color: #72AE74;\n"
                                        "    icon:url(:/hidden/Hidden.svg)\n"
                                        "}QPushButton:hover{\n"
                                        "    border: 2px solid    #72AE74;\n"
                                        "    color: #72AE74 ;\n"
                                        "}QPushButton:checked{\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1 stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                        "    icon:url(:/plain/plain.svg);\n"
                                        "}")
        self.b_pwToggle_3.setText("")
        self.b_pwToggle_3.setIconSize(QtCore.QSize(40, 40))
        self.b_pwToggle_3.setObjectName("b_pwToggle_3")
        self.b_pwToggle_3.setCheckable(True)
        self.b_pwToggle_3.setChecked(False)
        self.horizontalLayout_22.addWidget(self.b_pwToggle_3)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_22)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.l_addpage = QtWidgets.QLabel(self.add_new)
        self.l_addpage.setMinimumSize(QtCore.QSize(447, 40))
        self.l_addpage.setMaximumSize(QtCore.QSize(447, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.l_addpage.setFont(font)
        self.l_addpage.setStyleSheet("border: 2 px solid rgb(56, 102, 84);\n"
                                     "border-bottom: 2 px solid rgb(56, 102, 84);\n"
                                     "color: rgba(170, 255, 127,190);\n"
                                     "")
        self.l_addpage.setText("")
        self.l_addpage.setObjectName("l_addpage")
        self.horizontalLayout_21.addWidget(self.l_addpage)
        self.b_add_newa_dd = QtWidgets.QPushButton(self.add_new)
        self.b_add_newa_dd.setMinimumSize(QtCore.QSize(120, 40))
        self.b_add_newa_dd.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.b_add_newa_dd.setFont(font)
        self.b_add_newa_dd.setStyleSheet("QPushButton{\n"
                                         "    border-top:2px solid #0C8040;\n"
                                         "    border-bottom:2px solid #0C8040;\n"
                                         "    border-left:2px solid #0C8040;    \n"
                                         "    border-right:2px solid #0C8040;    \n"
                                         "    border-top-right-radius: 15px;\n"
                                         "    border-top-left-radius: 15px;\n"
                                         "    border-bottom-right-radius: 15px;\n"
                                         "    border-bottom-left-radius: 15px;\n"
                                         "    color: rgba(170, 255, 127,190);\n"
                                         "}QPushButton:hover{\n"
                                         "    color: rgba(170, 255, 127,255);\n"
                                         "}QPushButton:pressed{\n"
                                         "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,                                     stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                         "}")
        self.b_add_newa_dd.setObjectName("b_add_newa_dd")
        self.horizontalLayout_21.addWidget(self.b_add_newa_dd)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_21)
        self.verticalLayout_12.addLayout(self.formLayout)
        self.stackedWidget_main.addWidget(self.add_new)
        self.sync = QtWidgets.QWidget()
        self.sync.setObjectName("sync")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.sync)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label = QtWidgets.QLabel(self.sync)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_20.addWidget(self.label)
        self.stackedWidget_main.addWidget(self.sync)
        self.bandr = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(18)
        self.bandr.setFont(font)
        self.bandr.setObjectName("bandr")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.bandr)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.bandr)
        self.label_4.setMinimumSize(QtCore.QSize(0, 150))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("    color: rgba(170, 255, 127,190);\n"
                                   "")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_10.addWidget(self.label_4)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setContentsMargins(-1, -1, -1, 50)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_3 = QtWidgets.QLabel(self.bandr)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
                                   "    border:2px solid #0C8040;\n"
                                   "    border-radius:15px;\n"
                                   "    color: rgba(170, 255, 127,190);\n"
                                   "}QLabel:hover{\n"
                                   "    color: rgba(170, 255, 127,190);\n"
                                   "    border-color: black;\n"
                                   "}\n"
                                   "")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_17.addWidget(self.label_3)
        self.file_browser = QtWidgets.QPushButton(self.bandr)
        self.file_browser.setMinimumSize(QtCore.QSize(120, 40))
        self.file_browser.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.file_browser.setFont(font)
        self.file_browser.setStyleSheet("QPushButton{\n"
                                        "    border:2px solid #0C8040;\n"
                                        "    border-radius: 15px;\n"
                                        "    color: #72AE74\n"
                                        "}QPushButton:hover{\n"
                                        "    color: rgba(170, 255, 127,255);\n"
                                        "    border-color: black;\n"
                                        "}QPushButton:pressed{\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                        "}")
        self.file_browser.setObjectName("file_browser")
        self.horizontalLayout_17.addWidget(self.file_browser)
        self.verticalLayout_19.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_10 = QtWidgets.QLabel(self.bandr)
        self.label_10.setMinimumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("    color: rgba(170, 255, 127,190);\n"
                                    "")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_20.addWidget(self.label_10, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.b_bandr_pman_toggle = QtWidgets.QPushButton(self.bandr)
        self.b_bandr_pman_toggle.setMinimumSize(QtCore.QSize(40, 40))
        self.b_bandr_pman_toggle.setMaximumSize(QtCore.QSize(125, 40))
        self.b_bandr_pman_toggle.setStyleSheet("QPushButton{\n"
                                               "    icon:url(:/toggle_off/toggle_off.svg)\n"
                                               "}QPushButton:checked{\n"
                                               "    icon:url(:/toggle_on/toggle_on.svg)\n"
                                               "}")
        self.b_bandr_pman_toggle.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/toggle_off/toggle_off.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.b_bandr_pman_toggle.setIcon(icon11)
        self.b_bandr_pman_toggle.setIconSize(QtCore.QSize(35, 35))
        self.b_bandr_pman_toggle.setCheckable(True)
        self.b_bandr_pman_toggle.setFlat(True)
        self.b_bandr_pman_toggle.setObjectName("b_bandr_pman_toggle")
        self.horizontalLayout_20.addWidget(self.b_bandr_pman_toggle, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_19.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_5 = QtWidgets.QLabel(self.bandr)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border: 2 px solid rgb(56, 102, 84);\n"
                                   "border-bottom: 2 px solid rgb(56, 102, 84);\n"
                                   "color: rgba(170, 255, 127,190);\n"
                                   "")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_25.addWidget(self.label_5)
        self.b_bandr_restore = QtWidgets.QPushButton(self.bandr)
        self.b_bandr_restore.setMinimumSize(QtCore.QSize(120, 40))
        self.b_bandr_restore.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.b_bandr_restore.setFont(font)
        self.b_bandr_restore.setStyleSheet("QPushButton{\n"
                                          "    border:2px solid #0C8040;\n"
                                          "    border-radius: 15px;\n"
                                          "    color: #72AE74\n"
                                          "}QPushButton:hover{\n"
                                          "    color: rgba(170, 255, 127,255);\n"
                                          "    border-color: black;\n"
                                          "}QPushButton:pressed{\n"
                                          "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                          "}")
        self.b_bandr_restore.setObjectName("file_browser_2")
        self.horizontalLayout_25.addWidget(self.b_bandr_restore)
        self.verticalLayout_19.addLayout(self.horizontalLayout_25)
        self.label_11 = QtWidgets.QLabel(self.bandr)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("    color: rgba(170, 255, 127,190);\n"
                                    "")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_19.addWidget(self.label_11)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.l_bandr_b1 = QtWidgets.QLabel(self.bandr)
        self.l_bandr_b1.setMinimumSize(QtCore.QSize(0, 40))
        self.l_bandr_b1.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.l_bandr_b1.setFont(font)
        self.l_bandr_b1.setAutoFillBackground(False)
        self.l_bandr_b1.setStyleSheet("QLabel{\n"
                                      "    border:2px solid #0C8040;\n"
                                      "    border-radius:15px;\n"
                                      "    color: #72AE74;\n"
                                      "}QLabel:hover{\n"
                                      "    color: #72AE74;\n"
                                      "    border-color: black;\n"
                                      "}\n"
                                      "")
        self.l_bandr_b1.setObjectName("l_bandr_b1")
        self.horizontalLayout_18.addWidget(self.l_bandr_b1)
        self.file_browser_3 = QtWidgets.QPushButton(self.bandr)
        self.file_browser_3.setMinimumSize(QtCore.QSize(120, 40))
        self.file_browser_3.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.file_browser_3.setFont(font)
        self.file_browser_3.setStyleSheet("QPushButton{\n"
                                          "    border:2px solid #0C8040;\n"
                                          "    border-radius: 15px;\n"
                                          "    color: #72AE74\n"
                                          "}QPushButton:hover{\n"
                                          "    color: rgba(170, 255, 127,255);\n"
                                          "    border-color: black;\n"
                                          "}QPushButton:pressed{\n"
                                          "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                          "}")
        self.file_browser_3.setObjectName("file_browser_3")
        self.horizontalLayout_18.addWidget(self.file_browser_3)
        self.verticalLayout_19.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_16 = QtWidgets.QLabel(self.bandr)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_16.setFont(font)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_26.addWidget(self.label_16)
        self.b_band_backup = QtWidgets.QPushButton(self.bandr)
        self.b_band_backup.setMinimumSize(QtCore.QSize(120, 40))
        self.b_band_backup.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.b_band_backup.setFont(font)
        self.b_band_backup.setStyleSheet("QPushButton{\n"
                                         "    border:2px solid #0C8040;\n"
                                         "    border-radius: 15px;\n"
                                         "    color: #72AE74\n"
                                         "}QPushButton:hover{\n"
                                         "    color: rgba(170, 255, 127,255);\n"
                                         "    border-color: black;\n"
                                         "}QPushButton:pressed{\n"
                                         "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                         "}")
        self.b_band_backup.setObjectName("b_band_backup")
        self.horizontalLayout_26.addWidget(self.b_band_backup)
        self.verticalLayout_19.addLayout(self.horizontalLayout_26)
        self.verticalLayout_10.addLayout(self.verticalLayout_19)
        self.stackedWidget_main.addWidget(self.bandr)
        self.new_password = QtWidgets.QWidget()
        self.new_password.setObjectName("new_password")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.new_password)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(15, -1, 15, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.textEdit_2 = QtWidgets.QTextEdit(self.new_password)
        self.textEdit_2.setMinimumSize(QtCore.QSize(712, 150))
        self.textEdit_2.setMaximumSize(QtCore.QSize(712, 150))
        self.textEdit_2.setAutoFillBackground(False)
        self.textEdit_2.setStyleSheet("border: 2 px solid rgb(56, 102, 84);\n"
                                      "border-bottom: 2 px solid rgb(56, 102, 84);\n"
                                      "color: rgba(170, 255, 127,190);\n"
                                      "background-color:rgba(170, 255, 127,20)\n"
                                      "")
        self.textEdit_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_2.setUndoRedoEnabled(False)
        self.textEdit_2.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.WidgetWidth)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_8.addWidget(self.textEdit_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(15, -1, 0, 60)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gen_cap_symbol = QtWidgets.QPushButton(self.new_password)
        self.gen_cap_symbol.setMaximumSize(QtCore.QSize(80, 40))
        self.gen_cap_symbol.setStyleSheet("QPushButton{\n"
                                          "    icon:url(:/toggle_off/toggle_off.svg)\n"
                                          "}QPushButton:checked{\n"
                                          "    icon:url(:/toggle_on/toggle_on.svg)\n"
                                          "}")
        self.gen_cap_symbol.setText("")
        self.gen_cap_symbol.setIcon(icon11)
        self.gen_cap_symbol.setIconSize(QtCore.QSize(30, 30))
        self.gen_cap_symbol.setCheckable(True)
        self.gen_cap_symbol.setChecked(True)
        self.gen_cap_symbol.setFlat(True)
        self.gen_cap_symbol.setObjectName("gen_cap_symbol")
        self.gridLayout_3.addWidget(self.gen_cap_symbol, 3, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(200, -1, 0, -1)
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.h_slider = QtWidgets.QSlider(self.new_password)
        self.h_slider.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.h_slider.setFont(font)
        self.h_slider.setStyleSheet("QSlider::groove:horizontal { \n"
                                    "    background-color:  rgba(56, 102, 84, 140);\n"
                                    "    border: 0px solid #424242; \n"
                                    "    height:10px; \n"
                                    "    border-radius: 4px;\n"
                                    "}QSlider::handle:horizontal { \n"
                                    "    background-color: rgba(170, 255, 127,190); \n"
                                    "    border: 2px solid rgba(170, 255, 127,190);; \n"
                                    "    width: 16px; \n"
                                    "    height: 16px; \n"
                                    "    line-height: 16px; \n"
                                    "    margin-top: -5px; \n"
                                    "    margin-bottom: -5px; \n"
                                    "    border-radius: 10px; \n"
                                    "}QSlider::handle:horizontal:hover { \n"
                                    "    border-radius: 10px;\n"
                                    "}")
        self.h_slider.setMinimum(8)
        self.h_slider.setMaximum(60)
        self.h_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.h_slider.setTickPosition(QtWidgets.QSlider.TickPosition.NoTicks)
        self.h_slider.setObjectName("h_slider")
        self.horizontalLayout_15.addWidget(self.h_slider)
        self.length_slider = QtWidgets.QLabel(self.new_password)
        self.length_slider.setMinimumSize(QtCore.QSize(26, 32))
        self.length_slider.setMaximumSize(QtCore.QSize(26, 32))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.length_slider.setFont(font)
        self.length_slider.setStyleSheet("color: rgba(170, 255, 127,190);\n"
                                         "")
        self.length_slider.setObjectName("length_slider")
        self.horizontalLayout_15.addWidget(self.length_slider)
        self.gridLayout_3.addLayout(self.horizontalLayout_15, 0, 2, 1, 1)
        self.gen_cap_numeric = QtWidgets.QPushButton(self.new_password)
        self.gen_cap_numeric.setMaximumSize(QtCore.QSize(80, 40))
        self.gen_cap_numeric.setStyleSheet("QPushButton{\n"
                                           "    icon:url(:/toggle_off/toggle_off.svg)\n"
                                           "}QPushButton:checked{\n"
                                           "    icon:url(:/toggle_on/toggle_on.svg)\n"
                                           "}")
        self.gen_cap_numeric.setText("")
        self.gen_cap_numeric.setIcon(icon11)
        self.gen_cap_numeric.setIconSize(QtCore.QSize(30, 30))
        self.gen_cap_numeric.setCheckable(True)
        self.gen_cap_numeric.setChecked(True)
        self.gen_cap_numeric.setFlat(True)
        self.gen_cap_numeric.setObjectName("gen_cap_numeric")
        self.gridLayout_3.addWidget(self.gen_cap_numeric, 2, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gen_cap_letters = QtWidgets.QPushButton(self.new_password)
        self.gen_cap_letters.setMaximumSize(QtCore.QSize(80, 40))
        self.gen_cap_letters.setStyleSheet("QPushButton{\n"
                                           "    icon:url(:/toggle_off/toggle_off.svg)\n"
                                           "}QPushButton:checked{\n"
                                           "    icon:url(:/toggle_on/toggle_on.svg)\n"
                                           "}")
        self.gen_cap_letters.setText("")
        self.gen_cap_letters.setIcon(icon11)
        self.gen_cap_letters.setIconSize(QtCore.QSize(30, 30))
        self.gen_cap_letters.setCheckable(True)
        self.gen_cap_letters.setChecked(True)
        self.gen_cap_letters.setFlat(True)
        self.gen_cap_letters.setObjectName("gen_cap_letters")
        self.gridLayout_3.addWidget(self.gen_cap_letters, 1, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.label_6 = QtWidgets.QLabel(self.new_password)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border: 2 px solid rgb(56, 102, 84);\n"
                                   "border-bottom: 2 px solid rgb(56, 102, 84);\n"
                                   "color: rgba(170, 255, 127,190);\n"
                                   "")
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.new_password)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border: 2 px solid rgb(56, 102, 84);\n"
                                   "border-bottom: 2 px solid rgb(56, 102, 84);\n"
                                   "color: rgba(170, 255, 127,190);\n"
                                   "")
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.new_password)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border: 2 px solid rgb(56, 102, 84);\n"
                                   "border-bottom: 2 px solid rgb(56, 102, 84);\n"
                                   "color: rgba(170, 255, 127,190);\n"
                                   "")
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.new_password)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border: 2 px solid rgb(56, 102, 84);\n"
                                   "border-bottom: 2 px solid rgb(56, 102, 84);\n"
                                   "color: rgba(170, 255, 127,190);\n"
                                   "")
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.b_gen_generate_now = QtWidgets.QPushButton(self.new_password)
        self.b_gen_generate_now.setMinimumSize(QtCore.QSize(150, 40))
        self.b_gen_generate_now.setMaximumSize(QtCore.QSize(180, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.b_gen_generate_now.setFont(font)
        self.b_gen_generate_now.setStyleSheet("QPushButton{\n"
                                              "    border-top:2px solid #0C8040;\n"
                                              "    border-bottom:2px solid #0C8040;\n"
                                              "    border-left:2px solid #0C8040;    \n"
                                              "    border-right:2px solid #0C8040;    \n"
                                              "    border-top-right-radius: 15px;\n"
                                              "    border-top-left-radius: 15px;\n"
                                              "    border-bottom-right-radius: 15px;\n"
                                              "    border-bottom-left-radius: 15px;\n"
                                              "    color: rgba(170, 255, 127,190);\n"
                                              "}QPushButton:hover{\n"
                                              "    color: rgba(170, 255, 127,255);\n"
                                              "}QPushButton:pressed{\n"
                                              "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,                                     stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                              "}")
        self.b_gen_generate_now.setObjectName("b_gen_generate_now")
        self.horizontalLayout_23.addWidget(self.b_gen_generate_now, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout_3.addLayout(self.horizontalLayout_23, 4, 2, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_3)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.stackedWidget_main.addWidget(self.new_password)
        self.info_page = QtWidgets.QWidget()
        self.info_page.setObjectName("info_page")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.info_page)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(-1, 50, -1, 90)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_13 = QtWidgets.QLabel(self.info_page)
        self.label_13.setMinimumSize(QtCore.QSize(130, 50))
        self.label_13.setMaximumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("border: 2 px solid rgb(56, 102, 84);\n"
                                    "border-bottom: 2 px solid rgb(56, 102, 84);\n"
                                    "color: rgba(170, 255, 127,190);\n"
                                    "")
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 2, 0, 1, 1)
        self.l_uname_info = QtWidgets.QLabel(self.info_page)
        self.l_uname_info.setMinimumSize(QtCore.QSize(506, 50))
        self.l_uname_info.setMaximumSize(QtCore.QSize(506, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.l_uname_info.setFont(font)
        self.l_uname_info.setStyleSheet("color: #72AE74\n"
                                        "")
        self.l_uname_info.setOpenExternalLinks(False)
        self.l_uname_info.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse | QtCore.Qt.TextInteractionFlag.TextEditable | QtCore.Qt.TextInteractionFlag.TextEditorInteraction | QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard | QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.l_uname_info.setObjectName("l_uname_info")
        self.gridLayout_4.addWidget(self.l_uname_info, 2, 2, 1, 1)
        self.b_hid1 = QtWidgets.QPushButton(self.info_page)
        self.b_hid1.setMinimumSize(QtCore.QSize(40, 40))
        self.b_hid1.setMaximumSize(QtCore.QSize(50, 50))
        self.b_hid1.setStyleSheet("QPushButton{\n"
                                  "    border:2px solid #0C8040;\n"
                                  "    border-radius: 15px;\n"
                                  "    color: #72AE74;\n"
                                  "    icon:url(:/hidden/Hidden.svg)\n"
                                  "}QPushButton:hover{\n"
                                  "    border: 2px solid    #72AE74;\n"
                                  "    color: #72AE74 ;\n"
                                  "}QPushButton:checked{\n"
                                  "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1 stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                  "    icon:url(:/plain/plain.svg);\n"
                                  "}")
        self.b_hid1.setText("")
        self.b_hid1.setIcon(icon3)
        self.b_hid1.setIconSize(QtCore.QSize(40, 40))
        self.b_hid1.setCheckable(True)
        self.b_hid1.setChecked(False)
        self.b_hid1.setObjectName("b_hid1")
        self.gridLayout_4.addWidget(self.b_hid1, 2, 3, 1, 1)
        self.l_url_info = QtWidgets.QLabel(self.info_page)
        self.l_url_info.setMinimumSize(QtCore.QSize(506, 50))
        self.l_url_info.setMaximumSize(QtCore.QSize(506, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.l_url_info.setFont(font)
        self.l_url_info.setStyleSheet("color: #72AE74\n"
                                      "")
        self.l_url_info.setOpenExternalLinks(False)
        self.l_url_info.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse | QtCore.Qt.TextInteractionFlag.TextEditable | QtCore.Qt.TextInteractionFlag.TextEditorInteraction | QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard | QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.l_url_info.setObjectName("l_url_info")
        self.gridLayout_4.addWidget(self.l_url_info, 1, 2, 1, 1)
        self.b_ex_open = QtWidgets.QPushButton(self.info_page)
        self.b_ex_open.setMinimumSize(QtCore.QSize(40, 40))
        self.b_ex_open.setMaximumSize(QtCore.QSize(50, 50))
        self.b_ex_open.setStyleSheet("QPushButton{\n"
                                     "    border:2px solid #0C8040;\n"
                                     "    border-radius: 15px;\n"
                                     "    color: #72AE74\n"
                                     "}QPushButton:hover{\n"
                                     "    color: rgba(170, 255, 127,255);\n"
                                     "}QPushButton:pressed{\n"
                                     "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                     "}")
        self.b_ex_open.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/external/External_option.svg"), QtGui.QIcon.Mode.Normal,
                         QtGui.QIcon.State.Off)
        self.b_ex_open.setIcon(icon12)
        self.b_ex_open.setIconSize(QtCore.QSize(40, 40))
        self.b_ex_open.setObjectName("b_ex_open")
        self.gridLayout_4.addWidget(self.b_ex_open, 1, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.info_page)
        self.lineEdit.setMinimumSize(QtCore.QSize(130, 50))
        self.lineEdit.setMaximumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: 2 px solid rgb(56, 102, 84);\n"
                                    "border-bottom: 2 px solid rgb(56, 102, 84);\n"
                                    "color: rgba(170, 255, 127,190);\n"
                                    "")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.info_page)
        self.label_15.setMinimumSize(QtCore.QSize(130, 50))
        self.label_15.setMaximumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("border: 2 px solid rgb(56, 102, 84);\n"
                                    "border-bottom: 2 px solid rgb(56, 102, 84);\n"
                                    "color: rgba(170, 255, 127,190);\n"
                                    "")
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 3, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.info_page)
        self.label_20.setMinimumSize(QtCore.QSize(18, 50))
        self.label_20.setMaximumSize(QtCore.QSize(18, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("border: 2 px solid rgb(56, 102, 84);\n"
                                    "border-bottom: 2 px solid rgb(56, 102, 84);\n"
                                    "color: rgba(170, 255, 127,190);\n"
                                    "")
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 1, 1, 1, 1)
        self.l_title_info = QtWidgets.QLabel(self.info_page)
        self.l_title_info.setMinimumSize(QtCore.QSize(506, 50))
        self.l_title_info.setMaximumSize(QtCore.QSize(506, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.l_title_info.setFont(font)
        self.l_title_info.setStyleSheet("color: #72AE74\n"
                                        "")
        self.l_title_info.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse | QtCore.Qt.TextInteractionFlag.TextEditable | QtCore.Qt.TextInteractionFlag.TextEditorInteraction | QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard | QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.l_title_info.setObjectName("l_title_info")
        self.gridLayout_4.addWidget(self.l_title_info, 0, 2, 1, 1)
        self.l_passwordinfo = QtWidgets.QLabel(self.info_page)
        self.l_passwordinfo.setMinimumSize(QtCore.QSize(506, 50))
        self.l_passwordinfo.setMaximumSize(QtCore.QSize(506, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.l_passwordinfo.setFont(font)
        self.l_passwordinfo.setStyleSheet("color: #72AE74\n"
                                          "")
        self.l_passwordinfo.setOpenExternalLinks(False)
        self.l_passwordinfo.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse | QtCore.Qt.TextInteractionFlag.TextEditable | QtCore.Qt.TextInteractionFlag.TextEditorInteraction | QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard | QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.l_passwordinfo.setObjectName("l_passwordinfo")
        self.gridLayout_4.addWidget(self.l_passwordinfo, 3, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.info_page)
        self.label_19.setMinimumSize(QtCore.QSize(18, 50))
        self.label_19.setMaximumSize(QtCore.QSize(18, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("border: 2 px solid rgb(56, 102, 84);\n"
                                    "border-bottom: 2 px solid rgb(56, 102, 84);\n"
                                    "color: rgba(170, 255, 127,190);\n"
                                    "")
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 0, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.info_page)
        self.label_22.setMinimumSize(QtCore.QSize(18, 50))
        self.label_22.setMaximumSize(QtCore.QSize(18, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("border: 2 px solid rgb(56, 102, 84);\n"
                                    "border-bottom: 2 px solid rgb(56, 102, 84);\n"
                                    "color: rgba(170, 255, 127,190);\n"
                                    "")
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 3, 1, 1, 1)
        self.b_hid2 = QtWidgets.QPushButton(self.info_page)
        self.b_hid2.setMinimumSize(QtCore.QSize(40, 40))
        self.b_hid2.setMaximumSize(QtCore.QSize(50, 50))
        self.b_hid2.setStyleSheet("QPushButton{\n"
                                  "    border:2px solid #0C8040;\n"
                                  "    border-radius: 15px;\n"
                                  "    color: #72AE74;\n"
                                  "    icon:url(:/hidden/Hidden.svg)\n"
                                  "}QPushButton:hover{\n"
                                  "    border: 2px solid    #72AE74;\n"
                                  "    color: #72AE74 ;\n"
                                  "}QPushButton:checked{\n"
                                  "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1 stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                  "    icon:url(:/plain/plain.svg);\n"
                                  "}")
        self.b_hid2.setText("")
        self.b_hid2.setIcon(icon3)
        self.b_hid2.setIconSize(QtCore.QSize(40, 40))
        self.b_hid2.setCheckable(True)
        self.b_hid2.setObjectName("b_hid2")
        self.gridLayout_4.addWidget(self.b_hid2, 3, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.info_page)
        self.label_12.setMinimumSize(QtCore.QSize(130, 50))
        self.label_12.setMaximumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border: 2 px solid rgb(56, 102, 84);\n"
                                    "border-bottom: 2 px solid rgb(56, 102, 84);\n"
                                    "color: rgba(170, 255, 127,190);\n"
                                    "")
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.info_page)
        self.label_21.setMinimumSize(QtCore.QSize(18, 50))
        self.label_21.setMaximumSize(QtCore.QSize(18, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("border: 2 px solid rgb(56, 102, 84);\n"
                                    "border-bottom: 2 px solid rgb(56, 102, 84);\n"
                                    "color: rgba(170, 255, 127,190);\n"
                                    "")
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 2, 1, 1, 1)
        self.verticalLayout_11.addLayout(self.gridLayout_4)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem)
        self.l_info_3 = QtWidgets.QLabel(self.info_page)
        self.l_info_3.setMinimumSize(QtCore.QSize(300, 40))
        self.l_info_3.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.l_info_3.setFont(font)
        self.l_info_3.setStyleSheet("border: 2 px solid rgb(56, 102, 84);\n"
                                    "border-bottom: 2 px solid rgb(56, 102, 84);\n"
                                    "color: rgba(170, 255, 127,190);\n"
                                    "")
        self.l_info_3.setText("")
        self.l_info_3.setObjectName("l_info_3")
        self.horizontalLayout_24.addWidget(self.l_info_3)
        self.b_delete_info = QtWidgets.QPushButton(self.info_page)
        self.b_delete_info.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.b_delete_info.setFont(font)
        self.b_delete_info.setStyleSheet("QPushButton{\n"
                                         "    border:2px solid #0C8040;\n"
                                         "    border-radius: 15px;\n"
                                         "    color: #72AE74\n"
                                         "}QPushButton:hover{\n"
                                         "    color: rgba(170, 255, 127,255);\n"
                                         "}QPushButton:pressed{\n"
                                         "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                         "}")
        self.b_delete_info.setObjectName("b_delete_info")
        self.horizontalLayout_24.addWidget(self.b_delete_info)
        self.b_update_info = QtWidgets.QPushButton(self.info_page)
        self.b_update_info.setMinimumSize(QtCore.QSize(120, 40))
        self.b_update_info.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.b_update_info.setFont(font)
        self.b_update_info.setStyleSheet("QPushButton{\n"
                                         "    border:2px solid #0C8040;\n"
                                         "    border-radius: 15px;\n"
                                         "    color: #72AE74\n"
                                         "}QPushButton:hover{\n"
                                         "    color: rgba(170, 255, 127,255);\n"
                                         "}QPushButton:pressed{\n"
                                         "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                         "}")
        self.b_update_info.setObjectName("b_update_info")
        self.horizontalLayout_24.addWidget(self.b_update_info)
        self.verticalLayout_11.addLayout(self.horizontalLayout_24)
        self.stackedWidget_main.addWidget(self.info_page)
        self.personal_info = QtWidgets.QWidget()
        self.personal_info.setObjectName("personal_info")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.personal_info)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.textBrowser = QtWidgets.QTextBrowser(self.personal_info)
        self.textBrowser.setMinimumSize(QtCore.QSize(720, 470))
        self.textBrowser.setMaximumSize(QtCore.QSize(720, 470))
        self.textBrowser.setStyleSheet("color: #72AE74\n"
                                       "")
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setOpenLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_18.addWidget(self.textBrowser)
        self.horizontalLayout_19.addLayout(self.verticalLayout_18)
        self.stackedWidget_main.addWidget(self.personal_info)
        self.verticalLayout_7.addWidget(self.stackedWidget_main)
        self.mainbox.addWidget(self.maininfo)
        self.horizontalLayout_8.addLayout(self.mainbox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addWidget(self.mainpage_frame)
        self.stackedWidget.addWidget(self.mainpage)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_main.setCurrentIndex(0)
        self.b_close.clicked.connect(MainWindow.close)
        self.b_close_2.clicked.connect(MainWindow.close)
        self.b_minimize.clicked.connect(MainWindow.hide)
        self.b_minimize_2.clicked.connect(MainWindow.hide)
        self.b_close_3.clicked.connect(MainWindow.close)
        self.b_minimize_3.clicked.connect(MainWindow.hide)
        self.h_slider.valueChanged['int'].connect(self.length_slider.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PMan"))
        self.tb_username.setPlaceholderText(_translate("MainWindow", "User Name!"))
        self.tb_mkey.setPlaceholderText(_translate("MainWindow", "Please enter the Master Key"))
        self.b_pwToggle.setToolTip(_translate("MainWindow", "Toggle visibility"))
        self.b_login.setShortcut(_translate("MainWindow", "Return"))
        self.l_info.setText(_translate("MainWindow", "hello"))
        self.n_newUser.setToolTip(_translate("MainWindow", "Create a New user"))
        self.n_newUser.setText(_translate("MainWindow", "   New User"))
        self.tb_username_2.setPlaceholderText(_translate("MainWindow", "User Name!"))
        self.tb_email.setPlaceholderText(_translate("MainWindow", "Email Address!"))
        self.tb_mkey_2.setPlaceholderText(_translate("MainWindow", "Please enter the Master Key"))
        self.b_pwToggle_2.setToolTip(_translate("MainWindow", "Toggle visibility"))
        self.l_info_2.setText(_translate("MainWindow", "hello"))
        self.n_newUser_2.setToolTip(_translate("MainWindow", "Create a New user"))
        self.n_newUser_2.setText(_translate("MainWindow", "Add new"))
        self.b_info.setWhatsThis(_translate("MainWindow", "Info "))
        self.tb_search.setPlaceholderText(_translate("MainWindow", "Search!"))
        self.b_allItems.setText(_translate("MainWindow", "   All Items             "))
        self.b_addNew.setText(_translate("MainWindow", "   Add New            "))
        self.b_sync.setStyleSheet(_translate("MainWindow", "QPushButton{\n"
                                                           "    border: 0px solid green ;\n"
                                                           "    color: rgba(170, 255, 127,190);\n"
                                                           "}QPushButton:hover{\n"
                                                           "    border-bottom: 2px solid rgba(0, 255, 0, 10);\n"
                                                           "    color: rgba(170, 255, 127,255);\n"
                                                           "}QPushButton:pressed{\n"
                                                           "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,                                     stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                                           "}\n"
                                                           ""))
        self.b_sync.setText(_translate("MainWindow", "    Sync                  "))
        self.b_bandr.setStyleSheet(_translate("MainWindow", "QPushButton{\n"
                                                            "    border: 0px solid green ;\n"
                                                            "    color: rgba(170, 255, 127,190);\n"
                                                            "}QPushButton:hover{\n"
                                                            "    border-bottom: 2px solid rgba(0, 255, 0, 10);\n"
                                                            "    color: rgba(170, 255, 127,255);\n"
                                                            "}QPushButton:pressed{\n"
                                                            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,                                     stop: 0 rgba(56, 102, 84, 180), stop: 1 rgba(56, 102, 84, 140));\n"
                                                            "}\n"
                                                            ""))
        self.b_bandr.setText(_translate("MainWindow", "    Backup & Restore "))
        self.b_generatenew.setText(_translate("MainWindow", "   New Password    "))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Last Used"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "Title                    :"))
        self.tb_add_new_title.setPlaceholderText(_translate("MainWindow", "The Website Name"))
        self.url.setText(_translate("MainWindow", "Website URL     :"))
        self.tb_add_new_url.setPlaceholderText(_translate("MainWindow", "Copy the URL from your browser"))
        self.username.setText(_translate("MainWindow", "User name         :"))
        self.tb_add_new_uname.setPlaceholderText(_translate("MainWindow", "Your User Name"))
        self.label_14.setText(_translate("MainWindow", "Password           :"))
        self.tb_mkey_3.setPlaceholderText(_translate("MainWindow", "Enter Your Password"))
        self.b_add_newa_dd.setText(_translate("MainWindow", "Add "))
        self.label.setText(_translate("MainWindow", "I dont know How I would do google Authentication Yet"))
        self.label_4.setText(_translate("MainWindow", "Import a backup from web browsers or previous backups"))
        self.label_3.setText(_translate("MainWindow", "Browse Directory"))
        self.file_browser.setText(_translate("MainWindow", "Browse"))
        self.label_10.setText(_translate("MainWindow", "Pman Backup:"))
        self.b_bandr_restore.setText(_translate("MainWindow", "Restore"))
        self.label_11.setText(_translate("MainWindow", "Create an encrypted backup:"))
        self.l_bandr_b1.setText(_translate("MainWindow", "Browse directory"))
        self.file_browser_3.setText(_translate("MainWindow", "Browse"))
        self.b_band_backup.setText(_translate("MainWindow", "Backup"))
        self.textEdit_2.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KG?(p}UNC&amp;*L%PVHDngto&gt;Q2@$`_X|:7[4m50zu{IEOhR^FfrA6\\)+8!1,j3</span></p>\n"
                                           "<p align=\"right\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\"><br /></span></p></body></html>"))
        self.length_slider.setText(_translate("MainWindow", "8"))
        self.label_6.setText(_translate("MainWindow", "Capital Letters"))
        self.label_9.setText(_translate("MainWindow", "Length"))
        self.label_8.setText(_translate("MainWindow", "Symbols [!@#$%^&]"))
        self.label_7.setText(_translate("MainWindow", "Numbers"))
        self.b_gen_generate_now.setText(_translate("MainWindow", "Generate now"))
        self.label_13.setText(_translate("MainWindow", "Username"))
        self.l_uname_info.setText(_translate("MainWindow", "TextLabel"))
        self.l_url_info.setText(_translate("MainWindow", "TextLabel"))
        self.lineEdit.setText(_translate("MainWindow", "Title"))
        self.label_15.setText(_translate("MainWindow", "Password"))
        self.label_20.setText(_translate("MainWindow", ":"))
        self.l_title_info.setText(_translate("MainWindow", "TextLabel"))
        self.l_passwordinfo.setText(_translate("MainWindow", "TextLabel"))
        self.label_19.setText(_translate("MainWindow", ":"))
        self.label_22.setText(_translate("MainWindow", ":"))
        self.label_12.setText(_translate("MainWindow", "URL"))
        self.label_21.setText(_translate("MainWindow", ":"))
        self.b_delete_info.setText(_translate("MainWindow", "Delete"))
        self.b_update_info.setText(_translate("MainWindow", "Update"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Created by Aziz M Khan @LtAbstergo</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">github : </span><a href=\"https://github.com/Lt-Abstergo/\"><span style=\" font-size:18pt; text-decoration: underline; color:#aaff7f;\">LtAbstergo</span></a></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Project link: </span><a href=\"https://github.com/Lt-Abstergo/PasswordMan\"><span style=\" font-size:18pt; text-decoration: underline; color:#aaff7f;\">github</span></a></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Login info are stored as encrypted tuple and the whole database  will be saved encrypted upon exiting</span></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
