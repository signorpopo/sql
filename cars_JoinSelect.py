#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 19:02:55 2023

@author: davidyoshii
"""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    c.execute("""CREATE TABLE orders(make TEXT, model TEXT, order_date DATE)""")
    orders = [
        ('Ford', 'F-Series', '2022-03-15'),
        ('Ford', 'F-Series', '2022-06-15'),
        ('Ford', 'F-Series', '2022-09-15'),
        ('Ford', 'Explorer', '2022-03-15'),
        ('Ford', 'Explorer', '2022-06-15'),
        ('Ford', 'Explorer', '2022-09-15'),
        ('Ford', 'Escape', '2022-03-15'),
        ('Ford', 'Escape', '2022-06-15'),
        ('Ford', 'Escape', '2022-09-15'),
        ('Honda', 'CR-V', '2022-03-15'),
        ('Honda', 'CR-V', '2022-06-15'),
        ('Honda', 'CR-V', '2022-09-15'),
        ('Honda', 'Accord', '2022-03-15'),
        ('Honda', 'Accord', '2022-06-15'),
        ('Honda', 'Accord', '2022-09-15')       
        ]
    c.executemany("INSERT INTO orders VALUES(?, ?, ?)", orders)

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    for row in c.execute("""SELECT DISTINCT inventory.make, inventory.model, inventory.quantity, orders.order_date
                         FROM inventory INNER JOIN orders
                         WHERE inventory.model=orders.model"""):
         print(f"Make/model: {row[0]}/{row[1]}")
         print(f"Quantity: {row[2]}")
         print(f"Order: {row[3]}")
         print()