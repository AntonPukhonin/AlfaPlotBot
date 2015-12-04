from datetime import datetime

class Asset:
	def __init__(self, id):
		self.id = id

	def get_timeseries(self, indx):
		print "try"
		if 1==1:
			print "success"
		if (indx == "AdjClose"):
			b = [datetime.datetime(2015, 1, 5, 10, 15), datetime.datetime(2015, 1, 5, 10, 30), datetime.datetime(2015, 1, 5, 10, 45), datetime.datetime(2015, 1, 5, 11, 0), datetime.datetime(2015, 1, 5, 11, 15), datetime.datetime(2015, 1, 5, 11, 30), datetime.datetime(2015, 1, 5, 11, 45), datetime.datetime(2015, 1, 5, 12, 0), datetime.datetime(2015, 1, 5, 12, 15), datetime.datetime(2015, 1, 5, 12, 30), datetime.datetime(2015, 1, 5, 12, 45), datetime.datetime(2015, 1, 5, 13, 0), datetime.datetime(2015, 1, 5, 13, 15), datetime.datetime(2015, 1, 5, 13, 30), datetime.datetime(2015, 1, 5, 13, 45), datetime.datetime(2015, 1, 5, 14, 0), datetime.datetime(2015, 1, 5, 14, 15), datetime.datetime(2015, 1, 5, 14, 30), datetime.datetime(2015, 1, 5, 14, 45), datetime.datetime(2015, 1, 5, 15, 0), datetime.datetime(2015, 1, 5, 15, 15), datetime.datetime(2015, 1, 5, 15, 30), datetime.datetime(2015, 1, 5, 15, 45), datetime.datetime(2015, 1, 5, 16, 0), datetime.datetime(2015, 1, 5, 16, 15), datetime.datetime(2015, 1, 5, 16, 30), datetime.datetime(2015, 1, 5, 16, 45), datetime.datetime(2015, 1, 5, 17, 0), datetime.datetime(2015, 1, 5, 17, 15), datetime.datetime(2015, 1, 5, 17, 30)]
			c = [Decimal('54.33'), Decimal('54.30'), Decimal('54.55'), Decimal('54.10'), Decimal('54.94'), Decimal('55.63'), Decimal('55.69'), Decimal('56.23'), Decimal('56.30'), Decimal('56.26'), Decimal('56.58'), Decimal('56.15'), Decimal('56.30'), Decimal('56.12'), Decimal('55.92'), Decimal('55.92'), Decimal('56.01'), Decimal('56.23'), Decimal('56.12'), Decimal('55.99'), Decimal('55.97'), Decimal('55.78'), Decimal('56.08'), Decimal('56.09'), Decimal('56.45'), Decimal('56.13'), Decimal('56.29'), Decimal('56.10'), Decimal('56.07'), Decimal('56.07')]
			return b, c
