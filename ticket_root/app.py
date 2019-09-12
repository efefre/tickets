import datetime

def convert_date(date):
    day,month,year = date.split('-')
    return datetime.date(int(year), int(month), int(day))

class Ticket:
    #handling fee is 20% but not more than 50 zl
    handling_fee_percent = 0.2

    def __init__(self, start_date = None, day = 0, end_date = None, cancel_date = None, ticket_price = None):
        self.start_date = start_date
        self.day = day
        self.end_date = end_date
        self.cancel_date = cancel_date
        self.money_back = None
        self.ticket_price = ticket_price

    def count_money_back(self):
        self.handling_fee = self.handling_fee_percent * self.ticket_price
        if self.handling_fee > 50:
            self.handling_fee = 50

        self.cancled_days = self.end_date - self.cancel_date
        self.money_back = float((self.ticket_price - self.handling_fee)/self.day * int(self.cancled_days.days))
        return '\nDo zwrotu: {:.2f} zł.' \
               '\nPoniesiony koszt: {:.2f} zł' \
               '\n\nOpłata manipulacyjna: {:.2f} zł' \
               '\nKoszt jednego dnia: {:.2f} zł'.format(self.money_back,
                                                        self.ticket_price - self.money_back,
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

    if start_date == '':
        start_date = None
        end_date = input('Do kiedy bilet jest ważny (DD-MM-YYYY)? ')
        while True:
            try:
                end_date = convert_date(end_date)
                break
            except ValueError:
                print('--- Wprowadzono błędną datę ważności biletu ---')
                end_date = input('Do kiedy bilet jest ważny (DD-MM-YYYY)? ')

    else:
        while True:
            try:
                start_date = convert_date(start_date)
                break
            except ValueError:
                print('--- Wprowadzono błędną datę aktywacji biletu ---')
                start_date = input('Kiedy aktywowałaś/aktywowałeś bilet (DD-MM-YYYY)? ')
        end_date = None

    day = int(input('Na ile dni kupiłaś/kupiłeś bilet (30/90)? '))

    if end_date == None:
        end_date = start_date + datetime.timedelta(days=day)

    while day != 30 and day != 90:
        print('--- Wprowadzono błędną wartość ---')
        day = int(input('Na ile dni kupiłaś/kupiłeś bilet (30/90)? '))

    cancel_date = input('Do kiedy chcesz korzystać z biletu (DD-MM-YYYY)? ')

    while True:
        try:
            cancel_date = convert_date(cancel_date)
            if cancel_date > start_date:
                break
            else:
                print('-- Wprowadzono błędną datę. Nie można zwrócić biletu przed jego aktywacją i w dniu jego aktywacji --')
                cancel_date = input('Do kiedy chcesz korzystać z biletu (DD-MM-YYYY)? ')
        except ValueError:
            print('--- Wprowadzono błędną datę ---')
            cancel_date = input('Do kiedy chcesz korzystać z biletu (DD-MM-YYYY)? ')

    ticket_price = input('Ile zapłaciłaś/zapłaciłeś za bilet? ')
    if ',' in ticket_price:
        ticket_price = ticket_price.replace(',','.')

    ticket_price = round(float(ticket_price),2)
