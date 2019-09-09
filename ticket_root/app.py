import datetime

def convert_date(date):
    year,month,day = date.split('-')
    return datetime.date(int(year), int(month), int(day))

class Ticket:
    #handling fee is 20% but not more than 50 zl
    handling_fee_percent = 0.2

    def __init__(self, start_date = None, day = 0, end_date = None, cancel_date = None, ticket_price = None):
        self.start_date = convert_date(start_date)
        self.day = day
        self.end_date = convert_date(end_date)
        self.cancel_date = convert_date(cancel_date)
        self.money_back = None
        self.ticket_price = ticket_price

    def count_money_back(self):
        self.handling_fee = self.handling_fee_percent * self.ticket_price
        if self.handling_fee > 50:
            self.handling_fee = 50

        self.cancled_days = self.end_date - self.cancel_date
        self.money_back = (self.ticket_price - self.handling_fee)/self.day * int(self.cancled_days.days)
        return 'Do zwrotu: {} zł.' \
               '\nOpłata manipulacyjna: {} zł' \
               '\nKoszt jednego dnia: {} zł'.format(self.money_back,
                                                 self.handling_fee,
                                                 (self.ticket_price - self.handling_fee)/self.day)

    def __str__(self):
        return 'Nowy bilet {} - {} (dni: {})'.format(self.start_date, self.end_date, self.day)


def menu():
    print("""
    ******************************************************************************************************
    Program oblicza ile otrzymasz pieniędzy za zwrócenie biletu długookresowego (30/90 dni) w Warszawie.
    Aby obliczyć kwotę zwrotu, potrzebuję kilku informacji.

    Jeżeli nie pamiętasz daty aktywacji biletu, to przejdź do kolejnego pytania przyciskiem <<enter>>.
    W takiej sytuacji potrzebna będzie data ważności biletu i rodzaj biletu (30/90 dni).
    ******************************************************************************************************
    """)

    start_date = input('Kiedy aktywowałaś/aktywowałeś bilet (DD-MM-YYYY)? ')
    day = input('Na ile dni kupiłaś/kupiłeś bilet (30/90)? ')
    end_date = input('Do kiedy bilet jest ważny (DD-MM-YYYY)? ')
    cancel_date = input('Do kiedy chcesz korzystać z biletu (DD-MM-YYYY)? ')
    ticket_price = input('Ile zapłaciłaś/zapłaciłeś za bilet? ')
