#!/usr/bin/python
# coding: utf8

import logging
import traceback
from datetime import datetime, date, timedelta
from utils import get_connection
PATH ="./config.json"
CONN_NAME = "RBPROD"


def get_cities_names():
	#return dict {name: [id]}
	conn = get_connection(CONN_NAME, PATH)
	cur = conn.cursor()
	##cur.execute("SELECT asset_id, symb, name, conn_name FROM exprm.assets")
	try:
		cur.execute("SELECT REGION_, (case when REGION_ = 1 then 'Moscow' when REGION_=2 then 'SPB' else 'Perm' end) city FROM expm_balances GROUP BY REGION_")
		conn.commit()
		assets_list = {}
		for row in cur:
			assets_list[row[1]] = [row[0]]
	except:
		logging.error(traceback.format_exc())
	conn.close()
	return assets_list

def get_ages(city_id):
	#return dict {name: [id]}
	conn = get_connection(CONN_NAME, PATH)
	cur = conn.cursor()
	##cur.execute("SELECT asset_id, symb, name, conn_name FROM exprm.assets")
	try:
		cur.execute("SELECT age FROM expm_balances where AGE<80 and AGE > 10 and region_ = " + str(city_id) + "GROUP BY AGE")
		conn.commit()
		ages_list = []
		for row in cur:
			assets_list.append([0])
	except:
		logging.error(traceback.format_exc())
	conn.close()
	return ages_list


def get_chart(city_id, age_id):
	conn = get_connection(CONN_NAME, PATH)
	cur = conn.cursor()
	cur.execute("SELECT * FROM EXPM_MCCRATE WHERE AGE = " + str(age_id) + "AND REGION_ = " + str(city_id) + " ORDER BY 4 asc")
	conn.commit()
	mccrate = []
	mccname = []
	for row in cur:
		mccrate.append(row[3])
		mccname.append(row[0])
#		res[row[2]] = row[3]
	conn.close()
	return mccrate, mccname
