#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import json

con = sqlite3.connect('geography.mbtiles')
bounds = con.cursor()
bounds.execute("SELECT value AS bounds FROM metadata  WHERE name = 'bounds'")

center = con.cursor()
center.execute("SELECT value AS center FROM metadata  WHERE name = 'center'")

minzoom = con.cursor()
minzoom.execute("SELECT value AS minzoom FROM metadata  WHERE name = 'minzoom'")

maxzoom = con.cursor()
maxzoom.execute("SELECT value AS maxzoom FROM metadata  WHERE name = 'maxzoom'")

name = con.cursor()
name.execute("SELECT value AS name FROM metadata  WHERE name = 'name'")

description = con.cursor()
description.execute("SELECT value AS description FROM metadata  WHERE name = 'description'")

bounds = bounds.fetchall()
center = center.fetchall()
minzoom = minzoom.fetchall()
maxzoom = maxzoom.fetchall()
name = name.fetchall()
description = description.fetchall()

all = bounds + center + minzoom + maxzoom + name + description


print bounds
print center
print minzoom
print maxzoom
print name
print description


with open('data.txt', 'w') as outfile:
    json.dump(all, outfile)

con.close()


