#!/usr/bin/python
# coding: utf8

import logging
import traceback
from datetime import datetime, date, timedelta
from utils import get_connection
from config import PATH
from config import CONN_NAME

def get_assets_names():
	#return dict {symb: [id, name]}
	conn = get_connection(CONN_NAME, PATH)
	cur = conn.cursor()
	##cur.execute("SELECT asset_id, symb, name, conn_name FROM exprm.assets")
	try:
		cur.execute("SELECT * FROM exprm.assets")
		conn.commit()
		assets_list = {}
		for row in cur:
			assets_list[row[1]] = [row[0], row[2]]
	except:
		logging.error(traceback.format_exc())
	conn.close()
	return assets_list

def get_asset_metadata(id):
	conn = get_connection(CONN_NAME, PATH)
	cur = conn.cursor()
	cur.execute("SELECT symb, name FROM exprm.assets WHERE asset_id = " + str(id))
	conn.commit()
	for row in cur:
		conn.close()
		return row[1], row[0]

def get_asset_quotes(id):
	conn = get_connection(CONN_NAME, PATH)
	cur = conn.cursor()
	cur.execute("SELECT dayref, adj_close, vol FROM exprm.hist_quotes WHERE asset_id = " + str(id))
	conn.commit()
	res = {}
	for row in cur:
		res[row[0]] = {'AdjClose': row[1], 'Vol': row[2]}
	conn.close()
	return res

class Asset:
	def __init__(self, id):
		self.id = id
		self.name, self.symb = get_asset_metadata(id)
		self.quotes = get_asset_quotes(id) #example: {'dd-mm-yyyy': {'AdjClose': xx, 'Vol': xx}}
		self.dt_format = '%Y-%m-%d'

	def get_timeseries(self, indx):
		days = [day for day in self.quotes]
		days = sorted(days)
		values = [self.quotes[day][str(indx)] for day in days]
		return days, values



