import time
import calendar

class date(object):
    def get_date_time(self):
        return time.localtime(time.time())
    def get_exact_date_and_time(self):
        return time.asctime(time.localtime(time.time()))
class cal(date):
    def month(self):
        return calendar.month(2018,10)
c = cal() #thi is the object for class and with inherit upper class or base class
print('month is:',c.month())
print('Todays date,day and time is:',c.get_exact_date_and_time())
