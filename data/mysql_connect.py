#! /usr/bin/env python3
# coding: utf-8

"""
Pizza Mysql Connect
"""

import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "xxxxx",
    database = "xxxxx")
cursor = db.cursor()
