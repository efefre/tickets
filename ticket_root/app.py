class Ticket:

    def __init__(self, start_date = None, day = 0, end_date = None):
        self.start_date = start_date
        self.day = day
        self.end_date = end_date

    def __str__(self):
        return 'New ticket: {} - {} (days: {})'.format(self.start_date, self.end_date, self.day)
