import datetime
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
