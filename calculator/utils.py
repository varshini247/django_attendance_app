from datetime import datetime, timedelta
from calendar import HTMLCalendar

from .models import Day
import json

class Calendar(HTMLCalendar):
    def __init__(self, year=None, month = None, uid=None):
        self.year = year
        self.month = month
        self.firstweekday = 0
        self.uid = uid
        #super(Calender, self).__init__()
    
    def formatday(self,day,marked=False):
        if day!=0:
          if marked:
            return f"<td data-status='0' style='background-color:pink' class='marked--date'><span class='date'>{day}</span></td>"
          else:
             return f"<td data-status='0'><span class='date'>{day}</span></td>"
        return '<td></td>'
    
    def formatweek(self,theweek,days):
      week = ''
      for d,weekday in theweek:
        if d in days:
            marked=True
            week+= self.formatday(d,marked=True)
            print(week)
        else:
             week+= self.formatday(d)          
      return f'<tr > {week} </tr>'

    def formatmonth(self, withyear=True):
        print('ochesaa')
        days_object = Day.objects.filter(uid=self.uid,year__year=self.year, month__month=self.month).values_list('abs_days')
        try:
         days =list(map(int, json.loads(days_object[0][0]) ))
         print(days)
        except:
          days = []
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal+= f'{(self.formatweek(week,days))}\n'
        return cal
