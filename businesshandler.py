import random
import sqlite3
import string
from urllib.parse import urlparse as parse
import ast
import os
import csv

import AES256Handler
import databasehandler as dbh
import AES256Handler as encH


class BusinessHandlerException(Exception):
    """Raised: Base Exception case"""


class NoUsersException(BusinessHandlerException):
    """Raised: There are No users; Please Create an User to Start"""


class WrongCredentialsException(BusinessHandlerException):
    """Raised: The Pass Key specified does not Match: Please Check your Credentials"""


class UserExists(BusinessHandlerException):
    """Raised: The user already exists"""


def generate_pass(length: int = 8, cap: bool = True, numeric: bool = True, symbol: bool = True):
    all = string.ascii_lowercase
    if cap:
        all += string.ascii_uppercase
    if numeric:
        all += string.digits
    if symbol:
        all += string.punctuation
    pwd = ""
    for i in range(length):
        pwd += random.choice(all)
    return pwd


class BusinessHandler:
    __DB_LOC = "./cache/users/"
    __USER_DB = __DB_LOC + "users.db"
    __USERTBN = "users"
    __LGNTBN = "login_details"
    __pkey: str

    def __init__(self, flag: bool = True, u_name: str = None, m_key: str = None, u_email: str = None):
        if flag:
            if not os.path.isfile(self.__USER_DB):
                raise NoUsersException
            if self.total_users() < 1:
                raise NoUsersException
            self.user_name = u_name
            self.__pkey = m_key
            user_check = self.user_exist()
            if user_check == -1:
                raise WrongCredentialsException
        else:
            self.base_init()
            sameUsers = dbh.check_user(self.__USER_DB, u_name)
            if sameUsers is None or len(sameUsers) == 0:
                self.user_name = u_name
                self.__pkey = m_key
                self.create_new_user(u_name=u_name, u_email=u_email, m_key=m_key)
            else:
                raise UserExists

    def get_user_name(self):
        return self.user_name

    def base_init(self):
        if not os.path.isfile(self.__USER_DB):
            dbh.create_user_table(self.__USER_DB)
            dbh.create_login_table(self.__USER_DB)
        else:
            if not dbh.table_exists(self.__USER_DB, self.__USERTBN):
                dbh.create_user_table(self.__USER_DB)
            if not dbh.table_exists(self.__USER_DB, self.__LGNTBN):
                dbh.create_login_table(self.__USER_DB)

    def create_new_user(self, u_name: str, u_email: str, m_key: str):
        enc_mKey = self.encrypt_data(m_key)
        dbh.add_new_user(self.__USER_DB, u_name, u_email, enc_mKey)

    def user_exist(self) -> int:
        item = dbh.check_user(self.__USER_DB, self.user_name)
        try:
            decrypted = self.decrypt_data(item[2])
            if decrypted.__eq__(self.__pkey):
                return int(item[4])
            return -1
        except IndexError as c:
            dbh.print_file("I failed", c)

    def get_user(self, rowid):
        return dbh.get_user(self.__USER_DB, str(rowid))

    def add_new_login(self, url: str, username: str, password: str, name: str = None, flag: bool = True):
        u_name = username
        p_word = password
        if flag:
            u_name = self.encrypt_data(username)
            p_word = self.encrypt_data(password)
        if name is None:
            name = parse(url).netloc
        dbh.add_one(dbname=self.__USER_DB, user=self.user_name, name=name, url=url, username=u_name, password=p_word, )

    def reset_db_login(self):
        dbh.delete_all(self.__USER_DB)

    def extract_backup(self, backup_path, flag: bool = True):
        try:
            with open(backup_path, newline='')as csv_file:
                spam_reader = csv.reader(csv_file, delimiter=',')
                for row in spam_reader:
                    name, url, username, password = row
                    if name == "name" and url == "url" and username == "username" and password == "password":
                        pass
                    else:
                        if flag:
                            self.add_new_login(url, username, password, name)
                        else:
                            self.add_new_login(url, username, password, name,flag=flag)

        except OSError as error:
            dbh.error_handler(error)
        finally:
            csv_file.close()

    def total_users(self) -> int:
        return dbh.get_users(self.__USER_DB)

    def show_all(self):
        return dbh.show_all(self.__USER_DB, self.user_name)

    def show_detail(self, rowid):
        return dbh.show_one(self.__USER_DB, rowid)

    def get_login_count(self):
        return dbh.login_count(self.__USER_DB, self.user_name)

    def encrypt_data(self, data: str) -> str:
        return str(encH.encrypt(data, self.__pkey))

    def decrypt_data(self, data: str) -> str:
        enc_tuple = ast.literal_eval(data)
        return encH.decrypt(enc_tuple, self.__pkey)

    def delete_entry(self, rowid):
        dbh.delete_one(self.__USER_DB, rowid)

    def update_entry(self, rowid, name, url, username, password):
        dbh.update_entry(self.__USER_DB, rowid, name, url, username, password)

    def update_entry_title(self, rowid, name, url):
        dbh.update_entry_title(self.__USER_DB, rowid, name, url)

    def time_update(self, rowid):
        dbh.update_time(self.__USER_DB, rowid)

    def save_to_disk(self, source):
        pass
