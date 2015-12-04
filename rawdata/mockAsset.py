from datetime import datetime, date, timedelta
import datetime
from decimal import *

class Asset:
    def __init__(self, id):
        self.id = id
        print id

    def get_timeseries(self, indx):
        print indx
        if (indx == "AdjClose"):
            b = [datetime.datetime(2015, 1, 5, 10, 15), datetime.datetime(2015, 1, 5, 10, 30), datetime.datetime(2015, 1, 5, 10, 45), datetime.datetime(2015, 1, 5, 11, 0), datetime.datetime(2015, 1, 5, 11, 15), datetime.datetime(2015, 1, 5, 11, 30), datetime.datetime(2015, 1, 5, 11, 45), datetime.datetime(2015, 1, 5, 12, 0), datetime.datetime(2015, 1, 5, 12, 15), datetime.datetime(2015, 1, 5, 12, 30), datetime.datetime(2015, 1, 5, 12, 45), datetime.datetime(2015, 1, 5, 13, 0), datetime.datetime(2015, 1, 5, 13, 15), datetime.datetime(2015, 1, 5, 13, 30), datetime.datetime(2015, 1, 5, 13, 45), datetime.datetime(2015, 1, 5, 14, 0), datetime.datetime(2015, 1, 5, 14, 15), datetime.datetime(2015, 1, 5, 14, 30), datetime.datetime(2015, 1, 5, 14, 45), datetime.datetime(2015, 1, 5, 15, 0), datetime.datetime(2015, 1, 5, 15, 15), datetime.datetime(2015, 1, 5, 15, 30), datetime.datetime(2015, 1, 5, 15, 45), datetime.datetime(2015, 1, 5, 16, 0), datetime.datetime(2015, 1, 5, 16, 15), datetime.datetime(2015, 1, 5, 16, 30), datetime.datetime(2015, 1, 5, 16, 45), datetime.datetime(2015, 1, 5, 17, 0), datetime.datetime(2015, 1, 5, 17, 15), datetime.datetime(2015, 1, 5, 17, 30)]
            c = [Decimal('54.33'), Decimal('54.30'), Decimal('54.55'), Decimal('54.10'), Decimal('54.94'), Decimal('55.63'), Decimal('55.69'), Decimal('56.23'), Decimal('56.30'), Decimal('56.26'), Decimal('56.58'), Decimal('56.15'), Decimal('56.30'), Decimal('56.12'), Decimal('55.92'), Decimal('55.92'), Decimal('56.01'), Decimal('56.23'), Decimal('56.12'), Decimal('55.99'), Decimal('55.97'), Decimal('55.78'), Decimal('56.08'), Decimal('56.09'), Decimal('56.45'), Decimal('56.13'), Decimal('56.29'), Decimal('56.10'), Decimal('56.07'), Decimal('56.07')]
            return b, c
        elif indx == "Vol":
            b = [datetime.datetime(2015, 1, 5, 10, 15), datetime.datetime(2015, 1, 5, 10, 30), datetime.datetime(2015, 1, 5, 10, 45), datetime.datetime(2015, 1, 5, 11, 0), datetime.datetime(2015, 1, 5, 11, 15), datetime.datetime(2015, 1, 5, 11, 30), datetime.datetime(2015, 1, 5, 11, 45), datetime.datetime(2015, 1, 5, 12, 0), datetime.datetime(2015, 1, 5, 12, 15), datetime.datetime(2015, 1, 5, 12, 30), datetime.datetime(2015, 1, 5, 12, 45), datetime.datetime(2015, 1, 5, 13, 0), datetime.datetime(2015, 1, 5, 13, 15), datetime.datetime(2015, 1, 5, 13, 30), datetime.datetime(2015, 1, 5, 13, 45), datetime.datetime(2015, 1, 5, 14, 0), datetime.datetime(2015, 1, 5, 14, 15), datetime.datetime(2015, 1, 5, 14, 30), datetime.datetime(2015, 1, 5, 14, 45), datetime.datetime(2015, 1, 5, 15, 0), datetime.datetime(2015, 1, 5, 15, 15), datetime.datetime(2015, 1, 5, 15, 30), datetime.datetime(2015, 1, 5, 15, 45), datetime.datetime(2015, 1, 5, 16, 0), datetime.datetime(2015, 1, 5, 16, 15), datetime.datetime(2015, 1, 5, 16, 30), datetime.datetime(2015, 1, 5, 16, 45), datetime.datetime(2015, 1, 5, 17, 0), datetime.datetime(2015, 1, 5, 17, 15), datetime.datetime(2015, 1, 5, 17, 30)]
            c = [4138630, 1037280, 1399950, 1314020, 2931610, 4458850, 3818580, 2806210, 3607080, 2362130, 3067830, 3349020, 1785540, 997000, 1216630, 1553450, 1413770, 1573050, 1435330, 1035610, 373420, 1730770, 1509270, 659420, 2704650, 1179960, 479380, 561650, 584270, 1103060]
            return b, c
        else:
            print 'Invalid indx'
