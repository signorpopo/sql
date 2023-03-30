#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 18:53:11 2023

@author: davidyoshii
"""

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    
    cities = [
        ('Boston', 'MA', 600000),
        ('Los Angeles', 'CA', 38000000),
        ('Houston', 'TX', 2100000),
        ('Philadelphia', 'PA', 1500000),
        ('San Antonio', 'TX', 1400000),
        ('San Diego', 'CA', 130000),
        ('Dallas', 'TX', 1200000),
        ('San Jose', 'CA', 900000),
        ('Jacksonville', 'FL', 800000),
        ('Indianapolis', 'IN', 800000),
        ('Austin', 'TX', 800000),
        ('Detroit', 'MI', 700000)
        ]
    c.executemany("INSERT INTO population VALUES(?, ?, ?)", cities)
    for row in c.execute("SELECT * FROM population WHERE population > 1000000"):
        print(row)

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    
    c.execute("""CREATE TABLE regions(city TEXT, region TEXT)""")
    
    cities = [
        ('New York City', 'Northeast'),
        ('San Francisco', 'West'),
        ('Chicago', 'Midwest'),
        ('Houston', 'South'),
        ('Phoenix', 'West'),
        ('Boston', 'Northeast'),
        ('Los Angeles', 'West'),
        ('Houston', 'South'),
        ('Philadelphia', 'Northeast'),
        ('San Antonio', 'South'),
        ('San Diego', 'West'),
        ('Dallas', 'South'),
        ('San Jose', 'West'),
        ('Jacksonville', 'South'),
        ('Indianapolis', 'Midwest'),
        ('Austin', 'South'),
        ('Detroit', 'Midwest')
        ]
    
    c.executemany("INSERT INTO regions VALUES(?, ?)", cities)
    
    for row in c.execute("SELECT * FROM regions ORDER BY  region ASC"):
        print(row)

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    
    for row in c.execute("""SELECT population.city, population.population, regions.region 
                         FROM population, regions 
                         WHERE population.city = regions.city"""):
         print(row)


with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    
    for row in c.execute("""SELECT DISTINCT population.city, population.population, regions.region
                         FROM population, regions
                         WHERE population.city = regions.city
                         ORDER BY population.city ASC"""):
        print("City: " + row[0])
        print("Population: " + str(row[1]))
        print("Region: " + row[2])