import datetime
from ticket_root.app import Ticket


def test_convert_date():
    data = Ticket.convert_date('01-09-2019')
    assert data == datetime.date(2019,9,1)