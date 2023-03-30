#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 18:00:10 2023

@author: davidyoshii
"""

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    
    c.execute("SELECT firstname, lastname FROM employees")
    rows = c.fetchall()
    for r in rows:
        print(r[0], r[1])