from django.shortcuts import render
from rest_framework.views       import  APIView
from rest_framework.response    import  Response
from rest_framework             import  status
import requests
import cx_Oracle
from helpers import keys as k
import sys
import os
import base64
import json

#class get_data(APIView):



def get_foto(run=None):
    connection = cx_Oracle.connect(user="prueba", password="prueba01",
                                dsn="190.215.50.170:8521/principal")
    items=[]
    with connection.cursor() as cursor:
        statament = "select foto from foto where run=:run"
        cursor.execute(statament, {'run':1111})
        result = cursor.fetchone()[0]
        print(result.read())
        foto= base64.b64encode(result.read()).decode()
        items.append({'imagen':foto})
    return items

    
    #print(foto["foto"].decode("iso-8859-1"))
    connection.close()

