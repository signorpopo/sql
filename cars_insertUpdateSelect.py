#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 18:11:48 2023

@author: davidyoshii
"""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    c.execute("INSERT INTO inventory VALUES('Ford', 'F-Series', 653957)")
    c.execute("INSERT INTO inventory VALUES('Ford', 'Explorer', 207673)")
    c.execute("INSERT INTO inventory VALUES('Ford', 'Escape', 137370)")
    c.execute("INSERT INTO inventory VALUES('Honda', 'CR-V', 238155)")
    c.execute("INSERT INTO inventory VALUES('Honda', 'Accord', 154612)")
    
with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    c.execute("UPDATE inventory SET quantity=300000 WHERE make='Honda' AND model='CR-V'")
    c.execute("UPDATE inventory SET quantity=160000 WHERE make='Honda' AND model='Accord'")
    c.execute("SELECT * FROM inventory")
    rows = c.fetchall()
    
    for r in rows:
        print(r[0], r[1], r[2])
        
with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    for row in c.execute("SELECT * FROM inventory WHERE make='Ford'"):
        print(row)
    