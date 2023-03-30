#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 19:45:24 2023

@author: davidyoshii
"""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    for row in c.execute("""SELECT make, model, count(order_date) FROM orders
                         GROUP BY model"""):
        print(row)

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    
    for row in c.execute("""SELECT inventory.make, inventory.model, inventory.quantity, count(orders.order_date)
                         FROM inventory INNER JOIN orders
                         WHERE inventory.model = orders.model
                         GROUP BY inventory.model"""):
        print(f"Make/model: {row[0]}/{row[1]}")
        print(f"Quantity: {row[2]}")
        print(f"Order count: {row[3]}")
        print()