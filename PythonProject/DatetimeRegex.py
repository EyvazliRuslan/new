# from datetime import date,datetime,timedelta
# print(datetime.weekday(datetime.now()))
# print(date.year)
# print(date.month)
# print(date.today())
import re
phone_number = re.compile(r'[+]\d\d\d\d\d[-]\d\d\d[-]\d\d[-]\d\d')
string = 'My Phone +99455-666-75-22 number is +99455-663-75-22 '
macth = phone_number.search(string)
print(macth.group())