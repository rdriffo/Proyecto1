#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Requerimientos para que funcione
# sudo pip install cx_Oracle
# sudo dnf install oracle-instantclient12.2-basic-12.2.0.1.0-1.x86_64.rpm
# sudo dnf install libaio
# export LD_LIBRARY_PATH=/usr/lib/oracle/12.2/client64/lib:$LD_LIBRARY_PATH
# 

import cx_Oracle

#conn = cx_Oracle.connect('prueba','prueba01','190.215.50.170/principal')
connection = cx_Oracle.connect(user="prueba", password="",
                               dsn="190.215.50.170:8521/principal")

cursor = connection.cursor()
cursor.execute("""
        SELECT run, nombres, apellidos, nacionalidad
        FROM identificacion
        WHERE run = :run""",
        run = 1111)
for run, nombres, apellidos, nacionalidad in cursor:
    print("Values:", run, nombres, apellidos, nacionalidad)
 
cursor.close()
connection.close()
