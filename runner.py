import ast
from urllib.parse import urlparse as parse

import AES256Handler
import businesshandler as u
import databasehandler as dbh

#
# user = u.BusinessHandler(False, "Rafik Khan", "Rafiqur", "rrk@mail.com")
# user2 = u.BusinessHandler(False, u_name="aziz Khan", m_key="RCDIVMZS", u_email="azizmk@mail.com")

# user = u.BusinessHandler(False,"Rafik Khan", "Rafiqur", "rrk@mail.com")

# user2 = u.BusinessHandler(u_name="Rafik Khan", m_key="Rafiqur")
# user2.add_new_login(url="asda.ca", username="asd", password="dasdas")
user2 = u.BusinessHandler(u_name="aziz", m_key="aziz")
# user2.show_all()
# print(u.generate_pass(60, False, False, False))
# a = AES256Handler.encrypt("RCDIVMZS", "RCDIVMZS")
# b = str(a)
# c = {'c_t': b'/7MpDYSFFe34wTEFv0wOzQ==', 's': b'rnMal4cCmNkDwl2owYlVJQ==', 'i': b'SQteQr/WTR+HSCoQhonQ1Q=='}
# d = AES256Handler.decrypt(c, "aziz")
#
#
# print(c)
# print(d)
# print(dbh.show_one("./cache/users/users.db",1))
