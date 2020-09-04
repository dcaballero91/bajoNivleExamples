# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:05:24 2020

@author: dcaballe
http://localhost:5001/calculadora?tipo=suma&a=1&b=3
"""
from flask import Blueprint, request, jsonify


calculadora = Blueprint('calculadora', __name__)

@calculadora.route('/calculadora', methods=['GET'])
def llamarServicioSet():
    global tipo,tiporet,a,b,cretrun
    ##try:
    if 'tipo' in request.args and 'a' in request.args and 'b' in request.args:
        tipo = str(request.args['tipo'])
        a=str(request.args['a'])
        b=str(request.args['b'])
        inicializarVariables(tipo,a,b)
    else:
        return "Error: No mod tipo,a,b provmoded. Please specify an tipo,a,b"
    

    salida = {'codRes': codRes, 'menRes': menRes,'tipo':tiporet,'cretrun':cretrun,'a':a,'b':b}
    return jsonify({'ParmOut':salida})


def inicializarVariables(tipo,a,b):
    global codRes, menRes, cretrun,tiporet
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    accesoSet(tipo,a,b)
    


def accesoSet(tipo,a,b):
    global menRes,codRes,cretrun,tiporet
    

    try:
        print(tipo)
        if tipo == 'suma':
            print("suma")
            tiporet="suma"
            cretrun=(int(a)+int(b))
        elif tipo =='resta':
            print("resta")
            tiporet="resta"
        elif tipo == 'mul':
            print("mul")
            tiporet="mul"
        elif tipo == 'div':
            print("div")
            tiporet="div"
        else:
            print("No definido")
            tiporet="suma,resta,mul,div"
            codRes = 'ERROR'
            menRes = 'Valores Adminitidos'
            
        return tiporet,cretrun,a,b
       
    except Exception as e:
        print("Error en manipular datos",str(e))
        