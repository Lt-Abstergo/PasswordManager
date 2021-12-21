import sys

from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import businesshandler as bh

from ui_app import *


class MainWindow(QMainWindow):
    __user: bh.BusinessHandler

    def __init__(self):
        self.__user = None
        QMainWindow.__init__(self)
        self.ui = UiMainWindow()
        self.ui.setupUi(self)
        self.ui.b_addNew.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.add_new))
        self.ui.b_allItems.clicked.connect(self.show_all_item_page)
        self.ui.b_bandr.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.bandr))
        self.ui.b_generatenew.clicked.connect(self.setup_generate)
        self.ui.b_sync.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.sync))
        self.ui.b_info.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.personal_info))
        self.ui.n_newUser.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.splashnewuser))
        self.ui.b_pwToggle.clicked.connect(lambda: self.toggle_pass_handler(self.ui.b_pwToggle, self.ui.tb_mkey))
        self.ui.b_pwToggle_2.clicked.connect(lambda: self.toggle_pass_handler(self.ui.b_pwToggle_2, self.ui.tb_mkey_2))
        self.ui.b_pwToggle_3.clicked.connect(lambda: self.toggle_pass_handler(self.ui.b_pwToggle_3, self.ui.tb_mkey_3))
        self.ui.b_bandr_restore.clicked.connect(self.extract_backup)
        self.ui.n_newUser_2.clicked.connect(self.add_new_user)
        self.ui.b_login.clicked.connect(self.onclick_b_login)
        self.ui.b_gen_generate_now.clicked.connect(self.gen_password)
        self.ui.b_add_newa_dd.clicked.connect(self.add_new_login)
        self.ui.file_browser.clicked.connect(self.open_file_browser)
        self.show()

    def toggle_pass_handler(self, toggle_btn, textbox):
        if toggle_btn.isChecked():
            textbox.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            textbox.setEchoMode(QLineEdit.EchoMode.Password)

    def set_l_info(self, text: str):
        self.ui.l_info.setText(text)

    def onclick_b_login(self):
        uname = self.ui.tb_username.text()
        pw = self.ui.tb_mkey.text()
        if len(uname) == 0 and len(pw) == 0:
            self.set_l_info("Please Enter your credentials")
        elif len(uname) == 0:
            self.set_l_info("Username cant be empty")
        elif len(pw) == 0:
            self.set_l_info("Password cant be empty")
        else:
            try:
                self.__user = bh.BusinessHandler(u_name=uname, m_key=pw)
                self.set_l_info("Login Success")
                self.show_mainpage()
            except bh.WrongCredentialsException or IndexError or UnicodeDecodeError as error:
                self.set_l_info("Wrong Credentials: Please recheck your Credentials")
                print(error)

    def add_new_user(self):
        try:
            uname = self.ui.tb_username_2.text()
            email = self.ui.tb_email.text()
            pwd = self.ui.tb_mkey_2.text()
            self.__user = bh.BusinessHandler(False, u_name=uname, m_key=pwd, u_email=email)
            self.ui.l_info_2.setText("User created successfully: Please wait a moment")
            self.ui.stackedWidget.setCurrentWidget(self.ui.mainpage)
        except bh.UserExists as e:
            self.ui.l_info_2.setText("User already Exists. Try a different name")

    def gen_password(self):
        length = self.ui.h_slider.value()
        cap = self.ui.gen_cap_letters.isChecked()
        sym = self.ui.gen_cap_symbol.isChecked()
        num = self.ui.gen_cap_numeric.isChecked()

        pwd = bh.generate_pass(length=length, cap=cap, numeric=num, symbol=sym)
        self.ui.textEdit_2.setText(pwd)

    def add_new_login(self):
        title = self.ui.tb_add_new_title.toPlainText()
        url = self.ui.tb_add_new_url.toPlainText()
        username = self.ui.tb_add_new_uname.toPlainText()
        pwd = self.ui.tb_mkey_3.text()
        self.__user.add_new_login(url=url, username=username, password=pwd, name=title)
        self.ui.l_addpage.setText("Details saved in database")
        self.ui.tb_add_new_title.clear()
        self.ui.tb_add_new_url.clear()
        self.ui.tb_add_new_uname.clear()
        self.ui.tb_mkey_3.clear()

    def open_file_browser(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.FileMode.ExistingFile)
        filter = "CSV files(*.csv)"
        f_loc = dlg.getOpenFileName(dlg, caption="Select Backup File", filter=filter)
        self.ui.label_3.setText(f_loc[0])
        print(f_loc[0])

    def extract_backup(self):
        self.ui.l
        if self.__user is not None:
            if self.ui.b_bandr_pman_toggle.isChecked():
                self.__user.extract_backup(self.ui.label_3.text(), False)
            else:
                self.__user.extract_backup(self.ui.label_3.text())

    def setup_generate(self):
        self.ui.textEdit_2.setText(bh.generate_pass())
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.new_password)

    def show_mainpage(self):
        self.show_items()
        self.ui.stackedWidget.setCurrentWidget(self.ui.mainpage)

    def show_all_item_page(self):
        self.show_items()
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.all_items)

    def show_items(self):
        if self.__user is not None:
            items = self.__user.show_all()
            self.ui.tableWidget.setRowCount(self.__user.get_login_count())
            tb_row = 0
            for item in items:
                self.ui.tableWidget.setItem(tb_row, 0, QtWidgets.QTableWidgetItem(item[1]))
                self.ui.tableWidget.setItem(tb_row, 1, QtWidgets.QTableWidgetItem(item[2]))
                button = ButtonWidgetRow(item[0])
                self.ui.tableWidget.setCellWidget(tb_row, 2, button)
                button.clicked.connect(lambda: self.wb_handler())
                tb_row += 1
        else:
            print("User not initiated")

    def wb_handler(self):
        button = self.sender()
        if not button:
            return
        self.show_detail(button.rowID)

    def show_detail(self, rowid):
        self.ui.b_hid1.setChecked(False)
        self.ui.b_hid2.setChecked(False)
        self.__user.time_update(rowid)
        item = self.__user.show_detail(rowid)
        self.ui.l_title_info.setText(item[0])
        self.ui.l_url_info.setText(item[1])
        self.set_encryptable(self.ui.b_hid1, self.ui.l_uname_info, item[2])
        self.ui.b_hid1.clicked.connect(lambda: self.toggle_inf(self.ui.b_hid1, self.ui.l_uname_info, item[2]))
        self.set_encryptable(self.ui.b_hid2, self.ui.l_passwordinfo, item[3])
        self.ui.b_hid2.clicked.connect(lambda: self.toggle_inf(self.ui.b_hid2, self.ui.l_passwordinfo, item[3]))
        self.ui.b_update_info.clicked.connect(lambda: self.update_entry(rowid))
        self.ui.b_delete_info.clicked.connect(lambda: self.delete_entry(rowid))
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.info_page)

    def set_encryptable(self, button: QPushButton, label: QLabel, details):
        if button.isChecked():
            data = self.__user.decrypt_data(details)
            label.setText(data)
        else:
            label.setText("**********")

    def toggle_inf(self, button, label, info):
        try:
            if button.isChecked():
                data = self.__user.decrypt_data(info)
                label.setText(data)
            else:
                label.setText("**********")
        except IndexError as e:
            print(e)

    def delete_entry(self, rowid):
        self.__user.delete_entry(rowid)
        self.ui.l_info_3.setText("Entry Deleted")
        self.show_all_item_page()

    def update_entry(self, rowid):
        __un_uname = self.ui.l_uname_info.text()
        __un_key = self.ui.l_passwordinfo.text()
        title = self.ui.l_title_info.text()
        url = self.ui.l_url_info.text()
        ast_str = "**********"
        if __un_key == ast_str or __un_key == ast_str:
            self.__user.update_entry_title(rowid, title, url)
            self.ui.l_info.setText("Entry updated ")
        else:
            uname = self.__user.encrypt_data(__un_uname)
            mkey = self.__user.encrypt_data(__un_key)
            self.__user.update_entry(rowid, title, url, uname, mkey)
            self.ui.l_info.setText("Entry updated")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
