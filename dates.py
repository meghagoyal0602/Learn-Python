from datetime import datetime, timedelta
today=datetime.now()
current_date=datetime.now()
print('today is: ' + str(today))
# timedelta add or removes days,weeks
#  subtracting day
one_day=timedelta(days=1)
yesterday =today-one_day
print('yesterday was: ' + str(yesterday))

# subtracting week
one_week=timedelta(weeks=1)
last_week=today-one_week
print('last week: '+ str(last_week))


current_date=datetime.now()
print('DAte: ' + str(current_date.day))  #date
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))
print('Hour: ' + str(current_date.hour))
print('minute: ' + str(current_date.minute))
print('second: ' + str(current_date.second))
