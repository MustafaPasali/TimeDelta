import datetime

today = datetime.datetime.today()
a = datetime.timedelta(days=20, hours=3)
b = datetime.timedelta(days=40, hours=3)
c = datetime.timedelta(days=60, hours=3)

print(today-a)
print(today-b)
print(today-c)

