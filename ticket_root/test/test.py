import datetime
import pytest
from ticket_root.app import Ticket


def test_convert_date():
    data = Ticket.convert_date('01-09-2019')
    assert data == datetime.date(2019,9,1)

def test_create_object():
    new_ticket = Ticket('01-09-2019','30',None,'15-09-2019','100')
    assert new_ticket.start_date == '01-09-2019'
    assert new_ticket.day == '30'
    assert new_ticket.end_date == None
    assert new_ticket.cancel_date == '15-09-2019'
    assert new_ticket.ticket_price == '100'


@pytest.mark.parametrize('start_date, days,end_date, cancel_date, price,result',
                         [
                             ('01-09-2019',30,'30-09-2019','15-09-2019',100, 40),
                             ('01-09-2019',30,'30-09-2019','30-09-2019',100, 0),
                             ('01-09-2019',30,'30-09-2019','15-08-2019',100, 'Wprowadzono błędną datę. Nie można zwrócić biletu przed jego aktywacją'),
                             ('01-09-2019',30,'30-09-2019','15-11-2019',100, 'Wprowadzono błędną datę. Nie można zwrócić biletu po terminie ważności')
                         ]
                         )
def test_count_money_back(start_date, days,end_date, cancel_date, price,result):
    new_ticket = Ticket(Ticket.convert_date(start_date),days,Ticket.convert_date(end_date),Ticket.convert_date(cancel_date),price)
    if new_ticket.cancel_date < new_ticket.start_date or new_ticket.cancel_date > new_ticket.end_date:
        assert new_ticket.count_money_back() == result
    else:
        new_ticket.count_money_back()
        assert new_ticket.money_back == result