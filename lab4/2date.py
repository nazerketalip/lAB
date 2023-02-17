from datetime import date, timedelta
yesterday = date.today() - timedelta(1)
tomorrow = date.today() + timedelta(1)
print('YESTERDAY :', yesterday)
print('TODAY :', date.today())
print('TOMORROW :', tomorrow)
