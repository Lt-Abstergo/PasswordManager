import sqlite3
import sys
import traceback
from datetime import datetime as time


def create_user_table(dbname):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                            u_name      Text UNIQUE,
                            u_email     Text,
                            master_key  Text,
                            create_date text    
                       );""")
        print_file("Users table created")
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print_file(error_handler(error))


def add_new_user(dbname, u_name, u_email, m_key):
    try:
        date = time.now()
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users VALUES (?,?,?,?);", (u_name, u_email, m_key, date,))
        print_file("new user " + u_name + " created")
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as error:
        if error is sqlite3.IntegrityError:
            print_file(error_handler(error))
            return False


def check_user(dbname, u_name) -> list:
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("SELECT *,ROWID FROM users WHERE u_name=(?);", (u_name,))
        items = cursor.fetchone()
        # print_file("User Exist " + u_name)
        conn.commit()
        conn.close()
        return items
    except sqlite3.Error as error:
        print_file(error_handler(error))


def get_user(dbname, rowid) -> list:
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("SELECT *,ROWID FROM users WHERE ROWID=(?);", (rowid,))
        items = cursor.fetchall()
        # print_file("User Exist " + u_name)
        conn.commit()
        conn.close()
        return items
    except sqlite3.Error as error:
        print_file(error_handler(error))


def delete_user(dbname, rowid):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE ROWID=(?);", str(rowid))
        print_file("Removed entry " + rowid)
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print_file(error_handler(error))


def create_login_table(dbname):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS login_details(
                            u_name      TEXT,
                            name        TEXT,
                            url         TEXT,
                            username    TEXT,
                            password    TEXT,
                            entry_date  TEXT,
                            use_date    TEXT
                            );""")
        print_file("database successfully created")
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print_file(error_handler(error))


def add_one(dbname, user, name, url, username, password):
    try:
        curr_time = time.now()
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO login_details VALUES (?,?,?,?,?,?,?);",
                       (user, name, url, username, password, curr_time, curr_time))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print_file(error_handler(error))


def add_multiple(dbname, item_list):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO login_details VALUES (?,?,?,?,?,?,?);", item_list)
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print_file(error_handler(error))


def show_all(dbname, user):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("SELECT rowid, name, use_date FROM login_details WHERE u_name=(?) ORDER BY use_date;", (user,))
        items = cursor.fetchall()
        conn.commit()
        conn.close()
        return items
    except sqlite3.Error as error:
        print_file(error_handler(error))


def save_to_disk_helper(dbname, user):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("SELECT name, url,username,password FROM login_details WHERE u_name=(?);", (user,))
        items = cursor.fetchall()
        conn.commit()
        conn.close()
        return items
    except sqlite3.Error as error:
        print_file(error_handler(error))


def login_count(dbname, user):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(rowid) FROM login_details WHERE u_name=(?);", (user,))
        item = cursor.fetchone()
        conn.commit()
        conn.close()
        return item[0]
    except sqlite3.Error as error:
        print_file(error_handler(error))


def delete_one(dbname, rowid):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM login_details where rowid=(?);", (rowid,))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print_file(error_handler(error))


def delete_all(dbname):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM login_details WHERE TRUE;")
        print_file("Removed all entries.")
        conn.commit()
        conn.close()

    except sqlite3.Error as error:
        print_file(error_handler(error))


def get_row_id(dbname, name, url, username, password) -> list:
    row_id = []

    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("SELECT ROWID, * FROM login_details WHERE name=(?);", (name,))
        items = cursor.fetchall()
        print_tb(cursor.fetchall())

        for item in items:
            if item[2] == url and item[3] == username and item[4] == password:
                row_id.append(item[0])
        print_tb(cursor.fetchall())
        conn.commit()
        conn.close()
        return row_id
    except sqlite3.Error as error:
        print_file(error_handler(error))


def table_exists(dbname, table_name) -> bool:
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (table_name,))
        items = cursor.fetchone()
        if items is not None:
            return True
        conn.commit()
        conn.close()
        return False

    except sqlite3.Error as error:
        print_file(error_handler(error))
        return False


def get_users(dbname):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(ROWID) FROM users;")
        item = cursor.fetchone()
        conn.commit()
        conn.close()
        return int(item[0])
    except sqlite3.Error as error:
        print_file(error_handler(error))


def show_one(dbname, rowid):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("SELECT name, url, username, password FROM login_details where ROWID=(?)", (rowid,))
        item = cursor.fetchone()
        conn.commit()
        conn.close()
        return item
    except sqlite3.Error as error:
        print_file(error_handler(error))



def print_file(str_input):
    print(str_input)


def print_tb(items):
    for item in items:
        print(item)


def error_handler(error):
    exc_type, exc_value, exc_tb = sys.exc_info()
    er_string = "SQLite error: " + str(error)
    er_string += "\nSQLite traceback: "
    er_list = traceback.format_exception(exc_type, exc_value, exc_tb)
    for i in er_list:
        er_string += i
    return er_string


def update_time(dbname, rowid):
    try:
        curr_date = time.now()
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("UPDATE login_details SET use_date=? WHERE ROWID=? ", (curr_date, rowid,))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print_file(error_handler(error))


def update_entry(dbname, rowid, name, url, username, password):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("UPDATE login_details SET name=?, url=?, username=?,password=?  WHERE ROWID=? ",
                       (name, url, username, password, rowid,))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print_file(error_handler(error))


def update_entry_title(dbname, rowid, name, url):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("UPDATE login_details SET name=?, url=?  WHERE ROWID=? ",
                       (name, url, rowid,))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print_file(error_handler(error))


def search(dbname, search_key):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("SELECT rowid, name, use_date FROM login_details WHERE url LIKE ?", ('%' + search_key + '%',))
        items = cursor.fetchall()
        conn.commit()
        conn.close()
        return items
    except sqlite3.Error as error:
        print_file(error_handler(error))
