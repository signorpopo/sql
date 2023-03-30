#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 21:11:37 2023

@author: davidyoshii
"""

import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()
    
    c.execute("DROP TABLE if exists numbers")
    c.execute("CREATE TABLE numbers(num int)")
    
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)", (random.randint(0,100),))
        
        
import sqlite3

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()
    
    prompt = """
    Select the operation that you want to perform [1-5]:
        1. Average
        2. Max
        3. Min
        4. Sum
        5. Exit
        """
        
    while True:
        x = input(prompt)
        if x in set(["1", "2", "3", "4"]):
            operation = {1: "avg", 2: "max", 3: "min", 4: "sum"}[int(x)]
            for row in c.execute(f"SELECT {operation}(num) FROM numbers"):
                print(f"{operation}: {row}")
        elif x == "5":
            print("Exit")
            break