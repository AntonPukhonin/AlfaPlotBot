#!/usr/bin/python

import chart


#print chart.get_cities_names()
mccrate, mccname = chart.get_chart(1,20)
print type(mccrate[0])
print type(mccname[0])
