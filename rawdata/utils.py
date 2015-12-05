#!/usr/bin/python
# coding: utf8

import logging
import traceback
import json

def get_connection(conn_name, path):
	data = json.loads("""{
	"connections":
                {
                "RBPROD":       {
                        "connection_name": "RBPROD",
                        "connection_type": "oracle",
                        "connection_IP": "bi1db8",
                        "connection_port": "1521",
                        "connection_user": "LKULIGIN",
                        "connection_pwd": "qwerty12",
                        "connection_service_name": "RBPROD_TAF"
                        },
                "datahub21": {
                        "connection_name": "datahub21",
                        "connection_type": "postgresql",
                        "connection_IP": "datahub-21",
                        "connection_dbname": "db",
                        "connection_port": "5432",
                        "connection_user": "datahub",
                        "connection_pwd": "datahub"
                        }
                }
	}""")

#	try:
#		with open(path) as data_file:
#			data = json.load(data_file)
#	except:
#		logging.error("JSON config not found")

	connection_parameters = ""
	try:
		connection_parameters = data['connections'][conn_name]
	except:
		logging.error("Connection  is not configured: " + traceback.format_exc())

	if connection_parameters["connection_type"] == "oracle":
		import cx_Oracle
		conn_string = (connection_parameters["connection_user"] + "/" + connection_parameters["connection_pwd"] + "@" +
			connection_parameters["connection_IP"] + ":" + connection_parameters["connection_port"] + "/" + connection_parameters["connection_service_name"]);
		try:
			conn = cx_Oracle.connect(conn_string)
			return conn
		except:
			logging.error(traceback.format_exc());
	if connection_parameters["connection_type"] == "postgresql":
		conn_string_pg = ("host='" + connection_parameters["connection_IP"] + "' port='" + connection_parameters["connection_port"]
			+ "' dbname='" + connection_parameters["connection_dbname"] + "' user='"
			+ connection_parameters["connection_user"] + "' password='" + connection_parameters["connection_pwd"] + "'")
		try:
			conn=psycopg2.connect(conn_string_pg)
			return conn
		except:
			logging.error(traceback.format_exc());
