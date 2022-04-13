from datetime import datetime, timedelta
from calendar import HTMLCalendar
from.models import History

class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self, day, historys):
        historys_per_day = historys.filter(start_time__day=day)
        d = ''
        for history in historys_per_day:
            if history.avg_score >= 70:
                d += f'<img src="../../../static/images/good.png" style="width:50px;" />'
            elif history.avg_score >= 30:
                d += f'<img src="../../../static/images/soso.png" style="width:50px;" />'
            else:
                d += f'<img src="../../../static/images/bad.png" style="width:50px;" />'
            
            

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    def formatweek(self, theweek, historys):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, historys)
        return f'<tr> {week} </tr>'

    def formatmonth(self, user, withyear=True):
        historys = History.objects.filter(user=user, start_time__year=self.year, start_time__month=self.month).order_by('start_time')


        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'<tr><th colspan="7" class="month">{self.year}년 {self.month}월</th></tr>\n'
        cal += f'<tr><th class="mon">월</th><th class="tue">화</th><th class="wed">수</th><th class="thu">목</th><th class="fri">금</th><th class="sat">토</th><th class="sun">일</th></tr>\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, historys)}\n'
        cal += f'</table>'
        return cal