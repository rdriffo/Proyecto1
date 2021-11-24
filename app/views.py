from django.shortcuts import render
from rest_framework.views       import  APIView
from rest_framework.response    import  Response
from rest_framework             import  status
import requests
import cx_Oracle
from helpers import keys as k
import sys
import os


class get_data(APIView):
    '''
    Retornara la data
    ---------------------------------------------
    IN: 
    OUT:
    '''
    def post(self, request):
        print("-------------------------- Retornar data ------------------------------------")
        
        rut   =   request.POST["rut"]
        

        connection = cx_Oracle.connect(k.usuario, k.clave, k.host)

        # cursor = connection.cursor()
        # cursor.execute("""
        #     SELECT RUN, NOMBRE 
        #     FROM IDENTIFICACION""",
        #     family = 'AP')

        # for id, descripcion in cursor:
        #     print("Values:", id, descripcion)
        
        # cursor.close()
        # connection.close()
        
        return Response({
                     "status":   "stado",
                     "data":     "data"
                 })