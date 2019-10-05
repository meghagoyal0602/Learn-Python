from datetime import datetime,timedelta
birthday=input('When is you birthday: (dd/mm/yyyy)')
birth_date=datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birth_date))

one_day=timedelta(days=1)
day_before_eve=birth_date-one_day
print('Day before eve: ' + str(day_before_eve))