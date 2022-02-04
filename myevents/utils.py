import datetime as dt
from calendar import HTMLCalendar
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

January = 1

class ModelCalendar(HTMLCalendar):



    def __init__(self, year=dt.datetime.now().year, month=dt.datetime.now().month):
        self.year = year
        self.month = month

        super(ModelCalendar, self).__init__()

    def formatday(self,year,month, day, weekday,query):
        """
        Return a day as a table cell.
        """

        d = '<span>{0}</span>'.format(day)
        e =''
        ev = query.objects.filter(date__day=day,date__month = month,date__year = year).order_by('time')

        if len(ev) > 0:
            for obj in ev:
                e += '<li class="list-group-item text-left {1}">{2}  - {0}</li>'.format(obj.title,obj.csstag,obj.time)
            d += '<ul class="list-group"> {0} </ul>'.format(e)

        if day == 0:
            # day outside month
            return '<td class="%s">&nbsp;</td>' % self.cssclass_noday
        else:
            return '<td class="{0}">{1}</td>'.format(self.cssclasses[weekday],d)




    def formatweek(self, year,month,theweek,query):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday( year,month,d, wd, query) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s

    def formatmonth(self, theyear, themonth,query, withyear=True):
        """
        Return a formatted month as a table.
        """
        v = []
        a = v.append
        a('<table border="0" cellpadding="0" cellspacing="0" class="table table-hover %s">' % (
            self.cssclass_month))
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek( theyear,themonth,week,query))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)

    def formatyear(self, theyear,query, width=3):
        """
        Return a formatted year as a table of tables.
        """
        v = []
        a = v.append
        width = max(width, 1)
        a('<table border="0" cellpadding="0" cellspacing="0" class="table table-hover %s">' %
          self.cssclass_year)
        a('\n')
        a('<tr><th colspan="%d" class="%s">%s</th></tr>' % (
            width, self.cssclass_year_head, theyear))
        for i in range(January, January+12, width):
            # months in this row
            months = range(i, min(i+width, 13))
            a('<tr>')
            for m in months:
                a('<td>')
                a(self.formatmonth(theyear, m, query,withyear=False))
                a('</td>')
            a('</tr>')
        a('</table>')
        return ''.join(v)


