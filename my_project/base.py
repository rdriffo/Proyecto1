import os


ORACLE_PRUEBA = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'principal',
        'USER': 'prueba',
        'PASSWORD': 'prueba01',
        'HOST': '190.215.50.170',
        'PORT': '8521', 
}

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}