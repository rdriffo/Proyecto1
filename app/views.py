from django.shortcuts import render
from requests.api import post
from requests.api import get
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
import requests as rq
import json
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
        

        connection = cx_Oracle.connect(user=k.user, password=k.password, dsn=k.dsn)

        
        cursor = connection.cursor()
        cursor.execute("""
                SELECT run, dv_run, npi, dv_npi, apell_pat, apell_mat, primer_nombre, segundo_nombre, sigla_unid_rep, estado_cto
                FROM identificacion_pna
                WHERE run = :run""",
                run = rut)

        for run, dv_run, npi, dv_npi, apell_pat, apell_mat, primer_nombre, segundo_nombre, sigla_unid_rep, estado_cto in cursor:
            identificacion = {
                "run":run,
                "dv_run":dv_run,
                "npi":npi,
                "dv_npi":dv_npi,
                "apell_pat":apell_pat,
                "apell_mat":apell_mat,
                "primer_nombre":primer_nombre,
                "segundo_nombre":segundo_nombre,
                "sigla_unid_rep":sigla_unid_rep,
                "estado_cto":estado_cto
            }

            print("Values:", run, dv_run, npi, dv_npi, apell_pat, apell_mat, primer_nombre, segundo_nombre, sigla_unid_rep, estado_cto)

        imagen = self.foto(rut, connection)

        return Response({
                     "status":   "estado",
                     "identificacion":     identificacion,
                     "foto": imagen,
                 })



## --------------------------------------------------------------------------
    def foto(self, run=None, connection=None):
        
        items=[]
        with connection.cursor() as cursor:
            statament = "select foto_tin from foto_tin_pna where run=:run"
            cursor.execute(statament, {'run':run})
            result = cursor.fetchone()[0]
            print(result.read())
            foto= base64.b64encode(result.read()).decode()
            items.append({'imagen':foto})
        return foto

    
def retornar_page(request, rut):
    try:
        url = "http://127.0.0.1:8000/APP/get_data/"
        post = {'rut': rut}
        x = rq.post(url, data = post)

        #print(x.text)
        x_json = json.loads(x.text)
        return render (request, "pagina.html", {"x":x_json})
    
    except Exception as e:
        return render (request, "error.html")